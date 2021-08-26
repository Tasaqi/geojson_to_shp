# Geojson_to_shp 


## Installation

* we recommend to use the conda package manager. This can be obtained by installing the Anaconda Distribution (a free Python distribution for data science), or through miniconda (minimal distribution only containing Python and the conda package manager). See also the installation docs for more information on how to install Anaconda or miniconda locally.:
* Installing with Anaconda / conda [here]("https://docs.anaconda.com/anaconda/install/windows/").
  
* After sucessfully install conda,  windowkey+s (open search Panel), search Anaconda Command Prompt

  
* #### Dependencies
    0. Open Anaconda Command Prompt and type these commands
        ```bash
            $ conda create -n geo_env
            $ conda activate geo_env
            $ conda config --env --add channels conda-forge
            $ conda config --env --set channel_priority strict
            $ conda install python=3 geopandas
        ```
    1. Install requests package for API request:
        ```bash
            $ pip install requests
        ```
    2. Install geojson package for geojson file handling:
        ```bash
            $ pip install geojson
        ```

* #### Run It
    write this command:
    ```bash
        $ python script.py
    ```
