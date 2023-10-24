"""File with merge algorithms for creation dataset"""

# Standart library
import datetime
import numpy as np
import pandas as pd


# Function for converte ts to pandas.DataFreme
def ts2frame(ts :np.ndarray, ts_name: str) -> pd.DataFrame:
    df = pd.DataFrame(data= ts, columns= ['Time', ts_name])
    return df
    

# Function for merge two datafeme
def merge(major_df: pd.DataFrame, minor_df:pd.DataFrame, method: str = 'nearest', tol: str = '1000000h'):
    return pd.merge_asof(major_df, minor_df, on=0, tolerance= pd.Timedelta(tol), direction = method)


# Function for merge all ts
def merge_all(data_dict: dict, sync_name: str, config: dict, max_tol: str = '1000000h', default_method: str = 'nearest'):
    data_frame = pd.DataFrame(data_dict[sync_name])
    dict_temp = data_dict.copy()
    del dict_temp[sync_name]
    for key, value in dict_temp.items():
        temp = pd.DataFrame(value)
        try:
            data_frame = merge(data_frame, temp, config[key]["method"], config[key]["tol"])
        except:
            data_frame = merge(data_frame, temp, default_method, max_tol)
    
    data_frame = data_frame.dropna()
    res = {} 
    for num, name in enumerate(['Time', sync_name] + [x for x,y in dict_temp.items() ]):
        res[name] = np.atleast_2d(data_frame.iloc[:,num]).T
    
    res['Time'] = res['Time'].astype(datetime.datetime)

    return res