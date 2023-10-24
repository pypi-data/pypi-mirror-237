from setuptools import setup, find_packages

setup(
    name="pgn_manager",
    version="1.0.4",
    description="library for managing pgn files",
    author="Luca Canali",
    author_email="lucacanali.dev@gmail.com",
    packages=find_packages(),
    install_requires=[
        "python-chess",
    ],
)