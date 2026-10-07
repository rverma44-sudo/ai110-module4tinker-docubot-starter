from docubot import DocuBot


def test_document_directories_do_not_prevent_loading(tmp_path):
    (tmp_path / "archive.md").mkdir()
    (tmp_path / "notes.txt").mkdir()
    (tmp_path / "archive.md" / "nested.md").write_text("Nested", encoding="utf8")
    (tmp_path / "guide.md").write_text("Guide", encoding="utf8")

    bot = DocuBot(docs_folder=str(tmp_path))

    assert bot.documents == [("guide.md", "Guide")]
    assert bot.full_corpus_text() == "Guide"


def test_loads_supported_files_with_utf8_content(tmp_path):
    (tmp_path / "guide.md").write_text("Café guide", encoding="utf8")
    (tmp_path / "notes.txt").write_text("Notes", encoding="utf8")
    (tmp_path / "ignored.csv").write_text("Ignored", encoding="utf8")

    bot = DocuBot(docs_folder=str(tmp_path))

    assert dict(bot.documents) == {"guide.md": "Café guide", "notes.txt": "Notes"}


def test_directory_without_documents_loads_empty_corpus(tmp_path):
    (tmp_path / "archive.md").mkdir()
    (tmp_path / "notes.txt").mkdir()

    bot = DocuBot(docs_folder=str(tmp_path))

    assert bot.documents == []
    assert bot.full_corpus_text() == ""
