
def sparsemax(logits):
    z = list(logits)
    z_sorted = sorted(z, reverse=True)

    cumulative = 0.0
    k = 0

    for j, z_j in enumerate(z_sorted):
        cumulative += z_j
        t_hat = (cumulative - 1) / (j + 1)
        if z_j > t_hat:
            k = j + 1
    tau = (sum(z_sorted[:k]) - 1) / k
    return [max(z_i - tau, 0.0) for z_i in z]
