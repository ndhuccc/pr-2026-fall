# KP14 Cover's Theorem

!!! note "Self-study"
    This unit (KP14) is self-study: it is not taught in class, so please read it on your own.

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.13

[Slides: read and download](../../slides/lec05-kp14-cover-theorem-en.jbd.json) | [中文版](../lec05-kp14-cover-theorem.md)

## Learning objectives

- Use Cover's formula to compute the number of linear dichotomies and the probability of separable for $N$ points in general position in $l$ dimensions.
- Explain the critical point $N=2(l+1)$ and the phase transition, and predict the probability after lifting.
- Explain that lifting raises separability but does not guarantee generalization.

## KP14 Cover's Theorem

**One-sentence summary**: The higher the dimension, the more likely a set of points with random labels is still linearly separable, and there is a sharp critical point $N=2(l+1)$; this is the quantitative licence for lifting, but it only guarantees that the training data can be separated, not that they generalize.

### 1. How many splits

**Plain explanation**: does lifting really help? First count into how many two-class splits one line can cut some points.

**Dichotomy**: one way of labeling $N$ points with two classes; the ones a line (hyperplane) can realize are the linear dichotomies. For three points all 8 labelings are separable by a line; for four points at the corners of a square 14 of the 16 labelings are separable and the 2 that are not put the diagonal pairs together, $[(A,D),(B,C)]$, which are XOR and its mirror XNOR (A top-left, B bottom-left, C top-right, D bottom-right; checked one by one by a program).

Figure `lec05-kp14-dichotomy`: the 16 labelings, green separable and red not.

![16 labelings](../../assets/figures/lec05-kp14-dichotomy.png)

### 2. The counting formula

**General position**: points in $l$ dimensions with no $l+1$ of them on one $(l-1)$-dimensional hyperplane (in two dimensions, no three on a line).

**Formal definition** (Cover's formula, source):

$$
O(N,l)=2\sum_{i=0}^{l}\binom{N-1}{i}.
$$

**Example**: $N=4,l=2$: $2(1+3+3)=14$; $N=3$: $2(1+2+1)=8=2^3$. For $N\le l+1$, $O=2^N$: all labelings are separable. For $l=2$ and $N=1..8$, $O=2,4,8,14,22,32,44,58$ while $2^N=2,4,8,16,32,64,128,256$.

Figure `lec05-kp14-count`: $O(N,2)$ against $2^N$.

![Count table](../../assets/figures/lec05-kp14-count.png)

### 3. Probability of separable

With random labels, $P_N^l=O(N,l)/2^N$ and $P=1$ for $N\le l+1$. In two dimensions ($l=2$), for $N=1..10$: $P=1,1,1,0.875,0.6875,0.5,0.344,0.227,0.145,0.090$. Once $N$ passes $l+1=3$ the probability starts to fall and it reaches exactly half at $N=6$.

Figure `lec05-kp14-prob`: the probability for $l=2$ and $N=1..10$.

![Probability](../../assets/figures/lec05-kp14-prob.png)

### 4. The phase transition

**Phase transition**: the turn of the probability from 1 down to 0 gets sharper as the dimension grows, like water freezing. With $N=r(l+1)$, at $r=2$, i.e. $N=2(l+1)$, $O(2l+2,l)=2^{2l+1}$, so the probability is exactly $1/2$ (checked for $l=1..7$). $P$ at $r=1.5$ and $2.5$: $0.75,0.31$ for $l=1$; $0.97,0.08$ for $l=19$; $1.00,0.0007$ for $l=99$.

Figure `lec05-kp14-curves`: $P$ against $r$ for several $l$, all through $(2,1/2)$.

![Phase transition curves](../../assets/figures/lec05-kp14-curves.png)

### 5. A random test

Each run draws $N$ two-dimensional Gaussian points with random $\pm1$ labels and uses a linear program to decide whether a separating line exists, 1500 runs each: 0.865 at $N=4$ (formula 0.875) and 0.503 at $N=6$ (formula 0.500). With 1500 runs the standard error is about 0.01, so the gap is about one standard error (program, designed here).

Figure `lec05-kp14-mc`: formula against simulation.

![Random test](../../assets/figures/lec05-kp14-mc.png)

### 6. The effect of lifting

With the same random points and labels, $[x_1,x_2]$ is $l=2$; adding $x_1^2,x_2^2,x_1x_2$ makes $l=5$. The formula predicts $N=6\le l+1=6$, so $P=1$. The simulation (1500 runs) gives 0.494 for the original two dimensions and 1.000 for the quadratic features.

Figure `lec05-kp14-lift`: the separable fraction before and after lifting.

![Effect of lifting](../../assets/figures/lec05-kp14-lift.png)

### 7. How many dimensions

For $N>l+1$ some labelings fail; once the data exceed twice the degrees of freedom ($l+1$ adjustable parameters), $N>2(l+1)$, the probability of separable drops below half. For $N=100$: $l=40$ gives $0.035$; $48$ gives $0.42$; $49$ exactly $0.5$; $56$ gives $0.92$; $60$ gives $0.987$; $68$ gives $0.9999$. To separate random labels by lifting, the dimension must reach about half the number of samples or more.

Figure `lec05-kp14-need`: the probability for $N=100$ against the dimension $l$.

![How many dimensions](../../assets/figures/lec05-kp14-need.png)

### 8. Separable is not general

**Common misconception**: after lifting, if the training data can be separated then new data will be classified correctly. Experiment (designed here): 5 two-dimensional Gaussian points with random labels and a separating hyperplane in the quadratic features (5 dimensions) was found in all 300 runs with training all right; then 200 fresh points, also with random labels, were only 50.4% right on average, which is guessing. Lifting only guarantees that the training data can be separated; only data with a pattern can be learned, and generalization is a separate matter (Chapter 5).

Figure `lec05-kp14-gen`: accuracy on training and new points.

![Separable is not general](../../assets/figures/lec05-kp14-gen.png)

### Extension: why half, practice and worked solution

**Why half**: $\binom{2l+1}{i}=\binom{2l+1}{2l+1-i}$, so the sum over $i\le l$ is exactly half of the total $2^{2l+1}$, namely $2^{2l}$; $O(2l+2,l)=2\cdot2^{2l}=2^{2l+1}$ and $P=1/2$. For $l=1..5$, $O=8,32,128,512,2048$.

Figure `lec05-kp14-proof`: $O$ for $l=1..5$ and the symmetry.

![Why half](../../assets/figures/lec05-kp14-proof.png)

**Practice**: $N=5$ points in general position.

1. What are $O(5,2)$ and $P$ for $l=2$? Hint: $\binom{4}{i}=1,4,6,4,1$.
2. Lifting to $l=3$, what is $P$?

Figure `lec05-kp14-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp14-practice.png)

**Worked solution of questions 1 and 2**: (1) $O(5,2)=2(1+4+6)=22$ and $P=22/32=0.6875$. (2) $O(5,3)=2(1+4+6+4)=30$ and $P=30/32=0.9375$. (3) Check: 22 matches the table of section 2, and one more dimension raises the probability of separable from 0.6875 to 0.9375.

Figure `lec05-kp14-practice-sol`: $O$ and $P$ for the two dimensions.

![Practice solution](../../assets/figures/lec05-kp14-practice-sol.png)

## Terms and sources

| English | 中文 |
|---|---|
| Dichotomy | 二分 |
| General position | 一般位置 |
| Phase transition | 相變 |

Source: Chapter 4 KP14, §4.13 (read 2026-10-25). Cover's formula, the probability of separable, the critical point $N=2(l+1)$ and the phase transition, 14 against 16 for $N=4,l=2$, and "lifting raises separability, not generalization" follow the source; every number, the random test (linear programming), the before-and-after lifting fractions, the $N=100$ table and the random-label generalization experiment were designed and recomputed for this lecture ([added], (program)).
