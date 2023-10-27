import setuptools
from pathlib import Path

setuptools.setup(
    name='lyn_env',
    version='0.0.5',
    description='A OpenAI Env for lyn',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="lyn_env*"),
    install_requires=['gym']
)