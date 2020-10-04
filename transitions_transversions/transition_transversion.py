from Bio import SeqIO

def dna_strings(inputfile):
    sequences = []
    for record in SeqIO.parse(inputfile, 'fasta'):
        sequences.append(record.seq)
    return sequences

def transition_transversion(sequences):
    s1 = sequences[0]
    s2 = sequences [1]
    transition = 0
    transversion = 0
    AG = ['A', 'G']
    CT = ['C', 'T']
    for nt1, nt2 in zip(s1, s2):
        if nt1 != nt2:
            if nt1 in AG and nt2 in AG:
                transition += 1
            elif nt1 in CT and nt2 in CT:
                transition += 1
            else:
                transversion += 1
    return transition / transversion


def main():
    sequences = dna_strings("rosalind_tran.txt")
    ratio = transition_transversion(sequences)
    print(ratio)
main()