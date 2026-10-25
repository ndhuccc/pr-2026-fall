# KP01 XOR and the limit of one line

> Level: undergraduate (year 3)
>
> Pattern Recognition | Chapter 4, Sections 4.1 to 4.2

[Slides (view and download)](../../slides/lec05-kp01-xor-en.jbd.json) | [中文版](../lec05-kp01-xor.md)

## Learning objectives

- Turn the truth tables of OR, AND and XOR into classification problems in the plane.
- Compute each prediction from a score and a fixed rule, and check it against the label.
- Use the sums of two A scores and of two B scores to prove that one line cannot separate XOR, and tell a representational limit from a training problem.

## KP01 XOR and the limit of one line

**One-sentence summary**: For the same four points one line separates OR and AND but not XOR: the two A scores must sum to a positive number and the two B scores to at most 0, yet it is the same expression; more training cannot fix it, so what must change is the combination of boundaries.

### 1. Same four points, new labels: is one line enough?

**Plain explanation**: Chapter 3 let the model decide the class with one line. Here we keep the model and only change the labels of four points, to see whether it can still answer.

- **Label**: the class a point must be assigned to: A (circle, output 1) or B (square, output 0).
- **XOR (exclusive or)**: the output is 1 (A) only when the two inputs differ, and 0 (B) when they match. OR outputs 1 when at least one input is 1, and AND when both inputs are 1.

Figure `lec05-kp01-three-labels`: The four inputs are $(0,0),(0,1),(1,0),(1,1)$, each input being 0 or 1. The three panels use the same coordinates with different labels; under each is the output in that order: OR 0111, AND 0001, XOR 0110.

![Three labellings](../../assets/figures/lec05-kp01-three-labels.png)

For OR the class A occupies three corners and for AND only the upper-right corner, so one line seems enough; XOR puts each class on a diagonal, and we are not sure.

### 2. Give every point a score: positive means class A

**Formal definition**: We consider binary inputs and two classes. The score with a constant term and the prediction rule are (strictly this is an affine function, but by convention the classifier is still called linear):

$$
g(\mathbf{x})=w_1x_1+w_2x_2+w_0,\qquad
\widehat y(\mathbf{x})=\begin{cases}1\;(A),&g(\mathbf{x})>0,\\0\;(B),&g(\mathbf{x})\le0.\end{cases}
$$

$w_1,w_2$ are coefficients and $w_0$ is a constant that shifts the line. A positive score gives class A and anything else gives B, including exactly 0; the tie rule must not depend on the true label. The set $g=0$ is the line in the figure.

**Linearly separable**: some coefficients classify every point correctly by this rule. What matters is that such coefficients exist, not only how the current ones perform.

**Example**: For OR take $w_1=w_2=1,\ w_0=-0.5$, that is $g=x_1+x_2-0.5$. The four scores are $-0.5, 0.5, 0.5, 1.5$; the last three are positive, so they are class A, exactly OR.

![OR and its boundary](../../assets/figures/lec05-kp01-or-line.png)

Figure `lec05-kp01-or-line`: Look at the boundary $x_1+x_2=0.5$ first and then at the tinted positive side (arrow); each point shows its score, and all three A points are on the positive side.

### 3. The same line: OR all right, XOR one wrong

Use the same line on XOR and substitute each point into the same $g=x_1+x_2-0.5$:

| Input | Substitution | Score | Prediction | XOR truth |
|---|---|---:|---|---|
| $(0,0)$ | $0+0-0.5$ | $-0.5$ | B | B |
| $(0,1)$ | $0+1-0.5$ | $0.5$ | A | A |
| $(1,0)$ | $1+0-0.5$ | $0.5$ | A | A |
| $(1,1)$ | $1+1-0.5$ | $1.5$ | A | B ✗ |

The predictions equal OR; for XOR one point is wrong:

$$
\text{accuracy}=\frac{3}{4}=0.75=75\%,\qquad 75\%+25\%=100\%\ \text{(check)}.
$$

This is the result of one line only and does not rule out other lines.

![XOR with the same line](../../assets/figures/lec05-kp01-xor-check.png)

### 4. Three other lines: 2, 3 and 1 errors

![Three candidate lines](../../assets/figures/lec05-kp01-attempts.png)

| Score | Predictions (in the order $(0,0),(0,1),(1,0),(1,1)$) | Errors |
|---|---|---:|
| $x_1-0.5$ | $(0,0,1,1)$ | 2 |
| $x_1+x_2-1.5$ | $(0,0,0,1)$ | 3 |
| $x_1-x_2$ | $(0,0,1,0)$ | 1 |

The second line cuts off only the upper-right corner, but that side is predicted A, so the errors are two A points and one B point. On the third line $x_1=x_2$ two points have score 0 and are predicted B by the rule. Three failed lines are **not a proof**: there are too many lines we did not try.

### 5. The two A scores must add up to a positive number

To rule out every line at once, assume some $w_1,w_2,w_0$ classify all of XOR correctly and write down what they must satisfy. For the two A points:

$$
g(0,1)=w_2+w_0>0,\qquad g(1,0)=w_1+w_0>0.
$$

Positive plus positive is positive, so adding the two gives:

$$
(w_2+w_0)+(w_1+w_0)=w_1+w_2+2w_0>0.
$$

Geometrically the two A points form a diagonal with midpoint $M=(\tfrac12,\tfrac12)$. Since $g$ is linear, $g(M)=\frac{w_1+w_2+2w_0}{2}$ is exactly the average of the two scores and is positive too.

![The A diagonal and its midpoint](../../assets/figures/lec05-kp01-diag-a.png)

### 6. The B scores add up to at most 0: a contradiction

For the two B points the scores must be at most 0 (by the fixed rule):

$$
g(0,0)=w_0\le0,\qquad g(1,1)=w_1+w_2+w_0\le0.
$$

A sum of at most 0 numbers cannot be positive:

$$
w_0+(w_1+w_2+w_0)=w_1+w_2+2w_0\le0.
$$

Both sums are the **same expression**; A demands that it be greater than 0 and B that it be at most 0, a contradiction. Hence no coefficients classify every point correctly: this rules out every line, not just the plotted candidates. Geometrically the two diagonals share the midpoint $M$: $g(M)$ would be the average of the A scores and also the average of the B scores, impossible to be both positive and at most 0.

![The diagonals share a midpoint](../../assets/figures/lec05-kp01-diag-both.png)

### 7. However it is trained, no single line classifies XOR perfectly

**Common misconception**: More iterations, a smaller learning rate or a new initialization should eventually get everything right. These only search the same family of lines for fewer errors, with no guarantee of finding the best one; they can turn 3 errors into 1, but that family has no perfect answer, so the lowest error is 1, not 0.

**Representational capacity**: whether the shape of the boundary can express the answer at all. Whether training finds the best line and whether the best line is good enough are different questions.

![Errors against training](../../assets/figures/lec05-kp01-best.png)

Figure `lec05-kp01-best`: This is a schematic, not an experiment; the dashed line is 0, which is never reached.

### 8. Change the boundaries: two lines make a strip

The proof rules out a single linear score with a fixed threshold, not combinations of boundaries. [Added] Let $s=x_1+x_2$. The four XOR points have $s=0,1,2$ and A is exactly $s=1$, so the intersection of two decisions selects it:

$$
\widehat y=1\quad\Longleftrightarrow\quad 0.5<s\le1.5.
$$

![The strip between two lines](../../assets/figures/lec05-kp01-strip.png)

Figure `lec05-kp01-strip`: Two parallel lines enclose a slanted strip with both A points inside and both B points outside. This verifies only the four Boolean points and does not define a unique extension of XOR to the continuous plane.

What changes is the combination of boundaries a model may use, not another choice of old coefficients. The next KP asks how neurons can carry out these two decisions.

### Extension: practice and implementation

**Code**: Compute each score, predict with "score > 0" and compare with the true labels. Include boundary points in tests so that code and text use the same inequality. The half-integers here are exactly representable; general real data still need care with floating-point errors.

![Points on the boundary](../../assets/figures/lec05-kp01-ties.png)

**Practice**:

1. Compute the four inputs with $g=x_1+x_2-1.5$ and check AND and XOR separately. Hint: compute the scores, apply the same rule $g>0$, and only then compare the two sets of labels.
2. Is XOR failing because of few samples, noise, learning rate, or the restricted boundary shape? Hint: which does the contradiction rule out?
3. Which of OR, XOR and XNOR is separable by one line? XNOR outputs 1 when the inputs match. Hint: draw the labels first.

**Worked solution (question 1)**: ① Formula $g=x_1+x_2-1.5$, class A if $g>0$. ② Substitute the four points $(0,0),(0,1),(1,0),(1,1)$: the scores are $-1.5, -0.5, -0.5, 0.5$. ③ Only $(1,1)$ is positive, so the predictions are B, B, B, A. ④ Check: AND is B, B, B, A, all correct; for XOR the points $(0,1)$ and $(1,0)$ are predicted B and $(1,1)$ is predicted A, 3 errors.

![AND and XOR](../../assets/figures/lec05-kp01-and-xor.png)

## Terminology and source

| Term | Meaning |
|---|---|
| Label | the class a point must be assigned to |
| XOR | output 1 only when the two inputs differ |
| Score, constant | the number $g$ obtained by substitution; the term that shifts the line |
| Linearly separable | some coefficients classify every point correctly |
| Representational capacity | whether the boundary shape can express the answer |

Source: Chapter 4, KP01, Sections 4.1 to 4.2, accessed 2026-10-24. The four points, parameters and demonstrations follow the source; the explanations and figures are newly written; the strip condition of two boundaries and the midpoint proof are [Added].
