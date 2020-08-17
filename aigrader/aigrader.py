import glob
import os
import os.path
import shutil

import click
import numpy as np
import pickle
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram, linkage as scipy_linkage, fcluster
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns

from aigrader import assignment_helper as ah, human_in_the_loop as hloop


@click.group()
def cli():
    return


basename = os.path.basename
SCAFFOLD_NAME = 'scaffold.py'
EDITDISTANCE_NAME = 'edit_distances.npy'
LINKAGE_NAME = 'linkage.npy'


def get_output_directory(path_or_submissions):
    if isinstance(path_or_submissions, str):
        return os.path.join(path_or_submissions, 'output')
    return os.path.join(os.path.commonpath(path_or_submissions), 'output')


def get_submissions(path):
    return [py_file for py_file in glob.glob(os.path.join(path, '*.py'))
            if basename(py_file) != SCAFFOLD_NAME]


@cli.command(help=f'Compute edit distance between all files provided. Result saved in {{submissions}}/output/{EDITDISTANCE_NAME}')
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--function-match', '-f', is_flag=True, help='Match functions directly instead of comparing full source code ASTs.')
@click.option('--ignore-assignments', '-i', is_flag=True, help='Ignore all assignment statements when parsing the ASTs (may speed up computation speed).')
def editdist(path_to_submissions_directory, function_match, ignore_assignments):
    click.echo('Computing edit distances.')
    submissions = get_submissions(path_to_submissions_directory)
    output_directory = get_output_directory(submissions)
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, EDITDISTANCE_NAME)
    submission_asts = [ah.parse_file(submission, ignore_assignments=ignore_assignments) for submission in submissions]
    scaffold_path = os.path.join(path_to_submissions_directory, SCAFFOLD_NAME)
    scaffold = ah.find_functions(ah.parse_file(scaffold_path, ignore_assignments=True))
    edit_distances = ah.calculate_edit_distance(submission_asts,
                                                function_match,
                                                scaffold,
                                                submissions)
    click.echo(edit_distances)
    np.save(output_file, edit_distances)
    click.echo(f'Saved as \'{output_file}\'.')


@cli.command(help=f'Create linkage matrix for submissions based on edit distance file and save in {{submissions}}/output/{LINKAGE_NAME}')
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--method', default='ward', help='Clustering method to use.', show_default=True)
def linkage(path_to_submissions_directory, method):
    click.echo('Cluster submissions based on comparison file.')
    output_directory = get_output_directory(path_to_submissions_directory)
    edit_distance_file = os.path.join(output_directory, EDITDISTANCE_NAME)
    comparison_table = np.load(edit_distance_file)
    click.echo(comparison_table)
    dists = squareform(comparison_table)
    linkage_matrix = scipy_linkage(dists, method, optimal_ordering=True)
    output_file = os.path.join(output_directory, LINKAGE_NAME)
    np.save(output_file, linkage_matrix)
    click.echo(f'Saved as \'{output_file}\'.')

@cli.command()
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--function-match', '-f', is_flag=True, help='Not Implemented. Match functions directly instead of comparing full source code ASTs.')
@click.option('--scaffold', '-s', type=click.Path(), help='Not Implemented. Provide a scaffold file to use for function name matching.')
def abctest(path_to_submissions_directory, function_match, scaffold):
    click.echo('Test computed edit distance.')
    submissions = get_submissions(path_to_submissions_directory)
    cont = True
    edit_distance_file_path = os.path.join(get_output_directory(submissions), EDITDISTANCE_NAME)
    edit_distances = np.load(edit_distance_file_path)
    click.echo(edit_distances)

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
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
def mclust(path_to_submissions_directory):
    output_path = os.path.join(path_to_submissions_directory, 'output')
    submissions = get_submissions(path_to_submissions_directory)
    comparison_table = np.load(os.path.join(output_path, EDITDISTANCE_NAME))
    linkage_matrix = np.load(os.path.join(output_path, LINKAGE_NAME))
    tree = hloop.create_tree(linkage_matrix, len(submissions))
    clustering = hloop.split_tree(submissions, comparison_table, tree)
    output_cluster_path = os.path.join(output_path, 'clusters-human-in-the-loop')
    save_clustering_as_directory_structure(submissions, clustering, output_cluster_path)
    click.echo(f'Clusters have been saved in {output_cluster_path}')

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
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--max-distance', '-d', help='Set a maximum distance between two clusters.', type=float)
@click.option('--num-clusters', '-n', help='Set the number of preferred clusters (overrides --max-distances).', type=int)
def cluster(path_to_submissions_directory, max_distance, num_clusters):
    output_path = os.path.join(path_to_submissions_directory, 'output')
    submissions = get_submissions(path_to_submissions_directory)
    linkage_matrix = np.load(os.path.join(output_path, LINKAGE_NAME))
    if num_clusters is not None:
        clustering = fcluster(linkage_matrix, num_clusters, 'maxclust')
    elif max_distance is not None:
        clustering = fcluster(linkage_matrix, max_distance, 'distance')
    else:
        click.echo('Must provide either a max distance or a set number of clusters (using -d or -n flags).')
        return
    clustering = fcluster_to_clustering(clustering)
    print(f'Clusters: {clustering}')
    output_cluster_path = os.path.join(output_path, 'clusters')
    save_clustering_as_directory_structure(submissions, clustering, output_cluster_path)
    click.echo(f'Clusters have been saved in {output_cluster_path}')

@cli.command(help='Draw a dendrogram for the linkage produced by the clustering,\nsaved in {output}/dendrogram.png')
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--clustermap', '-c', help='Generate the dendrogram together with a clustermap (see seaborn.clustermap for documentation).', is_flag=True, default=False)
def dendrogram(path_to_submissions_directory, clustermap):
    click.echo(f'Draw a dendrogram for the linkage produced by the clustering.')
    output_path = os.path.join(path_to_submissions_directory, 'output')
    linkage_matrix = np.load(os.path.join(output_path, LINKAGE_NAME))
    edit_distances = np.load(os.path.join(output_path, EDITDISTANCE_NAME))
    plt.figure()
    if not clustermap:
        scipy_dendrogram(linkage_matrix)
    else:
        sns.clustermap(edit_distances,
                       row_linkage=linkage_matrix,
                       col_linkage=linkage_matrix)
    output_chart_path = os.path.join(output_path, 'dendrogram.png')
    plt.savefig(output_chart_path)
    click.echo(f'Saved as \'{output_chart_path}\'.')

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
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--cluster-number', '-c', type=int, default=0)
def stats(path_to_submissions_directory, cluster_number):
    cluster_number = cluster_number
    output_path = os.path.join(path_to_submissions_directory, 'output')
    submissions = get_submissions(path_to_submissions_directory)
    click.echo('opening: '+os.path.join(output_path, EDITDISTANCE_NAME))
    comparison_table = np.load(os.path.join(output_path, EDITDISTANCE_NAME))
    path_to_clusters = os.path.join(output_path, 'clusters')

    cluster_members = get_cluster_members(cluster_number, path_to_clusters)
    if len(cluster_members) <= 2:
        raise click.ClickException('Cluster size must be >=3.')
    all_members = np.arange(len(submissions))
    cluster_non_members = np.setdiff1d(all_members, cluster_members)
    cluster_median = find_representative(comparison_table, cluster_members)
    cluster_outlier = find_outlier(comparison_table, cluster_members)
    cluster_neighbor = find_neighbor(comparison_table, cluster_members, cluster_non_members)
    click.echo(' Cluster representative: '.center(80, '#') + '\n')
    hloop.print_submission(submissions[cluster_median])
    click.echo()
    click.echo(' Cluster outlier: '.center(80, '#') + '\n')
    hloop.print_submission(submissions[cluster_outlier])
    click.echo()
    if cluster_neighbor is not None:
        click.echo(' Cluster neighbor: '.center(80, '#') + '\n')
        hloop.print_submission(submissions[cluster_neighbor])
        click.echo()
    click.echo('#' * 80)

if __name__ == '__main__':
    cli()
