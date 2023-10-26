import os

import numpy as np

from shard_math import normalize


class LVShard:
    def __init__(self, shard_id: int, device: str):
        super(LVShard, self).__init__()

        self.__id = shard_id
        self.__ref = None
        self.__device = device
        self.__vector_count = 0

    def insert(self, vector):
        if not self.__ref:
            np.save(f"lv_shrd{self.__id}", vector)
            self.__ref = f"lv_shrd{self.__id}.npy"
            self.__vector_count += 1
        else:
            with open(self.__ref, 'wb') as f:
                np.save(f, vector)
                self.__vector_count += 1

    def delete(self, vector, first: bool):
        nx = False
        keep = []

        with open(self.__ref, 'rb') as f:
            v = np.load(f)
            while v:
                if nx:
                    keep.append(v)
                elif first:
                    if v == vector:
                        self.__vector_count -= 1
                        nx = True
                    else:
                        keep.append(v)
                elif not first and v == vector:
                    keep.append(v)
                else:
                    self.__vector_count -= 1
                v = np.load(f)

        if keep: np.save(f"lv_shrd{self.__id}", keep[0])
        with open(self.__ref, 'wb') as f:
            for i in range(1, len(keep)):
                np.save(f, keep[i])
                self.__vector_count += 1

    def get_data(self, partial: bool, lo: float, hi: float):
        with open(self.__ref, 'rb') as f:
            v = np.load(f)
            while v:
                if partial:
                    if lo <= normalize(v) <= hi:
                        yield v
                else:
                    yield v
                v = np.load(f)

    def clear(self):
        os.remove(self.__ref)
        self.__vector_count = 0
        self.__ref = None

    def __len__(self):
        return self.__vector_count