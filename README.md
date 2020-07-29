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

## Testing the installation

This assumes you have a folder called `assignments`, containing files with the prefix `assignment-`.

First, cd into the `assignments` directory.

Then run `aigrader editdist assignment-*`; this will compute the distance between all of the assignments within the directory, which is saved as `edit_distances.npy` within the folder `output`.

> If computations are very slow you can try out the `-i` flag which ignores parts of the code.

> If you have a scaffold file that you want to provide you can use `-f` to tell it to match functions and `-s` together with the path to the scaffold file, to tell it to use that scaffold file.

When the distances have been computed the next step is to produce a linkage matrix.
This is done with `aigrader linkage`. The linkage matrix is then saved in the output folder as `linkage.npy`.

Lastly, you can run `aigrader cluster assignment-*` with either the `-n` flag to provide the maximum number of clusters, or the `-d` flag to determine the maximum distance between the members within the clusters.
