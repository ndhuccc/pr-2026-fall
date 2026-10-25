# KP16 RBF Networks

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.15

[Slides: read and download](../../slides/lec05-kp16-rbf-en.jbd.json) | [中文版](../lec05-kp16-rbf.md)

## Learning objectives

- Write the form of an RBF network and explain local against global response.
- Solve XOR with two centres and relate the line in the feature space to the closed curve in the original space.
- Explain how centres are chosen, the dimension price of locality and the contrast between the MLP and the RBF.

## KP16 RBF Networks

**One-sentence summary**: Replace the interpolation function by a function of the distance to a centre so that every node responds only to data near itself; locality makes it learn fast and also forces it to fill the space with many centres, hungry for dimensions.

### 1. Gaussian nodes

**Plain explanation**: The products of KP15 respond over the whole space. Can the new coordinates be nodes that respond only to data nearby?

- **Radial basis function** (RBF): a function of the distance to a centre $c_i$, most often Gaussian.

**Formal definition** (the RBF network):

$$
g(x)=w_0+\sum_{i=1}^{k}w_i\exp\!\Big(-\frac{\|x-c_i\|^2}{2\sigma_i^2}\Big),
$$

one layer of Gaussian hidden nodes and a linear output. It is close kin of the Parzen estimate, almost the same form, but Parzen uses one kernel per training point ($k=N$) while here $k\ll N$.

Figure `lec05-kp16-bumps`: top, one sigmoid answers along the whole line; bottom, three Gaussians each answer near their centre.

![Gaussian nodes](../../assets/figures/lec05-kp16-bumps.png)

### 2. Local against global

**Local response**: a node answers only near its centre and fades to 0 away from it; a **global response** instead follows a whole hyperplane. The equal-output set of a sigmoid node is a hyperplane (a line in two dimensions); that of an RBF node is a hypersphere (a circle). **Example** ($2\sigma^2=1$): at distances 0, 1, 2, 3 from the centre the Gaussian answers $1,0.368,0.0183,0.000123$.

Figure `lec05-kp16-contours`: left the equal-output lines of a sigmoid, right the concentric circles of an RBF.

![Local against global](../../assets/figures/lec05-kp16-contours.png)

### 3. XOR needs only two centres

$k=2$, $c_1=(1,1)$, $c_2=(0,0)$ and $f(x)=\exp(-\|x-c\|^2)$: $(0,0)\to(0.135,1)$, $(1,1)\to(1,0.135)$, and both $(1,0)$ and $(0,1)$ go to $(0.368,0.368)$, folded onto one point again. $g(y)=y_1+y_2-1$ gives $+0.135$ for the first two points and $-0.264$ for the other two, so one line separates them.

Figure `lec05-kp16-xormap`: the input plane (centres as stars) and the feature plane after the map.

![XOR with two centres](../../assets/figures/lec05-kp16-xormap.png)

### 4. Back in the original space

$g(x)=e^{-\|x-c_1\|^2}+e^{-\|x-c_2\|^2}-1=0$ is a closed curve around the two centres. The values of $g$: $+0.135$ at $(0,0)$ and $(1,1)$ (inside the curve) and $-0.264$ at $(1,0)$ and $(0,1)$ (outside). Far from every centre $g\to-1$, so faraway points all fall on the outside class, a property of local response.

Figure `lec05-kp16-xorcurve`: the decision curve and the four points on the original plane.

![Closed curve](../../assets/figures/lec05-kp16-xorcurve.png)

### 5. Fixed centres

**Fixed centres**: pick $k$ training points at random as the centres; with the centres fixed only $w$ remains, the linear problem of KP13 (least squares). **Example** (designed here): concentric rings (radii about 1 and 2.2), 200 training and 500 held-out new points, $\sigma^2=0.5$, averaged over 20 random choices for each $k$. Accuracy on new points: $k=2$ gives 64.2%, $k=8$ gives 91.5%, $k=16$ gives 99.5% and $k=32$ gives 99.9%.

Figure `lec05-kp16-ringsk`: accuracy against the number of centres $k$.

![Number of centres](../../assets/figures/lec05-kp16-ringsk.png)

### 6. Choosing the centres

**Clustering** (k-means here): split the data into $k$ groups, use each group mean as a centre and then learn $w$ with supervised least squares, a mix of unsupervised and supervised learning. **Example** (designed here): two moons of 60 points each with noise, 500 new points, $\sigma^2=0.3$, 20 repeats each. Accuracy on new points: $k=6$: 90.5% against 92.7%; $k=8$: 93.3% (sd 0.018) against 95.0% (0.004); at $k=2,4$ random is slightly higher. **Common misconception**: clustering is always more accurate than random picks. It is mainly steadier.

Figure `lec05-kp16-centers`: accuracy on new points for random and k-means centres.

![Choosing the centres](../../assets/figures/lec05-kp16-centers.png)

### 7. The price of locality

**Curse of dimensionality**: as the dimension grows the number of points or centres needed to fill the space grows exponentially, while the data and the centres are never enough. **Example** (designed here): $l$ is the input dimension; 100 random centres in the unit cube, $\sigma=0.3$ and 2000 test points; the median distance to the nearest centre for $l=2,5,10,20$ is $0.05,0.30,0.67,1.22$. Test points with a response above 0.1: 100% for $l\le5$, 40% for $l=10$ and 0% for $l=20$. A grid of 5 centres per axis needs 25, 3125 and 9,765,625 centres ($l=2,5,10$).

Figure `lec05-kp16-curse`: the fraction of test points with a response above 0.1.

![Price of locality](../../assets/figures/lec05-kp16-curse.png)

### 8. MLP against RBF

The MLP node is $\sum_jw_jx_j$ with hyperplanes and a global response; the RBF is $\|x-c_i\|$ with hyperspheres and a local one. The RBF learns faster; the MLP generalizes better where training data are sparse; for the same accuracy the RBF needs many more nodes (source). **To remember**: the MLP thinks in terms of which side of a hyperplane, the RBF in terms of how close to a centre; local learns fast but is hungry for dimensions.

Figure `lec05-kp16-compare`: comparison table of the MLP and the RBF network.

![Comparison table](../../assets/figures/lec05-kp16-compare.png)

### Extension: other ways, practice and worked solution

**Other ways to choose the centres** (source): train the centres ($w_i,c_i,\sigma_i$ all by gradient descent, costly); orthogonal least squares (start from many candidates and pick a compact set by forward regression, which also estimates $k$); support vectors (view the RBF network as a kernel map; training is a quadratic programme with a global optimum and the number of centres decided automatically); growing (a new sample far from every centre with a large error becomes a new centre).

Figure `lec05-kp16-ways`: the six ways to choose the centres.

![Six ways](../../assets/figures/lec05-kp16-ways.png)

**Practice**: $c_1=(1,1)$, $c_2=(0,0)$, $f=\exp(-\|x-c\|^2)$ and $g=y_1+y_2-1$ ($g>0$ is $\omega_1$).

1. Map $(0.5,0.5)$ to $y$ and find its class. Hint: its squared distance to both centres is 0.5.
2. Do the same for the faraway point $(3,3)$.

Figure `lec05-kp16-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp16-practice.png)

**Worked solution of questions 1 and 2**: (1) $y=(e^{-0.5},e^{-0.5})=(0.607,0.607)$ and $g=0.607+0.607-1=+0.213>0$, so $\omega_1$. (2) The squared distances 8 and 18 give $y=(0.0003,1.5\times10^{-8})$ and $g\approx-1.0<0$, so $\omega_2$. (3) Check: the middle point lies between the centres, inside the curve; the faraway point falls to the bias $-1$ and takes the default class.

Figure `lec05-kp16-practice-sol`: the maps and $g$ of the two points.

![Practice solution](../../assets/figures/lec05-kp16-practice-sol.png)

## Terms and sources

| English | 中文 |
|---|---|
| Radial basis function | 徑向基函數 |
| Local response | 局部反應 |
| Fixed centres | 固定中心 |
| Clustering | 分群 |
| Curse of dimensionality | 維度詛咒 |

Source: Chapter 4 KP16, §4.15 (read 2026-10-25). The RBF form, its kinship with Parzen, the local-against-global comparison table, the two centres for XOR with 0.135 and 0.368, the centre-selection methods and the "to remember" line follow the source; the experiments on the number of centres for rings and moons, the random against k-means comparison and the dimension experiment on locality were designed and recomputed for this lecture ([added], (program)).
