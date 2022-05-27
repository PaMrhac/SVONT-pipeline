# SVONT-pipeline
SVONT-pipeline is pipeline for structural variant detection and annotation using Oxford Nanopore data. 

Files in following formats are used as input:
- sequences in FAST5 format
- sequences in FASTQ format zipped in .gz files
- reference sequence in FASTA format

Annotated structural variants are summarized in tsv file which is the output of SVONT-pipeline. 

### Features
SVONT-pipeline perform following steps:
- unzip of zipped FASTQ files
- transformation of fastq files to file in FASTA format
- computing statistics from reads, visualization 
- mapping reads to reference sequence
- detection of structural variant
- annotation of detected variants


## Dependencies
minimap2, nanopolish, pysam, samtools, snakemake, sniffles2, gzip, NanoPlot, NanoStat, AnnotSV

Packages nanopolish, minimap2, samtools, pysam, sniffles=2.0, snakemake, NanoPlot and NanoStat can be install from Bioconda:
´´´
conda install -c bioconda nanopolish minimap2 samtools pysam sniffles=2.0 snakemake NanoPlot NanoStat
´´´

conda install -c conda-forge gzip
git clone https://github.com/lgmgeo/AnnotSV.git | make install
skript fastq_to_fasta.py

SVONT-pipeline uses a configuration file, where are written paths to interested files.
