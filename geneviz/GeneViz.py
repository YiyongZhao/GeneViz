#!/usr/bin/env python3
"""
GeneViz: A User-Friendly Toolkit for Visualizing Pairwise Genomic Microsynteny
Author: Yiyong Zhao (yiyong.zhao@yale.edu)
"""

import argparse
import sys

LOGO = """
###############################################################################################
  ██████╗ ███████╗███╗   ██╗███████╗██╗   ██╗██╗███████╗
 ██╔════╝ ██╔════╝████╗  ██║██╔════╝██║   ██║██║╚══███╔╝
 ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██║   ██║██║  ███╔╝
 ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ╚██╗ ██╔╝██║ ███╔╝
 ╚██████╔╝███████╗██║ ╚████║███████╗  ╚████╔╝ ██║███████╗
  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═══╝  ╚═╝╚══════╝
###############################################################################################
GeneViz: A User-Friendly Toolkit for Visualizing Pairwise Genomic Microsynteny across Any Species
Github:  https://github.com/YiyongZhao/GeneViz
Contact: yiyong.zhao@yale.edu
"""

MODULES = [
    "LinkView_Visualizer",
    "MicroSynteny_Plotter",
    "GD_Classifier",
    "TE_Annotator",
]

def main():
    print(LOGO)
    parser = argparse.ArgumentParser(
        description="GeneViz: Pairwise Genomic Microsynteny Visualization Toolkit",
        usage="GeneViz <module> [options]"
    )
    parser.add_argument(
        "module",
        nargs="?",
        choices=MODULES,
        help="Module to run: " + " | ".join(MODULES)
    )
    parser.add_argument("--version", action="version", version="GeneViz 1.0.0")

    args, remaining = parser.parse_known_args()

    if args.module is None:
        parser.print_help()
        print("\nAvailable modules:")
        for m in MODULES:
            print(f"  GeneViz {m} --help")
        sys.exit(0)

    # Dispatch to module
    if args.module == "LinkView_Visualizer":
        from geneviz.LinkView_Visualizer import run
        run(remaining)
    elif args.module == "MicroSynteny_Plotter":
        from geneviz.MicroSynteny_Plotter import run
        run(remaining)
    elif args.module == "GD_Classifier":
        from geneviz.GD_Classifier import run
        run(remaining)
    elif args.module == "TE_Annotator":
        from geneviz.TE_Annotator import run
        run(remaining)

if __name__ == "__main__":
    main()
