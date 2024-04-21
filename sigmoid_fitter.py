import argparse
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import group_extract as ge


def logistic_curve(x, a, k, xc):
    return a / (1 + np.exp(-k * (x - xc)))


def fit_group_with_logistic_curve(group: ge.ExtractedPeak):
    x_values = group.x_values
    h_values = group.h_values

    x_values = x_values - x_values[0]
    h_values = h_values - h_values[0]
    # fit the logistic curve
    popt, _ = curve_fit(
        logistic_curve, x_values, h_values, p0=[max(h_values), 1, np.mean(x_values)]
    )
    return popt


def calculate_big_K(popt):
    _, k, xc = popt
    return k * 2 * xc


def plot_extracted_peaks(extracted_peaks):
    for group in extracted_peaks:
        x_values = group.x_values
        m_values = group.m_values
        plt.plot(x_values, m_values)

    plt.title("Extracted Peaks (Close to see big K plot)")
    plt.xlabel("x")
    plt.ylabel("m")
    plt.show()


def plot_big_k_values(file_name, big_K_values):
    print(f"Big K values: {big_K_values}")
    plt.plot(big_K_values)
    plt.xlabel("Peak Index (higher index $\\rightarrow$ peak is further to the right)")
    plt.ylabel("Big K")
    plt.title(f"Big K values for each peak ({file_name})")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Sigmoid Fitter")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print("Error: Input file does not exist")
        sys.exit(1)

    df = ge.load_fortran_format_as_pandas(args.input_file)
    extracted_peaks = ge.extract_peaks(df)
    plot_extracted_peaks(extracted_peaks)

    fitting_results = (
        fit_group_with_logistic_curve(group) for group in extracted_peaks
    )
    big_K_values = [calculate_big_K(popt) for popt in fitting_results]

    plot_big_k_values(Path(args.input_file).name, big_K_values)


if __name__ == "__main__":
    main()
