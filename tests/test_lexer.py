import unittest

from src.lexer import Lexer, Token, TokenType


class TestLexer(unittest.TestCase):
    def test_demo_text_1(self):
        text = "print: 4 * var + 1"
        lexer = Lexer()
        tokens = lexer.parse_tokens(text)
        expect = [
            Token(token_type=TokenType.variable, value='print'),
            Token(token_type=TokenType.operator, value=':'),
            Token(token_type=TokenType.variable, value='4'),
            Token(token_type=TokenType.operator, value='*'),
            Token(token_type=TokenType.variable, value='var'),
            Token(token_type=TokenType.operator, value='+'),
            Token(token_type=TokenType.unknown, value='1')]
        print(expect)
        self.assertEqual(tokens, expect)


if __name__ == '__main__':
    unittest.main()
