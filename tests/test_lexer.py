import unittest

from src.lexer import Lexer, Token, TokenType


class TestLexer(unittest.TestCase):
    def test_demo_text_1(self):
        text = "print: 4 * var + 1"
        lexer = Lexer()
        tokens = lexer.parse_tokens(text)
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


if __name__ == '__main__':
    unittest.main()
