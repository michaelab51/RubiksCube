from setuptools import setup, find_packages

setup(
    name="Rubikovka",
    version="1.0",
    author="Michaela Brzková",
    description="Řešitel Rubikovy kostky",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'Rubikovka = Rubikovka:main',
        ],
    },
)
