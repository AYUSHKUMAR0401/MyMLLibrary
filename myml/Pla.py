# Perceptron Learning Algorithm

def activation(z):
    if z >= 0:
        return 1
    else:
        return 0


def train_perceptron(X, y, learning_rate=1, epochs=10):

    n_features = len(X[0])

    # Initialize weights
    weights = [0] * n_features

    # Initialize bias
    bias = 0

    for epoch in range(epochs):

        for i in range(len(X)):

            # Calculate weighted sum
            z = bias

            for j in range(n_features):
                z += weights[j] * X[i][j]

            # Prediction
            y_pred = activation(z)

            # Error
            error = y[i] - y_pred

            # Update weights
            for j in range(n_features):
                weights[j] += learning_rate * error * X[i][j]

            # Update bias
            bias += learning_rate * error

    return weights, bias


def predict(X, weights, bias):

    predictions = []

    for sample in X:

        z = bias

        for j in range(len(weights)):
            z += weights[j] * sample[j]

        predictions.append(activation(z))

    return predictions


def show_perceptron_code():

    import sys
    from .code_viewer import show_code1

    module = sys.modules[__name__]

    show_code1(module)