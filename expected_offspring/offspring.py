def offspring_dom_allele (k, l, m, n, o, p):
    # Catch the number of couples with certain offspring as dominant alleles 
    E1 = 2*k + 2*l + 2*m
    # Catch the number of couples with 75% certainty of 2 offspring with dominant alleles
    E2 = 2*0.75*n
    # Catch the number of couple with 50% certainty of 2 offspring with dominant alleles
    E3 = 2*0.5*o
    # The couples with no dominant alleles
    E4 = 2*0*p
    return sum([E1,E2,E3,E4])
        
        
def main():
    with open ("rosalind_iev.txt", 'r') as f:
        AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = map(float, (f).read().split())
        num_offspring = offspring_dom_allele(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa)   
    print(num_offspring)
main()