import numpy as np
import pandas as pd

# featureNormalize normalizes the features in X
# featureNormalize(X) returns a normalized version of X where
# the mean value of each feature is 0 and the standard deviation
# is 1. This is often a good preprocessing step to do when
# working with learning algorithms.

def featureNormalize(X):
    # Normaliza las caracteristicas de X restando la media y diviendo entre la desviacion 
    # estándar para cada atributo

    mu = np.mean(X, axis = 0)
    sigma = np.std(X, axis = 0, ddof = 0)

    X_norm = (X - mu) / sigma

    return X_norm, mu, sigma


