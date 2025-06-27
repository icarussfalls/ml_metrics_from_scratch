from gini import *
from kl_divergence import *
from softmax import *
from sparsemax import *
from entropy import *


P = [0.1, 0.9]
Q = [0.3, 0.7]
x = [1.0, 2.0, 3.0]

print("KL(P||Q)", kl_divergence(P, Q))
print("Entropy(P)", entropy(P))
print("Gini(P)", gini_impurity(P))
print("Softmax(x)", softmax(x))
print("Sparsemax(x)", sparsemax(x))
