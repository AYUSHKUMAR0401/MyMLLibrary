import numpy as np
import matplotlib.pyplot as plt
def distance(point, centroid):
    return np.sqrt(
        np.sum((point - centroid) ** 2)
    )
def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = []
        for centroid in centroids:
            distances.append(
                distance(point, centroid)
            )
        # Get index of minimum distance
        cluster = np.argmin(distances)
        clusters.append(cluster)
    return np.array(clusters, dtype=int)
def calculate_centroids(data, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_points = data[clusters == i]
        centroid = np.mean(
            cluster_points,
            axis=0
        )
        new_centroids.append(centroid)
    return np.array(new_centroids)
def kmeans(data, k):
    # Initial centroids = first k points
    centroids = data[:k].copy()
    while True:
        # Assign clusters
        clusters = assign_clusters(
            data,
            centroids
        )
        # Calculate new centroids
        new_centroids = calculate_centroids(
            data,
            clusters,
            k
        )
        # Check convergence
        if np.allclose(
            centroids,
            new_centroids
        ):
            break
        centroids = new_centroids
    return clusters, centroids
def display_clusters(
    names,
    data,
    clusters,
    centroids
):
    print("\n----- FINAL CLUSTERS -----")
    for i in range(len(centroids)):
        print("\nCluster", i + 1)
        for j in range(len(data)):
            if clusters[j] == i:
                print(
                    names[j],
                    "->",
                    data[j]
                )
        print(
            "Centroid =",
            centroids[i]
        )
def plot_graph(
    data,
    clusters,
    centroids,
    names
):
    for i in range(len(centroids)):
        points = data[clusters == i]
        plt.scatter(
            points[:, 0],
            points[:, 1],
            label="Cluster " + str(i + 1)
        )
    # Display point names
    for i in range(len(data)):
        plt.annotate(
            names[i],
            (data[i][0], data[i][1])
        )
    # Display centroids
    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="X",
        s=200,
        label="Centroids"
    )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("K-Means Clustering")
    plt.legend()
    plt.grid(True)
    plt.show()
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# import numpy as np
# data = pd.read_csv("points.csv")
# names = data["ID"].values
# X = data[["X", "Y"]].values
# X = np.array(X, dtype=float)
# k = 3
# clusters, centroids = kmeans(X, k)
# display_clusters(
#     names,
#     X,
#     clusters,
#     centroids
# )
# plot_graph(
#     X,
#     clusters,
#     centroids,
#     names
# )
def show_kmeans():
    import sys
    from .code_viewer import show_code6
    module = sys.modules[__name__]
    show_code6(module)   