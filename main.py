from seqfold import fold, dot_bracket
import os
import sys
sys.setrecursionlimit(1000000)

# load the reference genome sequence file
ref_genome = open("data/GRCh38_latest_genomic.fna", "r") 

# get next item from the FASTA file
def get_next_item(file):
    # read the first line
    line = file.readline()
    # check if the line is empty
    if not line:
        return None
    # get the sequence id
    seq_id = line[1:].strip()
    # read the sequence
    seq = ""
    while True:
        line = file.readline()
        if not line or line.startswith(">"):
            break
        seq += line.strip()
    # return seq_id, seq.upper()
    return seq.upper()

# get all sequences starting at 'CGCGCG' and ending at 'AATAA'
def get_seqs(seq):
    seqs = []
    start = 0
    while True:
        start = seq.find("CGCGCG", start)
        if start == -1:
            break
        end = seq.find("AATAA", start)
        if end == -1:
            break
        seqs.append(seq[start:end+5])
        start = end + 5
    return seqs

def to_rna(dna):
    rna = ""
    for i in dna:
        if i == 'G':
            rna += 'C'
        elif i == 'C':
            rna += 'G'
        elif i == 'T':
            rna += 'A'
        elif i == 'A':
            rna += 'U'
    return rna

# get all transcripts
transcripts = []

seq = get_next_item(ref_genome)
while seq:
    transcripts.extend(get_seqs(seq))
    seq = get_next_item(ref_genome)

# convert all transcripts to RNA
rna_transcripts = [to_rna(transcript) for transcript in transcripts]

i = 0
for transcript in rna_transcripts:        
    i += 1
    
    # skip if folded/{i} already exists
    if os.path.exists(f"folded/{i}"):
        continue
    
    # create a directory folded/{i}
    os.makedirs(f"folded/{i}", exist_ok=True)
    
    print(f"Folding transcript {i}")
    folded_transcript = fold(transcript)
    
    # save to file folded/{i}/fold
    with open(f"folded/{i}/fold", "w") as f:
        f.write("\n".join([str(x) for x in folded_transcript]))
    
    with open(f"folded/{i}/seq", "w") as f:
        f.write(transcript)
