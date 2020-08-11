import glob
import os, shutil

import click
import numpy as np
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram, linkage as scipy_linkage, fcluster
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns

from aigrader import assignment_helper as ah, human_in_the_loop as hloop


@click.group()
def cli():
    return

@cli.command(help='Compute edit distance between all files provided. Result saved in {output}/edit_distances.npy')
@click.argument('submissions', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output', show_default=True)
@click.option('--function-match', '-f', is_flag=True, help='Match functions directly instead of comparing full source code ASTs.')
@click.option('--scaffold', '-s', type=click.Path(), help='Provide a scaffold file to use for function name matching.')
@click.option('--ignore-assignments', '-i', is_flag=True, help='Ignore all assignment statements when parsing the ASTs (may speed up computation speed).')
def editdist(submissions, output, function_match, scaffold, ignore_assignments):
    if not function_match and scaffold:
        raise click.BadArgumentUsage('Must specify function match when using scaffold (using --function-match or -f).')

    click.echo('Computing edit distances.')

    output_path = os.path.join(output, 'filenames.npy')
    np.save(output_path, submissions)

    submissions = [ah.parse_file(submission, ignore_assignments=ignore_assignments) for submission in submissions]
    if scaffold is not None:
        scaffold = ah.find_functions(ah.parse_file(scaffold, ignore_assignments=True))
    edit_distances = ah.calculate_edit_distance(submissions, function_match, scaffold)
    click.echo(edit_distances)
    os.makedirs(output, exist_ok=True)
    output_path = os.path.join(output, 'edit_distances.npy')
    np.save(output_path, edit_distances)

    click.echo(f'Saved as \'{output_path}\'.')

@cli.command(help='Create linkage matrix for submissions based on edit distance file, saved in {output}/linkage.npy.')
@click.option('--method', default='ward', help='Clustering method to use.', show_default=True)
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
def linkage(method, path_to_editdist, output):
    click.echo('Cluster submissions based on comparison file.')
    comparison_table = np.load(path_to_editdist)
    dists = squareform(comparison_table)
    linkage_matrix = scipy_linkage(dists, method, optimal_ordering=True)
    os.makedirs(output, exist_ok=True)
    output_path = os.path.join(output, 'linkage.npy')
    np.save(output_path, linkage_matrix)
    click.echo(f'Saved as \'{output_path}\'.')

@cli.command()
@click.option('--path-to-filenames', help='Path to filenames.npy file.', type=click.Path(exists=True), default='output/filenames.npy')
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--function-match', '-f', is_flag=True, help='Not Implemented. Match functions directly instead of comparing full source code ASTs.')
@click.option('--scaffold', '-s', type=click.Path(), help='Not Implemented. Provide a scaffold file to use for function name matching.')
def abctest(path_to_filenames, path_to_editdist, function_match, scaffold):
    click.echo('Test computed edit distance.')
    cont = True
    edit_distances = np.load(path_to_editdist)
    click.echo(edit_distances)
    submissions = np.load(path_to_filenames)

    trials = 0
    correct = 0

    while cont:
        trials += 1
        a, b, c = sorted(np.random.choice(len(submissions), 3, replace=False))
        dist_ab = edit_distances[a][b]
        dist_ac = edit_distances[a][c]

        click.echo(' Submission A '.center(80, '#') + '\n', nl=False)
        with open(submissions[a]) as f:
            for line in f:
                click.echo(line, nl=False)
        click.echo('\n' + ' Submission B '.center(80, '#') + '\n', nl=False)
        with open(submissions[b]) as f:
            for line in f:
                click.echo(line, nl=False)
        click.echo('\n' + ' Submission C '.center(80, '#') + '\n', nl=False)
        with open(submissions[c]) as f:
            for line in f:
                click.echo(line, nl=False)
        click.echo('#' * 80)

        reply = click.confirm('A is closer to B than it is to C', default=True)
        edit_dist_answer = dist_ab < dist_ac
        if reply == edit_dist_answer:
            correct += 1
        cont = click.confirm('Continue?', default=True)
    click.echo(f'Agreement = {100.0 * correct / trials:.2f}%')

def _symlink_rel(src, dst):
    rel_path_src = os.path.relpath(src, os.path.dirname(dst))
    os.symlink(rel_path_src, dst)

def save_clustering_as_directory_structure(submissions, clustering, output_path):
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)
    num_clusters = len(clustering)
    if num_clusters > 1:
        zero_padding = int(np.log10(num_clusters - 1)) + 1
    else:
        zero_padding = 0
    for index, file_ids in enumerate(clustering):
        cluster_dir_path = os.path.join(output_path, f'{index}'.zfill(zero_padding))
        os.mkdir(cluster_dir_path)
        for file_id in file_ids:
            submission_name = submissions[file_id]
            _symlink_rel(submission_name, os.path.join(cluster_dir_path, str(file_id)))

@cli.command(help='Create cluster groups from linkage using a human-in-the-loop method.')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output', show_default=True)
@click.option('--path-to-filenames', help='Path to filenames.npy file.', type=click.Path(exists=True), default='output/filenames.npy')
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
def mclust(output, path_to_filenames, path_to_editdist, path_to_linkage):
    comparison_table = np.load(path_to_editdist)
    linkage_matrix = np.load(path_to_linkage)
    submissions = np.load(path_to_filenames)
    tree = hloop.create_tree(linkage_matrix, len(submissions))
    clustering = hloop.split_tree(submissions, comparison_table, tree)
    output_path = os.path.join(output, 'clusters')
    save_clustering_as_directory_structure(submissions, clustering, output_path)
    click.echo(f'Clusters have been saved in {output_path}')

def fcluster_to_clustering(fcluster):
    clusters_dict = dict()
    for i in range(len(fcluster)):
        if fcluster[i] not in clusters_dict:
            clusters_dict[fcluster[i]] = set()
        clusters_dict[fcluster[i]].add(i)
    clusters = []
    for _, value in clusters_dict.items():
        clusters.append(list(value))
    return clusters

@cli.command(help='Create cluster groups from linkage using either a max distance or a max number of clusters.')
@click.option('--max-distance', '-d', help='Set a maximum distance between two clusters.', type=float)
@click.option('--num-clusters', '-n', help='Set the number of preferred clusters (overrides --max-distances).', type=int)
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output', show_default=True)
@click.option('--path-to-filenames', help='Path to filenames.npy file.', type=click.Path(exists=True), default='output/filenames.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
def cluster(max_distance, num_clusters, output, path_to_filenames, path_to_linkage):
    linkage_matrix = np.load(path_to_linkage)
    if num_clusters is not None:
        clustering = fcluster(linkage_matrix, num_clusters, 'maxclust')
    elif max_distance is not None:
        clustering = fcluster(linkage_matrix, max_distance, 'distance')
    else:
        click.echo('Must provide either a max distance or a set number of clusters (using -d or -n flags).')
        return
    clustering = fcluster_to_clustering(clustering)
    print(f'Clusters: {clustering}')
    output_path = os.path.join(output, 'clusters')
    submissions = np.load(path_to_filenames)
    save_clustering_as_directory_structure(submissions, clustering, output_path)
    click.echo(f'Clusters have been saved in {output_path}')

@cli.command(help='Draw a dendrogram for the linkage produced by the clustering,\nsaved in {output}/dendrogram.png')
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
@click.option('--path-to-linkage', help='Path to linkage.npy file.', type=click.Path(exists=True), default='output/linkage.npy')
@click.option('--output', help='Directory to save the result in.', type=click.Path(), default='output')
@click.option('--clustermap', '-c', help='Generate the dendrogram together with a clustermap (see seaborn.clustermap for documentation).', is_flag=True, default=False)
def dendrogram(path_to_editdist, path_to_linkage, output, clustermap):
    click.echo(f'Draw a dendrogram for the linkage produced by the clustering.')
    linkage_matrix = np.load(path_to_linkage)
    comparison_table = np.load(path_to_editdist)
    plt.figure()
    if not clustermap:
        scipy_dendrogram(linkage_matrix)
    else:
        sns.clustermap(comparison_table,
                       row_linkage=linkage_matrix,
                       col_linkage=linkage_matrix)
    output_path = os.path.join(output, 'dendrogram.png')
    plt.savefig(output_path)
    click.echo(f'Saved as \'{output_path}\'.')

def get_cluster_members(cluster_number, path_to_clusters):
    cluster_members = np.array([], dtype=int)
    for f in os.listdir(os.path.join(path_to_clusters, str(cluster_number))):
        cluster_members = np.append(cluster_members, int(f))
    return cluster_members

def find_representative(comparison_table, cluster_members):
    submission_comparison = comparison_table[cluster_members][:,cluster_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_min = distances.argmin()
    return cluster_members[ix_with_min]

def find_outlier(comparison_table, cluster_members):
    submission_comparison = comparison_table[cluster_members][:,cluster_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_max = distances.argmax()
    return cluster_members[ix_with_max]

def find_neighbor(comparison_table, cluster_members, cluster_non_members):
    if len(cluster_non_members) == 0:
        return None
    submission_comparison = comparison_table[cluster_members][:,cluster_non_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_min = distances.argmin()
    return cluster_non_members[ix_with_min]

@cli.command(help='Print some statistics and information about a certain cluster')
@click.argument('cluster-number', default=0)
@click.option('--path-to-clusters', help='Path to cluster directory', type=click.Path(exists=True), default='output/clusters')
@click.option('--path-to-filenames', help='Path to filenames.npy file.', type=click.Path(exists=True), default='output/filenames.npy')
@click.option('--path-to-editdist', help='Path to edit_distances.npy file.', type=click.Path(exists=True), default='output/edit_distances.npy')
def stats(cluster_number, path_to_clusters, path_to_filenames, path_to_editdist):
    cluster_number = int(cluster_number)
    comparison_table = np.load(path_to_editdist)
    filenames = np.load(path_to_filenames)
    cluster_members = get_cluster_members(cluster_number, path_to_clusters)
    if len(cluster_members) <= 2:
        raise click.ClickException('Cluster size must be >=3.')
    all_members = np.arange(len(filenames))
    cluster_non_members = np.setdiff1d(all_members, cluster_members)
    cluster_median = find_representative(comparison_table, cluster_members)
    cluster_outlier = find_outlier(comparison_table, cluster_members)
    cluster_neighbor = find_neighbor(comparison_table, cluster_members, cluster_non_members)
    click.echo(' Cluster representative: '.center(80, '#') + '\n')
    hloop.print_submission(filenames[cluster_median])
    click.echo()
    click.echo(' Cluster outlier: '.center(80, '#') + '\n')
    hloop.print_submission(filenames[cluster_outlier])
    click.echo()
    if cluster_neighbor is not None:
        click.echo(' Cluster neighbor: '.center(80, '#') + '\n')
        hloop.print_submission(filenames[cluster_neighbor])
        click.echo()
    click.echo('#' * 80)

if __name__ == '__main__':
    cli()
