import math
# --------------------------------------------------
# Function 1: Gaussian Probability
# --------------------------------------------------
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
#--------------------------------------------------
# Function 2: Calculate Mean
# --------------------------------------------------
def calculate_mean(values):
    return sum(values) / len(values)
# --------------------------------------------------
# Function 3: Calculate Variance
# --------------------------------------------------
def calculate_variance(values):
    mean = calculate_mean(values)
    variance = sum(
        (x - mean) ** 2 for x in values
    ) / len(values)
    return variance
# --------------------------------------------------
# Function 4: Calculate Class Probability
# --------------------------------------------------
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
# --------------------------------------------------
# Function 5: Naive Bayes Classification
# --------------------------------------------------
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
# -------------------------------------------------
# Function 6: Display Naive Bayes Source Code
# --------------------------------------------------
def show_naive_bayes_code():
    import sys
    from .code_viewer import show_code5
    module = sys.modules[__name__]
    show_code5(module)