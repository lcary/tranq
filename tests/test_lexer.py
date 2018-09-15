import unittest

from src.lexer import Lexer
from src.token import Token, TokenType


class TestLexer(unittest.TestCase):
    def test_oneline_computation(self):
        text = "print: 4 * var + 1"
        lexer = Lexer()
        tokens = lexer.get_tokens(text)
        expect = [
            Token(token_type=TokenType.identifier, value='print'),
            Token(token_type=TokenType.operator, value=':'),
            Token(token_type=TokenType.number, value='4'),
            Token(token_type=TokenType.operator, value='*'),
            Token(token_type=TokenType.identifier, value='var'),
            Token(token_type=TokenType.operator, value='+'),
            Token(token_type=TokenType.number, value='1')]
        for i in tokens:
            print(i)
        self.assertEqual(tokens, expect)

    def test_multiline_computation(self):
        text = """
        var = 2
        x = 4 * var"
        print: x / 3
        """
        pass

    def test_collection_of_numbers(self):
        text = "l = [1, 2, 3]"
        pass

    def test_nested_collection(self):
        # test collection of collections
        text = """
        l = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
        """
        pass

    def test_oneline_loop(self):
        text = "for i in [1, 2, 3]: print: i"
        pass

    def test_multline_loop(self):
        text = """
        for i in [1, 2, 3]:
        print: i"
        """
        pass


if __name__ == '__main__':
    unittest.main()
