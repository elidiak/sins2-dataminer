from typing import Any

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
        result: dict[str, Any] = {}

        while self.peek() not in (None, "}"):
            key = self.consume()

            if self.peek() == "=":
                self.consume("=")
                value = self.parse_value()
                result[key] = value
                continue

            if self.peek() == "{":
                self.consume("{")
                block = self.parse_block()
                self.consume("}")

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

        if tok.replace(".", "", 1).isdigit():
            return float(tok) if "." in tok else int(tok)

        return tok