import math
import matplotlib.pyplot as plt
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )
def get_neighbors(points, point, eps):
    neighbors = []
    for p in points:
        if p != point:
            if distance(
                points[point],
                points[p]
            ) <= eps:
                neighbors.append(p)
    return neighbors
def dbscan(points, eps, minPts):
    visited = set()
    clusters = []
    noise = []
    for point in points:
        if point in visited:
            continue
        visited.add(point)
        neighbors = get_neighbors(
            points,
            point,
            eps
        )
        # Include the point itself
        # when checking MinPts
        if len(neighbors) + 1 < minPts:
            noise.append(point)
            continue
        # Start a new cluster
        cluster = [point]
        # Expand cluster
        i = 0
        while i < len(neighbors):
            current = neighbors[i]
            if current not in visited:
                visited.add(current)
                current_neighbors = get_neighbors(
                    points,
                    current,
                    eps
                )
                if len(current_neighbors) + 1 >= minPts:
                    for n in current_neighbors:
                        if n not in neighbors:
                            neighbors.append(n)
            # Add point to cluster
            if current not in cluster:
                cluster.append(current)
            i += 1
        clusters.append(cluster)
    return clusters, noise
def plot_dbscan(points, clusters, noise):
    # Plot clusters
    for i, cluster in enumerate(clusters):
        x = [
            points[p][0]
            for p in cluster
        ]

        y = [
            points[p][1]
            for p in cluster
        ]
        plt.scatter(
            x,
            y,
            label="Cluster " + str(i + 1)
        )
    # Plot noise / outliers
    if len(noise) > 0:
        x = [
            points[p][0]
            for p in noise
        ]
        y = [
            points[p][1]
            for p in noise
        ]
        plt.scatter(
            x,
            y,
            label="Noise / Outlier"
        )
    # Display point names
    for p, (x, y) in points.items():

        plt.text(
            x + 0.3,
            y + 0.3,
            p
        )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DBSCAN Clustering")
    plt.legend()
    plt.grid(True)
    plt.show()
def display_clusters(clusters, noise):
    print("Clusters:")
    for i in range(len(clusters)):
        print(
            "Cluster",
            i + 1,
            ":",
            clusters[i]
        )
    print(
        "Noise / Outliers:",
        noise
    )
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# data = pd.read_csv("points.csv")
# points = {}
# for index, row in data.iterrows():
#     points[row["ID"]] = (
#         row["X"],
#         row["Y"]
#     )
# eps = 2
# minPts = 2
# clusters, noise = dbscan(
#     points,
#     eps,
#     minPts
# )
# display_clusters(
#     clusters,
#     noise
# )
# plot_dbscan(
#     points,
#     clusters,
#     noise
# )
def show_dbscan():

    import sys
    from .code_viewer import show_code7

    module = sys.modules[__name__]

    show_code7(module)