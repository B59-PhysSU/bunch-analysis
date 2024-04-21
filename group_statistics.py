#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt
import pandas as pd


def measure_group(df):
    W = df["x"].values[-1]  - df["x"][0]
    H = df["h"].values[-1] - df["h"][0]
    return W, H

for file in os.listdir("output"):
    if file.endswith(".csv"):
        df = pd.read_csv(f"output/{file}")
        W, H = measure_group(df)
        print(f"{file}: {W=}, {H=}")
        