from    lexer import Lexer


def main():
    l = Lexer()
    t = l.parse_tokens("print: 4 * var + 1")
    print(t)

if __name__ == '__main__':
    main()
