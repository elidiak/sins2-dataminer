from sins2_dataminer.parser.parser_core import Parser

def parse(text: str):
    from sins2_dataminer.parser.tokenizer import tokenize
    tokens = tokenize(text)
    return Parser(tokens).parse_block()

def test_parse_simple_assignment():
    struct = parse("hull = 1200")
    assert struct == {"hull": 1200}

def test_parse_nested_block():
    text = """
    ability {
        type = "ShieldBoost"
        amount = 50
    }
    """
    struct = parse(text)
    assert struct == {
        "ability": {
            "type": "ShieldBoost",
            "amount": 50
        }
    }

def test_parse_multiple_blocks():
    text = """
    ability { type = A }
    ability { type = B }
    """
    struct = parse(text)
    assert struct == {
        "ability": [
            {"type": "A"},
            {"type": "B"}
        ]
    }