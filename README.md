# Bunch analysys

## General (Start here)

To install the dependencies for all scripts run in a terminal:

```shell
$ pip install -r requirements.txt
```

## group_extract.py

Given a trajectory (**a table with columns x, h, m in fixed-width Fortran format**)
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

1. Click the **Browse** button for the **input_path** field at the top and select the trajectory (**.dat file**).

2. Press **Start**

#### Advanced Usage

1. Click the **Browse** button for the **input_path** field at the top and select the trajectory (**.dat file**).
2. You can select a different output_dir than the default one using the **Browse** button for the **output_dir** field.
3. Choose a different prefix for extracted CSV files (default is "peak")
4. Select a peak extraction threshold (the smaller the value, the smaller the width of the extracted peak).
