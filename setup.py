from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
 
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip()]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT) 
  
setup(
    name="FraudDetection",
    version="0.1.0",
    author="Nikhil Kaushik",
    author_email="nikhilkaushik171@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)   