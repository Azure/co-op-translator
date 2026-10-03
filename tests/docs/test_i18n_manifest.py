"""Check language availability against MkDocs' published files and URL rules."""

import gzip
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

if importlib.util.find_spec("mkdocs") is None:
    raise unittest.SkipTest("Documentation tests require requirements-docs.txt")

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PluginCollection
from mkdocs.structure.files import File, Files, InclusionLevel

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("docs_i18n", ROOT / "hooks/docs_i18n.py")
HOOK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HOOK)


class NavigationManifestTests(unittest.TestCase):
    def manifest(self, paths, directory_urls=True, excluded=()):
        with tempfile.TemporaryDirectory() as directory:
            config = MkDocsConfig()
            config.plugins = PluginCollection()
            config.plugins["docs_i18n"] = HOOK
            config.site_dir = directory
            config.use_directory_urls = directory_urls
            files = Files(
                File(
                    path,
                    directory,
                    directory,
                    directory_urls,
                    inclusion=(
                        InclusionLevel.EXCLUDED
                        if path in excluded
                        else InclusionLevel.INCLUDED
                    ),
                )
                for path in paths
            )
            files = config.plugins.on_files(files, config=config)
            content = files.get_file_from_path(
                "javascripts/i18n-pages.js"
            ).content_string
            return json.loads(content.split(" = ", 1)[1].split(";\n", 1)[0])["pages"]

    def test_only_published_translations_are_available(self):
        pages = self.manifest(
            [
                "index.md",
                "first.md",
                "i18n/ko/first.md",
                "i18n/fr/first.md",
                "asset.png",
            ],
            excluded=["i18n/fr/first.md"],
        )
        self.assertEqual(pages["first.md"], {"en": "first/", "ko": "i18n/ko/first/"})
        self.assertNotIn("asset.png", pages)
        self.assertEqual(pages["index.md"], {"en": "./"})

    def test_canonical_english_wins_over_duplicate_translation(self):
        pages = self.manifest(["i18n/en/index.md", "index.md", "i18n/ko/index.md"])
        self.assertEqual(pages["index.md"], {"en": "./", "ko": "i18n/ko/"})

    def test_nested_pages_follow_mkdocs_url_configuration(self):
        pages = self.manifest(
            ["guide/setup.md", "i18n/ko/guide/setup.md"], directory_urls=False
        )
        self.assertEqual(
            pages["guide/setup.md"],
            {"en": "guide/setup.html", "ko": "i18n/ko/guide/setup.html"},
        )

    def test_theme_language_metadata_does_not_trigger_separate_sitemaps(self):
        output = (
            '<head><link rel="alternate" href="/co-op-translator/i18n/ko/" '
            'hreflang="ko">\n'
            "<link hreflang='en' rel='alternate' href='/co-op-translator/'>"
            '<link rel="alternate" type="application/rss+xml" href="feed.xml">'
            '<link rel="canonical" href="/co-op-translator/"></head>'
            '<a class="md-select__link" hreflang="ko" href="i18n/ko/">Korean</a>'
        )
        result = HOOK.on_post_page(output)
        self.assertNotIn('<link rel="alternate" href=', result)
        self.assertNotIn("<link hreflang=", result)
        self.assertIn('type="application/rss+xml"', result)
        self.assertIn('rel="canonical"', result)
        self.assertIn('class="md-select__link" hreflang="ko"', result)

    def test_sitemap_alternates_are_reciprocal_and_only_include_published_pages(self):
        pages = self.manifest(
            ["first.md", "i18n/ko/first.md", "i18n/fr/first.md"],
            excluded=["i18n/fr/first.md"],
        )
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            config = MkDocsConfig()
            config.site_dir = directory
            config.site_url = "https://azure.github.io/co-op-translator/"
            (site / "javascripts").mkdir()
            (site / "javascripts/i18n-pages.js").write_text(
                "window.coOpI18n = " + json.dumps({"pages": pages}) + ";\n",
                encoding="utf-8",
            )
            root = ET.Element(f"{{{HOOK.SITEMAP_NS}}}urlset")
            for path in ["first/", "i18n/ko/first/", "i18n/en/first/"]:
                entry = ET.SubElement(root, f"{{{HOOK.SITEMAP_NS}}}url")
                ET.SubElement(entry, f"{{{HOOK.SITEMAP_NS}}}loc").text = (
                    config.site_url + path
                )
                ET.SubElement(entry, f"{{{HOOK.SITEMAP_NS}}}lastmod").text = (
                    "2026-10-03"
                )
            ET.ElementTree(root).write(site / "sitemap.xml", encoding="utf-8")

            HOOK.on_post_build(config)

            entries = list(ET.parse(site / "sitemap.xml").getroot())
            expected = {
                "en": config.site_url + "first/",
                "ko": config.site_url + "i18n/ko/first/",
            }
            for entry in entries[:2]:
                links = entry.findall(f"{{{HOOK.XHTML_NS}}}link")
                self.assertEqual(
                    {link.get("hreflang"): link.get("href") for link in links},
                    expected,
                )
                self.assertEqual(
                    entry.findtext(f"{{{HOOK.SITEMAP_NS}}}lastmod"), "2026-10-03"
                )
            self.assertEqual(entries[2].findall(f"{{{HOOK.XHTML_NS}}}link"), [])
            self.assertEqual(
                gzip.decompress((site / "sitemap.xml.gz").read_bytes()),
                (site / "sitemap.xml").read_bytes(),
            )


if __name__ == "__main__":
    unittest.main()
