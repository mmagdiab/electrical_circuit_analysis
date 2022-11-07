import numpy as np
import pandas as pd

from branch import Branch
from itertools import chain


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
    # GET NUMBER OF NODES
    nodes = []
    for branch in circuit_branches:
        nodes.append(branch.starting_node, branch.ending_node)
    nodes = set(nodes)
    nodes_count = len(nodes)

    # GET NUMBER OF TREE BRANCHES
    branches_count = nodes_count - 1

    # GET NUMBER OF LINKS
    links_count = len(circuit_branches) - branches_count

    """
    STARTING FROM THE FIRST BRANCH, KEEP ADDING MORE BRANCHES TO THE TREE
    IF THE BRANCH ENDING NODE DOESN'T CONTAIN A NODE ADDED BEFORE
    """
    nodes_add_to_tree = []
    tree_branches = []
    links = []

    for index, branch in enumerate(circuit_branches):
        if index == 0:
            nodes_add_to_tree.append(branch.starting_node, branch.ending_node)
            tree_branches.append(branch)
        else:
            if branch.ending_node not in nodes_add_to_tree:
                nodes_add_to_tree.append(branch.ending_node)
                tree_branches.append(branch)
            else:
                links.append(branch)

    return tree_branches, links
