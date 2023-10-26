## maelstrom-yr

[![PyPI version](https://badge.fury.io/py/climetlab-maelstrom-yr.svg)](https://badge.fury.io/py/climetlab-maelstrom-yr)
[![workflow](https://github.com/metno/maelstrom-yr/workflows/build/badge.svg)](https://github.com/metno/maelstrom-yr/actions)

A dataset plugin for climetlab for the dataset maelstrom-yr. Check out this
[notebook](https://github.com/metno/maelstrom-yr/blob/main/notebooks/demo_yr.ipynb).

## Datasets description

Contains gridded weather data for the Nordics. It contains both predictors (gridded weather forecasts) and
predictand (gridded analysis fields). The forecasts are used operationally for the Nordic region on
[https://www.yr.no](https://www.yr.no) and currently a simple ML-solution is used, as described in
[Nipen et al. 2020](https://journals.ametsoc.org/view/journals/bams/101/1/bams-d-18-0237.1.xml).

## Using climetlab to access the data

The data can be loaded by the climetlab package (https://github.com/ecmwf/climetlab). The dataset has the
following arguments:
- size: Which dataset to load (currently 5GB is supported, but in the future a 5TB dataset will be added)
- parameter: Which predictand to load (currently "air_temperature" is supported)
- dates: If left blank, the whole dataset is loaded. Otherwise, provide a list of dates in "YYYY-MM-DD"
format to load a subset

Here is an example of how to load the data:
```
!pip install climetlab climetlab_maelstrom_yr
import climetlab as cml
ds = cml.load_dataset("maelstrom-yr", size="5GB", parameter="air_temperature", dates=['2020-06-29'])
ds.to_xarray()
```
