from setuptools import setup, find_packages


setup(
    name='aigrader',
    version='0.1',
    packages=['aigrader',],
    install_requires=[
        #'appnope==0.1.0',
        'astor==0.8.1',
        #'backcall==0.2.0',
        #'certifi==2020.6.20',
        #'chardet==3.0.4',
        'click==7.1.2',
        #'colorama==0.4.3',
        #'decorator==4.4.2',
        #'dgl==0.4.3.post2',
        #'flask==1.1.2',
        #'future==0.18.2',
        #'graphviz==0.13.2',
        #'idna==2.9',
        #'ipython==7.15.0',
        #'ipython-genutils==0.2.0',
        #'itsdangerous==1.1.0',
        #'jedi==0.17.1',
        #'jinja2==2.11.2',
        #'markupsafe==1.1.1',
        'matplotlib==3.2.2',
        #'networkx==2.4',
        #'numpy==1.19.0',
        #'parso==0.7.0',
        #'pexpect==4.8.0',
        #'pickleshare==0.7.5',
        #'prompt-toolkit==3.0.5',
        #'ptyprocess==0.6.0',
        #'pygments==2.6.1',
        #'requests==2.24.0',
        'scipy==1.5.0',
        'seaborn==0.10.1',
        #'six==1.15.0',
        #'tabulate==0.8.7',
        #'traitlets==4.3.3',
        #'urllib3==1.25.9',
        #'wcwidth==0.2.5',
        #'werkzeug==1.0.1',
        'zss @ https://github.com/melug/zhang-shasha/tarball/master#egg=zss',
    ],
    setup_requires=['pytest-runner',],
    scripts=[
        'scripts/aigrader.sh'
    ],
    tests_require=['pytest',],
    entry_points={
        'console_scripts': [
            'aigrader=aigrader.aigrader:cli',
        ]
    },
)
