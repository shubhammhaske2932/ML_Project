from setuptools import setup, find_packages
from typing import List

#Declaring varibale for setup functions
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
AUTHOR = 'Shubham Mhaske'
DESCRIPTION = 'Create a model to predict house price'
REQUIREMENT_FILE_NAME = 'requirement.txt'

#This functions return list of string
def get_requiremets_list()-->List[str]: 
    '''
    Description: This function is going to return list of requirement
    mentioned in the requirement.txt file

    Function: This function is going to return a list which contain name 
    of libraries mentioned in requirement.txt file 
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    vendor = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages() # find_packages return all the folder name wherever __init__ file is available
    install_requires = get_requiremets_list()
    
)
