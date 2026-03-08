# Example Data - LinkView_Visualizer

This directory contains example input files for `GeneViz LinkView_Visualizer`.

## Files

| File | Description |
|------|-------------|
| `gene_pairs.tsv` | Example gene pairs (geneA TAB geneB) |
| `speciesA.lens` | Chromosome length file for genome A |
| `blastn.out` | BLASTN output (-outfmt 6) — add your own |
| `speciesA.gff` | GFF3 annotation for genome A — add your own |
| `speciesB.gff` | GFF3 annotation for genome B — add your own |

## Usage

```bash
GeneViz LinkView_Visualizer \
    --input_pairs gene_pairs.tsv \
    --blast_result blastn.out \
    --gff_a speciesA.gff \
    --gff_b speciesB.gff \
    --lens_a speciesA.lens \
    --lens_b speciesB.lens \
    --output_dir results/
```
