# Multilayer Perceptron (MLP) from Scratch

import numpy as np
def normalize_data(X):
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    X = (X - X_min) / (X_max - X_min)
    return X
def one_hot_encode(y, number_of_classes):
    Y = np.zeros(
        (len(y), number_of_classes)
    )
    for i in range(len(y)):
        Y[i][y[i]] = 1
    return Y
def relu(x):
    return np.maximum(0, x)
def relu_derivative(x):
    return (x > 0).astype(float)
def softmax(x):

    # Prevent overflow
    x = x - np.max(
        x,
        axis=1,
        keepdims=True
    )
    exp_x = np.exp(x)
    return exp_x / np.sum(
        exp_x,
        axis=1,
        keepdims=True
    )
def initialize_parameters(
    input_size,
    hidden_size,
    output_size
):
    W1 = (
        np.random.randn(
            input_size,
            hidden_size
        ) * 0.01
    )
    W2 = (
        np.random.randn(
            hidden_size,
            output_size
        ) * 0.01
    )
    b1 = np.zeros(
        (1, hidden_size)
    )
    b2 = np.zeros(
        (1, output_size)
    )
    return W1, W2, b1, b2
def forward(
    X,
    W1,
    W2,
    b1,
    b2
):
    # Hidden layer
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    # Output layer
    Z2 = np.dot(A1, W2) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2
def loss_function(Y, Y_pred):
    epsilon = 1e-8
    loss = -np.mean(
        np.sum(
            Y * np.log(Y_pred + epsilon),
            axis=1
        )
    )
    return loss
def backpropagation(
    X,
    Y,
    Z1,
    A1,
    A2,
    W2
):
    m = len(X)
    # Output layer error
    dZ2 = A2 - Y
    # Gradient of W2
    dW2 = np.dot(
        A1.T,
        dZ2
    ) / m
    # Gradient of b2
    db2 = np.sum(
        dZ2,
        axis=0,
        keepdims=True
    ) / m
    # Hidden layer error
    dA1 = np.dot(
        dZ2,
        W2.T
    )
    dZ1 = (
        dA1 *
        relu_derivative(Z1)
    )
    # Gradient of W1
    dW1 = np.dot(
        X.T,
        dZ1
    ) / m
    # Gradient of b1
    db1 = np.sum(
        dZ1,
        axis=0,
        keepdims=True
    ) / m
    return dW1, dW2, db1, db2
def train_mlp(
    X,
    Y,
    input_size,
    hidden_size,
    output_size,
    learning_rate=0.1,
    epochs=1000
):
    W1, W2, b1, b2 = initialize_parameters(
        input_size,
        hidden_size,
        output_size
    )
    loss_history = []
    for epoch in range(epochs):
        # Forward propagation
        Z1, A1, Z2, A2 = forward(
            X,
            W1,
            W2,
            b1,
            b2
        )
        # Calculate loss
        loss = loss_function(
            Y,
            A2
        )
        # Backpropagation
        dW1, dW2, db1, db2 = backpropagation(
            X,
            Y,
            Z1,
            A1,
            A2,
            W2
        )
        # Update weights
        W2 = W2 - learning_rate * dW2
        W1 = W1 - learning_rate * dW1
        # Update biases
        b2 = b2 - learning_rate * db2
        b1 = b1 - learning_rate * db1
        loss_history.append(loss)
    return W1, W2, b1, b2, loss_history
def predict(
    X,
    W1,
    W2,
    b1,
    b2
):
    _, _, _, Y_pred = forward(
        X,
        W1,
        W2,
        b1,
        b2
    )
    predicted_class = np.argmax(
        Y_pred,
        axis=1
    )
    return predicted_class
def calculate_accuracy(
    actual_class,
    predicted_class
):
    correct = 0
    for i in range(
        len(actual_class)
    ):
        if (
            predicted_class[i]
            == actual_class[i]
        ):
            correct += 1
    accuracy = (
        correct /
        len(actual_class)
    ) * 100
    return accuracy
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# import numpy as np
# data = pd.read_csv("iris.csv")
# X = data[
#     [
#         "sepal_length",
#         "sepal_width",
#         "petal_length",
#         "petal_width"
#     ]
# ].values
# y = data["target"].values
# X = np.array(X, dtype=float)
# y = np.array(y, dtype=int)
# X = normalize_data(X)
# number_of_classes = 3
# Y = one_hot_encode(
#     y,
#     number_of_classes
# )
# W1, W2, b1, b2, loss_history = train_mlp(
#     X,
#     Y,
#     input_size=4,
#     hidden_size=10,
#     output_size=3,
#     learning_rate=0.1,
#     epochs=1000
# )
# predictions = predict(
#     X,
#     W1,
#     W2,
#     b1,
#     b2
# )
# accuracy = calculate_accuracy(
#     y,
#     predictions
# )
# print("Accuracy:", accuracy, "%")
def show_mlp():
    import sys
    from .code_viewer import show_code10
    module = sys.modules[__name__]
    show_code10(module)