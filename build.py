import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Enviroment name")
args = vars(ap.parse_args())
ENV_NAME = format(args["name"])

# TODO :
"""
check MLFLOW
follow Git extension status
"""


class Commands:
    """
    These are the commands that will be used to install everything.

    ACTIVATE -> env pre-activation before commands

    install_lab -> Jupyter Lab installation
    ipywid -> basic dependency to install extensions
    nodejs_addon -> basic dependency to install extensions
    git_setup -> Git extension for JupyterLab - Currently not supported for version 3.0
    rebuild -> Rebuild the app
    rebuild_nd -> Sometimes the one above wont work, you may you this one

    """

    ACTIVATE = f'conda activate ./{ENV_NAME} && '
    rebuild = 'jupyter lab build'
    install_lab = 'conda install -c conda-forge jupyterlab -y'
    rebuild_nd = f'jupyter lab build --dev-build=False'
    ipywid = 'conda install -c conda-forge ipywidgets -y'
    nodejs_addon = 'conda install -c conda-forge nodejs -y'
    git_setup = 'conda install -c conda-forge jupyterlab jupyterlab-git -y'


class Libs:
    """
    These are the basic libs that will be installed, you may add libs here safely.
    NOTE: Not all libs can be found or installed via conda, some of them may require you to install via pip.
    """
    libs_to_install = [
        'pandas',
        'Shapely',
        'geopandas',
        'rtree',
        'scipy',
        'scikit-learn',
        'matplotlib',
        'graphviz',
        'datatables',
        # 'mlflow' - need to view how to fix.
    ]


def start_build():
    os.system(f'conda activate && conda create --prefix ./{ENV_NAME} -y')


def run_command(command):
    print('\n' * 10, f'[Running] > {command}', '\n' * 3)
    os.system(f'{Commands.ACTIVATE}{command}')


def install_lib(lib_name):
    print('\n' * 10, f'[Running] > {lib_name} installation', '\n' * 3)
    os.system(f'{Commands.ACTIVATE}conda install -c conda-forge {lib_name} -y')


def build_jupyter_base():
    """
    Jupyter Lab Setup
    1 - Install Jupyter Labs
    2 - Install NodeJS addon for python (needed for Jupyter Lab Extensions)
    3 - Install ipywidget (Basic dependency for Jupyter Lab Extensions)
    4 - rebuild app (required to make it work properly)
    """
    run_command(Commands.install_lab)
    run_command(Commands.nodejs_addon)
    run_command(Commands.ipywid)
    run_command(Commands.rebuild)


def add_git_extension():
    """
    Git installation
    1 - install git
    2 - rebuild app (required to make it work)
    """
    run_command(Commands.git_setup)
    run_command(Commands.rebuild_nd)


if __name__ == '__main__':
    """
    Main Installation process
    HLD:
        - verify the user has conda
            if has :
                - create ENV with the name the user picks
                - building the base for jupyter labs
                - add git extension [CURRENTLY NOT WORKING]
                - install all of the base libraries
            else:
                sends the user a link for miniconda.
    """
    if 'conda' in os.popen('pip freeze').read():
        start_build()
        build_jupyter_base()
        # add_git_extension()
        for library in Libs.libs_to_install:
            install_lib(library)
    else:
        print('Could not find conda on your system, please install miniconda using the following link: \n'
              'https://docs.conda.io/en/latest/miniconda.html\n')
