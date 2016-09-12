"""convert dna to rna"""



def rna(seq):
    """
    convert a DNA sequence to RNA
    the returned sequences are all uppercase
    """

    #convert to upper
    seq = seq.upper()

    return seq.replace('T', 'U')
