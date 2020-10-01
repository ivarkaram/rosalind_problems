def file_id (sequence):
    gc_ids = {}
    seq = ''
    for line in sequence:
        if line.startswith('>'):
            id_s = line.strip()
            gc_ids[id_s] = seq

        else:
            line = line.strip()
            gc_ids[id_s] += line
    return gc_ids

def count_gc (seq_file):
    gc_counts = {}
    
    for gc_id, seq in seq_file.items():
        gc_count = seq.count('G') + seq.count ('C')
        gc_frac = float(gc_count) / len(seq) * 100
        gc_counts[gc_id] = gc_frac
    return gc_counts

def keywithmaxval(d):
    k=list(d.keys())
    v=list(d.values())
    return k[v.index(max(v))], max(v)
    

def main():
    with open ('rosalind_gc_3_dataset.txt', 'r') as f:
        gc_file = file_id (f)
        gc_count = count_gc (gc_file)
        max_gc = keywithmaxval(gc_count)
        print(max_gc)
main()