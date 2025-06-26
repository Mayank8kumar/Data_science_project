from setuptools import find_packages, setup
from typing import List

# HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirmeents
    '''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Datascience Project',
    version='0.0.1',
    author='Mayank',
    author_email='mayankkumar08132@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)



### For running the setup file ( Command - python setup.py install )
### Another way was using the -e . ( This will directly call the setup if we write it in the requirements.txt)