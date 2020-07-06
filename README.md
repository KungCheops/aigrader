# aigrader

## Installation

1) Download the repository

2) cd into the repository

3a) (optional) create a virtual environment

3) Run 'pip install .' or 'pip install --user .'

You should now have an installed the program 'aigrader'.

## Testing the installation

First, cd into 'examples/assignment-xx', where xx can be the number of any assignment in the folder.

Now try out the first command, 'aigrader editdist assignment\*', 'assignment\*' is a wildcard that will match all submissions in that folder. There should now be a file called 'comparison.py' in a folder called 'output'. This means that the edit distances have successfully been computed.

When the edit distances have been computed we can try out the next command, 'aigrader cluster'. This command will take the newly computed edit distances and create a hierachical clustering based on them (represented as a linkage matrix). The result of this computation is stored in 'output/linkage.py'.

Lastly we can produce a dendrogram for the linkage matrix using the command 'aigrader dendrogram'. There should now be a file called 'Dendrogram.py' in the output folder.

These are the most fundamental operations that aigrader can perform, you can now feel free to play around with the other options.
