#!/usr/bin/env python3
"""
MicroSynViz: Visualizing Pairwise Genomic Microsynteny Within and Between Species
Author: Yiyong Zhao (yiyong.zhao@yale.edu)
"""

import argparse
import sys

LOGO = r"""
###############################################################################################
 ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███████╗██╗   ██╗███╗   ██╗██╗   ██╗██╗███████╗
 ████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██║   ██║██║╚══███╔╝
 ██╔████╔██║██║██║     ██████╔╝██║   ██║███████╗ ╚████╔╝ ██╔██╗ ██║██║   ██║██║  ███╔╝
 ██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║╚════██║  ╚██╔╝  ██║╚██╗██║╚██╗ ██╔╝██║ ███╔╝
 ██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝███████║   ██║   ██║ ╚████║ ╚████╔╝ ██║███████╗
 ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═══╝  ╚═╝╚══════╝
###############################################################################################
MicroSynViz: Visualizing Pairwise Genomic Microsynteny Within and Between Species
GitHub:  https://github.com/YiyongZhao/MicroSynViz
Contact: yiyong.zhao@yale.edu
"""

from microsynviz import __version__

def main():
    print(LOGO)

    # If no args or first arg looks like a direct flag (--gene1, --region1, etc.),
    # run the core LinkView visualizer directly
    if len(sys.argv) > 1 and sys.argv[1].startswith('--'):
        from microsynviz.core import main as core_main
        core_main()
        return

    parser = argparse.ArgumentParser(
        description="MicroSynViz: Visualizing Pairwise Genomic Microsynteny Within and Between Species",
        usage="MicroSynViz [--gene1/--region1 ...] or MicroSynViz <module> [options]"
    )
    parser.add_argument(
        "module",
        nargs="?",
        choices=["LinkView_Visualizer", "MicroSynteny_Plotter", "GD_Classifier", "TE_Annotator"],
        help="Module to run (or pass --gene1/--region1 directly for LinkView visualization)"
    )
    parser.add_argument("--version", action="version", version=f"MicroSynViz {__version__}")

    args, remaining = parser.parse_known_args()

    if args.module is None:
        parser.print_help()
        print(f"\nDirect usage (most common):")
        print(f"  MicroSynViz --gene1 GeneA --gene2 GeneB --gff annotation.gff --fasta genome.fa")
        print(f"\nModule usage:")
        print(f"  MicroSynViz LinkView_Visualizer --help")
        sys.exit(0)

    if args.module == "LinkView_Visualizer":
        from microsynviz.core import main as core_main
        sys.argv = [sys.argv[0]] + remaining
        core_main()
    elif args.module == "MicroSynteny_Plotter":
        from microsynviz.MicroSynteny_Plotter import run
        run(remaining)
    elif args.module == "GD_Classifier":
        from microsynviz.GD_Classifier import run
        run(remaining)
    elif args.module == "TE_Annotator":
        from microsynviz.TE_Annotator import run
        run(remaining)

if __name__ == "__main__":
    main()
