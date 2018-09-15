import sys

from src.lexer import Lexer


def main():
    lexer = Lexer()
    tokens = lexer.get_tokens(*sys.argv[1:])
    print(tokens)


if __name__ == '__main__':
    main()
