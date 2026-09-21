import math
def gaussian_probability(x, mean, variance):
    if variance == 0:
        return 1.0
    exponent = math.exp(
        -((x - mean) ** 2) / (2 * variance)
    )
    probability = (
        1 / math.sqrt(2 * math.pi * variance)
    ) * exponent
    return probability
def calculate_mean(values):
    return sum(values) / len(values)
def calculate_variance(values):
    mean = calculate_mean(values)
    variance = sum(
        (x - mean) ** 2 for x in values
    ) / len(values)
    return variance
def calculate_probability(data, test_data, class_name):
    class_data = data[
        data["Class"] == class_name
    ]
    # Prior probability
    prior = len(class_data) / len(data)
    probability = prior
    features = [
        "Word_Free",
        "Word_Win",
        "Length",
        "Links"
    ]
    for feature in features:
        values = class_data[feature].tolist()
        mean = calculate_mean(values)
        variance = calculate_variance(values)
        likelihood = gaussian_probability(
            test_data[feature],
            mean,
            variance
        )
        probability *= likelihood
    return probability
def naive_bayes(data, test_data):
    spam_probability = calculate_probability(
        data,
        test_data,
        "Spam"
    )
    not_spam_probability = calculate_probability(
        data,
        test_data,
        "Not_Spam"
    )
    if spam_probability > not_spam_probability:
        prediction = "Spam"
    else:
        prediction = "Not_Spam"
    return prediction
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# data = pd.read_csv("dataset.csv")
# X = data[["Feature1", "Feature2"]].values
# y = data["Label"].values
# result = naive_bayes(X, y)
# print(result)
def show_naive():
    import sys
    from .code_viewer import show_code5
    module = sys.modules[__name__]
    show_code5(module)