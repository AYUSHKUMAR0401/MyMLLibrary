# MyMLLibrary
# Machine Learning Algorithms


# --------------------------------------------------
# PLA
# --------------------------------------------------

from .Pla import (
    activation as pla_activation,
    train_perceptron,
    predict as pla_predict,
    show_perceptron_code
)


# --------------------------------------------------
# Linear Regression
# --------------------------------------------------

from .Linear_regression import (
    linear_regression,
    error_metrics,
    plot_regression,
    show_linear_regression_code
)


# --------------------------------------------------
# Logistic Regression
# --------------------------------------------------

from .Logistic_regression import (
    sigmoid,
    hypothesis,
    cost_function,
    gradient_descent,
    logistic_regression,
    show_logistic_regression_code
)


# --------------------------------------------------
# KNN
# --------------------------------------------------

from .Knn import (
    calculate_distance as knn_distance,
    calculate_distances,
    knn_classification,
    show_knn_code
)


# --------------------------------------------------
# Naive Bayes
# --------------------------------------------------

from .Naive_bayes import (
    gaussian_probability,
    calculate_mean,
    calculate_variance,
    calculate_probability,
    naive_bayes,
    show_naive_bayes_code
)


# --------------------------------------------------
# K-Means Clustering
# --------------------------------------------------

from .K_mean_clustering import (
    distance as kmeans_distance,
    assign_clusters,
    calculate_centroids,
    kmeans,
    display_clusters as display_kmeans_clusters,
    plot_graph,
    show_kmeans_code
)


# --------------------------------------------------
# DBSCAN Clustering
# --------------------------------------------------

from .Dbscan_clustering import (
    distance as dbscan_distance,
    get_neighbors,
    dbscan,
    plot_dbscan,
    display_clusters as display_dbscan_clusters,
    show_dbscan_code
)


# --------------------------------------------------
# SLP
# --------------------------------------------------

from .Slp import (
    step as slp_step,
    train_slp,
    predict as slp_predict,
    show_slp_code
)


# --------------------------------------------------
# Performance Metrics
# --------------------------------------------------

from .Performance_matrix import (
    confusion_matrix,
    calculate_accuracy,
    show_performance_metrics_code
)


# --------------------------------------------------
# Multilayer Perceptron
# --------------------------------------------------

from .Multilayer_perceptron import (
    normalize_data,
    one_hot_encode,
    relu,
    relu_derivative,
    softmax,
    initialize_parameters,
    forward,
    loss_function,
    backpropagation,
    train_mlp,
    predict as mlp_predict,
    calculate_accuracy as mlp_calculate_accuracy,
    show_mlp_code
)