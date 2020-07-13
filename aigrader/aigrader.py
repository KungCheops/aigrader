import glob

import click
import os
from aigrader import assignment_helper as ah
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


@click.group()
def cli():
    # click.echo('Hello World!')
    return


@cli.command(help='Compute edit distance between all files provided. Result saved in {output}/edit_distances.npy')
@click.argument('submissions', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output', show_default=True)
# @click.option('--path-to-scaffold', help='Path to scaffold file. Ignored if scaffold flag is not set.', type=click.Path(), default='scaffold.py', show_default=True)
@click.option('--function-match', '-f', is_flag=True, help='Match functions directly instead of comparing full source code ASTs.')
@click.option('--scaffold', '-s', type=click.Path(), help='Provide a scaffold file to use for function name matching.')
@click.option('--ignore-assignments', '-i', is_flag=True, help='Ignore all assignment statements when parsing the ASTs (may speed up computation speed).')
def editdist(submissions, output, function_match, scaffold, ignore_assignments):
    click.echo('Computing edit distances.')
    submissions = [ah.parse_file(submission, ignore_assignments=ignore_assignments) for submission in submissions]
    if scaffold is not None:
        scaffold = ah.find_functions(ah.parse_file(scaffold, ignore_assignments=True))
    edit_distances = ah.calculate_edit_distance(submissions, function_match, scaffold)
    click.echo(edit_distances)
    os.makedirs(output, exist_ok=True)
    output_path = os.path.join(output, 'edit_distances.npy')
    np.save(output_path, edit_distances)
    click.echo(f'Saved as \'{output_path}\'.')

@cli.command(help='Cluster submissions based on edit distance file, saved in {output}/linkage.npy.')
@click.option('--method', default='ward', help='Clustering method to use.', show_default=True)
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
def cluster(method, path_to_editdist, output):
    click.echo('Cluster submissions based on comparison file.')
    comparison_table = np.load(path_to_editdist)
    dists = squareform(comparison_table)
    linkage_matrix = linkage(dists, method, optimal_ordering=True)
    os.makedirs(output, exist_ok=True)
    output_path = os.path.join(output, 'linkage.npy')
    np.save(output_path, linkage_matrix)
    click.echo(f'Saved as \'{output_path}\'.')

@cli.command()
def abctest():
    click.echo('Test computed edit distance.')
    # TODO implement

@cli.command(help='Create cluster groups from linkage using a human-in-the-loop method.')
@click.argument('submissions', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
def mclust(submissions, path_to_editdist, path_to_linkage):
    comparison_table = np.load(path_to_editdist)
    linkage_matrix = np.load(path_to_linkage)
    tree = hloop.create_tree(linkage_matrix, len(submissions))
    clustering = hloop.split_tree(submissions, comparison_table, tree)
    print(clustering)

@cli.command(help='Draw a dendrogram for the linkage produced by the clustering,\nsaved in {output}/dendrogram.png')
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
def dendrogram(path_to_editdist, path_to_linkage, output):
    click.echo(f'Draw a dendrogram for the linkage produced by the clustering.')
    linkage_matrix = np.load(path_to_linkage)
    comparison_table = np.load(path_to_editdist)
    plt.figure()
    scipy_dendrogram(linkage_matrix)
    # sns.clustermap(comparison_table,
    #                row_linkage=linkage_matrix,
    #                col_linkage=linkage_matrix)
    output_path = os.path.join(output, 'dendrogram.png')
    plt.savefig(output_path)
    click.echo(f'Saved as \'{output_path}\'.')
