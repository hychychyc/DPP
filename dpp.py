import numpy as np
import math


def dpp(kernel_matrix, max_length, epsilon=1E-10):
    """
    Our proposed fast implementation of the greedy algorithm
    :param kernel_matrix: 2-d array
    :param max_length: positive int
    :param epsilon: small positive scalar
    :return: list
    """
    item_size = kernel_matrix.shape[0]
    cis = np.zeros((max_length, item_size))
    di2s = np.copy(np.diag(kernel_matrix))
    selected_items = list()
    selected_item = np.argmax(di2s)
    selected_items.append(selected_item)
    while len(selected_items) < max_length:
        k = len(selected_items) - 1
        ci_optimal = cis[:k, selected_item]
        di_optimal = math.sqrt(di2s[selected_item])
        elements = kernel_matrix[selected_item, :]
        eis = (elements - np.dot(ci_optimal, cis[:k, :])) / di_optimal
        cis[k, :] = eis
        di2s -= np.square(eis)
        di2s[selected_item] = -np.inf
        selected_item = np.argmax(di2s)
        if di2s[selected_item] < epsilon:
            break
        selected_items.append(selected_item)
    return selected_items


def dpp_sw(kernel_matrix, window_size, max_length, epsilon=1E-10):
    """
    Sliding window version of the greedy algorithm
    :param kernel_matrix: 2-d array
    :param window_size: positive int
    :param max_length: positive int
    :param epsilon: small positive scalar
    :return: list
    """
    item_size = kernel_matrix.shape[0]
    v = np.zeros((max_length, max_length))
    cis = np.zeros((max_length, item_size))
    di2s = np.copy(np.diag(kernel_matrix))
    selected_items = list()
    selected_item = np.argmax(di2s)
    selected_items.append(selected_item)
    window_left_index = 0
    while len(selected_items) < max_length:
        k = len(selected_items) - 1
        ci_optimal = cis[window_left_index:k, selected_item]
        di_optimal = math.sqrt(di2s[selected_item])
        v[k, window_left_index:k] = ci_optimal
        v[k, k] = di_optimal
        elements = kernel_matrix[selected_item, :]
        eis = (elements - np.dot(ci_optimal, cis[window_left_index:k, :])) / di_optimal
        cis[k, :] = eis
        di2s -= np.square(eis)
        if len(selected_items) >= window_size:
            window_left_index += 1
            for ind in range(window_left_index, k + 1):
                t = math.sqrt(v[ind, ind] ** 2 + v[ind, window_left_index - 1] ** 2)
                c = t / v[ind, ind]
                s = v[ind, window_left_index - 1] / v[ind, ind]
                v[ind, ind] = t
                v[ind + 1:k + 1, ind] += s * v[ind + 1:k + 1, window_left_index - 1]
                v[ind + 1:k + 1, ind] /= c
                v[ind + 1:k + 1, window_left_index - 1] *= c
                v[ind + 1:k + 1, window_left_index - 1] -= s * v[ind + 1:k + 1, ind]
                cis[ind, :] += s * cis[window_left_index - 1, :]
                cis[ind, :] /= c
                cis[window_left_index - 1, :] *= c
                cis[window_left_index - 1, :] -= s * cis[ind, :]
            di2s += np.square(cis[window_left_index - 1, :])
        di2s[selected_item] = -np.inf
        selected_item = np.argmax(di2s)
        if di2s[selected_item] < epsilon:
            break
        selected_items.append(selected_item)
    return selected_items
Selected_items=[]
ans=0
import copy
def dpp_beemserach(kernel_matrix, max_length, epsilon=1E-10,beemsize=2):
    """
    Our proposed fast implementation of the greedy algorithm
    :param kernel_matrix: 2-d array
    :param max_length: positive int
    :param epsilon: small positive scalar
    :return: list
    """
    item_size = kernel_matrix.shape[0]
    cis=[]
    di2s=[]
    sum_di2s=[]
    selected_items = list()
    selected_item=[]
    for i in range(beemsize):
        selected_items.append([])
        cis.append(np.zeros((max_length, item_size)))
        di2s.append(np.copy(np.diag(kernel_matrix)))

    sorted_di2s = np.sort(di2s[0])
    sortedarg_di2s = np.argsort(di2s[0])
    for i in range(beemsize):

        selected_item.append(copy.copy(sortedarg_di2s[item_size-1-i]))
        selected_items[i].append(copy.copy(selected_item[i]))
        sum_di2s.append(copy.copy(sorted_di2s[item_size-1-i]))
    while len(selected_items[0]) < max_length:
            k = len(selected_items[0]) - 1
            #print(selected_items[0])
            #print(selected_items[1])
            #print(len(selected_items[0]))
            #print(len(selected_items[1]))

            for p in range(beemsize):
                if di2s[p][selected_item[p]] < epsilon:
                    break
                ci_optimal = cis[p][:k, selected_item[p]]
                di_optimal = math.sqrt(di2s[p][selected_item[p]])
                elements = kernel_matrix[selected_item[p], :]
                eis= (elements - np.dot(ci_optimal, cis[p][:k, :])) / di_optimal
                cis[p][k, :] = eis
                di2s[p] -= np.square(eis)
                di2s[p][selected_item[p]] = -np.inf


            di2s_tmp=copy.copy(di2s)

            selected_items_tmp =  copy.copy(selected_items)
            selected_item_tmp=copy.copy(selected_item)
            cis_tmp=copy.copy(cis)
            tmp_di2s = []
            beem_id={}
            for i in range(beemsize):
                    for j in range(item_size):

                        beem_id[i*item_size+j]=i
                        tmp_di2s.append(sum_di2s[i]+di2s[i][j])
            sorted_di2s = np.sort(tmp_di2s)
            sortedarg_di2s = np.argsort(tmp_di2s)
            #print(beem_id)
            #print(selected_items[0])
            #print(selected_items[1])
            for p in range(beemsize):
                sum_di2s[p]=sorted_di2s[beemsize*item_size-1-p]
                #print(beem_id[sortedarg_di2s[beemsize*item_size-p-1]])
                selected_items[p]=copy.copy(selected_items_tmp[beem_id[sortedarg_di2s[beemsize*item_size-p-1]]])
                selected_item[p] = copy.copy(selected_item_tmp[beem_id[sortedarg_di2s[beemsize*item_size-p - 1]]])
                #print(selected_items[0])
                #print(selected_items[1])
                cis[p]=copy.copy(cis_tmp[beem_id[sortedarg_di2s[beemsize*item_size-p-1]]])
                di2s[p]=copy.copy(di2s_tmp[beem_id[sortedarg_di2s[beemsize*item_size-p-1]]])
                selected_item[p]=copy.copy(sortedarg_di2s[beemsize*item_size-p-1]%item_size)
                selected_items[p].append(selected_item[p])
                #print(selected_items[0])
                #print(selected_items[1])
                if di2s[p][selected_item[p]] < epsilon:
                    break

    Selected_items=[]
    ans=0
    for i in range(beemsize):
        if(sum_di2s[i]>ans):
            ans=sum_di2s[i]
            Selected_items=selected_items[p]
    return Selected_items