ELBO (Evidence Lower Bound): ELBO stands for Evidence Lower Bound, which is a term used in variational inference, a technique in machine learning and statistics. In variational inference, ELBO is a lower bound on the log-likelihood of the observed data. It is used to approximate the intractable posterior distribution by optimizing a tractable variational distribution.
$$\begin{aligned}
\log p(X)& =\log\int_{Z}p(X,Z)  \\
&=\log\int_{Z}p(X,Z)\frac{q(Z)}{q(Z)} \\
&=\log\left(\mathbb{E}_{q}\left[\frac{p(X,Z)}{q(Z)}\right]\right) \\
&\geq\mathbb{E}_{q}\left[\log\frac{p(X,Z)}{q(Z)}\right] \\
&=\mathbb{E}_q\left[\log p(X,Z)\right]+H[Z]
\end{aligned}$$
shannon Entropy:
$$H[Z]=-\mathbb{E}_q[\log q(Z)]$$
变分置信下界，其中q(z)是p(z|x)的近似
$$ L=\mathbb{E}_q\left[\log p(X,Z)\right]+H[Z]$$
Shannon entropy, named after Claude Shannon, is a measure of the uncertainty or information content in a random variable or distribution. It quantifies the average amount of information needed to describe or predict an outcome from a given set of possibilities.

In the context of information theory and statistics, Shannon entropy is often used to quantify the amount of uncertainty or randomness in a set of data. It is calculated using the probabilities of different outcomes. The formula for Shannon entropy is:

$$H(X) = - Σ (p(x) * log2(p(x)))$$

Where H(X) represents the Shannon entropy of a random variable X, p(x) is the probability of outcome x, and the summation is taken over all possible outcomes.

A higher entropy value indicates greater uncertainty or randomness, while a lower entropy value indicates less uncertainty or more predictability. Shannon entropy has applications in various fields, including data compression, cryptography, machine learning, and data analysis.

## what does elbo doing？
The lower bound L hits the log probability _iff_ the approximation distribution is perfectly closed to the true posterior distribution.


$$\mathrm{KL}\left(q(\mathbf{z})||p(\mathbf{z}|\mathbf{x})\right)=\int q(\mathbf{z})\log\frac{q(\mathbf{z})}{p(\mathbf{z}|\mathbf{x})}d\mathbf{z}=-\int q(\mathbf{z})\log\frac{p(\mathbf{z}|\mathbf{x})}{q(\mathbf{z})}d\mathbf{z}.$$

瓦瑟斯坦散度（Wasserstein distance），也称为地面距离（earth mover's distance），是一种用于度量两个概率分布之间的距离的方法。它是基于最小化将一个分布转换为另一个分布所需的最小成本或工作量来定义的。

瓦瑟斯坦散度考虑了两个分布之间的几何结构和形状，并量化了将一个分布变换为另一个分布所需的最小成本。它可以用来比较两个分布之间的相似性或差异性。与其他常用的距离度量方法（如KL散度）相比，瓦瑟斯坦散度在处理具有重叠或不连续性的分布时更具优势。

瓦瑟斯坦散度可以通过求解一个优化问题来计算，其中目标是找到具有最小成本的分布转换方案。这个问题可以通过线性规划或其他数值优化方法来解决。

瓦瑟斯坦散度在许多领域有广泛的应用，包括图像处理、机器学习、生成模型、经济学等。它被用作衡量分布之间的相似性或差异性的度量，以及在优化问题中的约束或目标函数。

The Wasserstein distance, also known as the Earth Mover's distance or Kantorovich-Rubinstein distance, is a measure of the dissimilarity between two probability distributions. It quantifies the minimum amount of "work" required to transform one distribution into the other.

Formally, given two probability distributions P and Q defined on a metric space X, the Wasserstein distance of order p (denoted as $W_p(P, Q)$) is defined as:

$$W_p(P, Q) = inf(γ) { (∫∫ dist(x, y)^p dγ(x, y))^{1/p} }$$

where the infimum is taken over all joint distributions γ(x, y) with marginals P and Q, and dist(x, y) is the distance metric between points x and y in X.

In simpler terms, the Wasserstein distance calculates the minimum amount of "work" needed to move the mass from one distribution to the other. The distance is computed by finding the optimal transportation plan γ that minimizes the total cost of moving each unit of mass from P to Q, where the cost is given by the distance raised to the power of p.

The Wasserstein distance has several desirable properties, including being a true metric, meaning it satisfies the triangle inequality and is non-negative. It is also a powerful tool in various fields, such as optimal transport theory, image processing, and machine learning, as it provides a meaningful measure of dissimilarity between probability distributions.

POT (Python Optimal Transport) library:

```python
import numpy as np
import ot

def gWasserstein_distance(X, Y, p=2, reg=0.1):
    """
    Compute the gWasserstein distance between two sets of points.

    Parameters:
        X (numpy array): First set of points, shape (n_samples, n_features).
        Y (numpy array): Second set of points, shape (n_samples, n_features).
        p (float): Power parameter for the distance metric (default: 2).
        reg (float): Regularization parameter for optimal transport (default: 0.1).

    Returns:
        float: The gWasserstein distance between X and Y.
    """
    # Compute the distance matrix
    M = ot.dist(X, Y, metric='euclidean')

    # Compute the gWasserstein distance using POT library
    gW_distance = ot.gromov.gromov_wasserstein2(M, M, np.ones(len(X)), np.ones(len(Y)), 'square_loss', reg=reg, log=False)

    return gW_distance**p

# Example usage
X = np.random.rand(100, 2)  # First set of points
Y = np.random.rand(100, 2)  # Second set of points

distance = gWasserstein_distance(X, Y)
print("gWasserstein distance:", distance)
```

