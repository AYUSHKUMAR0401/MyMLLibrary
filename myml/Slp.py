# Single Layer Perceptron (SLP)


# --------------------------------------------------
# Function 1: Step Activation Function
# --------------------------------------------------

def step(z):

    if z >= 0:
        return 1
    else:
        return 0


# --------------------------------------------------
# Function 2: Train SLP
# --------------------------------------------------

def train_slp(X, Y, learning_rate=1, epochs=10):

    # Number of input features
    n_features = len(X[0])

    # Initialize weights
    weights = [0] * n_features

    # Initialize bias
    bias = 0

    # Training
    for epoch in range(epochs):

        for i in range(len(X)):

            # Calculate weighted sum
            z = bias

            for j in range(n_features):

                z = z + (
                    weights[j] * X[i][j]
                )

            # Calculate output
            output = step(z)

            # Calculate error
            error = Y[i] - output

            # Update weights
            for j in range(n_features):

                weights[j] = weights[j] + (
                    learning_rate *
                    error *
                    X[i][j]
                )

            # Update bias
            bias = bias + (
                learning_rate * error
            )

    return weights, bias


# --------------------------------------------------
# Function 3: Predict Using SLP
# --------------------------------------------------

def predict(X, weights, bias):

    predictions = []

    for i in range(len(X)):

        z = bias

        for j in range(len(weights)):

            z = z + (
                weights[j] * X[i][j]
            )

        output = step(z)

        predictions.append(output)

    return predictions


# --------------------------------------------------
# Function 4: Display SLP Source Code
# --------------------------------------------------

def show_slp_code():

    import sys
    from .code_viewer import show_code8

    module = sys.modules[__name__]

    show_code8(module)