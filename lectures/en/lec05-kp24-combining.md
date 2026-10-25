# KP24 Combining Classifiers: Product, Sum, Majority Vote and the Bayesian View

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.21

[Slides: read and download](../../slides/lec05-kp24-combining-en.jbd.json) | [中文版](../lec05-kp24-combining.md)

## Learning objectives

- Explain the value of combining classifiers (complementary information) and write the product and sum rules with their KL derivations.
- Explain the majority-vote formula, why independence is an illusion and the three ways to create diversity.
- Explain the one-vote veto of the product rule and the Bayesian view, and know that no rule is always best.

## KP24 Combining Classifiers: Product, Sum, Majority Vote and the Bayesian View

**One-sentence summary**: Even the best classifier errs on samples that others get right; complementary information is the whole value of combining. But combining does not guarantee a gain and there is no panacea.

### 1. Complementary information

**Plain explanation**: What is there to gain by combining classifiers?

**Example** (designed here): logistic, a depth-4 tree and 3-NN on noisy half-moons (100 training points per class, 2000 new points in all): 85.2%, 82.6% and 87.8% on new points. The best, 3-NN, is wrong on 12.2%, and for 60% of those at least one other classifier is right. But the vote of the three gets only 86.2%, below the 87.8% of 3-NN; complementary information must be mined to be worth anything.

Figure `lec05-kp24-comp`: the accuracies of three classifiers and the share of complementary errors.

![Complementary information](../../assets/figures/lec05-kp24-comp.png)

### 2. The product rule

**KL distance** $D=\sum_iP\ln(P/P_j)$: how far apart two probability distributions are; asymmetric, so strictly not a distance. The **product rule** (formal definition): minimizing $\tfrac1L\sum_jD_j$ gives

$$
P(\omega_i|x)=\frac1C\prod_{j=1}^{L}P_j(\omega_i|x)^{1/L},
$$

and the class with the largest product is chosen. **Example**: two classes, three classifiers $(0.8,0.2)$, $(0.6,0.4)$, $(0.7,0.3)$: products 0.336 against 0.024, so $\omega_1$.

Figure `lec05-kp24-prod`: the product rule and the example.

![The product rule](../../assets/figures/lec05-kp24-prod.png)

### 3. The sum rule

**Sum rule**: swap the two arguments of $D_j$ ($P_j$ first) and the optimum is $P(\omega_i|x)=\tfrac1L\sum_jP_j(\omega_i|x)$, the arithmetic mean. For the same three classifiers: means 0.70 against 0.30, also $\omega_1$. Each rule has a rigorous information-theoretic origin; there is no theoretical preference, and in practice the product is clean but fragile when an output is near zero, and in practice the sum is often safer (source [Mill 99]).

Figure `lec05-kp24-sum`: the sum rule and the example.

![The sum rule](../../assets/figures/lec05-kp24-sum.png)

### 4. The veto

**Example** (designed here): five classifiers give the correct class $\omega_1$ the values 0.7, 0.7, 0.7, 0.7, 0.001 (the rest to $\omega_2$). The product gives $\omega_1$ 0.00024 against $\omega_2$ 0.00809, wrong; the sum 0.5602 against 0.4398, right; the vote is 4 to 1, right. A single near-zero factor drags the whole product to zero, a one-vote veto.

Figure `lec05-kp24-veto`: the outputs of five classifiers and the result of three rules.

![The veto](../../assets/figures/lec05-kp24-veto.png)

### 5. Majority vote

**Majority vote**: decide only if at least $l_c$ classifiers agree ($l_c=\tfrac{L+1}2$ for odd $L$); otherwise reject. For independent decisions with equal accuracy $p$,

$$
P_c(L)=\sum_{m=l_c}^{L}\binom Lm p^m(1-p)^{L-m}.
$$

$p=0.6$: $L=3$: 0.648, $L=11$: 0.754, $L=51$: 0.927; $p=0.55$: $L=51$: 0.764; $p=0.45$: $L=51$: 0.236; $p=0.5$ stays 0.5.

Figure `lec05-kp24-vote`: $P_c(L)$ against $L$.

![Majority vote](../../assets/figures/lec05-kp24-vote.png)

### 6. The independence illusion

**Example** (designed here): the half-moon data of KP23, 20 training sets, 25 bagged trees each, 2000 new points. A single tree gets 83.8% on average; the independence formula $P_c(25,p)$ gives 99.99%; the real majority vote 87.7%; the share of member decisions differing from the majority is $V=0.095$. The trees are trained on resamples of the same data, so their mistakes are strongly shared. **Common misconception**: as long as every classifier beats guessing the vote tends to 100%; this relies on independence, which fails in practice and the more so the larger $L$ (source).

Figure `lec05-kp24-indep`: a single tree, the independence formula and the real vote.

![The independence illusion](../../assets/figures/lec05-kp24-indep.png)

### 7. Creating diversity

**Diversity**: how much the members' decisions differ; one measure is $V$, the share of member decisions that differ from the majority. Three ways (source): the same feature space with different data points (bootstrap, most effective for unstable trees); different classifier types; different feature subspaces. **Experiment** (designed here, 10-D, 150 points, 15 runs): one tree 71.2%; 11 bootstrap trees 77.9±2.1% ($V=0.197$); 11 random-subset trees 75.9±2.3% (0.241); 5 classifiers 82.1±1.2% (0.114). The ensemble with the largest $V$ is not the most accurate, and the 5 classifiers include logistic regression, which happens to suit this data, so we cannot conclude that different classifiers are always better.

Figure `lec05-kp24-div`: the vote accuracy and $V$ of three ensemble types.

![Creating diversity](../../assets/figures/lec05-kp24-div.png)

### 8. The Bayesian view and how to remember

Assuming independent $x_j$ gives $\max_kP(\omega_k)^{1-L}\prod_jP(\omega_k|x_j)$: the product rule again, but very sensitive to errors in the posterior estimates; the sum tolerates errors better and often beats the product in practice (source [Kitt 98]). The source's handwritten-digit experiments: no rule is always best; in some cases the combination is worse than the best single classifier; combining one classifier on different feature sets works best (our random subsets on page 7 did worst). Page 1 agrees: the vote gets 86.2%, below 87.8%. **To remember**: the sum and the majority vote are the most used; there is no panacea theorem.

Figure `lec05-kp24-bayes`: the Bayesian view and the trade-offs of the three rules.

![The Bayesian view](../../assets/figures/lec05-kp24-bayes.png)

### Extension: the median, practice and worked solution

**The median** (designed here): five classifiers give $\omega_1$: 0.80, 0.85, 0.75, 0.01, 0.01. The sum gives 0.484 against 0.516, wrong; the product $5.1\times10^{-5}$ against $7.4\times10^{-3}$, wrong; the median 0.75 against 0.25, right. With outlying outputs the sum is pulled away while the median holds; the source also mentions max, min and median, motivated by the chain product ≤ min ≤ mean ≤ max.

Figure `lec05-kp24-median`: the three rules with two extreme outputs.

![The median](../../assets/figures/lec05-kp24-median.png)

**Practice**: every classifier is right with probability $p=0.7$, decisions are independent and the majority vote has odd $L$.

1. What is the accuracy $P_c(3)$ for $L=3$?
2. What is the accuracy $P_c(5)$ for $L=5$, and how much more than for $L=3$?

Figure `lec05-kp24-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp24-practice.png)

**Worked solution of questions 1 and 2**: (1) $l_c=2$: $3\cdot0.7^2\cdot0.3+0.7^3=0.441+0.343=0.784$. (2) $l_c=3$: $10\cdot0.7^3\cdot0.3^2+5\cdot0.7^4\cdot0.3+0.7^5=0.3087+0.36015+0.16807=0.837$, 0.053 more than for $L=3$. (3) Check: $0.7\to0.784\to0.837$ rises monotonically (under independence); real dependent classifiers do not rise this much.

Figure `lec05-kp24-practice-sol`: the computation.

![Practice solution](../../assets/figures/lec05-kp24-practice-sol.png)

## Terms and source

| 中文 | English |
|---|---|
| KL 距離 | KL distance |
| 乘積規則 | Product rule |
| 加總規則 | Sum rule |
| 多數投票 | Majority vote |
| 多樣性 | Diversity |

Source: Chapter 4, KP24, §4.21 (read 2026-10-25). Complementary information, the KL derivations of the product and sum rules, the majority vote and the independence assumption, the three ways to create diversity, the measure $V$, the Bayesian view, the conclusions of the Jain 00 experiments and no panacea follow the source; the three-classifier comparison, the veto example, the independence experiment, the diversity experiment, the median example and the practice were designed and recomputed for this lecture ([added], (program-computed)).
