import datetime
import numpy as np
import datetime

def side2_percentile_filter(ts: np.ndarray, percentile: float) -> np.ndarray:
    values = ts[:,1]
    up_percentile = np.percentile(values,percentile)
    low_percentile = np.percentile(values,100 - percentile)

    mask = (values < up_percentile) ,(values > low_percentile)
    return ts[np.logical_and(*mask)]

def set_delay(ts: np.ndarray, delay:datetime.timedelta) -> np.ndarray:
    data = ts.copy()
    data[:,0] = data[:,0] + delay
    return data
