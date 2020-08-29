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
    return sorted([py_file for py_file in glob.glob(os.path.join(path, '*.py'))
            if basename(py_file) != SCAFFOLD_NAME])


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
    scaffold = ah.find_functions(ah.parse_file(scaffold_path, ignore_assignments=ignore_assignments))
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

def save_clustering_as_directory_structure(submissions, clustering, output_path, comparison_table):
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
        with open(os.path.join(cluster_dir_path, "table.csv"), "w") as f:
            f.write(''.join('{:>4}'.format(file_id) for file_id in [0]+file_ids)+'\n')
            for file_id, row in zip(file_ids, comparison_table[file_ids,:][:,file_ids]):
                f.write(''.join('{:>4}'.format(n) for n in [file_id]+list(row))+'\n')
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
    click.echo(f'Clusters: {clustering}')
    output_cluster_path = os.path.join(output_path, 'clusters-human-in-the-loop')
    save_clustering_as_directory_structure(submissions, clustering, output_cluster_path, comparison_table)
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
    comparison_table = np.load(os.path.join(output_path, EDITDISTANCE_NAME))
    submissions = get_submissions(path_to_submissions_directory)
    linkage_matrix = np.load(os.path.join(output_path, LINKAGE_NAME))
    if num_clusters is not None:
        if max_distance is not None:
            click.echo('Ignoring distance flag as max cluster flag is set.')
        clustering = fcluster(linkage_matrix, num_clusters, 'maxclust')
    elif max_distance is not None:
        clustering = fcluster(linkage_matrix, max_distance, 'distance')
    else:
        click.echo('Must provide either a max distance or a set number of clusters (using -d or -n flags).')
        return
    clustering = fcluster_to_clustering(clustering)
    print(f'Cluster sizes: {[len(cluster) for cluster in clustering]}')
    output_cluster_path = os.path.join(output_path, 'clusters')
    save_clustering_as_directory_structure(submissions, clustering, output_cluster_path, comparison_table)
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
        sns.set(font_scale=.5)
        sns.clustermap(edit_distances,
                       row_linkage=linkage_matrix,
                       col_linkage=linkage_matrix,
                       annot_kws={"size": 16})
    output_chart_path = os.path.join(output_path, 'dendrogram.png')
    plt.savefig(output_chart_path)
    click.echo(f'Saved as \'{output_chart_path}\'.')

def find_representative(comparison_table, cluster_members):
    submission_comparison = comparison_table[cluster_members][:,cluster_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_min = distances.argmin()
    average_dist = distances[ix_with_min] / (len(cluster_members) - 1)
    return cluster_members[ix_with_min], average_dist

def find_outlier(comparison_table, cluster_members):
    submission_comparison = comparison_table[cluster_members][:,cluster_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_max = distances.argmax()
    average_dist = distances[ix_with_max] / (len(cluster_members) - 1)
    return cluster_members[ix_with_max], average_dist

def find_neighbor(comparison_table, cluster_members, cluster_non_members):
    if len(cluster_non_members) == 0:
        return None
    submission_comparison = comparison_table[cluster_members][:,cluster_non_members]
    distances = submission_comparison.sum(axis=0)
    ix_with_min = distances.argmin()
    average_dist = distances[ix_with_min] / len(cluster_members)
    return cluster_non_members[ix_with_min], average_dist

def compute_all_average_distances(comparison_table, clusters):
    distances = {}
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            distances[i, j] = compute_average_distance(comparison_table, clusters[i], clusters[j])
    return distances


def compute_average_distance(comparison_table, cluster_members_1, cluster_members_2):
    submission_comparison = comparison_table[cluster_members_1][:,cluster_members_2]
    distances = np.sum(submission_comparison)
    average_dist = distances / (len(submission_comparison) * len(submission_comparison[0]))
    return average_dist

@cli.command(help='Print some statistics and information about a certain cluster')
@click.argument('path_to_submissions_directory', nargs=1, default='.', type=click.Path(exists=True))
@click.option('--cluster-number', '-c', type=int, default=0)
def stats(path_to_submissions_directory, cluster_number):
    output_path = os.path.join(path_to_submissions_directory, 'output')
    submissions = get_submissions(path_to_submissions_directory)
    click.echo('opening: ' + os.path.join(output_path, EDITDISTANCE_NAME))
    comparison_table = np.load(os.path.join(output_path, EDITDISTANCE_NAME))
    path_to_clusters = os.path.join(output_path, 'clusters')

    clusters = {}
    for root, folders, files in os.walk(path_to_clusters):
        try:
            root_int = int(root.split('/')[-1])
        except:
            continue
        clusters[root_int] = sorted([int(f) for f in files])
    click.echo(clusters)
    click.echo(compute_all_average_distances(comparison_table, clusters))

    if len(clusters[cluster_number]) <= 2:
        raise click.ClickException('Cluster size must be >=3.')
    all_members = np.arange(len(submissions))
    cluster_non_members = np.setdiff1d(all_members, clusters[cluster_number])
    cluster_median, cluster_median_avg_dist = find_representative(comparison_table, clusters[cluster_number])
    cluster_outlier, cluster_outlier_avg_dist = find_outlier(comparison_table, clusters[cluster_number])
    cluster_neighbor, cluster_neighbor_avg_dist = find_neighbor(comparison_table, clusters[cluster_number], cluster_non_members)
    click.echo(' Cluster representative: '.center(80, '#') + '\n')
    click.echo('File name: {}\nAverage distance: {}\n'.format(basename(submissions[cluster_median]), cluster_median_avg_dist))
    hloop.print_submission(submissions[cluster_median])
    click.echo()
    click.echo(' Most distant cluster member: '.center(80, '#') + '\n')
    click.echo('File name: {}\nAverage distance: {}\n'.format(basename(submissions[cluster_outlier]), cluster_outlier_avg_dist))
    hloop.print_submission(submissions[cluster_outlier])
    click.echo()
    if cluster_neighbor is not None:
        click.echo(' Non cluster member closest to the cluster: '.center(80, '#') + '\n')
        click.echo('File name: {}\nAverage distance: {}\n'.format(basename(submissions[cluster_neighbor]), cluster_neighbor_avg_dist))
        hloop.print_submission(submissions[cluster_neighbor])
        click.echo()
    click.echo('#' * 80)

if __name__ == '__main__':
    cli()
