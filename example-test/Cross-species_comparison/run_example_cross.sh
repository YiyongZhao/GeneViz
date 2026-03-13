#!/bin/bash
# MicroSynViz example: Cross-species comparison

cd "$(dirname "$0")"

MicroSynViz \
    --region1 SpeciesA_Chr1:4901-6596 \
    --region2 SpeciesB_Chr7:4901-14119 \
    --gff1 speciesA.gff \
    --fasta1 speciesA.fa \
    --gff2 speciesB.gff \
    --fasta2 speciesB.fa \
    --te_gff1 speciesA_te.gff \
    --te_gff2 speciesB_te.gff \
    --auto_complementary \
    --bezier \
    --output cross_region_output
