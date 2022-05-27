# SVONT-pipeline
SVONT-pipeline is pipeline for structural variant detection and annotation using Oxford Nanopore data. Oxford Nanopore Technologies provide technology for  It is implemented by Snakemake, workflow manager based od python.

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
minimap2, nanopolish, pysam, samtools, snakemake, sniffles2, gzip, NanoPlot, NanoStat, AnnotSV, script fastq_to_fasta.py

Packages nanopolish, minimap2, samtools, pysam, sniffles=2.0, gzip, snakemake, NanoPlot and NanoStat can be install using Conda:
```
conda install -c bioconda nanopolish minimap2 samtools pysam sniffles=2.0 snakemake NanoPlot NanoStat
conda install -c conda-forge gzip
```
A tool AnnotSV can´t be installed using Conda, it need to be clone from github repository:
```
git clone https://github.com/lgmgeo/AnnotSV.git 
make install
```
The python script fastq_to_fasta.py can be download from this repository.

## How to run SVONT-pipeline
### Configuration file
SVONT-pipeline uses a configuration file which has to contain folowing variables:
```
**run:** 		name of the run
**fast5Dir:**   	path to fast5 directory
**ref:** 		path to reference fasta file (index file should also be present in the same folder)
**fastqDir:**	path to fastq directory
**AnnotSV:**	path to AnnotSV directory which was installed
```









