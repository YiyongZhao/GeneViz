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

MODULES = [
    "LinkView_Visualizer",
    "MicroSynteny_Plotter",
    "GD_Classifier",
    "TE_Annotator",
]

def main():
    print(LOGO)
    parser = argparse.ArgumentParser(
        description="MicroSynViz: Visualizing Pairwise Genomic Microsynteny Within and Between Species",
        usage="MicroSynViz <module> [options]"
    )
    parser.add_argument(
        "module",
        nargs="?",
        choices=MODULES,
        help="Module to run: " + " | ".join(MODULES)
    )
    parser.add_argument("--version", action="version", version="MicroSynViz 1.0.0")

    args, remaining = parser.parse_known_args()

    if args.module is None:
        parser.print_help()
        print("\nAvailable modules:")
        for m in MODULES:
            print(f"  MicroSynViz {m} --help")
        sys.exit(0)

    # Dispatch to module
    if args.module == "LinkView_Visualizer":
        from microsynviz.LinkView_Visualizer import run
        run(remaining)
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
