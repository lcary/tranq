class Lexer(object):

    split_chars = (' ', ':', ';', ',', '(', ')', '{', '}', '[', ']', '=', '<',
                   '>', '|', '@', '#', '$', '%', '^', '&', '*', '?', '-', '+',
                   '*', '/', '~', '`', '"', '\'', '\\')
    group_chars = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>',
        '`': '`',
        '"': '"',
        '\'': '\''
    }
    escape_chars = ('\\', )
    newline_chars = ('\n')
    whitespace_chars = (' ')

    def __init__(self):
        self.tokens = []
        self.temp = ''
        self.start_group = False
        self.end_group_char = None

    def parse_tokens(self, *args, **kwargs):
        for string in args:
            length = len(string)
            for index, char in enumerate(string):
                self.parse_token(char)
                if index == length - 1 and self.temp:
                    self.tokens.append(self.temp)
        return self.tokens

    def parse_token(self, char: str) -> None:

        if self.is_start_group(char):
            return self.parse_start_group(char)

        if self.is_end_group(char):
            return self.parse_end_group(char)

        if self.is_group_part(char):
            return self.parse_group_part(char)

        if self.is_split_char(char):
            return self.parse_split_char(char)
        else:
            return self.parse_generic_char(char)

    def is_start_group(self, char: str) -> bool:
        return not self.start_group and char in self.group_chars

    def parse_start_group(self, char: str) -> None:
        self.start_group = True
        self.end_group_char = self.group_chars[char]
        self.tokens.append(char)
        return

    def is_end_group(self, char: str) -> bool:
        return self.start_group and char == self.end_group_char

    def parse_end_group(self, char: str) -> None:
        self.tokens.append(self.temp)
        self.tokens.append(char)
        self.temp = ''
        self.start_group = False
        self.end_group_char = None
        return

    def is_group_part(self, char: str) -> bool:
        return self.start_group and char != self.end_group_char

    def parse_group_part(self, char: str) -> None:
        self.temp += char
        return

    def is_split_char(self, char: str) -> bool:
        return char in self.split_chars

    def parse_split_char(self, char: str) -> None:
        if self.temp != '':
            self.tokens.append(self.temp)
            self.temp = ''
        if char not in self.whitespace_chars:
            self.tokens.append(char)
        return

    def parse_generic_char(self, char: str) -> None:
        self.temp += char
        return
