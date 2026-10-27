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

### Prerequisites and symbols

**Three things you need first**:

- **Linear classifier** (Chapter 3): separate two classes with a straight line; one side is assigned to one class and the other side to the other.
- **Score**: the number obtained by putting a point into the line's formula; its sign says which side of the line the point is on.
- **Truth table**: lists the output for each input combination; here there are only the four inputs $(0,0),(0,1),(1,0),(1,1)$.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $x_1,x_2$ | the two coordinates of the input | each 0 or 1 |
| $g(\mathbf x)$ | score | $g=w_1x_1+w_2x_2+w_0$ |
| $w_1,w_2,w_0$ | coefficients and constant | the constant shifts the line up or down |
| $\widehat y$ | prediction | 1 means A, 0 means B |
| $s$ | $x_1+x_2$ | used in section 8 |
| A, B | the two classes | A outputs 1 (circle), B outputs 0 (square) |

### 1. Same four points, new labels: is one line enough?

**Plain explanation**: Chapter 3 let the model decide the class with one line. Here we keep the model and only change the labels of four points, to see whether it can still answer.

- **Label**: the class a point must be assigned to: A (circle, output 1) or B (square, output 0).
- **XOR (exclusive or)**: the output is 1 (A) only when the two inputs differ, and 0 (B) when they match. OR outputs 1 when at least one input is 1, and AND when both inputs are 1.

Figure `lec05-kp01-three-labels`: First see the coordinates of the three panels, which are identical; then see the outputs below each panel, where only the labels differ. The four inputs are (0,0), (0,1), (1,0), (1,1). The panels use the same coordinates and differ only in labels; below each panel are the outputs in order: OR is 0111, AND is 0001, XOR is 0110. [Function: 1]

![Three labelings of the same four points: OR outputs 0111, AND outputs 0001, XOR outputs 0110.](../../assets/figures/lec05-kp01-three-labels-en.png)

For OR the class A occupies three corners and for AND only the upper-right corner, so one line seems enough; XOR puts each class on a diagonal, and we are not sure. The next question: how does one line give scores and decide the class? First the rule must be stated clearly.

### 2. Give every point a score: positive means class A

**Formal definition**: We consider binary inputs and two classes. The score with a constant term and the prediction rule are (strictly this is an affine function, but by convention the classifier is still called linear):

$$
g(\mathbf{x})=w_1x_1+w_2x_2+w_0,\qquad
\widehat y(\mathbf{x})=\begin{cases}1\;(A),&g(\mathbf{x})>0,\\0\;(B),&g(\mathbf{x})\le0.\end{cases}
$$

$w_1,w_2$ are coefficients and $w_0$ is a constant that shifts the line. A positive score gives class A and anything else gives B, including exactly 0; the tie rule must not depend on the true label. The set $g=0$ is the line in the figure.

**Linearly separable**: some coefficients classify every point correctly by this rule. What matters is that such coefficients exist, not only how the current ones perform.

**Example**: For OR take $w_1=w_2=1,\ w_0=-0.5$, that is $g=x_1+x_2-0.5$. The four scores are $-0.5, 0.5, 0.5, 1.5$; the last three are positive, so they are class A, exactly OR.

Figure `lec05-kp01-or-line`: First see the boundary x1 + x2 = 0.5, then the blue positive side; each point is marked with its score -0.5, 0.5, 0.5, 1.5, and the three A points lie on the positive side. [Function: 1, 3]

![The OR boundary x1 + x2 = 0.5: the four scores are -0.5, 0.5, 0.5, 1.5 and the three A points are on the positive side.](../../assets/figures/lec05-kp01-or-line-en.png)

The next question: what happens when the same line is used on XOR?

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

Figure `lec05-kp01-xor-check`: First see the table on the left: the same g on the four points predicts B, A, A, A and (1, 1) is wrong; then see the grey line on the right, which puts (0,1), (1,0) and (1,1) on the same side although (1,1) is B. [Function: 1, 3]

![The same line g = x1 + x2 - 0.5 on XOR: scores -0.5, 0.5, 0.5, 1.5, one error, accuracy 3/4 = 75%.](../../assets/figures/lec05-kp01-xor-check-en.png)

The next question: would another line do better?

### 4. Three other lines: 2, 3 and 1 errors

Figure `lec05-kp01-attempts`: First see where each of the three lines lies, then the red rings on each plot: the wrong points number 2, 3 and 1. [Function: 1]

![Three candidate lines x1 - 0.5, x1 + x2 - 1.5, x1 - x2 get 2, 3 and 1 XOR points wrong.](../../assets/figures/lec05-kp01-attempts-en.png)

| Score | Predictions (in the order $(0,0),(0,1),(1,0),(1,1)$) | Errors |
|---|---|---:|
| $x_1-0.5$ | $(0,0,1,1)$ | 2 |
| $x_1+x_2-1.5$ | $(0,0,0,1)$ | 3 |
| $x_1-x_2$ | $(0,0,1,0)$ | 1 |

- The first line $x_1=0.5$ predicts the right side as A: $(0,1)$ is A but predicted B and $(1,1)$ is B but predicted A, 2 errors.
- The second line $x_1+x_2=1.5$ cuts off only the upper-right corner, but that side is predicted A, so the errors are two A points and one B point.
- On the third line $x_1=x_2$ two points have score 0 and are predicted B by the rule.

Three failed lines are **not a proof**: there are too many lines we did not try. The next question: how can every line be ruled out at once?

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

Figure `lec05-kp01-diag-a`: First see the diagonal joining the two A points, then its midpoint M; g(M) is the average of the end scores and so is positive. [Function: 2, 3]

![The diagonal joining the two A points and its midpoint M = (1/2, 1/2); g(0,1) > 0 and g(1,0) > 0 give w1 + w2 + 2w0 > 0 and g(M) > 0.](../../assets/figures/lec05-kp01-diag-a-en.png)

The next question: what condition do the two B points give?

### 6. The B scores add up to at most 0: a contradiction

For the two B points the scores must be at most 0 (by the fixed rule):

$$
g(0,0)=w_0\le0,\qquad g(1,1)=w_1+w_2+w_0\le0.
$$

Numbers that are at most 0 cannot add up to a positive number:

$$
w_0+(w_1+w_2+w_0)=w_1+w_2+2w_0\le0.
$$

Both sums are the **same expression**; A demands that it be greater than 0 and B that it be at most 0, a contradiction. Hence no coefficients classify every point correctly: this rules out every line, not just the plotted candidates. Geometrically the two diagonals share the midpoint $M$: $g(M)$ would be the average of the A scores and also the average of the B scores, impossible to be both positive and at most 0.

Figure `lec05-kp01-diag-both`: First see the two diagonals, then that they cross at the same midpoint M; A requires w1 + w2 + 2w0 > 0 and B requires it to be <= 0, so g(M) cannot be positive and at most 0 at once. [Function: 2, 3]

![Both diagonals share the midpoint M: A requires w1 + w2 + 2w0 > 0 and B requires <= 0, a contradiction.](../../assets/figures/lec05-kp01-diag-both-en.png)

The next question: if every line fails, does more training help?

### 7. However it is trained, no single line classifies XOR perfectly

**Common misconception**: More iterations, a smaller learning rate or a new initialization should eventually get everything right. These only search the same family of lines for fewer errors, with no guarantee of finding the best one; they can turn 3 errors into 1, but that family has no perfect answer, so the lowest error is 1, not 0.

**Representational capacity**: whether the shape of the boundary can express the answer at all. Whether training finds the best line and whether the best line is good enough are different questions.

Figure `lec05-kp01-best`: This is a schematic, not a real experiment. First see the errors fall with training, then the dashed 0: it is never reached; the right side explains that capacity and training are different questions. [Function: 1]

![Schematic: errors fall from 3 to 1 and never reach the dashed 0; a grid search over coefficients has lowest error 1.](../../assets/figures/lec05-kp01-best-en.png)

### 8. Change the boundaries: two lines make a strip

The proof rules out a single linear score with a fixed threshold, not combinations of boundaries. [Added] Let $s=x_1+x_2$. The four XOR points have $s=0,1,2$ and A is exactly $s=1$, so the intersection of two decisions selects it:

$$
\widehat y=1\quad\Longleftrightarrow\quad 0.5<s\le1.5.
$$

Figure `lec05-kp01-strip`: First see the diagonal strip between the two parallel lines, then the two A points inside it and the two B points outside; the right side lists the four values of s = x1 + x2: 0, 1, 1, 2. This only checks the four Boolean points and does not fix a unique extension of XOR to the continuous plane. [Function: 1, 3]

![The strip 0.5 < x1 + x2 <= 1.5 between two parallel lines: the two A points (s = 1) are inside and the two B points (s = 0, 2) are outside.](../../assets/figures/lec05-kp01-strip-en.png)

What changes is the combination of boundaries a model may use, not another choice of old coefficients. The next KP asks how neurons can carry out these two decisions.

### Extension: practice and implementation

**Code**: Compute each score, predict with "score > 0" and compare with the true labels. Include boundary points in tests so that code and text use the same inequality. The half-integers here are exactly representable; general real data still need care with floating-point errors.

Figure `lec05-kp01-ties`: First see the points (0,0) and (1,1) exactly on the boundary, then that predicting with > and with >= differs: for g = x1 - x2, > gives 1 error and >= gives 3. [Function: 1, 2]

![Points on the boundary: g = x1 - x2 scores 0 at (0,0) and (1,1); predicting with > gives 1 error and with >= gives 3.](../../assets/figures/lec05-kp01-ties-en.png)

**Practice**:

1. Compute the four inputs with $g=x_1+x_2-1.5$ and check AND and XOR separately. Hint: compute the scores, apply the same rule $g>0$, and only then compare the two sets of labels.
2. Is XOR failing because of few samples, noise, learning rate, or the restricted boundary shape? Hint: which does the contradiction rule out?
3. Which of OR, XOR and XNOR is separable by one line? XNOR outputs 1 when the inputs match. Hint: draw the labels first.

**Worked solution (question 1)**: ① Formula $g=x_1+x_2-1.5$, class A if $g>0$. ② Substitute the four points $(0,0),(0,1),(1,0),(1,1)$: the scores are $-1.5, -0.5, -0.5, 0.5$. ③ Only $(1,1)$ is positive, so the predictions are B, B, B, A. ④ Check: AND is B, B, B, A, all correct; for XOR the points $(0,1)$ and $(1,0)$ are predicted B and $(1,1)$ is predicted A, 3 errors.

**Worked solution (question 2)**: rule the causes out one by one.

- Too few samples? The four inputs are all the data, nothing is missing.
- Noise? The labels are taken straight from the XOR truth, so no label is wrong.
- Learning rate? The contradiction of section 6 holds for **any** coefficients, however they are adjusted.
- What is left is that the shape "one line" limits the boundary, so the answer is the boundary shape.

**Worked solution (question 3)**:

- OR can: take $g=x_1+x_2-0.5$; the four scores are $-0.5,\ 0.5,\ 0.5,\ 1.5$, the predictions B, A, A, A, equal to the OR truth.
- XNOR cannot: it has 1 at $(0,0),(1,1)$ and 0 at $(0,1),(1,0)$; the same-class points are still on the diagonals, it differs from XOR only by swapping the labels, so the same contradiction remains.
- Conclusion: of the three only OR is separable by one line.

Figure `lec05-kp01-and-xor`: First see AND classified perfectly by the same line on the left, then XOR with 3 errors on the right. [Function: 1, 2]

![The same line g = x1 + x2 - 1.5: AND is all right and XOR is wrong at (0,1), (1,0), (1,1), 3 points.](../../assets/figures/lec05-kp01-and-xor-en.png)

Figure `lec05-kp01-practice-23`: First see the four eliminations of question 2 on the left: few samples, noise and learning rate are excluded, leaving the limited boundary shape; then see question 3 on the right: OR is separable, XOR and XNOR are not. [Function: 1, 3]

![Exercises 2 and 3: XOR fails because the single-line boundary shape is limited; among OR, XOR, XNOR only OR is separable by one line.](../../assets/figures/lec05-kp01-practice-23-en.png)

## Terms and source

| Term | Meaning |
|---|---|
| Label | the class a point must be assigned to |
| Truth table | lists the output for every input combination |
| XOR | output 1 only when the two inputs differ |
| Score, constant | the number $g$ obtained by substitution; the term that shifts the line |
| Linearly separable | some coefficients classify every point correctly |
| Representational capacity | whether the boundary shape can express the answer |

Source: Chapter 4, KP01, Sections 4.1 to 4.2, accessed 2026-10-24. The four points, parameters and demonstrations follow the source; the explanations and figures are newly written; the strip condition of two boundaries and the midpoint proof are [Added].
