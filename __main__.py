import sys

from src.lexer import Lexer
from src.parser import Parser


def main():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.get_tokens(*sys.argv[1:])
    ast = parser.parse_ast(tokens)
    print(ast)


if __name__ == '__main__':
    main()
