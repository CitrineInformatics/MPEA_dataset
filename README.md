# Expanded dataset of mechanical properties and observed phases of multi-principal element alloys

This repositoy contains data and processing scripts to generate a dataset of mechanical properties of MPEAs.

1. [2018 data](/2018_data/2018_data.csv)
This file was generated from previous reviews ([Gorsse2018](https://doi.org/10.1016/j.dib.2018.11.111), [Couzinine2018](https://doi.org/10.1016/j.dib.2018.10.071)).

2. [2019 data](/2019_data/2019_data.csv)
This file was generated through the extraction of data from references in [wos_query_refs.bib](/2019_data/wos_query_refs.bib).

3. [Combine and process](combine_and_process.ipynb) Takes 2018 and 2019 data as input and generates [MPEA dataset](MPEA_dataset.csv) (the master data file). This file is shared publicly on [Figshare](https://doi.org/10.6084/m9.figshare.12642953) and in PIF format on [Citrination](https://citrination.com/datasets/190954).

4. [Get stats and tables](get_stats_and_tables.ipynb) This script produces data tables from the master data file.

5. [Get compositions](get_compositions.ipynb) This script produces different views of the data to promote interpretation.

6. [Get figures](get_figures.ipynb) This script produces figures shown in the manuscript.