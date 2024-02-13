from Bio.Seq import Seq
from Bio.SeqUtils import nt_search

# Define the transcription factor binding site motif
tf_binding_site_motif = "GCTGCACC AAT"

# Define the DNA sequences
sequences = [
    "ATGGATTCTGCAAG GCTGCACC AAT CAAAGAGGAAACATTGGAAAAACTTGATCAAGAAATTACAGTGAACCT",
    "GCAGAAGATAGACTCTAACTTGAGTTTCTGCTTTCA GCTGCACC AAT TAAGATCACCCAGGACATCATCCCACA",
    "GTGGCTACATATTCAGAAATATGTGAGCGGATCATGGATAGCACCGAAT GCTGCACC AAT GGCTGGGGACTAT",
    "TTTCAAGAGACTGCTGCACC AATAAT GGGCTG AAT GTGAAT AAT TTGC AAT AGG AAT CAAATGCA AAT GCTGCACC AAT GCTGCACC AAT"
]

# Iterate through each sequence
for i, sequence in enumerate(sequences, start=1):
    # Remove spaces from the sequence (assuming they are typos)
    sequence = sequence.replace(" ", "")

    # Create a Seq object from the sequence
    seq_obj = Seq(sequence)

    # Find the transcription factor binding site motif
    binding_site_positions = nt_search(str(seq_obj), tf_binding_site_motif)

    # Print the results
    print(f"Sequence {i}:")
    print(f"DNA Sequence: {sequence}")
    print(f"Transcription Factor Binding Site '{tf_binding_site_motif}' Positions: {', '.join(map(str, binding_site_positions))}")
    print("\n")
