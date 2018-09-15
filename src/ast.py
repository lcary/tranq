from typing import List, Optional

from .token import Token


class Node(object):
    """
    Node for an abstract syntax tree, where each node is a `Token`
    that can optionally link to other tokens.
    """

    # Note: some type hints must use strings, since `Node` does not exist yet.
    def __init__(self,
                 token: Optional[Token] = None,
                 children: Optional[List['Node']] = None) -> None:
        """
        Initialize the node of an abstract syntax tree.
        """
        self.token: Optional[Token] = token
        self.children: Optional[List['Node']] = children

    def __repr__(self):
        try:
            num_children = len(self.children)
        except TypeError:
            num_children = 0
        return '{}({}, children={})'.format(
            self.__class__.__name__, self.token, num_children)


class AbstractSyntaxTree(object):
    pipe = ' │'
    fork = ' ├── '
    node = ' └── '

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root: Optional[Node] = root

    def _traverse(self, node: Node, lines, level=0):
        margin = '       ' * level
        if node.children:
            size = len(node.children)
            if size == 1:
                child = node.children[0]
                lines.append(margin + self.pipe + '\n' + str(child.token))
                self._traverse(child, lines, level=level)
            else:
                for index, child in enumerate(node.children):
                    if index < (size - 1):
                        lines.append(margin + self.fork + str(child.token))
                        self._traverse(child, lines, level=(level + 1))
                    else:
                        # last child
                        lines.append(margin + self.node + str(child.token))
                        self._traverse(child, lines, level=(level + 1))

    def __repr__(self):
        print(traverse(self.root))
        tree = ''
        # indent_level = 0
        tree += str(self.root.token)
        tree += '\n'

        lines = []
        if self.root.children is not None:
            self._traverse(self.root, lines)
        tree += '\n'.join(lines)

        tree += '\n'
        return tree


def traverse(node, level=0):
    print('Node at level {}: {}'.format(level, node))
    level += 1
    if node.children:
        for child in node.children:
            traverse(child, level=level)
