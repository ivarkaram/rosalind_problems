import itertools

def readfasta(inputfile):
    seq = ''
    with open(inputfile, 'r') as f:
        for line in f:
            if line.startswith ('>'):
                pass
            else:
                seq += line.strip()
    return seq


def possible_kmers (k):
    return [''.join(i) for i in itertools.product('ACGT', repeat = k) ]

def find_kmers (seq, k):
    kmers = {}
    # Iterate over the possible kmers
    for i in range(len(seq)-k+1):
        kmer = seq [i: i+k]
        if not kmer in kmers:
            kmers [kmer] = 1
        else:
            kmers [kmer] += 1
        
    return kmers

def kmer_composition_seq(kmer_seq, poss_kmer):
    kmer_frequency = {}
    # Iterate over the list of kmers
    for k in poss_kmer:
        # Iterate over the dictionary of kmers: frequency of the sequence
        for kmer, frequency in kmer_seq.items():
            if k in kmer:
                kmer_frequency [k] = frequency
            else:
                continue
    return kmer_frequency


def main():
    k = 4
    sequence = readfasta ('rosalind_kmer.txt')
    kmers = possible_kmers (k)
    kmer_seq = find_kmers(sequence, k)
    composition = kmer_composition_seq (kmer_seq, kmers)
    with open('k-mer_composition.txt', 'w') as f:
        result = ''
        for num in composition.values():
            result += str(num) + ' '
        f.write(result)
main()