import re

def dna_string(inputfile):
    seq = ''
    with open (inputfile, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                lines = line.strip()
                seq += lines
            else:
                continue
    return seq

def rev_comp(dna):
    reverse_complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_seq = ''.join([reverse_complement[nuc]for nuc in dna])
    return rev_seq

def transcribe_dna (dna):
    transcription = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
    transcribed_seq = ''.join([transcription[nuc] for nuc in dna])
    return transcribed_seq

def translate_rna(dna):
    protein = ''
    gencode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    length = len(dna)//3 *3
    
    for nuc in range(0, length, 3):
        codon = dna[nuc: nuc+3]
        aa = gencode[codon]
        if not aa =='Stop':
            protein += aa
        else:
            continue
                
    return protein

def find_orfs (dna):
    orfs = {}
    id = 1
    rev_dna = rev_comp (dna)
    for seq in [dna, rev_dna]:
        # Transcribe both the sequences
        rna = transcribe_dna (seq)
        # Find the start and stop codons
        starts = [nuc.start() for nuc in re.finditer('AUG', rna)]
        stops = [nuc.start() for nuc in re.finditer('UAG|UUG|UAA', rna)]
        
        # Iterate over the starts and stops
        for start_codon in starts:
            for stop_codon in stops:
                # Check if valid amino acids
                if (stop_codon-start_codon)>0 and ((stop_codon-start_codon)%3)== 0:
                    # Translare the sequence
                    protein = translate_rna(rna[start_codon: stop_codon +3])
                    # Store the ORF and the length of the ORF in a dictionary
                    if not protein in orfs:
                        orfs[id] = []
                    orfs[id] += [(protein, int(len(protein)))]
                    
                    id += 1
                    break
                
    return orfs



def main():
    dna = dna_string('rosalind_orf.txt')
    orf = find_orfs(dna)
    print(orf)    
main()
