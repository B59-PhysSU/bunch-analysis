import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import group_extract as ge


def count_unique_heights(peak: ge.ExtractedPeak) -> int:
    # Each unique height jump is a step
    return len(set(peak.h_values.tolist()))


def run(args: argparse.Namespace) -> None:
    # Validate input file existence
    if not os.path.isfile(args.input_path):
        print("Error: Input file does not exist.")
        return
    os.makedirs(args.output_dir, exist_ok=True)
    
    df = ge.load_fortran_format_as_pandas(args.input_path)
    extracted_peaks = ge.extract_peaks(df, rel_height=args.threshold)
    num_steps = [count_unique_heights(peak) for peak in extracted_peaks]
    
    print("Total number of steps: ", sum(num_steps))
    counts, bins = np.histogram(num_steps, bins="auto")
    plt.stairs(counts, bins, fill=True)
    file_name = Path(args.input_path).stem + "_histogram.png"
    plt.savefig(os.path.join(args.output_dir, file_name), dpi=300)
    
    if args.show_plot:
        plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract peaks from data and save as CSV files."
    )
    parser.add_argument(
        "input_path",
        help="Path to the input data file. "
        "Expected format is a fixed-width table with 3 columns. The order of columns "
        "should be x, m, h",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        default=os.path.join(os.getcwd(), "output"),
        help="Path to the output directory. Default is the current working directory + 'output'.",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.95,
        help="Threshold for peak width (between 0 and 1 - peak bottom). Default is 0.95.",
    )
    parser.add_argument(
        "-b",
        "--bin-count",
        type=int,
        default=20,
        help="Number of bins for the histogram. Default is 20.",
    )
    parser.add_argument(
        "--max-bin",
        type=int,
        default=100,
        help="Maximum bin value for the histogram. Default is 100.",
    )
    parser.add_argument(
        "--show-plot",
        action=argparse.BooleanOptionalAction,
        help="Whether to show the plot in a matplotlib window. Default is to show the plot",
    )

    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
