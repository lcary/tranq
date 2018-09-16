from typing import List
import unittest

from src.ast import AbstractSyntaxTree, Node
from src.parser import Parser
from src.token import Token, TokenType


def get_child_tokens(node: Node) -> List[Token]:
    return [c.token for c in node.children]


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

    def test_parse_simple_addition_ast(self):
        t0 = Token(token_type=TokenType.identifier, value='print')
        t1 = Token(token_type=TokenType.operator, value=':')
        t2 = Token(token_type=TokenType.number, value='4')
        t3 = Token(token_type=TokenType.operator, value='+')
        t4 = Token(token_type=TokenType.number, value='1')
        tokens = [t0, t1, t2, t3, t4]
        parser = Parser()
        ast = parser.parse_ast(tokens)
        n0 = ast.root
        self.assertEqual(n0.token, t0)
        self.assertEqual(get_child_tokens(n0), [t1])
        n1 = ast.root.children[0]
        self.assertEqual(n1.token, t1)
        self.assertEqual(get_child_tokens(n1), [t3])
        n2 = n1.children[0]
        self.assertEqual(n2.token, t3)
        self.assertEqual(get_child_tokens(n2), [t2, t4])
        n3 = n2.children[0]
        self.assertEqual(n3.token, t2)
        self.assertEqual(get_child_tokens(n3), [])
        n4 = n2.children[1]
        self.assertEqual(n4.token, t4)
        self.assertEqual(get_child_tokens(n4), [])

if __name__ == '__main__':
    unittest.main()
