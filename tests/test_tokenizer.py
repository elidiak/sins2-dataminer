from sins2_dataminer.parser.tokenizer import tokenize

def test_tokenizer_basic():
    text = 'name = "Frigate"'
    tokens = tokenize(text)
    assert tokens == ["name", "=", "Frigate"]

def test_tokenizer_braces():
    text = "ability { amount = 5 }"
    tokens = tokenize(text)
    assert tokens == ["ability", "{", "amount", "=", "5", "}"]

def test_tokenizer_comments():
    text = """
    // comment
    hull = 1200
    """
    tokens = tokenize(text)
    assert tokens == ["hull", "=", "1200"]

def test_tokenizer_strings():
    text = 'desc = "Long range frigate"'
    tokens = tokenize(text)
    assert tokens == ["desc", "=", "Long range frigate"]