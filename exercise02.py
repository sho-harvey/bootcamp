
#open the salmonella sequence
with open('data/salmonella_spi1_region.fna', 'r') as f:
    counter = 0

    #skip the first line of the file
    while counter < 1:
        f.readline()
        counter += 1
    f_list = f.readlines()

#convert f_list from a list into a string
for line in range(len(f_list)):
    f_list[line] = f_list[line].rstrip()

f_str = ''.join(f_list)

print(f_str[:100])


def gc_content(seq):
    """computes GC content"""
    return ((seq.count('C') + seq.count('G')) / len(seq))


def gc_blocks(seq, block_size):
    """computes GC content of a sequence within a given block size"""

    total_block_number = len(seq) // block_size

    i = 0
    GC_tuple = ()
    while i < total_block_number:
        GC_tuple += (gc_content(seq[i*block_size:i*block_size + block_size]),)
        i += 1

    return GC_tuple


def gc_map(seq, block_size, gc_thresh):
    """modifies the original sequence to be lowercase if it does not meet
    a specified GC content threshold"""

    new_seq = ''
    for i in range(len(seq) // block_size):
        if gc_blocks(seq, block_size)[i] < gc_thresh:
            new_seq += seq[i*block_size:i*block_size + block_size].lower()
        else:
            new_seq += seq[i*block_size:i*block_size + block_size].upper()

    return new_seq

gc_content_sequence = gc_map(f_str, 1000, 0.45)

with open('data/salmonella_spi1_region.fna', 'r') as f, open('pathogenicity_islands.fna', 'w') as f_out:
    counter = 0

    #write in the first line of the file
    while counter < 1:
        lines = f.readline()
        counter += 1
        f_out.write(lines)
    sequence_multiple_60 = len(f_str) // 60
    for i in range(sequence_multiple_60):
        f_out.write(gc_content_sequence[i*60:i*60 + 60])
        f_out.write('\n')
        counter = i + 61
    f_out.write(f_str[counter:])


def is_stop_codon(seq):
    if seq == 'TGA' or seq == 'TAG' or seq == 'TAA':
        return True
    else:
        return False


def seq_is_multiple_three(seq):
    if len(seq) % 3 == 0:
        return True
    else:
        return False


def count_stop_codons(seq):
    """counts the number of stop codons in a given sequence, that are in frame
    with the beginning codon of the sequence"""
    num_codons = len(seq) // 3

    counter = 0

    for codon in range(num_codons):
        if seq[codon*3:codon*3 + 3] == 'TGA' or seq[codon*3:codon*3 + 3] == 'TAG' or seq[codon*3:codon*3 + 3] == 'TAA':
            counter += 1
    return counter


def longest_orf(seq):

    orf_len = len(seq)

    while orf_len > 0:
        for i in range(len(seq) - orf_len + 1):
            if seq[i:i+3] == 'ATG' and is_stop_codon(seq[i+orf_len-3:i+orf_len]) == True and seq_is_multiple_three(seq[i:i+orf_len]) == True:
                if count_stop_codons(seq[i:orf_len]) < 2:
                    return seq[i:i+orf_len]
                else:
                    break
        orf_len -= 1
