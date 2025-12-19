from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ." 
"""
In the context of setup.py, the -e . in requirements.txt is often used as a "trigger" 
to run the setup.py file automatically when you run pip install -r requirements.txt.
"""

def get_requirements(file_path: str) -> list[str]:
    '''
    get list of require package from the requirements text file
    
    :param file_path: location of file
    :type file_path: str
    :return: list of package name
    :rtype: List[str]
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="Telecom Sony",
    version='0.0.1',
    author="Akshil Shah",
    author_email="shahakshil21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)