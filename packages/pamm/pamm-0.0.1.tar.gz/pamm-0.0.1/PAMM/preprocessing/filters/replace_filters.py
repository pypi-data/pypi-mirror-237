import numpy as np

def set_delay(ts: np.ndarray, delay: int) -> np.ndarray:
    ts[:,0] = ts[:,0] + delay
    return ts