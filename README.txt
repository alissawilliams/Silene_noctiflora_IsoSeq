Alissa M. Williams 
Alissa.Williams@colostate.edu
May 15, 2020

In this folder you'll find files related to the PacBio Iso-Seq transcriptome of Silene noctiflora population OPL. The files are:
1. This README file.
2. trinotate_annotation_report_full.csv.zip. This is the annotation report outputted by Trinotate. Note that you can import this file (once unzipped) into Excel. It may give you a warning about Excel versions, but open it anyway, as there doesn't seem to be anything actually wrong with it. 
3. final.partition.txt. This is the output of the Cogent family finding algorithm (https://github.com/Magdoll/Cogent/wiki/Running-Cogent), and it can also be imported into Excel. 
4. polished.hq.fasta.zip. This file contains all of the final transcript sequences reported by the Iso-Seq pipeline (version 3.1). 

NOTE: The fasta file contains ALL of the final transcript sequences, as do the annotation and family finding files. Some of these transcripts were excluded from NCBI TSA as follows:
- 1,166 transcripts were excluded because they were too short (less than 200 bp long). A full list can be provided if needed. 
- 14 transcripts were excluded due to being contaminants from Frankliniella occidentalis (the western flower thrip). These transcripts were:
transcript/9823
transcript/11780
transcript/18222
transcript/18987
transcript/19340
transcript/25839
transcript/29488
transcript/31808
transcript/32288
transcript/34789
transcript/37826
transcript/54014 
transcript/19507
transcript/53846
- 4 transcripts were excluded because they were a match to adapter sequences. These transcripts were:
transcript/8097 
transcript/10000
transcript/24436
transcript/50613
- 23 transcripts were excluded due to being exact duplicates (100% identity) of other transcripts. Here is the list of duplicates from the TSA upload screening. The first transcript listed in each set was kept, and the others were deleted. Most sets are pairs of transcripts, but there are two sets with three transcripts and one set with six transcripts. 
Duplicated:
Sequence names, length
lcl|transcript60494 lcl|transcript60678 (442 bp)
lcl|transcript7120 lcl|transcript8770 lcl|transcript9566 lcl|transcript9684 lcl|transcript9736 lcl|transcript10443 (2363 bp)
lcl|transcript3888 lcl|transcript4120 (2837 bp)
lcl|transcript4498 lcl|transcript6945 (2504 bp)
lcl|transcript40915 lcl|transcript43199 (1159 bp)
lcl|transcript48439 lcl|transcript51444 (855 bp)
lcl|transcript30547 lcl|transcript32317 (1544 bp)
lcl|transcript61865 lcl|transcript62132 (361 bp)
lcl|transcript63453 lcl|transcript64488 lcl|transcript64729 (247 bp)
lcl|transcript62067 lcl|transcript62106 (374 bp)
lcl|transcript12982 lcl|transcript16338 lcl|transcript16731 (2003 bp)
lcl|transcript7616 lcl|transcript9289 (2367 bp)
lcl|transcript32507 lcl|transcript32987 (1456 bp)
lcl|transcript1840 lcl|transcript2114 (3216 bp)
lcl|transcript53191 lcl|transcript53484 (744 bp)
lcl|transcript48279 lcl|transcript49893 (930 bp)
lcl|transcript35014 lcl|transcript36333 (1366 bp)
