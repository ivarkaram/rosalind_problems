out=open('out_rna.txt', 'w+')

with open ('rosalind_rna.txt', 'r') as f:
    
    r={'A':'A', 'C':'C', 'G':'G', 'T':'U' }
    
    seq=f.read().strip() #in a list
    
    for nucl in range(0,len(seq),1):
        nucl=seq[nucl]
        rna="" 
        rna+=r[nucl]        
        
        out.write(rna)