import unittest

from src.lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_demo_text_1(self):
        text = "print: 4 * var + 1"
        lexer = Lexer()
        tokens = lexer.parse_tokens(text)
        expect = ['print', ':', '4', '*', 'var', '+', '1']
        self.assertEqual(tokens, expect)


if __name__ == '__main__':
    unittest.main()
