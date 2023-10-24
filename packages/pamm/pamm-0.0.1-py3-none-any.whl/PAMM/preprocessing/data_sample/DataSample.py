from abc import ABC
import pandas as pd
import numpy as np
from typing import Union, Optional
from collections.abc import Iterable

class DataSample(ABC):
    
    def __init__(self, data: Union[dict, pd.DataFrame], y_column: str, edge: Union[int, float] = .3, time_name: str = 'Time'):

        self._data = data
        self._y = self._validate_y(y_column)
        self._edge = self._validate_edge(edge)
        self._time = time_name


    def __len__(self) -> int:
        return len(self._data[self._y])


    def __getitem__(self, col:str) -> np.ndarray:
        return self._data[col]


    def _percent2index(self):
        delimeter = int(np.ceil(len(self.data) * (100 - self._precent)/100))


    def _validate_edge(self,num) -> int:
        if num < 0:
            raise ValueError("Count values must be positve only.")
        if isinstance(num, int):
            if num > len(self._data[self._y]):
                raise ValueError(f"The value must be less than count of experiment: ({len(self._data[self._y])}).")
            return num
        if num > 1:
            raise ValueError("The value defined as a percentage must be less than 1.")
        return int(np.ceil(len(self._data[self._y]) * (1-num)))
    

    def _validate_y(self,y_column) -> int:
        if y_column in list(self._data.keys()):
            return y_column
        else:
            raise ValueError(f"The y_column name must be contained in the data table: {list(self._data.keys())}.")


    def _matrix(self, names: Union[None ,str, Iterable[str]], up: int, down: int) -> tuple[np.ndarray]:
        _res = None
        if isinstance(names,str):
            names = [names]
        elif names is None:
            names = [name for name in self._data.keys() if name not in [self._y, self._time]]
        for num, name in enumerate(names):
            if num == 0:
                _res = self._data.get(name)
            else:
                _res = np.hstack((_res, self._data.get(name)))
        return (_res[down:up],
        self._data[self._y][down:up],
        self._data[self._time][down:up])

    
    def train(self, names: Union[None, str, Iterable] = None) -> tuple[np.ndarray]:
            return self._matrix(names = names, up = self._edge, down = 0)


    def test(self, names: Union[None, str, Iterable] = None) -> tuple[np.ndarray]:
            return self._matrix(names = names, up = len(self), down = self._edge)


    @property
    def edge(self) -> int:
        return self._edge


    @property
    def data(self) -> dict:
        return self._data


    @edge.setter
    def edge(self, edge:Union[int, float]) -> None:
        self._edge = self._validate_edge(edge)


    @property
    def y(self) -> str:
        return self._y
    
    @property
    def to_DataFrame(self):
        all_names = [name for name in self._data.keys()]
        tmp = self._matrix(names = all_names, up = len(self), down = 0)[0]
        return pd.DataFrame(data = tmp, columns = all_names)