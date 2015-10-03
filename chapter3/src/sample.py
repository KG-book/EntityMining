# -*- coding: utf-8 -*-
import numpy as np



def sample_by_rate(data, rate):
    return [d for d in data if np.random.rand() < rate]
        

def reservoir(itr, n_samples):
    read_cnt = 0
    samples = np.empty(n_samples, dtype='|S20')
    for s in itr:
        if read_cnt < n_samples:
            samples[read_cnt] = s
        elif np.random.rand() < (n_samples * 1. / read_cnt):
            samples[np.random.randint(n_samples)] = s
        read_cnt += 1
    return samples


def file_iterate(file_name, n):
    for i in range(n):
        with open(file_name) as f:
            for l in f:
                yield l
                

def data_iterate(data, n):
    for i in range(n):
        for d in data:
            yield d
            
            
def over_sample(data, n_samples):
    return data[np.random.random_integers(0, data.shape[0]-1, size=n_samples)]
    

    