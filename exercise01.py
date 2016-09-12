def complement_base(base, material = 'DNA'):
    """return the watson crick complement of a base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Cc':
        return 'G'
    elif base in 'GG':
        return 'C'





def reverse_complement_no_reverse(seq, material = 'DNA'):
    """compute the reverse complement of a nucleic acid sequence"""

    #initialize an empty string
    rev_comp = ''

    for base in seq:
        rev_comp = complement_base(base, material = material) + rev_comp

    return rev_comp


def reverse_complement_no_for_loop(seq, material = 'DNA'):
    """compute the reverse complement of a nucleic acid sequence"""

    #initialize an empty string
    rev_comp = ''

    #compute the complement base of the sequence, starting with the 5 prime end
    if material == 'DNA':
        rev_comp = seq.replace('A', 't')
    else:
        rev_comp = seq.replace('A', 'u')

    rev_comp = rev_comp.replace('T', 'a')
    rev_comp = rev_comp.replace('G', 'c')
    rev_comp = rev_comp.replace('C', 'g')
    rev_comp = rev_comp.upper()[::-1]

    return rev_comp


def longest_common_substring(seq1, seq2):
    """find the longest common substring when comparing two strings"""
    substring_max = ''
    if len(seq1) < len(seq2):
        sequence_length = len(seq1)
    else:
        sequence_length = len(seq2)
    for n in reversed(range(sequence_length)):
        for i in range(sequence_length):
            for j in range(len(seq2)):
                if seq1[i:i+n] == seq2[j:j+n]:
                    substring_max = seq1[i:i+n]
                    return substring_max

def are_num_parentheses_equal(dot_notation):
    if dot_notation.find('(') == dot_notation.find(')'):
        return True
    else:
        return False

def convert_parens_to_tuples(dot_notation):
    parens_list = []

    list_of_pairs = []
    tuple_of_pairs = ()
    for i, base in enumerate(dot_notation):
        if base == '(' or base == ')':
            parens_list += [i]

    num_pairs = len(dot_notation)//2

    while len(parens_list) > 0:
        list_of_pairs += [parens_list.pop(0)]
        list_of_pairs += [parens_list.pop()]
        tuple_of_pairs += (tuple(list_of_pairs),)
        list_of_pairs = []

    return tuple_of_pairs

def verify_hairpin_requirement(dot_notation):
    hairpin_length = 0
    for i, base in enumerate(dot_notation):
        if base == '(' and dot_notation[i + 1] == '.':
            n = i + 1
            while dot_notation[n] == '.':
                hairpin_length += 1
                n += 1
    if hairpin_length >= 4 and dot_notation[n] == ')':
        return True
    else:
        return False

def rna_ss_validator(seq, sec_struc, wobble=True):
    counter = 0
    count = tuple(range(len(seq)//2))

    if verify_hairpin_requirement(sec_struc) == False:
        return False

    for i, base, parens in zip(count, seq, sec_struc):
        if ((base == 'G' and seq[-i + 1] == 'C') or (base == 'C' and seq[-i + 1] == 'G') or
        (base == 'A' and seq[-i + 1] == 'T') or (base == 'T' and seq[-i + 1] == 'A')
        or (wobble == True and base == 'G' and seq[-i + 1] == 'U') or
        (wobble == True and base == 'U' and seq[-i + 1] == 'G')):
            if sec_struc[i] == '(' and sec_struc[-i + 1] == ')':
                counter += 1
        else:
            if sec_struc[i] == '.' and sec_struc[-i] == '.':
                counter += 1
    if counter == len(seq)//2:
        return True
    else:
        return False
