from strings import get_hamming_distance, get_dna_compliment


def menu():
    choice = input('\nChoose an option please:\n\n1-Hamming Distance\n2-Dna Complement\n3-Exit\n\nChoice: ')
    if(choice == '1'):
        dna1 = input('\nEnter a DNA string: ')
        dna2 = input('\nEnter a second DNA string: ')
        result = get_hamming_distance(dna1, dna2)
        print('\nThe Hamming Distance is ' + str(result) + '.')
        choice2 = input('\nChoose an option please:\n\n1-Menu\n2-Exit\n\nChoice: ')
        if(choice2 == '1'):
            menu()
        elif(choice2 == '2'):
            print('\nExiting ...\n')
    if(choice == '2'):
        dna = input('\nEnter a DNA string: ')
        result = get_dna_compliment(dna)
        print('\nThe complementary DNA string is: ' + result + '.')
        choice2 = input('\nChoose an option please:\n\n1-Menu\n2-Exit\n\nChoice: ')
        if(choice2 == '1'):
            menu()
        elif(choice2 == '2'):
            print('\nExiting ...\n')
    if(choice == '3'):
        print('\nExiting ...\n')

menu()