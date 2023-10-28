# imports
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from GPy.kern import Matern32

from polire import (
    Random,
    Trend,
    Spline,
    IDW,
    Kriging,
    SpatialAverage,
    NaturalNeighbor,
    GP,
)

# sample data
X = [[0, 0], [0, 3], [3, 0], [3, 3]]
y = [0, 1.5, 1.5, 3]
X = np.array(X)
y = np.array(y)
regressors = [
    Random(),
    SpatialAverage(),
    Spline(kx=1, ky=1),
    Trend(),
    IDW(coordinate_type="Geographic"),
    Kriging(),
    GP(Matern32(input_dim=2)),
]


def test_grid():
    # Gridded interpolation testing
    print("\nTesting on small dataset")
    for r in regressors:
        r.fit(X, y)
        y_pred = r.predict_grid()
        Z = y_pred
        sns.heatmap(Z)
        plt.title(r)
        plt.show()
        plt.close()
    print("\nTesting completed on a small dataset\n")

    print("\nTesting on a reasonable dataset")

    df = pd.read_csv("tests/data/30-03-18.csv")
    X1 = np.array(df[["longitude", "latitude"]])
    y1 = np.array(df["value"])

    for r in regressors:
        r.fit(X1, y1)
        y_pred = r.predict_grid()
        Z = y_pred
        sns.heatmap(Z)
        plt.title(r)
        plt.show()
        plt.close()


def test_point():
    # Pointwise interpolation testing
    for r in regressors:
        r.fit(X, y)
        test_data = [
            [0, 0],
            [0, 3],
            [3, 0],
            [3, 3],
            [1, 1],
            [1.5, 1.5],
            [2, 2],
            [2.5, 2.5],
            [4, 4],
        ]
        y_pred = r.predict(np.array(test_data))
        print(r)
        print(y_pred)


def test_nn():
    print("\nNatural Neighbors - Point Wise")
    nn = NaturalNeighbor()
    df = pd.read_csv("tests/data/30-03-18.csv")
    X = np.array(df[["longitude", "latitude"]])
    y = np.array(df["value"])
    nn.fit(X, y)
    test_data = [[77.16, 28.70], X[0]]
    y_pred = nn.predict(np.array(test_data))
    print(y_pred)
    del nn
    print("\nNatural Neighbors - Entire Grid")
    # Suggested by Apoorv as a temporary fix
    # Patience pays
    nn = NaturalNeighbor()
    nn.fit(X, y)
    y_pred = nn.predict_grid()
    print(y_pred)
    sns.heatmap(y_pred)
    plt.title(nn)
    plt.show()
    plt.close()


if __name__ == "__main__":
    print("Testing Gridded Interpolation")
    test_grid()
    print("\nTesting Pointwise Interpolation")
    test_point()
    print("\nTesting Natural Neighbors")
    test_nn()
