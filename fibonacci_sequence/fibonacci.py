def fsf(n,k):
    fibseq = [1,1]
    while len(fibseq) < n:
        j = len(fibseq)
        fibseq.append(fibseq[j-2]*k+fibseq[j-1]*k)
    return fibseq