import numpy as np
import pandas as pd

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
    # SO :  RHS * I_L = LHS      SO :   I_L = (RHS)^-1  * LHS
    I_L = np.linalg.inv(RHS) * LHS
    # 2- Second Find J_B from :   J_B = B.T * I_L
    J_B = np.dot(B.T, I_L)
    # 3- Third  Find V_B from  :  V_B = Z_B * (J_B+ I_B) - E_B
    # we should  reshape the size of I_B , E_B from (4,) to (4,1)
    I_B = np.reshape(I_B, (-1, 1))
    E_B = np.reshape(E_B, (-1, 1))
    V_B = np.dot(Z_B, (J_B + I_B)) - E_B
    # just for enhancement we wil convert V_B, J_B to Pandas Data Frame for good display
    V_B = pd.DataFrame(V_B)
    J_B = pd.DataFrame(J_B)
    # then we will return just he first column of each one of them
    return V_B[0], J_B[0]


# ----------------------------------------------------------
# REQUIRED :  A_tree, A_link , Z_B , E_B , I_B
# --------------------- FOR TEST [tie_set_method] ----------------
A_tree = [[1, 1], [0, -1], [-1, 0]]
A_link = [[-1, 0], [0, 1], [1, -1]]
Z_B = [[5, 0, 0, 0], [0, 10, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]
E_B = [0, 0, 10, 0]
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
