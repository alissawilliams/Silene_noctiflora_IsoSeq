# make_gene_trans_map.py
# script to make a "fake" gene trans map file for use in Trinotate
# Alissa Williams
# September 19, 2019

from Bio import SeqIO

def main():

	outfilename = "polished.hq.fasta.gene_trans_map"
	outfile = open(outfilename, "w") #this will be the gene trans map file
	
	for entry in SeqIO.parse("polished.hq.fasta","fasta"):
		outfile.write("g_" + str(entry.id) + "\t" + str(entry.id) + "\n")	
		
	outfile.close()
		

if __name__ == "__main__":
	main()

