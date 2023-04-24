# Towards reproducible hydrological modeling with HydroMT

This repository was build for the EGU GA 2023 presentation ["Towards reproducible hydrological modeling with HydroMT"](https://doi.org/10.5194/egusphere-egu23-13770)

The input data and poster are archived at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7858596.svg)](https://doi.org/10.5281/zenodo.7858596)

Try the script yourself through [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DirkEilander/hydromt-wflow-sfincs/HEAD?labpath=src)

## Why HydroMT?

> "results might be reproduced for only 0.6% to 6.8% of all 1,989 articles." (Stagge et al. 2019)

> "models created with a graphical user interface are not easily reproduced, archived, or independently verified." (Bakker et al. 2014)

HydroMT (Eilander et al. 2023a) aims to make the model building and analysis process:

- **Reproducible** by well-defined model building workflows, good documentation and meta data
- **Fast** by automating the boring
- **Modular** through building blocks which can be reused between different model software
- **Data- and model-agnostic** through a common data and model interface.
- **Easy to extend** to new model software  through a plugin infrastructure

## How to use HydroMT?

Building a model with HydroMT consists of three steps:

1. Prepare a data catalog file
2. Configure your model setup in a yaml file
3. Run HydroMT build command

## Case Study

### Introduction

Mozambique's Sofala province was hit by tropical Cyclone Idai in March 2019. With torrential rainfall, 165 km/h winds and 4.4m surge, it caused extensive flooding and destroyed over 60k homes, leaving 286k homeless.

### Model experiment

Using HydroMT, we setup an offline coupled hydrological (Wflow; van Verseveld et al. 2022) - hydrodynamic (SFINCS; Leijnse et al. 2021) model to replicate the flood event (Eilander et al. 2023b). Subsequently, we devise a model experiment to evaluate the sensitivity of both models towards two different land use (Vito, Globcover) and rainfall (ERA5, Chirps) data products. 

## Lessons learned 
- HydroMT facilitates setting up a reproducible model experiment: The workflow is well-defined, each step is documented, and the used input data is  open and accessible. See link to GitHub repository below for the full experiment.
- HydroMT makes it easy to setup offline coupled models for supported software. See HydroMT docs for full list of supported model software.
- Model input data is scattered around the web and behind many different APIs. More work should be done in making this data better accessible. 

## Folder structure

```
src
  *.ipynb           -> scripts to setup and run the model experiment
  *.yml             -> workflows for how to setup the models
  *.py              -> support scripts
data                -> input data directory (will be downloaded by the scripts)
models              -> model data directory (will be prepared by the scripts)
bin                 -> binary exectables for SFINCS and Wflow (not contained in the repo)
```

## HydroMT docs

- [HydroMT Core docs](https://deltares.github.io/hydromt/latest/)
- [HydroMT-SFINCS docs](https://deltares.github.io/hydromt_sfincs/latest/)
- [HydroMT-WFLOW docs](https://deltares.github.io/wflow_sfincs/latest/)


## References
- Bakker (2014). Python scripting: the return to programming. Ground Water, 52(6), 821–822. https://doi.org/10.1111/gwat.12269
- Eilander et al. (2023a). HydroMT: Automated and reproducible model building and analysis. Journal of Open Source Software, 8(83), 4897. https://doi.org/10.21105/joss.04897
- Eilander et al. (2023b). A globally-applicable framework for compound flood hazard modeling. Natural Hazards and Earth System Sciences, 23(2), 1–40. https://doi.org/10.5194/nhess-23-823-2023
- Leijnse et al. (2021). Modeling compound flooding in coastal systems using a computationally efficient reduced-physics solver: Including fluvial, pluvial, tidal, wind- and wave-driven processes. Coastal Engineering, 163, 103796. https://doi.org/10.1016/j.coastaleng.2020.103796
- van Verseveld et al. (2022). Wflow_sbm v0.6.1, a spatially distributed hydrologic model: from global data to local applications. In Geoscientific Model Development Discussions. https://doi.org/10.5194/gmd-2022-182
- Stagge et al. (2019). Assessing data availability and research reproducibility in hydrology and water resources. Scientific Data, 6, 190030. https://doi.org/10.1038/sdata.2019.30

