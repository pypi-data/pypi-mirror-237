"""File with ridge regression model algorithm."""
# Third Party Library
from pamm.algorithms.regression.regression_model import RegressionAlgorithm

import numpy as np

class RidgeRegressionAlgorithm(RegressionAlgorithm):
        
    def fit(self, x: np.ndarray, y: np.ndarray, alpha: float = .1) -> None:
        """Fit model.

        Args:
            x (np.ndarray): matrix of regressors
            y (np.ndarray): matrix a teacher
            alpha (float): regularization parameter
        """
        x = self._add_bias(x)
        I = np.eye(x.shape[1])
        tmp = np.linalg.inv(x.T @ x + alpha * I) @ x.T @ y
        self._beta = tmp[int(self._fit_bias):]
        self._bias  = tmp[0][0] * int(self._fit_bias)
