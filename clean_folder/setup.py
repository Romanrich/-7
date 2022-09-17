from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version='1.0',
    entry_points = {
        "console_scripts" : ["clean = clean_folder.clean:mein"],
    },
    packages=find_packages(),
    description="Clean folder script",
)