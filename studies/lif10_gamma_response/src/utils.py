import numpy as np
import os

def read_txt(textpath, start = 32):
    with open(textpath, 'r') as f:
        lines = f.readlines()
        lines = lines[start:]

        x_arr = []
        y_arr = []
        
        for line in lines:
            x, y = np.array(line.strip().split('\t')).astype(float)
            x_arr.append(x)
            y_arr.append(y)

        return np.array(x_arr), np.array(y_arr)


def combine_spectra(sample_dir_path, its = 5):
    y_matrix = []
    for it in range(its):
        filepath = os.path.join(sample_dir_path, f"it_{it}.txt")
        x,y = read_txt(filepath)
        y_matrix.append(np.array(y))

    y_comb = np.add.reduce(y_matrix)/its

    return x, y_comb


def gaussian(x, A, s, m):
    return A * np.exp(-(((x-m)**2)/(2*s**2)))

def gaussian2(x, A1, s1, m1, A2, s2, m2):
    return gaussian(x, A1, s1, m1) + gaussian(x, A2, s2, m2)