import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.cluster import KMeans
import os


def dbscan(input_file):
    columns = ['lon', 'lat']
    in_df = pd.read_csv(input_file, sep=',', header=None, names=columns)
    # print(in_df.head(10))

    # represent GPS points as (lon, lat)
    coords = in_df.as_matrix(columns=['lon', 'lat'])
    coords = coords.astype(np.float)
    # earth's radius in km
    kms_per_radian = 6371.0086
    # define epsilon as 0.5 kilometers, converted to radians for use by haversine
    # This uses the 'haversine' formula to calculate the great-circle distance between two points
    # that is, the shortest distance over the earth's surface
    # http://www.movable-type.co.uk/scripts/latlong.html
    epsilon = 0.5 / kms_per_radian

    # radians() Convert angles from degrees to radians
    db = DBSCAN(eps=epsilon, min_samples=15, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_

    # get the number of clusters (ignore noisy samples which are given the label -1)
    num_clusters = len(set(cluster_labels) - set([-1]))

    print('Clustered ' + str(len(in_df)) + ' points to ' + str(num_clusters) + ' clusters')

    # turn the clusters in to a pandas series
    # clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    # print(clusters)
    kmeans = KMeans(n_clusters=1, n_init=1, max_iter=20, random_state=20)

    for n in range(num_clusters):
        # print('Cluster ', n, ' all samples:')
        one_cluster = coords[cluster_labels == n]
        # print(one_cluster[:1])
        # clist = one_cluster.tolist()
        # print(clist[0])
        kk = kmeans.fit(one_cluster)
        print(kk.cluster_centers_)


def main():
    path = './coordinate.csv'
    filelist = os.listdir(path)
    for f in filelist:
        datafile = os.path.join(path, f)
        print(datafile)
        dbscan(datafile)


if __name__ == '__main__':
    dbscan('coordinate.csv')
