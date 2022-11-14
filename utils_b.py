import numpy as np
import pandas as pd
from utils import *
from branch import *
'''
GOALS        : Get V_B, J_B
REQUIREMENTS : A_Tree , A_Link , Z_B , E_B , I_B
STEPS        : 
        1 - Calculate Cut_Set_matrix From A_Tree, A_Link
        2 - Calculate Tie_Set_Matix From Cut_Set_matrix
        3 - Calculate  V_B,J_B from Tie_Set_Matrix 
'''
# ------------------------------------
#  Calculate cut_set_matrix : Take [A_tree, A_link] and return C_Link to pass it to [tie_set_matrix_from_cut_set_matrix] function


def cut_set_matrix_from_incidence_matrix(A_tree, A_link):
    # here I dropped the last row of incidence_matrix
    A_tree = pd.DataFrame(A_tree).iloc[0:-1, :]
    A_link = pd.DataFrame(A_link).iloc[0:-1, :]
    A_tree_inv = (np.linalg.inv(A_tree))
    C_Link = np.dot(A_tree_inv, A_link)
    C_tree = np.identity(C_Link.shape[1])
    C_matrix = np.concatenate((C_tree, C_Link), axis=1)
    C_matrix = pd.DataFrame(C_matrix, dtype='int64')
    return C_Link  # C_matrix , C_tree,


# ------------------------------------
#  Calculate tie_set_matrix and return tie_set_matrix to pass it to [tie_set_method] function
def tie_set_matrix_from_cut_set_matrix(C_link):
    C_link = np.array(C_link)
    B_tree = -(C_link.T)
    B_Link = np.identity(B_tree.shape[1])
    tie_set_matrix = np.concatenate((B_tree, B_Link), axis=1)
    tie_set_matrix = pd.DataFrame(tie_set_matrix, dtype='int64')
    return tie_set_matrix


# tie_set_method : Takes numpy array of tie_set_matrix, Z_B, E_B, I_B,and return  V_B, J_B as pandas Data Frame
def tie_set_method(tie_set_matrix, Z_B, E_B, I_B):
    # 1- First Find I_L from:       B * Z_B * B.T  * I_L = B * E_B - B * Z_B * IB
    B = np.array(tie_set_matrix)
    RHS = np.dot(np.dot(B, Z_B), B.T)
    LHS = (np.dot(B, E_B)) - (np.dot(np.dot(B, Z_B), I_B))
    LHS = np.reshape(LHS, (-1,1))
    # SO :  RHS * I_L = LHS      SO :   I_L = (RHS)^-1  * LHS
    I_L = np.dot(np.linalg.inv(RHS), LHS)
    I_L = np.ceil(I_L)
    # 2- Second Find J_B from :   J_B = B.T * I_L
    J_B = np.dot(B.T, I_L)
    # 3- Third  Find V_B from  :  V_B = Z_B * (J_B+ I_B) - E_B
    # we should  reshape the size of I_B , E_B from (4,) to (4,1)
    I_B = np.reshape(I_B, (-1, 1))
    E_B = np.reshape(E_B, (-1, 1))
    V_B = np.dot(Z_B, (J_B + I_B)) - E_B
    # just for enhancement we wil convert V_B, J_B to Pandas Data Frame for good display
    V_B = list(np.ravel(V_B))
    J_B = list(np.ravel(J_B))
    V_B = [round(abs(value), 2) for value in V_B]
    J_B = [round(abs(value), 2) for value in J_B]
    # then we will return just he first column of each one of them
    return V_B, J_B


# FOR TESTING ONLY
if __name__ == '__main__':
    # ----------------------------------------------------------
    # REQUIRED :  A_tree, A_link , Z_B , E_B , I_B
    # --------------------- FOR TEST [tie_set_method] ----------------
    # A_tree = [[1, 1], [0, -1], [-1, 0]]
    # A_link = [[-1, 0], [0, 1], [1, -1]]
    A_tree = [[-1, 1], [0, -1], [1, 0]]
    A_link = [[1, 0], [0, 1], [-1, -1]]
    Z_B = [[5, 0, 0, 0], [0, 10, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]
    E_B = [10, 0, 0, 0]
    I_B = [0, 0, 0, 0]
    # -------------------- DISPLAY -----------------------------
    # print('-----------------------')
    C_link = cut_set_matrix_from_incidence_matrix(A_tree=A_tree, A_link=A_link)
    # print(C_link)
    print('-----------------------')
    tie_set_matrix = tie_set_matrix_from_cut_set_matrix(C_link=C_link)
    print("B_Matrix : \n", tie_set_matrix)
    print('-----------------------')
    V_B, J_B = tie_set_method(tie_set_matrix=tie_set_matrix, Z_B=Z_B, E_B=E_B, I_B=I_B)
    print("V_B : ")
    print(V_B)
    print('-----------------------')
    print("J_B : ")
    print(J_B)
    print('-----------------------')

    # Z_B = [[5, 0, 0, 0], [0, 10, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]
    # E_B = [0, 0, 10, 0]
    # I_B = [0, 0, 0, 0]

    Z_B = [[5, 0, 0, 0], [0, 10, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]
    E_B = [10, 0, 0, 0]
    I_B = [0, 0, 0, 0]
    print('NEW ===============')
    a = Branch(1, 3, 1, 10, 0, 5)
    b = Branch(2, 1, 3, 0, 0, 5)
    c = Branch(0, 1, 2, 0, 0, 10)
    d = Branch(3, 2, 3, 0, 0, 5)
    circuit_branches = [b, d, c, a]
    tree_branches, links = tree(circuit_branches)
    print('tree:')
    for branch in tree_branches:
        print(branch)
    print('links:')
    for link in links:
        print(link)
    i_b = get_i_b(circuit_branches)
    print('ib:', i_b)
    e_b = get_e_b(circuit_branches)
    print('eb:', e_b)
    z_b = get_z_b(circuit_branches)
    print('zb:', z_b)

    # -------------------- DISPLAY -----------------------------
    # print('-----------------------')
    a_matrix_tree, a_matrix_links = get_a_matrix(circuit_branches)
    print('a_matrix_tree', a_matrix_tree)
    print('a_matrix_links', a_matrix_links)
    C_link = cut_set_matrix_from_incidence_matrix(A_tree=a_matrix_tree, A_link=a_matrix_links)
    # print(C_link)
    print('-----------------------')
    tie_set_matrix = tie_set_matrix_from_cut_set_matrix(C_link=C_link)
    print("B_Matrix : \n", tie_set_matrix)
    print('-----------------------')
    V_B, J_B = tie_set_method(tie_set_matrix=tie_set_matrix, Z_B=z_b, E_B=e_b, I_B=i_b)
    print("V_B : ")
    print(V_B)
    print('-----------------------')
    print("J_B : ")
    print(J_B)
    print('-----------------------')


def solve(circuit_branches):
    i_b = get_i_b(circuit_branches)
    e_b = get_e_b(circuit_branches)
    z_b = get_z_b(circuit_branches)
    a_matrix_tree, a_matrix_links = get_a_matrix(circuit_branches)
    c_link = cut_set_matrix_from_incidence_matrix(A_tree=a_matrix_tree, A_link=a_matrix_links)
    tie_set_matrix = tie_set_matrix_from_cut_set_matrix(C_link=c_link)
    V_B, J_B = tie_set_method(tie_set_matrix=tie_set_matrix, Z_B=z_b, E_B=e_b, I_B=i_b)
    return V_B, J_B