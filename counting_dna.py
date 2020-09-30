out="output_rosalind.txt"
result=open(out, 'w')

with open ('rosalind_dna.txt', 'r') as f:
    for line in f:
        a=line.count('A')
        c=line.count('C')
        g=line.count('G')
        t=line.count('T')

        result.write("{} {} {} {}".format(a,c,g,t))