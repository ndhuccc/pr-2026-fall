# KP21 The Representer Theorem, Kernel Expansions and Sparsification

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.19.1

[Slides: read and download](../../slides/lec05-kp21-representer-en.jbd.json) | [中文版](../lec05-kp21-representer.md)

## Learning objectives

- Explain how the SVM solution differs from a Parzen expansion and what a sparse solution is.
- State the representer theorem and check it with numbers; solve kernel least squares and its version with $CI$.
- Explain that sparsity comes from the regularization term and is not automatic, and list four routes to sparsification.

## KP21 The Representer Theorem, Kernel Expansions and Sparsification

**One-sentence summary**: Even when we search an infinite-dimensional space, the best solution is a combination of $N$ kernels placed on the $N$ training points; the regularization term decides how many of the $N$ coefficients are zero.

### 1. A sparse solution

**Plain explanation**: The SVM solution is also a sum of kernels; how many does it use?

- **Sparse solution**: an expansion in which most coefficients are 0 and only a few terms are really used.

The SVM solution is $g(x)=\sum_{i=1}^{N_s}a_iK(x,x_i)+w_0$ with $a_i=\lambda_iy_i$, and with a Gaussian kernel it resembles a Parzen expansion. Two differences: (1) $g$ is not a density (it does not integrate to 1); (2) the number of terms: Parzen uses all $N$ points, the SVM only the $N_s$ support vectors. **Example** (KP19 data, $C=10$, $\gamma=0.5$): only 19 of the 120 training points are support vectors, with 96.8% on new points.

Figure `lec05-kp21-sparse`: the 120 Parzen kernels on the left and the 19 of the SVM on the right.

![A sparse solution](../../assets/figures/lec05-kp21-sparse.png)

### 2. The representer theorem

**The representer theorem** (formal definition): let $\mathcal L$ be any non-negative loss and $\Omega$ strictly increasing; then the regularized cost

$$
\sum_{i=1}^{N}\mathcal L(g(x_i),y_i)+\Omega(\|g\|)
$$

has in the RKHS a minimizer of the form $g(x)=\sum_{j=1}^{N}a_jK(x,x_j)$. The **regularization term** $\Omega(\|g\|)$ penalizes the norm of the solution and keeps it small and simple. The search space may be infinite-dimensional, yet only $N$ coefficients remain.

Figure `lec05-kp21-rep`: the content of the theorem.

![The representer theorem](../../assets/figures/lec05-kp21-rep.png)

### 3. A numerical check

**Gram matrix** $\mathcal K$: the $N\times N$ array of $K(x_i,x_j)$. **Example** (designed here): the quadratic kernel has 6 explicit features; 30 random points and targets, $C=0.7$. Solving $w=(\Phi^T\Phi+CI)^{-1}\Phi^Ty$ in 6-D and $a=(\mathcal K+CI)^{-1}y$ with the kernel: $w$ and $\Phi^Ta$ differ by at most $1.9\times10^{-14}$, and predictions on new points by at most $2.2\times10^{-14}$. $w=\sum_ja_j\phi(x_j)$ lies in the span of the training feature vectors, a special case of the theorem.

Figure `lec05-kp21-repcheck`: the gap between the 6-D and the kernel solution.

![A numerical check](../../assets/figures/lec05-kp21-repcheck.png)

### 4. Kernel least squares

Substituting $g(x)=\sum_ja_jK(x,x_j)$: $J(a)=(y-\mathcal Ka)^T(y-\mathcal Ka)$, a zero gradient gives $a=\mathcal K^{-1}y$ and $g(x)=y^T\mathcal K^{-1}p$ with $p=[K(x,x_1),\dots,K(x,x_N)]^T$ ($\mathcal K$ must be invertible). **Example** (designed here): points $x=0,1$, targets $+1,-1$, kernel $K=xz+1$: $\mathcal K=\begin{bmatrix}1&1\\1&2\end{bmatrix}$, $a=(3,-2)$, $g(x)=3-2(x+1)=1-2x$, $g(0.5)=0$. **Common misconception**: the representer theorem guarantees a sparse solution; in fact this solution is not sparse and all the $a_j$ are usually nonzero.

Figure `lec05-kp21-hand`: $g$ on two points for $C=0$ and $C=1$.

![Kernel least squares](../../assets/figures/lec05-kp21-hand.png)

### 5. Noisy data

**Example** (designed here): $y=\sin x+$ noise (sd 0.2), 9 points, Gaussian kernel $\exp(-\|x-z\|^2/2\sigma^2)$ with $\sigma=0.8$; the condition number of $\mathcal K$ is 49. Kernel least squares: all 9 $a_j$ are nonzero (largest 2.82); the training error is 0, passing through every point; the mean squared error against the true $\sin x$ is 0.047. With these settings the curve does not oscillate wildly; passing through the noise points is the direction of overfitting, but the size is modest.

Figure `lec05-kp21-sin`: the 9 points and the curves for $C=0$, 0.1 and 10.

![Noisy data](../../assets/figures/lec05-kp21-sin.png)

### 6. Adding C·I

$a=(\mathcal K+CI)^{-1}y$; $C=0$ is kernel least squares and a larger $C$ squeezes the norm of the solution; $CI$ also makes the matrix easier to invert. (Training error, error against $\sin x$): $C=0.01$: 0.0003, 0.043; $C=0.1$: 0.0063, 0.033 (best); $C=1$: 0.078, 0.079; $C=10$: 0.349, 0.355; $C=100$: 0.465, 0.479. A small $C$ passes through the noise and a large one flattens the curve; all 9 $a_j$ stay nonzero for every $C$, so $CI$ creates no sparsity.

Figure `lec05-kp21-csweep`: the errors against $C$.

![Adding C·I](../../assets/figures/lec05-kp21-csweep.png)

### 7. Where sparsity comes from

In $J=\tfrac12\|w\|^2+C\sum I(\xi_i)$ the term $\|w\|^2$ is a regularization term that implicitly drives most $\lambda_i$ to 0. **Example** (designed here, 120 ring points, $\gamma=0.5$) support vectors (new-point accuracy): $C=0.01$: 120 (94.3%); $C=1$: 39 (97.3%); $C=10$: 19 (96.8%); $C=1000$: 13 (95.4%). Sparsity is not automatic (this $C$ is the SVM penalty, larger means less regularization, the opposite of the ridge $C$): at $\gamma=50$ there are 116 whatever $C$ (86.8%); at $\gamma=0.01$, $C=1$: 120 (71.5%).

Figure `lec05-kp21-svcount`: the support-vector count against $C$.

![Where sparsity comes from](../../assets/figures/lec05-kp21-svcount.png)

### 8. Routes to sparsity

Four routes (source): RVM (Bayesian prior, sparser, but memory grows with the square and computation with the cube of the basis count); online adaptation (kernel LMS with a norm constraint); projection (a hyperball constraint equal to a forgetting factor, linear cost); dictionary (add a point only if its similarity is below a threshold, quadratic cost). **Dictionary experiment** (designed here, 120 ring points, $\gamma=0.5$, points arriving one by one in random order): threshold 0.99 keeps 90; 0.9: 38; 0.7: 17; 0.5: 9. **To remember**: the representer theorem leaves $N$ coefficients; the SVM zeroes most through its regularization term, a dictionary through a threshold.

Figure `lec05-kp21-dict`: the 17 points kept at threshold 0.7 and the dictionary size per threshold.

![Routes to sparsity](../../assets/figures/lec05-kp21-dict.png)

### Extension: few is not always good, practice and worked solution

**Comparison** (designed here, $C=1000$): $\gamma=0.01$: 19 support vectors, 96.9%; $\gamma=0.5$: 13, 95.4%; $\gamma=50$: 116, 86.8%. The source reminds us that too many support vectors degrade generalization. But few does not guarantee good (one run, the gap may be noise): at $\gamma=0.5$, $C=1$, 39 support vectors give 97.3%, better than 13 with 95.4%; the count is a clue, not a goal.

Figure `lec05-kp21-dense`: support-vector counts and new-point accuracy.

![Few is not always good](../../assets/figures/lec05-kp21-dense.png)

**Practice**: training points $x=0,1$, targets $+1,-1$, kernel $K=xz+1$; $g(x)=a_1K(x,0)+a_2K(x,1)$.

1. For $C=1$ solve $a=(\mathcal K+I)^{-1}y$ and find $g(0)$ and $g(1)$.
2. Compared with $g(0)=1$, $g(1)=-1$ at $C=0$, what did $C$ do to the solution?

Figure `lec05-kp21-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp21-practice.png)

**Worked solution of questions 1 and 2**: (1) $\mathcal K+I=\begin{bmatrix}2&1\\1&3\end{bmatrix}$ with determinant 5 and inverse $\tfrac15\begin{bmatrix}3&-1\\-1&2\end{bmatrix}$; $a=\tfrac15(3+1,-1-2)=(0.8,-0.6)$; $g(0)=0.8-0.6=0.2$ and $g(1)=0.8-1.2=-0.4$. (2) At $C=0$ they are $+1$ and $-1$ (an exact fit) and $C=1$ shrinks them to $0.2$ and $-0.4$: $C$ pulls the solution toward 0, and both coefficients stay nonzero.

Figure `lec05-kp21-practice-sol`: the computation.

![Practice solution](../../assets/figures/lec05-kp21-practice-sol.png)

## Terms and source

| 中文 | English |
|---|---|
| 稀疏解 | Sparse solution |
| Representer 定理 | Representer theorem |
| 正則化項 | Regularization term |
| Gram 矩陣 | Gram matrix |

Source: Chapter 4, KP21, §4.19.1 (read 2026-10-25). The difference between the SVM solution and the Parzen expansion, the representer theorem, the closed form of kernel least squares, sparsity from the regularization term, the four routes to sparsification and the 'to remember' line follow the source; the 6-D check, the hand example, the 9 noisy points, the support-vector table, the dictionary experiment and the practice were designed and recomputed for this lecture ([added], (program-computed)).
