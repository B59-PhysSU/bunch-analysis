#!/bin/bash

DIR=$1

find "${DIR}" -name "*.dat" | parallel python3 ../../group_histogram.py {} --no-show-plot