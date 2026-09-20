# Performance Metrics


# --------------------------------------------------
# Function 1: Calculate Confusion Matrix
# --------------------------------------------------

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


# --------------------------------------------------
# Function 2: Calculate Accuracy
# --------------------------------------------------

def calculate_accuracy(TP, TN, FP, FN):

    accuracy = (
        (TP + TN) /
        (TP + TN + FP + FN)
    )

    return accuracy


# --------------------------------------------------
# Function 3: Display Performance Metrics Source Code
# --------------------------------------------------

def show_performance_metrics_code():

    import sys
    from .code_viewer import show_code9

    module = sys.modules[__name__]

    show_code9(module)