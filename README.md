# FLVENV

`Virtual ENV initialization in one line project for frontline.`

----
####requirements:
- `python 3` - https://www.python.org/downloads/
- `miniconda` - https://docs.conda.io/en/latest/miniconda.html
-----


##### how to use:
1) clone this repository

2) open(or navigate into) it with CMD / Terminal / Pycharm etc.
enter one of the following commands in the terminal - 

    `python build.py --name yourenvname`
    
    `python build.py -n yourenvname`

change yourenvname to the name you want.

The build will take some time, and will install all of the basic packages we need:

Of course we can add more, and you can install them normally using conda.
    
    Will install : 
     
    pandas
    Shapely
    geopandas
    rtree
    scipy
    scikit-learn
    matplotlib
    graphviz
    datatables
    mlflow
    

##### how to run:
you activate it just as any other conda env.

`conda activate ./yourenvname`



## `Changelog`
`28.12.20 [STABLE - no git extension]` :
- New JupyterLab version is out, so currently can't add Git, will need to wait a few days till it has support
- Working version, and rebuilding the installation to modular version.