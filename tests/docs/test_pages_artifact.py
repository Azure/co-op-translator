"""Check literal code examples separately from navigable article links."""

import unittest

from check_pages_artifact import PageAssets


class PageAssetsTests(unittest.TestCase):
    def test_highlighted_code_links_are_examples_not_navigable_links(self):
        page = PageAssets()
        page.feed(
            "<code>[Outside](ignore.md)</code><article>"
            '<a href="guide/">Guide</a>'
            "<pre><code>[Arabic]<span>(./translations/ar/README.md)</span>"
            "\n![Image](images/hero.png)</code></pre>"
            "<p><code>[text](URL)</code></p></article>"
        )
        self.assertEqual(page.article_links, ["guide/"])
        self.assertEqual(
            page.literal_link_destinations(),
            {"./translations/ar/README.md": 1, "images/hero.png": 1, "URL": 1},
        )

    def test_link_labels_can_translate_but_paths_and_occurrences_must_match(self):
        source = PageAssets()
        source.feed("<article><code>[text](URL) [text](URL)</code></article>")
        translated = PageAssets()
        translated.feed("<article><code>[글](URL) [글](URL)</code></article>")
        rewritten = PageAssets()
        rewritten.feed("<article><code>[글](../../URL) [글](URL)</code></article>")
        self.assertEqual(
            source.literal_link_destinations(), translated.literal_link_destinations()
        )
        self.assertNotEqual(
            source.literal_link_destinations(), rewritten.literal_link_destinations()
        )


if __name__ == "__main__":
    unittest.main()
