# Expanded dataset of mechanical properties and observed phases of multi-principal element alloys

This repository contains data and processing scripts to generate a dataset of mechanical properties of MPEAs.

To install the proper dependencies in your Python environment, a [requirements file](requirements.txt) has been included.

`pip install -r requirements.txt`

## Data
- [MPEA dataset](MPEA_dataset.csv)
The complete database file. Contains all compositions, properties, and reference info.

- [Compositions](compositions.csv)
A csv of all the unique compositions in the database. 

- [Groupd by composition](grouped_by_composition.xlsx)
A styled excel file grouping the data by composition.


## Processing files
- [2018 data](/2018_data/2018_data.csv)
This file was generated from previous reviews ([Gorsse2018](https://doi.org/10.1016/j.dib.2018.11.111), [Couzinine2018](https://doi.org/10.1016/j.dib.2018.10.071)).

- [2019 data](/2019_data/2019_data.csv)
This file was generated through the extraction of data from references in [wos_query_refs.bib](/2019_data/wos_query_refs.bib).

- [combined_data](combined_data.csv)
This is the raw input data for processing.

## Scripts
1. [Get references](get_references.ipynb)
This script combines data from previous reviews and 2019 data, assigns an updated identifier for each reference and searches for references info via Crossref. Outputs [combined_data.csv](combined_data.csv) and [references.csv](references.csv). 

2. [Process](process.ipynb)
Takes [combined_data.csv](combined_data.csv) as an input and generates [MPEA dataset](MPEA_dataset.csv) (the master data file). This file is shared publicly on [Figshare](https://doi.org/10.6084/m9.figshare.12642953) and in PIF format on [Citrination](https://citrination.com/datasets/190954).

3. [Get stats and tables](get_stats_and_tables.ipynb)
This script produces data tables from the master data file.

4. [Get compositions](get_compositions.ipynb)
This script produces [Compositions](compositions.csv) and [Groupd by composition](grouped_by_composition.xlsx) to promote interpretation.

5. [Get figures](get_figures.ipynb)
This script produces figures shown in the manuscript.