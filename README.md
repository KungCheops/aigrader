# aigrader

## Installation

1) Installing `aigrader` as dependency:

```
pip install https://github.com/KungCheops/aigrader/tarball/master#egg=aigrader
```

## For development (Testing)

1) Download repository and run tests with tox which will be installed:

```
git clone git@github.com:KungCheops/aigrader.git
cd aigrader
make test
```

### Alternatively

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

The editable flag makes it so you can edit the code without reinstalling the application.

## Testing the installation

This documentation assumes you have a folder called `assignments` which contains python files along with `scaffold.py`. The `scaffold.py` is a special file used for defining scaffolds. The scaffolds are used for collecting functions and calculation of edit distances among functions.

Run following command to run full analysis of all submissions for generating edit distance, linkage and clustering:

```
> aigrader.sh assignments
```

The `aigrader.sh` is nothing more than sequence of subtle commands of `aigrader`. The results such as edit distance and clustering informations are are saved in `aigrader/output/` directory.

For detailed information run:

```
> aigrader --help
```
