#!/usr/bin/python3

from Bio.Align.Applications import ClustalwCommandline
cline = ClustalwCommandline("clustalw2", infile="opuntia.fasta")
print(cline) 
stdout, stderr = cline()


