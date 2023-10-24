import setuptools 
from pathlib import Path 


setuptools.setup(
    name="pinto_db",
    version="1.0",
    long_description= Path("description.txt").read_text(),
    packages= setuptools.find_packages(exclude=["virt"]),
    author= "Aaron",
    
)