import dictionary

list1 = input('\nEnter a DNA string: ')
list2 = input('\nEnter a DNA string: ')
list3 = input('\nEnter a DNA string: ')
list4 = input('\nEnter a DNA string: ')

result = dictionary.get_p_distance_matrix(list1, list2, list3, list4)

print('Here is your matrix: ' + str(result))