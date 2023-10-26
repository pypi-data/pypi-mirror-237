from itertools import product
import numpy as np
import Quanthon as qt

def get_all_pauli(n):

    '''Returns a list of all possible Pauli strings of length n (number of qubits)'''
    pauli = 'IXYZ'
    # all_paulis = list(product(pauli, pauli, repeat=int(n/2)))
    perms = [''.join(p) for p in product(pauli, repeat=n)]
    return perms


def _get_single_rotations(op):
    
    if op == 'X':
        return ('H')
    if op == 'Y':
        return ('Sdag', 'H')
    if op == 'Z' or op == 'I':
        return ('I')
    else:
        raise ValueError(f'Invalid Pauli operator: {op}')


def _no_pauli_after_i(pauli_str):

    detected_I = False
    for op in pauli_str:
        if not detected_I:
            if op == 'I':
                detected_I = True
                continue
            else:
                continue
        if op != 'I':
            return False
    return True

def get_swaps(pauli_str, swap_list):

    if _no_pauli_after_i(pauli_str):
        return ''.join(pauli_str), swap_list

    found_I = False
    pauli_str = list(pauli_str)
    for i, op in enumerate(pauli_str):
        if op == 'I':
            found_I = True
            I_indx = i
            continue
        if found_I:
            if op != 'I':
                non_i_indx = i
            pauli_str[I_indx] = op 
            pauli_str[non_i_indx]= 'I'
            swap_list.append((I_indx, non_i_indx))
            found_I = False

    return get_swaps(pauli_str, swap_list)

def get_cnots(pauli_str): 

    if not _no_pauli_after_i:
        raise ValueError('Pauli string must not have any Pauli operator after I.')
    cnot_pairs = []

    for i in range(len(pauli_str)-1):
        if pauli_str[i+1] == 'I':
            break
        cnot_pairs.append((i+1, i))
        
    return cnot_pairs

def change_basis(pauli_str):

    for i in pauli_str:
        if i not in 'IXYZ':
            raise ValueError(f'Invalid Pauli operator: {i}')

    swaped_pauli, swaps = get_swaps(pauli_str, [])
    cnot_pairs = get_cnots(swaped_pauli)

    change_basis_op = []
    for pair in cnot_pairs:
        change_basis_op.append(('cnot', pair))

    for i, op in enumerate(pauli_str):
        change_basis_op.append([(_get_single_rotations(op), i)])
    
    for pair in swaps:
        change_basis_op.append(('swap', pair))
    
    return change_basis_op


def expectation(qc, pauli_ops, n_shots=1000):

    for pauli_str in pauli_ops:
        change_basis_op_lst = change_basis(pauli_str)
    
    
if __name__ == '__main__':
    # Test Pauli operators
    coeffs = {'IZ':0.5 , 'ZI': 0.5 , 'XX':0.5, 'YY':-0.5}
    # print(get_all_pauli(2))
    # pauli_str = 'YY'
    # for op in pauli_str:
    #     rotation_ops = get_rotations(op)
    #     print(rotation_ops)

    a = 'X'
    b = 'Y'
    c = 'IZ'
    d = 'ZXZZ'
    # test no_op_after_i
    
    # print(no_pauli_after_i(a), no_pauli_after_i(b), no_pauli_after_i(c))

    # print(no_pauli_after_i(d))

    # PASSED

    # test get_swaps
    
    # for i in [a, b, c, d]:
    #     result, swaps = get_swaps(i, [])
    #     result = "".join(result)
    #     print(result, swaps)
    
    # PASSED

    # test get_cnots

    # for paulis in [a, b, c, d]:
    #     result, swaps = get_swaps(paulis, [])
    #     result = "".join(result) 
    #     print(result)
    #     cnot_pairs = get_cnots(result)
    #     print(f"cnots: {paulis}", cnot_pairs)

    # PASSED

    # test change_basis

    for i in [a, b, c, d]:
        big_op = change_basis(i)
        print(f"big_op for {i}", big_op)
    