from enum import Enum
from typing import NamedTuple


class TokenType(Enum):
    operator = 1
    identifier = 2
    number = 3
    string = 4

    def __repr__(self):
        return self.name


class Token(NamedTuple):
    """
    A small unit of language, consisting of a type and value.

    For example, a token with value '+' might be an operator,
    or a token with value '1' might be a number.
    """
    token_type: TokenType
    value: str
