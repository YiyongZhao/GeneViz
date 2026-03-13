#!/bin/bash
# MicroSynViz example: Cross-species comparison

cd "$(dirname "$0")"

MicroSynViz \
    --region1 SpeciesA_Chr1:4901-6596 \
    --region2 SpeciesB_Chr7:4901-14119 \
    --g1 speciesA.fa --annos1 speciesA.gff speciesA_te.gff \
    --g2 speciesB.fa --annos2 speciesB.gff speciesB_te.gff \
    --auto_complementary \
    --bezier \
    --output cross_region_output
