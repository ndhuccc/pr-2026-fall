# KP16 RBF Networks

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4 §4.15

[Slides: read and download](../../slides/lec05-kp16-rbf-en.jbd.json) | [中文版](../lec05-kp16-rbf.md)

## Learning objectives

- Write the form of an RBF network and explain the difference between a local and a global response.
- Solve XOR with two centres, and explain how a straight line relates to a closed curve in the original space.
- Explain how centres are chosen, the dimension cost of locality, and the contrast between MLP and RBF.

## KP16 RBF Networks

**One-sentence summary**: Replace the interpolation function by a function of "how far from a centre"; each node responds only to data near itself; locality makes it learn fast, but also forces it to fill the space with many centres, which eats dimensions.

### Prerequisites and symbols

**Three things you need first**:

- **Generalized linear classifier** (KP13): first replace $x$ by new coordinates with fixed functions, then learn a classifier that is linear in the weights.
- **Distance and norm**: $\|x-c\|^2$ is the squared Euclidean distance from $x$ to $c$; for $x=(0.5,0.5)$ and $c=(0,0)$ it is $0.25+0.25=0.5$.
- **Least squares** (KP13): solve the weights by the normal equation.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $c_i$, $k$ | the $i$-th centre, the number of centres | one centre per hidden node |
| $\sigma_i$ | width of the Gaussian | this lecture mostly uses $2\sigma^2$ as denominator; the larger $\sigma$, the wider the response |
| $y$ | new coordinates after the mapping | $y_i=\exp(-\|x-c_i\|^2/(2\sigma^2))$ |
| $w_0,w_i$ | bias and output weights | the only ones learned by least squares (with fixed centres) |
| $g(x)$ | discriminant | $g>0$ decides one class, $g<0$ the other |
| $l$ | input dimension | section 7 |
| $N$ | number of training points | Parzen estimation uses $k=N$ |

### 1. Gaussian nodes

**Plain-words explanation**: The product terms of KP15 respond over the whole space. Can we use new coordinates that respond only to nearby data?

- **Radial basis function** (RBF): a function whose argument is "the distance to a centre $c_i$"; the Gaussian is the most common.

**RBF network**:

$$
g(x)=w_0+\sum_{i=1}^{k}w_i\exp\!\Big(-\frac{\|x-c_i\|^2}{2\sigma_i^2}\Big),
$$

one layer of Gaussian hidden nodes plus a linear output. It is closely related to Parzen estimation, with almost the same form, but Parzen has one kernel per training point ($k=N$) while here $k\ll N$.

Figure `lec05-kp16-bumps`: First look at the top: one sigmoid node responds high over one whole side of the line; then at the bottom: each of three Gaussians responds only near its own centre and falls to 0 away from it. [Function: 1]

![Gaussian nodes: one sigmoid responds on the whole line at the top; three Gaussians each respond near their centre at the bottom.](../../assets/figures/lec05-kp16-bumps.png)

The next question: what do local and global look like on a two-dimensional plane?

### 2. Local versus global

- **Local response**: the node responds only near its centre and goes to 0 away from it.
- **Global response**: the node responds along a whole hyperplane.

The equal-output set of a sigmoid node is a hyperplane (a line in two dimensions); that of an RBF node is a hypersphere (a circle in two dimensions).

**Example** ($2\sigma^2=1$): at distance $d=0,1,2,3$ from the centre the Gaussian response is $e^{-d^2}$:

| distance $d$ | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| response | 1 | 0.368 | 0.0183 | 0.000123 |

Figure `lec05-kp16-contours`: First look at the left panel: the equal-output lines of the sigmoid are a family of parallel straight lines; then the right panel: those of the RBF are concentric circles around the centre. [Function: 1]

![Local versus global: the equal-output lines of a sigmoid on the left, the concentric circles of an RBF on the right.](../../assets/figures/lec05-kp16-contours.png)

### 3. XOR needs only two centres

**Setting**: $k=2$, $c_1=(1,1)$, $c_2=(0,0)$, $y_i=\exp(-\|x-c_i\|^2)$ (that is, $2\sigma^2=1$).

Point by point:

| $x$ | squared distance to $c_1$ | squared distance to $c_2$ | $y=(y_1,y_2)$ | $g=y_1+y_2-1$ |
|---|---:|---:|---|---:|
| $(0,0)$ | 2 | 0 | $(0.135,\,1)$ | $+0.135$ |
| $(1,1)$ | 0 | 2 | $(1,\,0.135)$ | $+0.135$ |
| $(1,0)$ | 1 | 1 | $(0.368,\,0.368)$ | $-0.264$ |
| $(0,1)$ | 1 | 1 | $(0.368,\,0.368)$ | $-0.264$ |

$(1,0)$ and $(0,1)$ are both mapped to $(0.368,0.368)$, that is, "folded" onto one point; one line $y_1+y_2=1$ separates the two classes.

Figure `lec05-kp16-xormap`: First look at the left input plane: the two stars are the two centres and the four points are the corners of the square; then the right feature plane: the two points of the same XOR class coincide in the middle, the other two are at the two ends, and one slanted line separates them. [Function: 1, 2]

![XOR with two centres: the input plane (centres as stars) and the feature plane after the mapping.](../../assets/figures/lec05-kp16-xormap.png)

### 4. Back in the original space

$g(x)=e^{-\|x-c_1\|^2}+e^{-\|x-c_2\|^2}-1=0$ is a closed curve enclosing the two centres.

- $(0,0)$, $(1,1)$: $g=+0.135$, inside the curve.
- $(1,0)$, $(0,1)$: $g=-0.264$, outside the curve.
- Far from all centres both exponential terms go to 0, so $g\to-1$; far away everything goes to the class outside the curve, a property of local response.

Figure `lec05-kp16-xorcurve`: First look at the closed curve around the two centres on the original plane; then at which side of it each of the four points lies: $(0,0)$ and $(1,1)$ inside, $(1,0)$ and $(0,1)$ outside. [Function: 2]

![The decision curve (a closed curve) and the four XOR points on the original plane.](../../assets/figures/lec05-kp16-xorcurve.png)

The next question: the two XOR centres were chosen by hand. With a lot of data, where do the centres come from?

### 5. Fixed centres

- **Fixed centres**: pick $k$ training points at random as the centres; once the centres are fixed only $w$ is left to learn, which is the linear problem of KP13 (least squares).

**Experiment setting** (designed for this lecture, reproducible):

- Data: concentric rings. The angle is uniform in $[0,2\pi)$; the radius is $N(1.0,0.15^2)$ for class A and $N(2.2,0.2^2)$ for class B; 100 points per class, 200 training points in all (NumPy `default_rng(0)`); new points: 500 per class, 1000 in all (`default_rng(1)`).
- Model: $2\sigma^2=1$ (that is, $\sigma^2=0.5$); $k$ centres picked at random from the training points; $w_0,w_i$ by least squares; prediction by the sign of $g$.
- Repetition: for each $k$, the centres are picked once with each seed 0 to 19 (20 times) and the new-point accuracy is averaged.

| centres $k$ | 1 | 2 | 4 | 8 | 16 | 32 |
|---|---:|---:|---:|---:|---:|---:|
| new-point accuracy | 56.0% | 64.2% | 76.1% | 91.5% | 99.5% | 99.9% |

The more centres, the better the inner ring can be enclosed; $k=16$ is already nearly all right.

Figure `lec05-kp16-ringsk`: First see that the horizontal axis is the number of centres $k$ and the vertical axis the new-point accuracy; then that the curve climbs fast near $k=8$ and approaches 100% for $k\ge16$. [Function: 3]

![Accuracy against the number of centres k (concentric rings, random centres).](../../assets/figures/lec05-kp16-ringsk.png)

### 6. How to choose the centres

- **Clustering** (here k-means): first split the data into $k$ groups, take the mean of each group as a centre, then learn $w$ by supervised least squares; a mix of unsupervised and supervised learning.

**Experiment setting** (designed for this lecture, reproducible):

- Data: two half-moons. Class A takes the upper half circle $(\cos t,\sin t)$, class B the shifted lower half circle $(1-\cos t,\ 0.5-\sin t)$, $t$ uniform in $[0,\pi]$; each gets Gaussian noise with standard deviation 0.2. 60 points per class, 120 training points (seed 0); new points: 500 per class, 1000 in all (seed 1).
- Model: $2\sigma^2=0.6$ (that is, $\sigma^2=0.3$). Random centres: $k$ training points picked at random; k-means: 50 rounds, with the initial centres also $k$ randomly picked points.
- Repetition: for each $k$ once with each seed 0 to 19 (20 times), averaged.

| $k$ | random centres | k-means |
|---|---:|---:|
| 2 | 76.3% | 73.5% |
| 4 | 84.4% | 83.1% |
| 6 | 90.5% | 92.7% |
| 8 | 93.3% (standard deviation 0.018) | 95.0% (0.004) |
| 12 | 94.9% | 95.2% |

**Common misconception**: clustering is always more accurate than random. For $k=2,4$ random is slightly higher; for $k\ge6$ clustering is higher, but the main difference is that it is steadier (a smaller standard deviation).

Figure `lec05-kp16-centers`: First look at the two curves: random centres and k-means centres, with $k$ on the horizontal axis; then compare the gap at $k=6,8$ and the reversed order at $k=2,4$. [Function: 3]

![New-point accuracy of random and k-means centres.](../../assets/figures/lec05-kp16-centers.png)

### 7. The cost of locality

- **Curse of dimensionality**: as the dimension rises, the number of points or centres needed to fill the space grows exponentially, while data and centres are never enough.

**Experiment setting** (designed for this lecture, reproducible):

- Put 100 centres uniformly at random in the unit cube $[0,1]^l$, then draw 2000 test points; random numbers from `default_rng(0)`, used in sequence for $l=1,2,5,10,20$.
- Gaussian width $\sigma=0.3$; response $=\exp(-d^2/(2\sigma^2))$, where $d$ is the distance from the test point to the nearest centre.

| input dimension $l$ | 2 | 5 | 10 | 20 |
|---|---:|---:|---:|---:|
| median distance to the nearest centre | 0.05 | 0.30 | 0.67 | 1.22 |
| test points with response above 0.1 | 100% | 100% | 40% | 0% |

For comparison, a grid with 5 centres per axis needs $5^l=25$, 3125, 9,765,625 centres for $l=2,5,10$.

Figure `lec05-kp16-curse`: First see that the horizontal axis is the dimension $l$ and the vertical axis the "fraction of test points with response above 0.1"; then that the curve is near 100% for small $l$, drops to 40% at $l=10$ and to 0 at $l=20$. [Function: 3]

![Fraction of test points with response above 0.1 against dimension l.](../../assets/figures/lec05-kp16-curse.png)

### 8. MLP versus RBF

| Item | MLP | RBF network |
|---|---|---|
| argument of a node | $\sum_jw_jx_j$ | $\|x-c_i\|$ |
| equal-output set | hyperplane | hypersphere |
| response | global | local |
| learning speed | slower | faster |
| generalization where training data is sparse | better | worse |
| nodes needed for the same performance | fewer | many more |

(The comparison follows the source.)

**How to remember**: the MLP thinks "which side of a hyperplane", the RBF thinks "how close to a centre"; local learns fast, but eats dimensions.

### Extension: other choices, exercises and worked solutions

**Other ways to choose the centres** (source):

| Method | What it does |
|---|---|
| fixed centres | pick training points at random |
| trained centres | $w_i,c_i,\sigma_i$ all by gradient descent, expensive |
| clustering | k-means, group means as centres |
| orthogonal least squares | start from a large set of candidates, pick a compact set of centres by forward regression, and estimate $k$ on the way |
| support vectors | see the RBF network as a kernel mapping; training is quadratic programming with a guaranteed global optimum, and the number of centres is set automatically |
| growing | a new sample far from all centres and with a large error becomes a new centre |

**Small exercises**: $c_1=(1,1)$, $c_2=(0,0)$, $y_i=\exp(-\|x-c_i\|^2)$, $g=y_1+y_2-1$ ($g>0$ is $\omega_1$).

1. Map $(0.5,0.5)$ to $y$ and decide its class. Hint: both squared distances to the centres are 0.5.
2. Do the same for the far point $(3,3)$.

**Exercise 1, worked solution**: $y=(e^{-0.5},e^{-0.5})=(0.607,0.607)$, $g=0.607+0.607-1=+0.213>0$, so $\omega_1$.

**Exercise 2, worked solution**: the squared distances to $c_1$ and $c_2$ are $8$ and $18$, $y=(0.0003,\ 1.5\times10^{-8})$, $g\approx-1.0<0$, so $\omega_2$.

**Check**: the middle point lies between the two centres and is enclosed in the curve; the far point falls to the bias $-1$ and goes to the default class.

## Terms and source

| 中文 | English |
|---|---|
| 徑向基函數 | Radial basis function |
| 局部反應 | Local response |
| 固定中心 | Fixed centres |
| 分群 | Clustering |
| 維度詛咒 | Curse of dimensionality |

Source: Chapter 4 KP16, §4.15 (read 2026-10-25). The form of the RBF, the relation to Parzen, the local-versus-global comparison table, the two XOR centres and the numbers 0.135 and 0.368, the centre-selection methods and "how to remember" follow the source; the centre-count experiment on rings and half-moons, the random-versus-k-means comparison and the dimension experiment on locality were designed and recomputed for this lecture ([Supplement], computed by a program).
