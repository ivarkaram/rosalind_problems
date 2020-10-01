def query_dna_positions (seq, query):
    positions = []
    for nuc in range (0, len(seq) - len(query) + 1):
        if seq[nuc: nuc + len(query)] == query:
            positions.append(nuc+1)
    return positions
    
def main():
    seq = 'AATTCCGGAA'
    query = 'AA'
    positions = query_dna_positions(seq, query)
    print(positions)
main()