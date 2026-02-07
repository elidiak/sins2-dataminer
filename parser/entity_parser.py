from pathlib import Path

from .tokenizer import tokenize
from .parser_core import Parser
from .model_builder import build_entity
from ..models.entity import Entity

def parse_entity(path: Path) -> Entity:
    text = path.read_text(encoding="utf-8")
    tokens = tokenize(text)
    parser = Parser(tokens)
    struct = parser.parse_block()
    return build_entity(struct, name=path.stem)