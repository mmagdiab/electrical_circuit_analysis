from utils import *
from branch import *

import networkx as nx
import matplotlib.pyplot as plt

# Create a Directed Graph
G = nx.DiGraph()


def test_tree():
    a = Branch(3, 1)
    b = Branch(1, 2)
    c = Branch(2, 3)
    d = Branch(4, 1)
    e = Branch(2, 4)
    f = Branch(3, 4)
    Jb = [23,54,766,34,45,2]
    Vb = [23,4,56,7,554,132]
    circuit_branches = [a, b, c, d, e, f]

    tree_branches, links = tree(circuit_branches)
    
    for branch in tree_branches:
        print(branch)
    print('0000000000000000000-------------------0000000000000000')
    for branch in links:
        print(branch)

        
    #Count Nodes and add these nodes to the graph
    nodeList = []
    for node in tree_branches:
        nodeList.append(node.starting_node)
        nodeList.append(node.ending_node)
        G.add_node(node.starting_node)
        G.add_node(node.ending_node)
    
    # remove any douplicated nodes
    nodeList = set(nodeList)
    
    
    #edges (Branch data) contains starting, ending, current in branch, voltage on branch
    edgesList = []
    for i in tree_branches:
        #These str(2), str(3) should be replaced by the its corresponding values in the Voltage and Current matrices
        edgesList.append((i.starting_node, i.ending_node, str(2)+" mA, " + str(3)+" V" ))
    
    
    for i in links:
        #These str(4), str(5) should be replaced by the its corresponding values in the Voltage and Current matrices
        edgesList.append((i.starting_node, i.ending_node, str(4)+" mA, " + str(5)+" V" ))
    
    
    for i in edgesList:
        G.add_edge(i[0], i[1],edgesList=i[2])
    
    print("Node List :",G.nodes())
    print("Edge List :",G.edges())
    
    pos = nx.spring_layout(G)
    colors = range(20)
    nx.draw(G,alpha=1, with_labels = True, node_color= 'green')     
    #nx.draw(G,pos, edge_color = colors,width =4, edge_cmap= plt.cm.Blues)
    nx.draw_networkx_edge_labels(G,pos, font_size=15,edge_labels=nx.get_edge_attributes(G,'edgesList'))
    
    plt.show()
if __name__ == '__main__':
    test_tree()
