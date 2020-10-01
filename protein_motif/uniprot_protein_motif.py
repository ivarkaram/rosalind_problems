import requests
import re

def parse_uniprot_ids(inputfile):
    IDs = []
    with open (inputfile, 'r') as f:
        for line in f:
            IDs.append(line.strip())
    return IDs

def retrieve_uniprot_seq (IDs):
    sequences = {}
    url = 'https://www.uniprot.org/uniprot/'
    for proID in IDs:
        uniprot_url = url+proID+".fasta"
        response = requests.get(uniprot_url)
        data = response.text.split('\n')
        sequence = ''.join(data[1:])
        sequences[proID] = sequence
    return sequences

def N_gly_motif(sequence):
    uniprot_motif = {}
    motifs = re.compile(r'(?=(N[^P][ST][^P]))')
    for ids, seq in sequence.items():
        positions = []
        for motif in re.finditer(motifs, seq):
            positions.append(motif.start()+1)        
            uniprot_motif[ids] = positions
            
    return uniprot_motif
       
def main():
    ids = parse_uniprot_ids ('rosalind_mprt.txt')
    sequences = retrieve_uniprot_seq (ids)
    motifs = N_gly_motif(sequences)
    for ids, positions in motifs.items():
        print(ids)
        print(' '.join(map(str, positions)))
main()