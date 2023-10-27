#!/usr/bin/env python3

"""
** Configuration file for pip. **
---------------------------------
"""

import sys
from setuptools import find_packages, setup, Extension

import numpy as np

import cutcutcodec


COMP_RULES = {
    "define_macros": [("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")], # for warning
    "extra_compile_args": [
        "-O2", # hight optimisation
        "-march=native", # uses local processor instructions
        "-fopenmp", # for threads
    ],
    "include_dirs": [np.get_include()], # requires for #include numpy
}


if sys.version_info < (3, 9):
    print(
        "cutcutcodec requires Python 3.9 or newer. "
        f"Python {sys.version_info[0]}.{sys.version_info[1]} detected"
    )
    sys.exit(-1)

module_fractal = Extension(
    "cutcutcodec.core.generation.video.c_fractal",
    sources=["cutcutcodec/core/generation/video/fractal/fractal.c"],
    **COMP_RULES,
)


with open("README.rst", "r", encoding="utf-8") as file:
    long_description = file.read()


setup( # https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools
    name="cutcutcodec",
    version=cutcutcodec.__version__,
    author="Robin RICHARD (robinechuca)",
    author_email="serveurpython.oz@gmail.com",
    description="video editing software",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://framagit.org/robinechuca/cutcutcodec/-/blob/main/README.rst",
    ext_modules=[module_fractal],
    data_files=[
        ("cutcutcodec/", ["README.rst", ".pylintrc"]),
    ],
    packages=find_packages(),
    install_requires=[ # dependences: apt install graphviz-dev ffmpeg
        "av", # apt install ffmpeg python3-av
        "cairosvg",
        "click", # apt install python3-click
        "networkx >= 3.0", # apt install python3-networkx
        "numpy >= 1.22", # apt install python3-numpy
        "opencv-contrib-python-headless", # apt install python3-opencv
        "sympy >= 1.10", # apt install python3-sympy
        "torch >= 2.0",
        "tqdm", # apt install python3-tqdm
        "unidecode", # apt install python3-unidecode
    ],
    extras_require={
        "gui": [
            "black", # apt install black python3-pyls-black
            "pdoc3",
            "pyqt6", # apt install python3-pyqt6[.sip]
            "pyqtgraph >= 0.3.1",
            "qtpy",
            "qtpynodeeditor >= 0.3.1",
        ], # apt install pylint, python3-pylint-common, python3-pytest
        "optional": [
            "black",
            "pdoc3",
            "pylint == 2.17.7",
            "pyqt6",
            "pyqtgraph >= 0.3.1",
            "pytest",
            "qtpy",
            "qtpynodeeditor >= 0.3.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "cutcutcodec=cutcutcodec.__main__:main",
            "cutcutcodec-test=cutcutcodec.testing.runtests:test",
        ],
        "gui_scripts": [
            "cutcutcodec-qt=cutcutcodec.gui.__main__:main",
        ]
    },
    classifiers=[ # all classifiers https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Environment :: GPU",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: C",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.9",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Multimedia :: Sound/Audio :: Mixers",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Code Generators",
        "Typing :: Typed",
    ],
    keywords=[
        "effect",
        "ffmpeg",
        "filter",
        "graphical",
        "video editing",
    ],
    python_requires=">=3.9,<3.12",
    project_urls={
        "Source Repository": "https://framagit.org/robinechuca/cutcutcodec/",
        # "Bug Tracker": "https://github.com/engineerjoe440/ElectricPy/issues",
        # "Documentation": "http://python-docs.ddns.net/raisin/",
        # "Packaging tutorial": "https://packaging.python.org/tutorials/distributing-packages/",
        },
    include_package_data=True,
)
