from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.manifold import TSNE

# X = np.loadtxt(open("coordinate.csv", "rb"), delimiter=",", skiprows=0)

# kmeans = KMeans(n_clusters=500, random_state=0).fit(X)
#
# labels = kmeans.labels_
# labels = pd.DataFrame(labels, columns=['labels'])

X = pd.read_csv('coordinate.csv')
X.head()
kmeans_model = KMeans(n_clusters=500, init='k-means++', random_state=0)
y_kmeans = kmeans_model.fit_predict(X)
centers = kmeans_model.cluster_centers_
for i in range(500):
    plt.scatter(centers[i, 0], centers[i, 1], s=1, c='red')
# plt.show()
# plt.savefig("test.svg", format="svg")
# colors_list = ['red', 'blue', 'green', 'yellow', 'pink']
# X = X.values
#
# for j in range(500):
#     i = np.random.randint(0, 5)
#     plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors_list[i])
#
# plt.scatter(kmeans_model.cluster_centers_[:,0],kmeans_model.cluster_centers_[:,1], s=300,c='black',label='Centroids')
#
# plt.legend()
# plt.xlabel('Annual Income (k$)')
# plt.ylabel('Spending Score (1-100)')
plt.show()