import math

def kl_divergence(P, Q):
    eps = 1e-10
    result = 0.0
    for p, q in zip(P, Q):
        if p > 0:
            q = max(q, eps) # this is to prevent log(0)
            result += p * (math.log(p/q))
            return result