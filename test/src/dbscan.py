import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans


def dbscan(input_file):
    columns = ['lon', 'lat']
    in_df = pd.read_csv(input_file, sep=',', header=None, names=columns)
    coords = in_df.as_matrix(columns=['lon', 'lat'])
    kms_per_radian = 6371.0086
    epsilon = 0.5 / kms_per_radian
    db = DBSCAN(eps=epsilon, min_samples=50, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels) - set([-1]))
    print('Clustered ' + str(len(in_df)) + ' points to ' + str(num_clusters) + ' clusters')
    kmeans = KMeans(n_clusters=1, n_init=1, max_iter=20, random_state=20)

    for n in range(num_clusters):
        one_cluster = coords[cluster_labels == n]
        kk = kmeans.fit(one_cluster)
        print(kk.cluster_centers_)


if __name__ == '__main__':
    dbscan('coordinate.csv')
