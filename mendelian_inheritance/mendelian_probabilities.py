
def organisms(inputfile):
    with open (inputfile) as f:
        d, h, r =  map(float, (f).read().strip().split())
        return d, h, r
    
def mendelian_probabilities (d, h, r):
    # The total population
    t = d + h + r
    # Dominant and dominant 
    dd = d/t * (d-1)/(t-1)
    # Dominant and heterozygous 
    dh = d/t * h/(t-1) + h/t * d/(t-1)
    # Dominant and rececssive
    dr = d/t * r/(t-1) + r/t * d/(t-1)
    # Heterozygous and heterozygous
    hh = h/t * (h-1)/(t-1)
    # Heterozygous and recessive
    hr = h/t * r/(t-1)+ r/t * h/(t-1)
    # Recessive and recessive
    rr= r/t * (r-1)/(t-1)
    
    total_probability = dd + dh + dr + hh*0.75 + hr*0.5 + rr*0
               
    return total_probability
    

def main():
    d, h, r = organisms('ros_mendel.txt')
    probabilities = mendelian_probabilities (d, h, r)
    print(probabilities)
main()