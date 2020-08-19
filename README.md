# aigrader

## Installation

1) Installing `aigrader` as dependency:

```
pip install https://github.com/KungCheops/aigrader/tarball/master#egg=aigrader
```

## For development

```
# clone repository
git clone git@github.com:KungCheops/aigrader.git
cd aigrader

# create virtual environment
virtualenv venv
. venv/bin/activate

# install aigrader
pip install --editable .
```

You don't have to install it in a virtual environment but it is recommended.

The editable flag is also optional but it helps during development as it lets you edit the code without reinstalling the application.

## Testing the installation

This documentation assumes you have a folder called `assignments` which contains python files along with `scaffold.py`. The `scaffold.py` is a special file used for defining scaffolds. The scaffolds are used for speeding up distance computations between different files by matching their (scaffold) functions to each other.

Run the following command to run a full analysis of all submissions; generating edit distance, linkage and clustering:

```
> aigrader.sh assignments
```

The `aigrader.sh` is nothing more than sequence of commands of `aigrader`. The results such as edit distance and clustering informations are are saved in `aigrader/output/` directory.

For detailed information run:

```
> aigrader --help
```
