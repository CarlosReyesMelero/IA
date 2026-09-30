import pandas as pd
import numpy as np
# gradientDescentMulti performs gradient descent to learn theta
#       theta = gradientDescentMulti(x, y, theta, alpha, num_iters) updates theta by
#       taking num_iters gradient steps with learning rate alpha
from computeCostMulti import computeCostMulti


def gradientDescentMulti(X, y, theta, alpha, iterations):
    # Initialize some useful values
    m = len(y) # Number of training examples
    current_iter = [] # Empty arrays to create a history dataframe
    current_cost = []

    # ====================== YOUR CODE HERE ======================
    # Instructions: Perform a single gradient step on the parameter vector theta
    #
    # Hint: While debugging, it can be useful to print out the values
    #       of the cost function (computeCostMulti) and gradient here.

    return theta, J_history


