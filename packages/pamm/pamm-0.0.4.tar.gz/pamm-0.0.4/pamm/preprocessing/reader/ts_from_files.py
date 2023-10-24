"""File with functions for read ts from files"""

# Standart library
import os
import asyncio
import datetime
import numpy as np
import pandas as pd
import openpyxl as op
from io import StringIO
from xlsx2csv import Xlsx2csv

# delete void columns from data
def del_void_columns(df: pd.DataFrame) -> pd.DataFrame:
    void_columns = [col for col in df.columns if pd.isnull(pd.to_numeric(df[col], errors='coerce').mean())]
    return df.drop(void_columns ,axis=1)

# function for take the name of files in directory
def generate_files_list(folder_path :str) -> list[str]: 
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# function for search index with datetime
def search_date_index(df: pd.DataFrame) -> list[int]:
    date_index = [num for num, col in enumerate(df) if isinstance(np.datetime64('2005-02', 'D'), df[col].dtype.type)]
    date_index.append(len(df.columns)+1)
    return date_index

# function for generate data frames with ones dates
def generate_df(data_frame: pd.DataFrame) -> list[pd.DataFrame]:
    dates = search_date_index(data_frame)

    list_df = []

    for num, x in enumerate(dates):
        if len(dates) == num + 1:
            break
        list_df.append(data_frame.iloc[:, dates[num]:dates[num+1]])
    return list_df

# function for generate timeseries
def generate_ts(data_frame: pd.DataFrame) -> dict:
    data_frames = generate_df(data_frame)
    dict_ts = {}
    for df in data_frames:
        for num,col in enumerate(df.columns):
            if num != 0:
                temp_df = df.iloc[:,[0,num]]
                temp_df[col] = pd.to_numeric(data_frame[col], errors='coerce')
                dict_ts[col] = temp_df.dropna().to_numpy()
                dict_ts[col][:,0] = dict_ts[col][:,0].astype(np.datetime64)
    return dict_ts

# function for read excel files
def read_excel(path: str) -> dict[str : np.array]:
    data = {}
    file = pd.ExcelFile(path)
    for sheet in file.sheet_names:
        tmp = del_void_columns(pd.read_excel(file, sheet_name=sheet))
        data.update(generate_ts(tmp))
    return data


# function for read csv files
def read_csv(path: str) -> None:
    tmp = del_void_columns(pd.read_csv(path))
    data = generate_ts(tmp)

# dictionary with file-extentions : function for read
EXTENTION_DICT = {
    '.xlsx':read_excel,
    '.xlsm':read_excel,
    '.xlsb':read_excel,
    '.xlam':read_excel,
    '.xltx':read_excel,
    '.xltm':read_excel,
    '.xls':read_excel,
    '.xla':read_excel,
    '.xlt':read_excel,
    '.csv':read_csv,
    '.odf':read_excel
}

# function for read all tables-like files in directory
def read_directory(path: str) -> None:
    data = {}
    file_names = generate_files_list(path)
    for filename in file_names:
        _, fileExtension = os.path.splitext(filename)
        if fileExtension in EXTENTION_DICT:
            tempFrame = EXTENTION_DICT[fileExtension](filename)
            data.update(tempFrame)
    return data