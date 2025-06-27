def gini_impurity(P):
    result = 0.0
    for p in P:
        result += p*p
    return 1 - result

# P is the proportion of the class i in the node