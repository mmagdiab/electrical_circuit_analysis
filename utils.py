import numpy as np
import pandas as pd

""" Get a valid tree/co-tree of the electrical circuit

Params:
-------
@:param circuit_branches: B x 5 matrix, where B is the number of branches,
        each row defines a particular branch.
        (starting_node, ending_node, voltage_source, current_source, resistance)
@:type list[list[int]]

Returns:
--------
@:return tree_branches: N-1 x 5 matrix, defines a valid tree,
                        where N is the number of nodes.
@:rtype list[list[int]]

@:return links: B - (N-1) x 5 matrix, define co-tree.
@:rtype list[list[int]]
"""


def tree(circuit_branches):
    pass
