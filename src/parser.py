from typing import List

from .ast import AbstractSyntaxTree, Node
from .token import Token, TokenType


class Parser(object):
    """
    Adds structure to an ordered list of tokens produced
    by the `Lexer`.

    Primary responsibilities:
     - Take groupings of tokens into account.
     - Order of operations (PEMDAS, plus assignment and other operators).

    Returns an `AbstractSyntaxTree`.
    """

    def parse_ast(self, tokens: List[Token]) -> AbstractSyntaxTree:
        """
        Returns an `AbstractSyntaxTree` for an ordered list of tokens.
        """
        root = Node(tokens[0])
        ast = AbstractSyntaxTree(root)
        last_parent: Node = root
        for index, token in enumerate(tokens[1:]):
            node = Node(token)
            if token.token_type in [TokenType.identifier,
                                    TokenType.number,
                                    TokenType.string]:
                last_parent.add_child(node)
                continue
            if token.token_type == TokenType.operator:
                if token.value in ('+', '-', '*', '/', '<', '>'):
                    ast.insert_parent_into_hierarchy(node, last_parent)
                else:
                    last_parent.add_child(node)
                last_parent = node

        return ast
