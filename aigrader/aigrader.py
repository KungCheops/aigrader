import glob

import click
import os
from aigrader import assignment_helper, human_in_the_loop as hloop
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


@click.group()
def cli():
    # click.echo('Hello World!')
    return


@cli.command(help='Compute edit distance between all file provided.')
@click.argument('submissions', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output', show_default=True)
@click.option('--path-to-scaffold', help='Path to scaffold file. Ignored if \'--no-scaffold\' flag is set.', type=click.Path(), default='scaffold.py', show_default=True)
@click.option('--function-match/--no-function-match', ' /-f', default=True, help='Whether or not to match functions directly instead of full source code ASTs.', show_default=True)
@click.option('--scaffold/--no-scaffold', ' /-s', default=True, help='Whether or not to use a scaffold file.', show_default=True)
@click.option('--assignments/--ignore-assignments', ' /-a', default=True, help='Whether or not to consider assignment statements when parsing the ASTs (ignoring assignments can speed up computation speed).', show_default=True)
def editdist(submissions, path_to_scaffold, output, scaffold, function_match, assignments):
    if not function_match:
        assignment_helper.calculate_edit_distance_no_function_matching(submissions, output, not assignments)
    else:
        assignment_helper.calculate_edit_distance(submissions, scaffold_path, output)

@cli.command(help='Cluster submissions based on comparison file, saved in {output}/linkage.npy.')
@click.option('--method', default='ward', help='Clustering method to use.', show_default=True)
@click.option('--path-to-comparison', help='Path to comparsion.npy file.', type=click.Path(exists=True), default='output/comparison.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
def cluster(method, path_to_comparison, output):
    click.echo(f'Cluster submissions based on comparison file, saved in \'{output}/linkage.npy\'.')
    comparison_table = assignment_helper.get_comparison_table(None, path_to_comparison)
    dists = squareform(comparison_table)
    linkage_matrix = linkage(dists, method, optimal_ordering=True)
    np.save(os.path.join(output, 'linkage.npy'), linkage_matrix)

@cli.command()
def abctest():
    click.echo('Test computed edit distance.')

@cli.command(help='Create cluster groups from linkage using a human-in-the-loop method.')
@click.argument('submissions', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--path-to-comparison', help='Path to comparsion.npy file.', type=click.Path(exists=True), default='output/comparison.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
def mclust(submissions, path_to_comparison, path_to_linkage):
    comparison_table = np.load(path_to_comparison)
    linkage_matrix = np.load(path_to_linkage)
    tree = hloop.create_tree(linkage_matrix, len(submissions))
    clustering = hloop.split_tree(submissions, comparison_table, tree)
    print(clustering)

@cli.command(help='Draw a dendrogram for the linkage produced by the clustering,\nsaved in {output}/dendrogram.png')
@click.option('--path-to-comparison', help='Path to comparsion.npy file.', type=click.Path(exists=True), default='output/comparison.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
def dendrogram(path_to_comparison, path_to_linkage, output):
    click.echo(f'Draw a dendrogram for the linkage produced by the clustering, saved in {output}/dendrogram.png')
    linkage_matrix = np.load(path_to_linkage)
    comparison_table = np.load(path_to_comparison)
    plt.figure()
    scipy_dendrogram(linkage_matrix)
    # sns.clustermap(comparison_table,
    #                row_linkage=linkage_matrix,
    #                col_linkage=linkage_matrix)
    plt.savefig(os.path.join(output, 'dendrogram.png'))
