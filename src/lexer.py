from typing import List, Optional

from .token import Token, TokenType


class Lexer(object):
    """
    Produces ordered lists of tokens from input text.

    Inspired by https://medium.freecodecamp.org/the-programming-language-pipeline-91d3f449c919  # noqa: E501
    """

    split_chars = (' ', ':', ';', ',', '(', ')', '{', '}', '[', ']', '=', '<',
                   '>', '|', '@', '#', '$', '%', '^', '&', '*', '?', '-', '+',
                   '/', '~', '`', '"', '\'', '\\')
    group_chars = {
        '(': ')',
        '{': '}',
        '[': ']',
        '`': '`',
        '"': '"',
        '\'': '\''
    }
    escape_chars = ('\\', )
    newline_chars = ('\n')
    whitespace_chars = (' ')

    def __init__(self) -> None:
        self.tokens: List[Token] = []
        self.temp: str = ''
        self.start_group: bool = False
        self.end_group_char: Optional[str] = None

    def get_tokens(self, *args, **kwargs) -> List[Token]:
        """
        Returns an ordered list of tokens for given input text.
        """
        for text in args:
            for char in text:
                self.set_tokens(char)
            self.flush_temp()

        return self.tokens

    def set_tokens(self, char: str) -> None:
        """
        Updates `self.tokens` based on the input character and
        returning nothing. The returns are used to exit the function early.
        """
        if self.is_start_group(char):
            self.set_start_group(char)
            return

        if self.is_end_group(char):
            self.set_end_group(char)
            return

        if self.is_group_part(char):
            self.set_group_part(char)
            return

        if self.is_split_char(char):
            self.set_split_char(char)
            return
        else:
            self.set_generic_char(char)
            return

        raise ValueError(
            'Edge case encountered: token ({}) '
            'not parsed during Lexer state: ({})'.format(char, self.__dict__))

    def is_start_group(self, char: str) -> bool:
        return not self.start_group and char in self.group_chars

    def set_start_group(self, char: str) -> None:
        self.start_group = True
        self.end_group_char = self.group_chars[char]
        self.tokens.append(Token(TokenType.operator, char))
        return

    def is_end_group(self, char: str) -> bool:
        return self.start_group and char == self.end_group_char

    def set_end_group(self, char: str) -> None:
        self.tokens.append(Token(TokenType.identifier, self.temp))
        self.tokens.append(Token(TokenType.operator, char))
        self.temp = ''
        self.start_group = False
        self.end_group_char = None
        return

    def is_group_part(self, char: str) -> bool:
        return self.start_group and char != self.end_group_char

    def set_group_part(self, char: str) -> None:
        self.temp += char
        return

    def is_split_char(self, char: str) -> bool:
        return char in self.split_chars

    def set_split_char(self, char: str) -> None:
        self.flush_temp()
        if char not in self.whitespace_chars:
            self.tokens.append(Token(TokenType.operator, char))
        return

    def set_generic_char(self, char: str) -> None:
        self.temp += char
        return

    def flush_temp(self):
        if self.temp != '':
            try:
                int(self.temp)
            except ValueError:
                self.tokens.append(Token(TokenType.identifier, self.temp))
            else:
                self.tokens.append(Token(TokenType.number, self.temp))
            self.temp = ''
