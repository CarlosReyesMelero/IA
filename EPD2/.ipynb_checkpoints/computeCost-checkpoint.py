import numpy as np

# computeCost computes cost for linear regression using theta as the parameter for linear regression to fit the data points in X and y
def computeCost(X, y, theta):
    # Initialize some useful values
    m = len(y) # number of training examples
    # You need to return the following variables correctly
    J = 0.0
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta. You should set J to the cost.
    J = np.sum(np.power(np.dot(X, theta) - y.values, 2)) / (2 * m)
    
    # Obetener el coste nos permite obtener la recta de regresion para evaluar valores futuros
    
    return J

