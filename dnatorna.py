"""convert dna to rna"""



def rna(seq):
    """
    convert a DNA sequence to RNA
    """

    #convert to upper
    seq = seq.upper()

    return seq.replace('T', 'U')
