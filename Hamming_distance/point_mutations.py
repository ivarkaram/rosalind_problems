def hamming_distance(s,t):
    counter = 0
    for seq1,seq2 in zip(s,t):
       if seq1 != seq2:
            counter += 1
    return counter

def main():
    s = 'TCGTCGTGCAGATTGTGACACCCATTACAAAGCTGCAAACAGCTTAAGGATATCCTATACCGTCTGCTTCAGACTTCCGCGGCTACA'
    t = 'TCGTCGTGAAGGCTTTGCAATCATTGCTAATGCTGCGATCATCTTAAGGATTTGCATTCGCAATAGCAATAGCAAAAGGTGCTATGA'
    distance = hamming_distance (s,t)
    print(distance)
main()