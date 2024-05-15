mkdir data

# Reference Genome Sequence 
wget https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz -P data
gunzip data/GRCh38_latest_genomic.fna.gz
