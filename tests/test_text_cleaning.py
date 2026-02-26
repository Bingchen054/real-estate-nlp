from scripts.text_cleaning import TextCleaner

cleaner = TextCleaner()

def test_price_normalization():
    assert "450000" in cleaner.normalize_prices("priced at 450k")
    assert "1200000" in cleaner.normalize_prices("$1.2m home")

def test_measurement_normalization():
    assert "2000 square feet" in cleaner.normalize_measurements("2,000 sqft")

def test_abbreviation_expansion():
    assert "bedroom" in cleaner.expand_abbreviations("3 br home")

def test_html_removal():
    assert "<" not in cleaner.remove_html("<p>Beautiful home</p>")

def test_unicode():
    assert isinstance(cleaner.normalize_unicode("café"), str)

def test_whitespace():
    assert cleaner.remove_extra_whitespace("a   b") == "a b"