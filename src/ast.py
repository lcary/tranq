from typing import Optional

from .token import Token


class Node(object):
    """
    Simple binary tree node for an abstract syntax tree,
    where each node is a Token.
    """

    def __init__(self,
                 data: Optional[Token] = None,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None) -> None:
        """
        Initialize the node of an abstract syntax tree.

        Note: type hints must use strings, since `Node` does not exist yet.
        """
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.data: Optional[Token] = None


class AbstractSyntaxTree(object):

    def __init__(self, root: Node) -> None:
        self.root: Node = root
