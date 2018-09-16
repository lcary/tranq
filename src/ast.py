import hashlib
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
                 parent: Optional['Node'] = None,
                 children: Optional[List['Node']] = None) -> None:
        """
        Initialize the node of an abstract syntax tree.
        """
        if children is None:
            children = []

        self.token: Optional[Token] = token
        self.parent: Optional['Node'] = parent
        self.children: List['Node'] = children
        self._siblings: Optional[List[Node]] = None

    def __repr__(self):
        try:
            num_children = len(self.children)
        except TypeError:
            num_children = 0
        return '{}({}, children={})'.format(
            self.__class__.__name__, self.token, num_children)

    def add_children(self, children: List['Node']) -> None:
        self.children.extend(children)
        for child in self.children:
            child.parent = self

    @property
    def hash(self):
        hash_object = hashlib.md5(str(self.__dict__))
        return hash_object.hexdigest()

    @property
    def siblings(self) -> Optional[List['Node']]:
        if self.parent:
            return list(set(self.parent.children) - set([self]))
        else:
            return None

    @property
    def is_only_child(self) -> bool:
        if self.parent:
            return len(self.parent.children) == 1
        raise self.orphan_error

    @property
    def is_first_child(self) -> bool:
        if self.parent:
            return self.parent.children.index(self) == 0
        raise self.orphan_error

    @property
    def is_last_child(self) -> bool:
        if self.parent:
            last_index = len(self.parent.children) - 1
            return self.parent.children.index(self) == last_index
        raise self.orphan_error

    @property
    def orphan_error(self) -> Exception:
        return ValueError(
            'Orphaned child node ({}) expected '
            'to have a parent but none was found.'.format(self))


class AstRepr(object):
    tab = '       '
    pipe = ' │'
    fork = ' ├── '
    node = ' └── '


class AbstractSyntaxTree(object):

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root: Optional[Node] = root

    def traverse(self, node: Node, depth=0):
        if node.children:
            for child in node.children:
                yield child, depth
                yield from self.traverse(child, depth=(depth + 1))

    def __repr__(self):
        lines = [str(self.root.token)]
        depth_offset = 0

        def get_margin(depth):
            return AstRepr.tab * (depth - depth_offset)

        for node, depth in self.traverse(self.root):
            token = node.token
            if node.is_only_child:
                depth_offset += 1
                margin = get_margin(depth)
                lines.append(margin + AstRepr.pipe + '\n' + str(token))
            elif node.is_last_child:
                margin = get_margin(depth)
                lines.append(margin + AstRepr.node + str(token))
            else:
                margin = get_margin(depth)
                lines.append(margin + AstRepr.fork + str(token))

        return '\n'.join(lines) + '\n'
