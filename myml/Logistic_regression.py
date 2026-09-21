import numpy as np
from .code_viewer import show_code3
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def hypothesis(X, w, b):
    z = w * X + b
    return sigmoid(z)
def cost_function(X, y, w, b):
    m = len(X)
    h = hypothesis(X, w, b)
    h = np.clip(h, 1e-10, 1 - 1e-10)
    cost = (-1 / m) * np.sum(
        y * np.log(h) + (1 - y) * np.log(1 - h)
    )
    return cost
def gradient_descent(X, y, w, b, learning_rate, iterations):
    m = len(X)
    for i in range(iterations):
        h = hypothesis(X, w, b)
        dw = (1 / m) * np.dot(X.T, (h - y))
        db = (1 / m) * np.sum(h - y)
        w -= learning_rate * dw
        b -= learning_rate * db
    return w, b
def logistic_regression(
    X,
    y,
    learning_rate=0.0001,
    iterations=100000
):
    w = 0.0
    b = 0.0
    w, b = gradient_descent(
        X,
        y,
        w,
        b,
        learning_rate,
        iterations
    )
    return w, b
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# import numpy as np
# data = pd.read_csv("marks.csv")
# X = data["Class_Test_Marks"].values
# y = data["Result"].values
# X = np.array(X, dtype=float)
# y = np.array(y, dtype=float)
# w, b = logistic_regression(
#     X,
#     y,
#     learning_rate=0.0001,
#     iterations=100000
# )
# print("Weight:", w)
# print("Bias:", b)
def show_logistic():
    import sys
    from .code_viewer import show_code2
    module = sys.modules[__name__]
    show_code3(module)