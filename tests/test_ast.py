from textwrap import dedent
import unittest

from src.ast import AbstractSyntaxTree, Node
from src.token import Token, TokenType


class TestAbstractSyntaxTree(unittest.TestCase):
    def test_print_simple_addition_repr(self):
        n0 = Node(Token(token_type=TokenType.identifier, value='print'),)
        n1 = Node(Token(token_type=TokenType.operator, value=':'))
        n2 = Node(Token(token_type=TokenType.number, value='4'))
        n3 = Node(Token(token_type=TokenType.operator, value='+'))
        n4 = Node(Token(token_type=TokenType.number, value='1'))

        ast = AbstractSyntaxTree(n0)
        n0.add_children([n1])
        n1.add_children([n3])
        n3.add_children([n2, n4])

        expect = dedent('''\
        Token(token_type=identifier, value='print')
         │
        Token(token_type=operator, value=':')
         │
        Token(token_type=operator, value='+')
         ├── Token(token_type=number, value='4')
         └── Token(token_type=number, value='1')
        ''')

        self.assertEqual(repr(ast), expect)

if __name__ == '__main__':
    unittest.main()
