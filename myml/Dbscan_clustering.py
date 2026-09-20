import math
import matplotlib.pyplot as plt


# --------------------------------------------------
# Function 1: Calculate Euclidean Distance
# --------------------------------------------------

def distance(p1, p2):

    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )


# --------------------------------------------------
# Function 2: Find Neighbors of a Point
# --------------------------------------------------

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


# --------------------------------------------------
# Function 3: DBSCAN Algorithm
# --------------------------------------------------

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


# --------------------------------------------------
# Function 4: Plot DBSCAN Clusters
# --------------------------------------------------

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


# --------------------------------------------------
# Function 5: Display DBSCAN Results
# --------------------------------------------------

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
# Function 6: Display DBSCAN Source Code
# --------------------------------------------------

def show_dbscan_code():

    import sys
    from .code_viewer import show_code7

    module = sys.modules[__name__]

    show_code7(module)