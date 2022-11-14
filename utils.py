from random import shuffle
import networkx as nx
import matplotlib.pyplot as plt


""" Get a valid tree/co-tree of the electrical circuit

Params:
-------
@:param circuit_branches: B x 5 matrix, where B is the number of branches,
        each row defines a particular branch.
        (starting_node, ending_node, voltage_source, current_source, resistance)
@:type list[Branch]

Returns:
--------
@:return tree_branches: N-1 x 5 matrix, defines a valid tree,
                        where N is the number of nodes.
@:rtype list[Branch]

@:return links: B - (N-1) x 5 matrix, define co-tree.
@:rtype list[Branch]
"""


def tree(circuit_branches):
    # Next line to get a random tree each time
    shuffle(circuit_branches)
    # GET NUMBER OF NODES
    nodes = []
    for branch in circuit_branches:
        nodes.append(branch.starting_node)
        nodes.append(branch.ending_node)
    nodes = set(nodes)
    nodes_count = len(nodes)

    # GET NUMBER OF TREE BRANCHES
    branches_count = nodes_count - 1

    # GET NUMBER OF LINKS
    # links_count = len(circuit_branches) - branches_count

    """
    STARTING FROM THE FIRST BRANCH, KEEP ADDING MORE BRANCHES TO THE TREE
    IF THE BRANCH ENDING NODE DOESN'T CONTAIN A NODE ADDED BEFORE
    """
    nodes_added_to_tree = []
    tree_branches = []

    # Initially insert first branch to the tree
    nodes_added_to_tree.append(circuit_branches[0].starting_node)
    nodes_added_to_tree.append(circuit_branches[0].ending_node)
    tree_branches.append(circuit_branches[0])

    while len(tree_branches) < branches_count:
        for index, branch in enumerate(circuit_branches):
            if index == 0:
                continue
            if branch.ending_node not in nodes_added_to_tree and branch.starting_node in nodes_added_to_tree:
                nodes_added_to_tree.append(branch.ending_node)
                tree_branches.append(branch)

    links = [branch for branch in circuit_branches if branch not in tree_branches]
    return tree_branches, links

def generate_graph(tree_branches, links):
    
    # Create a Directed Graph object
    G = nx.DiGraph()

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
        edgesList.append((i.starting_node, i.ending_node,str("Tree\n") + str(2)+" mA, " + str(3)+" V" ))
    
    
    for i in links:
        #These str(4), str(5) should be replaced by the its corresponding values in the Voltage and Current matrices
        edgesList.append((i.starting_node, i.ending_node, str("Link\n") +str(4)+" mA, " + str(5)+" V" ))
    
    
    for i in edgesList:
        G.add_edge(i[0], i[1],edgesList=i[2])
    
    print("Node List :",G.nodes())
    print("Edge List :",G.edges())
    
    pos = nx.spring_layout(G)
    colors = range(20)
    nx.draw(G,alpha=1, with_labels = True, node_color= 'green')     
    #nx.draw(G,pos, edge_color = colors,width =4, edge_cmap= plt.cm.Blues)
    nx.draw_networkx_edge_labels(G,pos, font_size=8,edge_labels=nx.get_edge_attributes(G,'edgesList'))
    
    plt.show()