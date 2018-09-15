from typing import List

from .token import Token


class Parser(object):
    """
    Adds structure to an ordered list of tokens produced
    by the Lexer.
    """

    def parse_tokens(self, tokens: List[Token]):
        pass
