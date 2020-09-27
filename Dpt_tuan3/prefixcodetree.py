class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Tree:
    def __init__(self):
        self.root = Node(None)
        self.current = None

    def add(self, codeword, symbol):
        self.current = self.root
        for i in range(0, len(codeword) - 1):
            if codeword[i] == 0:
                if self.current.left is None:
                    self.current.left = Node(None)
                self.current = self.current.left
            else:
                if self.current.right is None:
                    self.current.right = Node(None)
                self.current = self.current.right
        end = len(codeword) -1
        if codeword[end] == 0:
            self.current.left = Node(symbol)
        else:
            self.current.right = Node(symbol)

    def find(self, sbin):
        message = ""
        self.current = self.root
        for c in sbin:
            if c== '1' :
                self.current = self.current.right
            else:
                self.current = self.current.left
            if self.current.val is not None:
                message += self.current.val
                self.current = self.root

        return message


class PrefixCodeTree:
    def __init__(self):
        self.tree = Tree()

    def insert(self, codeword, symbol):
        self.tree.add(codeword, symbol)

    def decode(self, encodedData, dataLen):
        sbin = ""
        l = list(encodedData)
        for i in l:
            s2bin = bin(i)[2:].zfill(8)
            sbin += s2bin
        sbin = sbin[:dataLen]
        message = self.tree.find(sbin)
        return message