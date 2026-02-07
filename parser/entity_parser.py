from __future__ import annotations
from pathlib import Path
from typing import Any
from .model_builder import build_entity
from ..models.entity import Entity

def parse_entity(path: Path) -> Entity:
    text = path.read_text(encoding="utf-8")
    tokens = tokenize(text)
    parser = Parser(tokens)
    struct = parser.parse_block()
    return build_entity(struct, name=path.stem)

def tokenize(text: str) -> list[str]:
    """
    Produces a flat list of tokens:
    identifiers, numbers, strings, {, }, =.
    Comments and whitespace are removed.
    """
    tokens = []
    current = []

    i = 0
    while i < len(text):
        c = text[i]

        # Skip whitespace
        if c.isspace():
            if current:
                tokens.append("".join(current))
                current = []
            i += 1
            continue

        # Comments
        if text.startswith("//", i):
            if current:
                tokens.append("".join(current))
                current = []
            # skip to end of line
            while i < len(text) and text[i] != "\n":
                i += 1
            continue

        # Braces and equals are standalone tokens
        if c in "{}=":
            if current:
                tokens.append("".join(current))
                current = []
            tokens.append(c)
            i += 1
            continue

        # Quoted string
        if c == '"':
            if current:
                tokens.append("".join(current))
                current = []
            i += 1
            start = i
            while i < len(text) and text[i] != '"':
                i += 1
            tokens.append(text[start:i])
            i += 1
            continue

        # Otherwise accumulate characters
        current.append(c)
        i += 1

    if current:
        tokens.append("".join(current))

    return tokens
class Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected: str | None = None) -> str:
        tok = self.peek()
        if tok is None:
            raise ValueError("Unexpected end of input")
        if expected and tok != expected:
            raise ValueError(f"Expected '{expected}', got '{tok}'")
        self.pos += 1
        return tok

    def parse_block(self) -> dict[str, Any]:
        """
        Parses a block of key/value pairs and nested blocks:
        key = value
        key { ... }
        """
        result: dict[str, Any] = {}

        while self.peek() not in (None, "}"):
            key = self.consume()

            # key = value
            if self.peek() == "=":
                self.consume("=")
                value = self.parse_value()
                result[key] = value
                continue

            # key { block }
            if self.peek() == "{":
                self.consume("{")
                block = self.parse_block()
                self.consume("}")

                # If multiple blocks share the same key → list
                if key in result:
                    if not isinstance(result[key], list):
                        result[key] = [result[key]]
                    result[key].append(block)
                else:
                    result[key] = block
                continue

            raise ValueError(f"Unexpected token after key '{key}': {self.peek()}")

        return result

    def parse_value(self) -> Any:
        tok = self.consume()

        # Try number
        if tok.replace(".", "", 1).isdigit():
            return float(tok) if "." in tok else int(tok)

        # Strings are already unquoted by tokenizer
        return tok