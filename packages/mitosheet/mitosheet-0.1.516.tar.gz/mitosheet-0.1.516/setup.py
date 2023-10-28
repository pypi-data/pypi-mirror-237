#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
The mitosheet package is distributed under the mitosheet and mitosheet3
package names on pip. The package.json will tell you all you need to 
know about which one we are in currently using.

As such, this setup.py script reads in the package.json and sets up
the proper package.
"""

from __future__ import print_function
from glob import glob
from os.path import join as pjoin
import json
import setuptools
from pathlib import Path


from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
    skip_if_exists,
)

from setuptools import setup

HERE = Path(__file__).parent.resolve()

package_json = json.loads(open('package.json').read())
lab_path = Path(pjoin(HERE, 'mitosheet', 'labextension'))
notebook_path = Path(pjoin(HERE, 'mitosheet', 'nbextension'))

python_requires='>=3.4'

name = 'mitosheet'

# Representative files that should exist after a successful build
jstargets = [
    str(lab_path / "package.json"),
    str(notebook_path / "index.js"),
]

package_data_spec = {
    'mitosheet': ["*"],
}

labext_name = name

data_files_spec = [
    # Notebook extension data files
    ('share/jupyter/nbextensions/mitosheet', notebook_path, '**'),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'mitosheet.json'),

    # Lab extension data files
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
]


cmdclass = create_cmdclass("jsdeps",
    package_data_spec=package_data_spec,
    data_files_spec=data_files_spec
)

js_command = combine_commands(
    install_npm(HERE, build_cmd="build:all", npm=["jlpm"]),
    ensure_targets(jstargets),
)

is_repo = (HERE / ".git").exists()
if is_repo:
    cmdclass["jsdeps"] = js_command
else:
    cmdclass["jsdeps"] = skip_if_exists(jstargets, js_command)

setup_args = dict(
    name                    = name,
    version                 = package_json["version"],
    url                     = package_json["homepage"],
    author                  = package_json["author"]["name"],
    author_email            = package_json["author"]["email"],
    description             = package_json["description"],
    license                 = "GNU Affero General Public License v3",
    long_description="""
    To learn more about Mito, checkout out our documentation: https://docs.trymito.io/getting-started/installing-mito\n\n
    Before installing Mito \n\n
    1. Check that you have Python 3.6 or above. To check your version of Python, open a new terminal, and type python3 --version. If you need to install or update Python, restart your terminal after doing so.\n\n
    2. Checkout our terms of service and privacy policy. By installing Mito, you're agreeing to both of them. Please contact us at aaron [@] sagacollab [dot] com with any questions.\n\n
    Installation Instructions \n\n
    For more detailed installation instructions, see our documentation: https://docs.trymito.io/getting-started/installing-mito\n\n
    1. pip install mitosheet\n\n
    2. Launch JupyterLab 3.0 and open a new notebook\n\n
    3. In the notebook, run the following code:\n\n
    import mitosheet\n\n
    mitosheet.sheet()\n\n
    """,
    long_description_content_type = "text/markdown",
    cmdclass                 = cmdclass,
    packages                 = setuptools.find_packages(exclude=['deployment']),
    package_data             = {'': ['*.js', '*.css', '*.html']},
    install_requires=[        
        "jupyterlab~=3.0",
        # We allow users to have many versions of pandas installed. All functionality should
        # work, with the exception of Excel import, which might require additonal dependencies
        'pandas>=0.24.2',
        'analytics-python',
        # Graphing libraries
        'plotly>=4.14.3',
        'chardet>=3.0.4',
        # For XLSX, reading - we don't fix so works on all python versions
        'openpyxl',
        # xlsxwriter is needed for adding formatting to exported Excel sheets. 
        # We pin to a pretty old version because the formatting functionality hasn't changed in a long time.
        'xlsxwriter>=0.6.9,<=3.1.3',
    ],
    extras_require = {
        'test': [
            'pytest',
            'flake8',
            'types-chardet',
            'types-requests',
            'mypy',
            'pytest_httpserver'
        ],
        'deploy': [
            'wheel', 
            'twine',
            "jupyter_packaging<=0.10.6",
            "setuptools==56.0.0"
        ],
        'streamlit': [
            'streamlit>=1.24',
        ],
        'optional_feature_dependencies': [
            # According to this documentation (https://github.com/snowflakedb/snowflake-connector-python),
            # snowflake-connect-python requires at least Python 3.7
            'snowflake-connector-python[pandas]; python_version>="3.7"',
            'streamlit>=1.24',
            'dash'
        ]
    },
    zip_safe                = False,
    include_package_data    = True,
    python_requires         = ">=3.6",
    platforms               = "Linux, Mac OS X, Windows",
    keywords                = ["Jupyter", "JupyterLab", "JupyterLab3"],
    classifiers             = [
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Jupyter",
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
