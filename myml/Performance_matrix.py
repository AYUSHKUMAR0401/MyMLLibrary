# Performance Metrics
def confusion_matrix(y_true, y_pred):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            TP += 1
        elif y_true[i] == 0 and y_pred[i] == 0:
            TN += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            FP += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            FN += 1
    return TP, TN, FP, FN
def calculate_accuracy(TP, TN, FP, FN):
    accuracy = (
        (TP + TN) /
        (TP + TN + FP + FN)
    )
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    specificity = TN / (TN + FP)
    f1 = (
        2 * (precision * recall) /
        (precision + recall)
    )
    return accuracy, precision , recall , specificity , f1
# --------------------------------------------------
# READ CSV DATASET
# --------------------------------------------------
# import pandas as pd
# data = pd.read_csv("predictions.csv")
# y_true = data["Actual"].values
# y_pred = data["Predicted"].values
# TP, TN, FP, FN = confusion_matrix(
#     y_true,
#     y_pred
# )
# accuracy = calculate_accuracy(
#     TP,
#     TN,
#     FP,
#     FN
# )
# print("TP:", TP)
# print("TN:", TN)
# print("FP:", FP)
# print("FN:", FN)
# print("Accuracy:", accuracy)
def show_performance():
    import sys
    from .code_viewer import show_code9
    module = sys.modules[__name__]
    show_code9(module)