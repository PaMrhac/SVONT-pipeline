from pathlib import Path

def fastq_to_fasta(path_fastq, path_out_fasta):
    path = Path(path_fastq)
    with open(path_out_fasta, mode='w') as reads:
        for file in sorted(path.iterdir()):
            with open(file,mode="r") as current:
                lines = current.readlines()
                n=1
                for line in lines:
                    if n == 1:
                        reads.write('>' + line[1:])
                        n += 1
                    elif n == 2:
                        reads.write(line)
                        n += 1
                    elif n == 3:
                        n += 1
                    else:
                        n = 1

fastq_to_fasta(snakemake.input[0], snakemake.output[0])