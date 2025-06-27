import math

def softmax(logits):
    max_logits = max(logits) 
    exps = [math.exp(x - max_logits) for x in logits]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]