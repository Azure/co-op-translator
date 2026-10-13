from PIL import Image

from co_op_translator.utils.markdown.readme_images import discover_readme_images
from co_op_translator.utils.markdown.image_links import update_image_links


def test_discover_readme_images_returns_only_existing_local_raster_images(tmp_path):
    image_dir = tmp_path / "images"
    image_dir.mkdir()
    local_image = image_dir / "hero image.png"
    reference_image = image_dir / "reference.png"
    html_image = image_dir / "html.png"
    Image.new("RGB", (2, 2), "white").save(local_image)
    Image.new("RGB", (2, 2), "white").save(reference_image)
    Image.new("RGB", (2, 2), "white").save(html_image)
    (tmp_path / "README.md").write_text(
        "\n".join(
            [
                "![Local](images/hero%20image.png)",
                "![Reference][cover]",
                "",
                "[cover]: images/reference.png",
                '<img src="images/html.png" alt="HTML">',
                "![Remote](https://example.com/remote.png)",
                "![Missing](images/missing.png)",
                "![Vector](images/logo.svg)",
            ]
        ),
        encoding="utf-8",
    )

    assert discover_readme_images(tmp_path / "README.md", tmp_path) == {
        local_image.resolve(),
        reference_image.resolve(),
        html_image.resolve(),
    }


def test_reference_style_readme_image_link_is_rewritten(tmp_path):
    image_dir = tmp_path / "images"
    image_dir.mkdir()
    source_image = image_dir / "cover.png"
    Image.new("RGB", (2, 2), "white").save(source_image)
    readme = tmp_path / "README.md"
    content = "![Cover][hero]\n\n[hero]: images/cover.png\n"

    updated = update_image_links(
        content,
        readme,
        "ko",
        tmp_path / "translations",
        tmp_path / "translated_images",
        tmp_path,
        use_translated_images=True,
        target_path=tmp_path / "translations" / "ko" / "README.md",
    )

    assert "[hero]: ../../translated_images/ko/" in updated
    assert updated.endswith(".webp\n")
