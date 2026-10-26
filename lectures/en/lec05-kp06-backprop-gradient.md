# KP06 From the Step to the Gradient of Backpropagation

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.6

[Slides: read and download](../../slides/lec05-kp06-backprop-gradient-en.jbd.json) | [中文版](../lec05-kp06-backprop-gradient.md)

## Learning objectives

- Explain why the step function is replaced by a sigmoid and what the trade-off of the slope parameter $a$ is.
- Use the chain rule to write the slope of one weight as "$-\delta$ times the input" and compute every $\delta$ of a 2–2–1 network step by step.
- Update all nine weights once, list "old value, gradient, update, new value", and check the gradients with numerical differences.

## KP06 From the Step to the Gradient of Backpropagation

**One-sentence summary**: The step function has no derivative, so it is replaced by a sigmoid that has slopes. By the chain rule the gradient of each weight (the slope of the cost with respect to it) equals "$-\delta$ times the input of that weight", so moving downhill means adding "$\delta$ times the input". And $\delta$ is computed from the output layer backwards, layer by layer, which is backpropagation.

### Prerequisites and symbols

**Three things you need first** (each in one plain sentence):

- **Slope (derivative)**: how much the output changes for one small step of the input. A positive slope means the output rises to the right and a negative slope that it falls. For example, $y=x^2$ has slope $6$ at $x=3$.
- **Partial derivative**: when a function has many inputs, move only one and keep the others fixed, and see how the output changes. It is written $\partial E/\partial w$ and read "the partial derivative of $E$ with respect to $w$".
- **Chain rule**: if $A$ affects $B$ and $B$ affects $C$, the slope of $C$ with respect to $A$ is the slope of $C$ with respect to $B$ times the slope of $B$ with respect to $A$.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $x_1,x_2$ | inputs | here $x=(1,0)$; every unit also has a "bias input" that is always $1$ |
| $w$ | weight | the multiplier on one connection; each unit has 3 (bias, $x_1$, $x_2$ or bias, $y_1$, $y_2$) |
| $v$ | weighted sum | the sum of the inputs times their weights in a unit |
| $f$ | sigmoid | $f(v)=1/(1+e^{-av})$, here $a=1$ |
| $y_1,y_2$ | outputs of the hidden units | $y_j=f(v_j)$ |
| $o$ | network output | $f(v_o)$ of the output unit |
| $t$ | target | here $t=1$ |
| $e$ | error | $e=t-o$ |
| $E$ | cost | $E=\tfrac12 e^2$ |
| $\delta$ | error signal | $\delta\equiv-\partial E/\partial v$, the convention of this lecture |
| $\eta$ | learning rate | the size of one step, here $\eta=0.3$ |

**Fixed settings of this lecture**: $a=1$ (so $f'(v)=f(v)\bigl(1-f(v)\bigr)$), $\eta=0.3$, the bias input is always $1$, input $x=(1,0)$, target $t=1$.

### 1. The step function has no slope to look at

**Plain explanation**: In KP05 the weights were given by a rule. To let a network learn its weights, we need the slope of the cost with respect to each weight and move the weight in the direction that lowers the cost.

- **Cost function**: one number that sums up how far the prediction is from the target; smaller is better. This lecture uses $E=\tfrac12(t-o)^2$.
- **Gradient descent**: look at the slope of the cost with respect to each weight and move the weight a little in the direction that lowers the cost.

The step function has slope 0 everywhere except at the jump, and at the jump there is no slope. Without a slope, gradient descent cannot start.

Figure `lec05-kp06-step-slope`: look at the upper plot first: the step has slope 0 everywhere and no slope at the jump; then the lower plot: the sigmoid has a tangent of slope 0.25 in the middle. The figure shows why a step cannot use gradients. [Function: 1]

![The slopes of a step and a sigmoid](../../assets/figures/lec05-kp06-step-slope.png)

The next question: can the step be rounded off so that every point has a slope?

### 2. Rounding the step into a sigmoid: slopes everywhere, but the more step-like, the shorter the stretch with a slope

**Formal definition**:

$$
f(x)=\frac{1}{1+e^{-ax}},\qquad f'(x)=a\,f(x)\,\bigl(1-f(x)\bigr).
$$

A **sigmoid** squeezes any number into the range 0 to 1. The larger $a$ is, the more the curve looks like a step.

**Why this shape**: it is differentiable everywhere and its slope can be computed from the function value itself ($f(1-f)$), with no extra differentiation.

**Common misconception**: the closer to a step the better. In fact the larger $a$ is, the narrower and higher the peak of the slope, and on both sides the slope is almost 0, so training with gradients gets harder. Also, once we leave the step, the geometric statement of KP03, "map to the vertices of a cube", no longer holds, and correct classification is carried by the cost function.

Figure `lec05-kp06-sigmoid-a`: look at the upper row of three sigmoids ($a=0.7,2,8$) and the dashed step: a larger $a$ hugs the step; then look at the lower row of slopes: the peak gets narrower. [Function: 1, 2]

![The effect of the slope parameter a](../../assets/figures/lec05-kp06-sigmoid-a.png)

The next question: with slopes available, how do we know how much to change a weight? Walk through a small network first.

### 3. Walking through a 2–2–1 network

**What the network looks like**: 2–2–1 means 2 inputs, 2 hidden units and 1 output unit. Each unit has 3 weights (bias, one for $x_1$ or $y_1$, one for $x_2$ or $y_2$).

**Forward pass**: compute from the inputs forwards, layer by layer. Each unit first computes its weighted sum $v$, then applies the sigmoid to get $y=f(v)$, and the intermediate values are stored.

**Example**: input $x=(1,0)$, target $1$. The weights in order (bias, $x_1$, $x_2$) are:

- hidden unit 1: $(-0.10,\ 0.20,\ 0.40)$.
- hidden unit 2: $(0.10,\ -0.30,\ 0.20)$.
- output unit: $(-0.20,\ 0.50,\ -0.40)$, where the last two weights multiply $y_1,y_2$.

Computation:

- Hidden unit 1: $v_1=-0.10+0.20\cdot1+0.40\cdot0=0.10$, $y_1=f(0.10)=0.525$.
- Hidden unit 2: $v_2=0.10-0.30\cdot1+0.20\cdot0=-0.20$, $y_2=f(-0.20)=0.450$.
- Output unit: $v_o=-0.20+0.50\cdot0.525-0.40\cdot0.450=-0.118$, $o=f(-0.118)=0.471$.
- Error and cost: $e=1-0.471=0.529$, $E=\tfrac12e^2=0.140$.

Figure `lec05-kp06-net-forward`: look first at the weights written beside the lines and the bias above; then follow the arrows through the three numbers $x\to y\to o$. [Function: 1]

![The forward pass](../../assets/figures/lec05-kp06-net-forward.png)

The next question: the output 0.471 is 0.529 short of the target 1. In which direction, and by how much, should each weight change?

### 4. How much to change one weight: split the slope of the cost into three slopes multiplied

**Chain rule**: $E$ depends on a weight $w$ only through $o$ and $v$, so

$$
\frac{\partial E}{\partial w}=\frac{\partial E}{\partial o}\cdot\frac{\partial o}{\partial v}\cdot\frac{\partial v}{\partial w}.
$$

**What the three slopes are** (take the weight $w_{o1}$ from hidden unit 1 to the output as an example):

1. $E=\tfrac12(t-o)^2$. Treat $(t-o)$ as one block: the slope of a square is the block itself, times $\partial(t-o)/\partial o=-1$, so $\partial E/\partial o=-(t-o)=-e=-0.529$.
2. $o=f(v_o)$, so $\partial o/\partial v_o=f'(v_o)=o(1-o)=0.471\times0.529=0.249$.
3. $v_o=\ldots+w_{o1}y_1+\ldots$ and only the term $w_{o1}y_1$ contains $w_{o1}$, so $\partial v_o/\partial w_{o1}=y_1=0.525$, the input of this weight.

Multiplying: $(-0.529)\times0.249\times0.525=-0.069$. The gradient is negative, which means that making $w_{o1}$ larger makes $E$ smaller.

Figure `lec05-kp06-chain`: look at the three arrows $w\to v\to o\to E$, each labelled with one slope; then at the product of the three on the right, $-0.069$. [Function: 1, 2]

![The chain rule](../../assets/figures/lec05-kp06-chain.png)

The next question: multiplying three slopes for every weight is tedious. Can the first two be combined and computed once?

### 5. The error signal $\delta$: the gradient is $-\delta$ times the input, and moving downhill adds $\delta$ times the input

**Convention**: $\delta\equiv-\partial E/\partial v$, that is, "the error times the slope". For the output unit:

$$
\delta_o=e\,f'(v_o)=0.529\times0.249=0.1319.
$$

**Two equivalent statements** (watch the signs):

- **Gradient**: $\partial E/\partial w=-\delta\cdot(\text{the input of this weight})$. For example, the $-0.069$ of section 4 equals $-0.1319\times0.525$.
- **Downhill direction**: $-\partial E/\partial w=+\delta\cdot(\text{input})$. The update is $\Delta w=\eta\,\delta\cdot\text{input}$.

**Learning rate** $\eta$: the size of one step of the weights, here $\eta=0.3$. The inputs of the three output weights are $1$ (bias), $y_1=0.525$ and $y_2=0.450$, so the updates are $+0.0396$, $+0.0208$ and $+0.0178$.

**Note on the sign** [Added]: the source writes $\delta$ both as $\partial E/\partial v$ and as "the error times the slope", which differ by a sign. This lecture defines $\delta=-\partial E/\partial v$ throughout, so the gradient is $-\delta\times$input and the update adds $\eta\,\delta\times$input.

Figure `lec05-kp06-out-bars`: look at the three bars, each the update $\eta\delta\times$input of one output weight; then note that all three are positive, because the target 1 is above the output 0.471 and all three weights should grow. [Function: 1, 2]

![The updates of the output layer](../../assets/figures/lec05-kp06-out-bars.png)

The next question: a hidden unit is not connected to the target directly. Where does its $\delta$ come from?

### 6. A hidden layer cannot see the target: pass the output $\delta$ back along the weights

**Backpropagation**: after the forward pass has computed all outputs, walk back from the output layer. Hidden unit $j$ affects $E$ only through the weights to the next layer. So its $\delta$ is "the sum over the next layer of each $\delta_k$ times the weight $w_{kj}$ leading to it", then times its own slope:

$$
\delta_j=f'(v_j)\sum_k\delta_k\,w_{kj}.
$$

**Indices**: $j$ numbers the hidden units (here 1 and 2); $k$ numbers the units of the next layer (here only the output unit); $w_{kj}$ is the weight from hidden unit $j$ to unit $k$, here $w_{o1}=0.50$ and $w_{o2}=-0.40$.

**Worked numbers**:

- $\delta_1=f'(v_1)\,\delta_o\,w_{o1}=0.2494\times0.1319\times0.50=0.0164$.
- $\delta_2=f'(v_2)\,\delta_o\,w_{o2}=0.2475\times0.1319\times(-0.40)=-0.0131$. $w_{o2}$ is negative, so $\delta_2<0$.

Figure `lec05-kp06-net-backward`: look at the red lines, the path of the error going back from the output; then compare the signs of the weights on the two paths: hidden unit 2 goes through a negative weight, so $\delta_2$ is negative. [Function: 1]

![Backpropagation](../../assets/figures/lec05-kp06-net-backward.png)

The next question: all nine weights now have their $\delta$. Does one update really lower the cost?

### 7. Nine weights, one step each: the cost falls from 0.140 to 0.132

In the table each row is one weight: "input" is what this weight multiplies, "gradient" $=-\delta\times$input and "update" $=\eta\,\delta\times$input ($\eta=0.3$).

| Weight | Old value | Input | $\delta$ of its unit | Gradient | Update | New value |
|---|---:|---:|---:|---:|---:|---:|
| output bias | $-0.2000$ | $1$ | $0.1319$ | $-0.1319$ | $+0.0396$ | $-0.1604$ |
| output $w_{o1}$ | $0.5000$ | $0.525$ | $0.1319$ | $-0.0692$ | $+0.0208$ | $0.5208$ |
| output $w_{o2}$ | $-0.4000$ | $0.450$ | $0.1319$ | $-0.0594$ | $+0.0178$ | $-0.3822$ |
| hidden 1 bias | $-0.1000$ | $1$ | $0.0164$ | $-0.0164$ | $+0.0049$ | $-0.0951$ |
| hidden 1 $x_1$ | $0.2000$ | $1$ | $0.0164$ | $-0.0164$ | $+0.0049$ | $0.2049$ |
| hidden 1 $x_2$ | $0.4000$ | $0$ | $0.0164$ | $0$ | $0$ | $0.4000$ |
| hidden 2 bias | $0.1000$ | $1$ | $-0.0131$ | $+0.0131$ | $-0.0039$ | $0.0961$ |
| hidden 2 $x_1$ | $-0.3000$ | $1$ | $-0.0131$ | $+0.0131$ | $-0.0039$ | $-0.3039$ |
| hidden 2 $x_2$ | $0.2000$ | $0$ | $-0.0131$ | $0$ | $0$ | $0.2000$ |

$x_2=0$, so the two $x_2$ weights do not move this time. A forward pass with the new weights gives the output $o=0.4857$ (was $0.4706$) and $E=0.1322$ (was $0.1401$). One step is a small step; many repeats are needed to get near the target.

Figure `lec05-kp06-before-after`: look at the output on the left, which moved a small step from 0.471 towards the target 1; then at the cost on the right, which fell from 0.140 to 0.132. [Function: 1, 2]

![Before and after the update](../../assets/figures/lec05-kp06-before-after.png)

The next question: how can we be sure the gradients in the table are not wrong?

### 8. Checking with numerical slopes

Add and subtract a tiny $\varepsilon=10^{-6}$ to one weight and see how $E$ changes: $[E(w+\varepsilon)-E(w-\varepsilon)]/(2\varepsilon)$, called the **central difference**. For the nine weights, $-\delta\times\text{input}$ and the difference slope differ by at most about $4\times10^{-11}$ (recomputed by a program with the same weights as the table and $a=1$).

This is the most common debugging method when writing backpropagation code. The next KP writes the whole procedure as an algorithm.

Figure `lec05-kp06-numcheck`: look at the bars, the $-\delta\times$input (the gradient) of the nine weights; then at the dots, the slopes by differences. They coincide, so the backpropagation formulas are right. [Function: 2]

![The numerical check](../../assets/figures/lec05-kp06-numcheck.png)

### Extension: saturation, practice and worked solution

**Saturation of the slope**: at $x=3$, $f'(3)=a\,f(1-f)$: $a=0.7$ gives $0.068$, $a=2$ gives $0.0049$ and $a=8$ gives $3\times10^{-10}$. With a large $a$, a point not far from the centre already enters "saturation": $\delta$ is multiplied by a slope of almost 0 and the weights hardly move. So $a$ is taken of moderate size.

Figure `lec05-kp06-saturation`: look at the three bars on a logarithmic scale: the larger $a$ is, the smaller the slope at $x=3$, by several orders of magnitude. [Function: 2]

![Saturation of the slope](../../assets/figures/lec05-kp06-saturation.png)

**Practice**: keep this example ($a=1$, $\eta=0.3$) and change only the target from 1 to 0; the forward pass stays the same.

1. What are the error $e$ and the output-layer $\delta_o$? Hint: $e=$ target $-$ output, and $f'(v_o)=0.249$ stays.
2. In which direction and by how much does each of the three output weights move ($\eta=0.3$)?

**Worked solution of questions 1 and 2**: (1) $e=0-0.471=-0.471$, $\delta_o=-0.471\times0.249=-0.1173$. (2) $\Delta w=0.3\times(-0.1173)\times\text{input}$: bias $-0.0352$, $w_{o1}$ $-0.0185$, $w_{o2}$ $-0.0158$, all three go down. (3) Check: the output 0.471 must fall towards 0, so all output weights should fall, the opposite of the signs for target 1.

Figure `lec05-kp06-practice-sol`: look at the three bars, all negative, so all three output weights go down. [Function: 1, 2]

![The practice solution](../../assets/figures/lec05-kp06-practice-sol.png)

## Terms and source

| 中文 | English |
|---|---|
| 代價函數 | Cost function |
| 梯度下降 | Gradient descent |
| 梯度 | Gradient |
| 偏導數 | Partial derivative |
| sigmoid | Sigmoid (logistic function) |
| 前向傳遞 | Forward pass |
| 連鎖律 | Chain rule |
| 誤差訊號 | Error signal ($\delta$) |
| 反向傳播 | Backpropagation |
| 學習率 | Learning rate |
| 中心差分 | Central difference |

Source: Chapter 4, KP06, §4.6 (read 2026-10-25). The sigmoid family, the chain rule and the backward recursion of $\delta$ follow the source; the weights, input and target of the 2–2–1 network are the initial setting of the source's interactive example, and every worked number, the update table of the nine weights and the numerical check were recomputed for this lecture ([added], (program-computed), $a=1$, $\eta=0.3$); the sign convention of $\delta$ is unified in this lecture.
