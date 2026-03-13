#!/bin/bash
# MicroSynViz 示例：比较 LOC_Os06g50440 和 LOC_Os06g50789

python ./MicroSynViz.py \
    --gene1 LOC_Os06g50440 \
    --gene2 LOC_Os06g50789 \
    --gff gene_subset.gff \
    --fasta genome_subset.fa \
    --te_gff te_subset.gff \
    --auto_complementary \
    --output example_output \
    --bezier \
    --extend 5000
