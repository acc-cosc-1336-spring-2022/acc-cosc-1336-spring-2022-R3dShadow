def get_hamming_distance (dna1, dna2):
    result = 0
    i = 0
    while i < len(dna1):
        if (dna1[i] != dna2[i]):
            result += 1
            i += 1
        else: i += 1
    return result

def get_dna_compliment (dna):
    reverse = ''
    result = ''
    i = (len(dna) - 1)
    while i > -1:
        reverse += dna[i]
        i -= 1
    i = 0
    while i < len(reverse):
        if (reverse[i] == 'A'):
            result += 'T'
            i += 1
        elif (reverse[i] == 'C'):
            result += 'G'
            i += 1
        elif (reverse[i] == 'G'):
            result += 'C'
            i += 1
        elif (reverse[i] == 'T'):
            result += 'A'
            i += 1
    return result