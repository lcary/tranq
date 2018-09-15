from typing import List

from .ast import AbstractSyntaxTree, Node
from .token import Token


class Parser(object):
    """
    Adds structure to an ordered list of tokens produced
    by the Lexer.

    Primary responsibilities:
     - Take groupings of tokens into account.
     - Order of operations (PEMDAS, plus assignment and other operators).

    Returns an `AbstractSyntaxTree`.
    """

    def parse_ast(self, tokens: List[Token]) -> AbstractSyntaxTree:
        """
        Returns an `AbstractSyntaxTree` for an ordered list of tokens.
        """
        ast = AbstractSyntaxTree()
        root_parsed = False
        for token in tokens:
            if not root_parsed:
                ast.root = Node(token)
                root_parsed = True
                continue
            # TODO: parse children nodes, need to check whether
            # binary/unary/etc-ary operator or an identifier

        return ast
