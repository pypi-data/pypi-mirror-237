"""File with methods for generate list algorithms."""

# Third Party Library
import numpy as np
from PAMM.algorithms.regression.wls.weights import weights_data_algorithms
from PAMM.algorithms.regression.wls.weights import weights_beta_algorithms 
from inspect import getmembers, isfunction
from collections.abc import Sequence


all_weights_data_algorithm = {func[0]:func[1] for func in getmembers(weights_data_algorithms, isfunction)}
all_weights_beta_algorithm = {func[0]:func[1] for func in getmembers(weights_beta_algorithms, isfunction)}

def apply_weights_data_algorithm(
    data: np.ndarray,
    algorithm: Sequence[list(all_weights_data_algorithm)]  = 'usual_algorithm'
    ) -> np.ndarray:

    return all_weights_data_algorithm[algorithm](data)


def apply_weights_beta_algorithm(
    data: np.ndarray,
    algorithm: Sequence[list(all_weights_beta_algorithm)]  = 'usual_algorithm'
    ) -> np.ndarray:

    return all_weights_beta_algorithm[algorithm](data)
