import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Function 1: Calculate Euclidean Distance
# --------------------------------------------------

def distance(point, centroid):

    return np.sqrt(
        np.sum((point - centroid) ** 2)
    )


# --------------------------------------------------
# Function 2: Assign each point to nearest centroid
# --------------------------------------------------

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


# --------------------------------------------------
# Function 3: Calculate new centroids
# --------------------------------------------------

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


# --------------------------------------------------
# Function 4: K-Means Algorithm
# --------------------------------------------------

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


# --------------------------------------------------
# Function 5: Display Final Clusters
# --------------------------------------------------

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


# --------------------------------------------------
# Function 6: Plot Graph
# --------------------------------------------------

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
# Function 7: Display K-Means Source Code
# --------------------------------------------------

def show_kmeans_code():
    import sys
    from .code_viewer import show_code6
    module = sys.modules[__name__]
    show_code6(module)