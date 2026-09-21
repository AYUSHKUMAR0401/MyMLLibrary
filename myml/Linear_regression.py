import numpy as np
import matplotlib.pyplot as plt
def linear_regression(X, Y):
    x_mean = np.mean(X)
    y_mean = np.mean(Y)
    numerator = np.sum((X - x_mean) * (Y - y_mean))
    denominator = np.sum((X - x_mean) ** 2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    Y_pred = intercept + slope * X
    return intercept, slope, Y_pred
def error_metrics(Y, Y_pred):
    MSE = np.mean((Y - Y_pred) ** 2)
    RMSE = np.sqrt(MSE)
    MAE = np.mean(np.abs(Y - Y_pred))
    SS_res = np.sum((Y - Y_pred) ** 2)
    SS_tot = np.sum((Y - np.mean(Y)) ** 2)
    R2 = 1 - (SS_res / SS_tot)
    return MSE, RMSE, MAE, R2
def plot_regression(X, Y, Y_pred):
    plt.scatter(X, Y, label="Actual Data")
    plt.plot(X, Y_pred, label="Regression Line")
    plt.xlabel("Class_Test_Marks")
    plt.ylabel("Semester_Marks")
    plt.title("Linear Regression")
    plt.legend()
    plt.grid(True)
    plt.show()
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# data = pd.read_csv("marks.csv")
# X = data["Class_Test_Marks"].values
# Y = data["Semester_Marks"].values
# intercept, slope, Y_pred = linear_regression(X, Y)
# MSE, RMSE, MAE, R2 = error_metrics(Y, Y_pred)
# print("Intercept:", intercept)
# print("Slope:", slope)
# print("MSE:", MSE)
# print("RMSE:", RMSE)
# print("MAE:", MAE)
# print("R2:", R2)
# plot_regression(X, Y, Y_pred)
def show_linear():
    import sys
    from .code_viewer import show_code2
    module = sys.modules[__name__]
    show_code2(module)