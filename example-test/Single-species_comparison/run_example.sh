#!/bin/bash
# MicroSynViz example: Single-species comparison

cd "$(dirname "$0")"

MicroSynViz \
    --gene1 LOC_Os06g50440 \
    --gene2 LOC_Os06g50789 \
    --g1 genome_subset.fa --annos1 gene_subset.gff te_subset.gff \
    --g2 genome_subset.fa --annos2 gene_subset.gff te_subset.gff \
    --auto_complementary \
    --bezier \
    --extend 5000 \
    --output example_output
