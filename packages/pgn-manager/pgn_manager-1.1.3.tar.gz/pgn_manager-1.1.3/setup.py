from setuptools import setup

setup(
    name="pgn_manager",
    version="1.1.3",
    description="library for managing pgn files",
    author="Luca Canali",
    author_email="lucacanali.dev@gmail.com",
    packages= ["pmanager"],
    install_requires=[
        "python-chess",
    ],
)