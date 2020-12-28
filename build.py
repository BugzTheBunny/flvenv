import os
import time
import logging
import argparse

# conda install -c conda-forge datatables

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Enviroment name")
args = vars(ap.parse_args())

# Logger
logging.basicConfig(filename='logs.log', level=logging.DEBUG)

# Settings
REQUIREMENTS_FILE = 'requirements.txt'
ENV_NAME = format(args["name"])
ACTIVATE = f'conda activate ./{ENV_NAME} && '

# Commands
# rebuilding jupyter
rebuild = f'{ACTIVATE}jupyter lab build'
rebuild_no_dev = f'{ACTIVATE}jupyter lab build --dev-build=False'

# jupyter lab basic dependencies
ipywid = f'{ACTIVATE}conda install -c conda-forge ipywidgets -y'
widget_manager = f'{ACTIVATE}jupyter labextension install @jupyter-widgets/jupyterlab-manager@2.0'
nodejs_addon = f'{ACTIVATE}conda install -c conda-forge nodejs -y'

# Installing git on jupyter
git_setup = f'{ACTIVATE}pip3 install --upgrade jupyterlab jupyterlab-git'


def start_build():
    logging.info('Starting build..')
    try:
        os.system(f'conda activate && conda create --prefix ./{ENV_NAME} --file requirements.txt -y')
        logging.info('ENV created')
    except Exception as e:
        print('Something went wrong, check log files.')
        logging.error(str(e))


def build_jupyter_base():
    try:
        print(
            '\n-------------------------------------------\n\t\t\t'
            'Upgrading Jupyter Lab'
            '\n-------------------------------------------\n')
        logging.info('Upgrading Jupyter Lab...')
        os.system(nodejs_addon)
        os.system(ipywid)
        os.system(widget_manager)
        os.system(rebuild)
    except Exception as e:
        print('Something went wrong, check log files.')
        logging.error(f'BUILD BASE ERROR : {str(e)}')


def add_git_extension():
    try:
        print('\n---Installing Git---\n')
        logging.info('Installing Git')
        os.system(git_setup)
        os.system(rebuild_no_dev)
        os.system(rebuild)
    except Exception as e:
        print('Something went wrong, check log files.')
        logging.error(f'ADD GIT ERROR : {str(e)}')


if __name__ == '__main__':
    if REQUIREMENTS_FILE in os.listdir():
        print(f'{REQUIREMENTS_FILE} loaded successfully')
        print('Searching for conda on your system...')
        if 'conda' in os.popen('pip freeze').read():
            print('conda found.')
            start_build()
            build_jupyter_base()
            add_git_extension()
            time.sleep(3)
        else:
            print('Could not find conda on your system, please install miniconda using the following link: \n'
                  'https://docs.conda.io/en/latest/miniconda.html\n')
    else:
        print(f'ERROR: {REQUIREMENTS_FILE} file was not found...')
