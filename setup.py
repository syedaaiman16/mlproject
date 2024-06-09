from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # when it readlines from requirements.txt it also includes \n and add it therefore we have to remove and replace with ""
        requirements=[req.replace("\n","") for req in requirements]

        # -e . should not become in the list of requirements therefore we add this if condition
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Aiman',
author_email='pc9763.aiman@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)