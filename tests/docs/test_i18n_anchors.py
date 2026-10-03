"""Exercise source fragment links against real MkDocs-rendered translations."""

from html.parser import HTMLParser
import logging
import tempfile
import unittest

from test_i18n_manifest import HOOK
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page


class Ids(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.values = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        identifier = dict(attrs).get("id")
        if identifier is not None:
            self.values.append(identifier)


class TranslationAnchorTests(unittest.TestCase):
    def render(self, documents):
        directory = self.enterContext(tempfile.TemporaryDirectory())
        config = MkDocsConfig()
        config.docs_dir = directory
        config.site_dir = directory
        config.markdown_extensions = ["toc"]
        files = Files(File(path, directory, directory, True) for path in documents)
        for file in files:
            page = Page(None, file, config)
            page.markdown = documents[file.src_uri]
            page.render(config, files)
        return config, files

    def test_cross_document_fragments_resolve_without_changing_translated_toc(self):
        config, files = self.render(
            {
                "configuration.md": "# Configuration\n\n## Model client backend\n",
                "i18n/ko/configuration.md": "# 구성\n\n## 모델 클라이언트 백엔드\n",
                "i18n/ko/api.md": "[설정](configuration.md#model-client-backend)",
            }
        )
        page = files.get_file_from_path("i18n/ko/configuration.md").page
        original_toc = list(HOOK._headings(page.toc))
        english = files.get_file_from_path("configuration.md").page.content
        HOOK.on_env(None, config, files)
        self.assertIn("model-client-backend", Ids(page.content).values)
        self.assertIn("모델 클라이언트 백엔드", page.content)
        self.assertEqual(list(HOOK._headings(page.toc)), original_toc)
        self.assertEqual(
            files.get_file_from_path("configuration.md").page.content, english
        )
        with self.assertNoLogs("mkdocs", level="WARNING"):
            files.get_file_from_path("i18n/ko/api.md").page.validate_anchor_links(
                files=files, log_level=logging.WARNING
            )

    def test_existing_ids_are_not_duplicated_and_repeated_builds_are_safe(self):
        config, files = self.render(
            {
                "configuration.md": "# Configuration\n\n## OpenAI\n",
                "i18n/fr/configuration.md": "# Configuration\n\n## OpenAI\n",
            }
        )
        page = files.get_file_from_path("i18n/fr/configuration.md").page
        before = page.content
        HOOK.on_env(None, config, files)
        HOOK.on_env(None, config, files)
        self.assertEqual(page.content, before)
        self.assertEqual(len(Ids(page.content).values), 2)

    def test_different_heading_structure_does_not_receive_guessed_aliases(self):
        config, files = self.render(
            {
                "configuration.md": "# Configuration\n\n## Setup\n",
                "i18n/ko/configuration.md": "# 구성\n\n### 설정\n",
            }
        )
        page = files.get_file_from_path("i18n/ko/configuration.md").page
        before = page.content
        HOOK.on_env(None, config, files)
        self.assertEqual(page.content, before)
        self.assertNotIn("setup", page.present_anchor_ids)


if __name__ == "__main__":
    unittest.main()
