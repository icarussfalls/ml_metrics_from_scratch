# ML Metrics from Scratch

## KL Divergence (Kullback-Leibler Divergence)

The Kullback-Leibler (KL) divergence is a measure of how one probability distribution $Q$ diverges from a true probability distribution $P$. It is defined as:

$$
D_{KL}(P \parallel Q) = \sum_{i} P(i) \log \left( \frac{P(i)}{Q(i)} \right)
$$

---

## Shannon Entropy

Shannon Entropy quantifies the uncertainty or randomness in a probability distribution $P$:

$$
H(P) = - \sum_{i} P(i) \log P(i)
$$

It is extensively used for the characterization of complex processes, detecting non-linearity in model series, and enhancing the understanding of complex systems characterized by non-equilibrium.

---

## Gini Impurity

Gini Impurity measures how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the set. Used in decision trees:

$$
G(P) = 1 - \sum_{i} P(i)^2
$$

---

## Softmax

The softmax function converts a vector of values (logits) into probabilities that sum to 1:

$$
\mathrm{softmax}(z_i) = \frac{\exp(z_i)}{\sum_{j} \exp(z_j)}
$$

For numerical stability, it is common to subtract the maximum value from the logits before exponentiating:

$$
\mathrm{softmax}(z_i) = \frac{\exp(z_i - \max_j z_j)}{\sum_{j} \exp(z_j - \max_j z_j)}
$$

---

## Sparsemax

Sparsemax maps logits to a sparse probability distribution by projecting them onto the simplex, resulting in some probabilities being exactly zero. This makes the output more interpretable and sparse, which is useful in attention mechanisms and classification tasks where sparsity is desired.

$$
\mathrm{sparsemax}(z) = \arg\min_{p \in \Delta^{K-1}} \| p - z \|^2
$$

where $\Delta^{K-1}$ is the probability simplex in $K$ dimensions.