import math
from collections import Counter
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )
    return distance
def calculate_distances(data, test_x, test_y):
    distances = []
    for index, row in data.iterrows():
        distance = calculate_distance(
            test_x,
            test_y,
            row["X"],
            row["Y"]
        )
        distances.append(
            (row["ID"], distance, row["Label"])
        )
    return distances
def knn_classification(data, test_x, test_y, k):
    distances = calculate_distances(
        data,
        test_x,
        test_y
    )
    # Sort according to distance
    distances.sort(key=lambda x: x[1])
    # Select k nearest neighbours
    nearest = distances[:k]
    # Get labels
    labels = [item[2] for item in nearest]
    count = Counter(labels)
    prediction = count.most_common(1)[0][0]
    return prediction
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# data = pd.read_csv("knn_dataset.csv")
# test_x = 5
# test_y = 6
# k = 3
# prediction = knn_classification(
#     data,
#     test_x,
#     test_y,
#     k
# )
# print("Predicted Class:", prediction)
def show_knn():
    import sys
    from .code_viewer import show_code4
    module = sys.modules[__name__]
    show_code4(module)