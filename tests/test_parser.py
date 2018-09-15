import unittest

from src.ast import AbstractSyntaxTree, Node
from src.parser import Parser
from src.token import Token, TokenType


class TestParser(unittest.TestCase):
    @unittest.skip("finish working on Parser")
    def test_print_computation(self):
        parser = Parser()
        tokens = [
            Token(token_type=TokenType.identifier, value='print'),
            Token(token_type=TokenType.operator, value=':'),
            Token(token_type=TokenType.number, value='4'),
            Token(token_type=TokenType.operator, value='*'),
            Token(token_type=TokenType.identifier, value='var'),
            Token(token_type=TokenType.operator, value='+'),
            Token(token_type=TokenType.number, value='1')]
        ast = parser.parse_ast(tokens)
        pass
        # self.assertEqual(ast, expect)

if __name__ == '__main__':
    unittest.main()
