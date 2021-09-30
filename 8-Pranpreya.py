# Assignment 8: Binary Search Tree
# Pranpreya Samasutthi (st122602)

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
                node.l.p = node
                print('add', val, 'parent is ', node.l.p.v)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
                node.r.p = node
                print('add', val, 'parent is ', node.r.p.v)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            return self._find(val, node.l)
        elif val > node.v and node.r is not None:
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    def successorTree(self, val):
        node = self.find(val)
        if self.root is not None:
            return self._successorTree(node)
        else:
            return None

    def _successorTree(self, node):
        # print('node.v', node.v)
        # print('node.p.v', node.p.v)
        if node.r is not None:
            return self.minimumTree(node.r)
        y = node.p
        # print('parent of successor', y.v)
        while y is not None and node == y.r:
            node = y
            y = y.p
        return y

    def minimumTree(self, node):
        if self.root is not None:
            return self._minimumTree(node)
        else:
            return None

    def _minimumTree(self, node):
        while node.l is not None:
            node = node.l
        return node


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print('Find 3:', tree.find(3).v)
print('Find 10:', tree.find(10))

print('Successor 3 is', tree.successorTree(3).v)
print('Successor 4 is', tree.successorTree(4).v)
print('Successor 8 is', tree.successorTree(8))

