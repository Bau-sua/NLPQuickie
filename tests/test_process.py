import pytest
from unittest.mock import Mock, patch
from process import process_text

@pytest.mark.parametrize(
    "text, expected_count",
    [
        ("", 0),
        ("Hola mundo", 2),
        ("test test", 2),
        ("¡Puntuación! 123", 2),
    ],
)
def test_word_count(text, expected_count):
    result = process_text(text)
    assert result["word_count"] == expected_count

@pytest.mark.parametrize(
    "text, expected_top",
    [
        ("test test foo", {"word": "test", "count": 2}),
        ("", {"word": "ninguna", "count": 0}),
        ("a b a", {"word": "a", "count": 2}),
    ],
)
def test_most_common_word(text, expected_top):
    result = process_text(text)
    assert result["most_common_word"] == expected_top

def test_entities():
    with patch("process.nlp") as mock_nlp:
        mock_doc = Mock()
        mock_ent = Mock(text="Apple", label_="ORG")
        mock_doc.ents = [mock_ent]
        mock_nlp.return_value = mock_doc
        result = process_text("Apple test")
        assert len(result["entities"]) == 1
        assert result["entities"][0]["text"] == "Apple"

def test_clean_sample_long():
    long_text = "a" * 300
    result = process_text(long_text)
    assert result["cleaned_sample"].endswith("...")
    assert len(result["cleaned_sample"]) <= 203