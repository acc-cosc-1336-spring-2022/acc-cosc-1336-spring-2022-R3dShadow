def get_p_distance(list1, list2):
    count = 0
    i = 0
    while i < len(list1):
        if (list1[i] != list2[i]):
            count += .1
        i += 1
    return count

def get_p_distance_matrix(list1, list2, list3, list4):
    dna1 = get_p_distance(list1, list1), get_p_distance(list1, list2), get_p_distance(list1, list3), get_p_distance(list1, list4)
    dna2 = get_p_distance(list2, list1), get_p_distance(list2, list2), get_p_distance(list2, list3), get_p_distance(list2, list4)
    dna3 = get_p_distance(list3, list1), get_p_distance(list3, list2), get_p_distance(list3, list3), get_p_distance(list3, list4)
    dna4 = get_p_distance(list4, list1), get_p_distance(list4, list2), get_p_distance(list4, list3), get_p_distance(list4, list4)
    return dna1, dna2, dna3, dna4