"""File with regression model algorithm on two-stage least sqares."""
# Third Party Library
from PAMM.algorithms.regression.regression_model import RegressionAlgorithm

import numpy as np

class BatchGradientRegressionAlgorithm(RegressionAlgorithm):
        
    def fit(self,
        x: np.ndarray,
        y: np.ndarray,
        eta: float = .1,
        max_iter: int = 1000) -> np.ndarray:
        
        x = self._add_bias(x)
        m, n = x.shape
        theta = np.random.randn(n,1)
        for iteration in range(max_iter): 
            gradients = 2/m * x.T @ (x @ theta - y) 
            theta = theta - eta * gradients
        
        self._beta = theta[int(self._fit_bias):]
        self._bias  = theta[0][0] * int(self._fit_bias)