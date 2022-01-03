def GenerateBBSTArray(a):
    if a is None:
        return None

    bst_array_length = len(a)

    if bst_array_length == 0:
        return None
    elif bst_array_length == 1:
        return a

    sorted_bst_array = sorted(a)
    processed_bst_array = bst_array_length * [None]

    return recursive_bst_build(sorted_bst_array, 0, processed_bst_array)


def recursive_bst_build(array, node_index, balanced_bst_array):
    array_length = len(array)
    if array_length == 1:
        balanced_bst_array[node_index] = array[0]
    else:
        middle_of_array = array_length // 2
        balanced_bst_array[node_index] = array[middle_of_array]

        left_child_index = 2 * node_index + 1
        right_child_index = left_child_index + 1

        recursive_bst_build(array[:middle_of_array],
                            left_child_index,
                            balanced_bst_array)
        recursive_bst_build(array[middle_of_array + 1:],
                            right_child_index,
                            balanced_bst_array)
        return balanced_bst_array

