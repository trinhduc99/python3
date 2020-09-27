from prefixcodetree import *
codebook = {
    'x1' : [0],
    'x2' : [1,0,0],
    'x3' : [1,0,1],
    'x4' :[1,1]
}

codeTree = PrefixCodeTree()
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd5\x6f\x2e',21)
print(message)