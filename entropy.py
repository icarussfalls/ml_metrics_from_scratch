import numpy as np


def entropy(P):
    P = np.asarray(P, dtype=np.float32)
    eps = 1e-10
    P = np.clip(P, eps, 1)
    return -np.sum(P * np.log(P))
