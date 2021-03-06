# SVONT-pipeline
SVONT-pipeline is pipeline for **structural variant detection and annotation using Oxford Nanopore data**. Oxford Nanopore Technologies provide technology for long reads sequencing. Pipeline is implemented by Snakemake and written in Snakefile. Snakemake is workflow manager based od python.

Files in following formats are used as input:
- sequences in FAST5 format
- sequences in FASTQ format zipped in .gz files
- reference sequence in FASTA format

Annotated structural variants are summarized in tsv file which is the output of SVONT-pipeline. 



### Features
SVONT-pipeline perform following steps:
- unzip of zipped FASTQ files
- make one FASTQ file where are extracted all FASTQ files
- transformation of fastq files to file in FASTA format
- computing statistics from reads, visualization 
- mapping reads to reference sequence
- detection of structural variant
- annotation of detected variants


## Dependencies
For execution SVONT-pipeline are reqiured following packages:\
[minimap2](https://github.com/lh3/minimap2), [nanopolish](https://nanopolish.readthedocs.io/en/latest/), [pysam](https://pysam.readthedocs.io/en/latest/api.html), [samtools](http://www.htslib.org/doc/samtools.html), [snakemake](https://snakemake.readthedocs.io/en/stable/), [sniffles2](https://github.com/fritzsedlazeck/Sniffles), [NanoPlot](https://github.com/wdecoster/NanoPlot), [NanoStat](https://github.com/wdecoster/nanostat), [AnnotSV](https://lbgi.fr/AnnotSV/), [gzip](https://www.gnu.org/software/gzip/), script fastq_to_fasta.py

Packages nanopolish, minimap2, samtools, pysam, sniffles=2.0, snakemake, gzip, NanoPlot and NanoStat can be install using Conda:
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
SVONT-pipeline uses a configuration file in format YAML which has to contain folowing variables:
```
run: name_of_the_run
fast5Dir: path_to_fast5_directory
ref: path_to_reference_fasta_file (index file should also be present in the same folder)
fastqDir: path_to_fastq_directory
AnnotSV: path_to_AnnotSV_directory_which_was_installed
```

### Folder structure
To run SVON-pipeline user need to have these folders in this structure:
```
  |
  ├── data/
  |    ├── example_input/
  |    └── ref/
  └── src/
      ├── Snakefile
      ├── scripts/
      |    └── fastq_to_fasta.py
      └── config/
           └── example_config.yaml
```

### Pipeline execution
Run 
`$ snakemake --configfile config/example_config.yaml -c1 ` 
 in the **src** folder. A successful run will create a run directory in the data folder. 
 
 ## Output
 The output comprises the following files and directories in the data folder:
 - AnnotSV.log
 - reads.fasta
 - reads.fasta.index
 - reads.fasta.index.fai
 - reads.fasta.index.gzi
 - reads.fasta.index.readdb
 - reads.vcf
 - reads_fastq_all.fastq
 - reads-ref.sorted.bam
 - reads-ref.sorted.bam.bai
 - stats
 - directory annotation
 - directory fastq
 - directory graphs
 - directory log
