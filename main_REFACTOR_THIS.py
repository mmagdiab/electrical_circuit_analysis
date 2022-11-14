from utils import *
from branch import *



def test_tree():
    a = Branch(3, 1)
    b = Branch(1, 2)
    c = Branch(2, 3)
    d = Branch(4, 1)
    e = Branch(2, 4)
    f = Branch(3, 4)
    
    circuit_branches = [a, b, c, d, e, f]

    tree_branches, links = tree(circuit_branches)
    
    for branch in tree_branches:
        print(branch)
    print('0000000000000000000-------------------0000000000000000')
    for branch in links:
        print(branch)

        
    
if __name__ == '__main__':
    test_tree()
