with open ('rosalind_revc.txt', 'r') as f:    
    
    seq=f.read().strip()
    
    output=open('rev_comp.txt_2.txt','w')    
    
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    
    output.write(reverse_complement)
    print(reverse_complement)