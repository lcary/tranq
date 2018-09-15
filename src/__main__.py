from .lexer import Lexer


def main():
    lexer = Lexer()
    tokens = lexer.parse_tokens("print: 4 * var + 1")
    print(tokens)


if __name__ == '__main__':
    main()
