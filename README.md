# Bunch analysys

## General (Start here)

To install the dependencies for all scripts run in a terminal:

```shell
$ pip install -r requirements.txt
```

## group_extract.py

Given a trajectory (a table with columns x, h, m in fixed-width Fortran format)
this script identifies all bunches and saves them as CSVs to analyze later.
Bunches are saved both "as-is" and with x rescaled to zero versions 
of themselves.

### How to use

```shell
python group_extract.py
```

This will bring up the following UI:


![Group extract GUI](static/group_extract.png)


#### Basic Usage

1. Click the **Browse** button for the **input_path** field at the top and select the trajectory.

2. Press **Start**
