"""Figure code: lec02-nb-spam-boundary.

Naive Bayes on two binary word features. The decision rule is a linear
discriminant function, so the boundary is a straight line in the (x1, x2)
plane of the two word indicators.

Numbers (computed here): P(spam)=0.4, P(not spam)=0.6;
p = P(word=1 | spam)  = [0.8, 0.6]
q = P(word=1 | nospam)= [0.2, 0.1]
w_i = ln( p_i (1-q_i) / (q_i (1-p_i)) ) = [2.772589, 2.602690]
w_0 = sum ln((1-p_i)/(1-q_i)) + ln(P(w1)/P(w2)) = -2.602690
Line crosses x1-axis: (0, 1.000000), (1, -0.065278), (2, -1.130557).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_SPAM, C_HAM = "#d97757", "#6a9fd6"

p = np.array([0.8, 0.6])
q = np.array([0.2, 0.1])
prior = np.array([0.4, 0.6])

w = np.log(p * (1 - q) / (q * (1 - p)))
w0 = np.log((1 - p) / (1 - q)).sum() + np.log(prior[0] / prior[1])

# grid of posteriors P(spam | x)
x1 = np.linspace(-0.6, 1.6, 500)
x2 = np.linspace(-0.6, 1.6, 500)
X1, X2 = np.meshgrid(x1, x2)
G = w[0] * X1 + w[1] * X2 + w0
POST = 1.0 / (1.0 + np.exp(-G))   # posterior of spam

fig, ax = plt.subplots(figsize=(6.6, 6.0))
cf = ax.contourf(X1, X2, POST, levels=np.linspace(0, 1, 41),
                  cmap="RdBu_r", alpha=0.75)
ax.contour(X1, X2, POST, levels=[0.5], colors="black", linewidths=2.0)
cs = ax.contour(X1, X2, POST, levels=[0.1, 0.5, 0.9], colors="#222222",
                linewidths=0.7, linestyles="--")
ax.clabel(cs, fmt={0.1: "0.1", 0.5: "0.5", 0.9: "0.9"}, fontsize=8)

# the observed email x = (1, 1)
ax.plot([1], [1], "o", ms=11, mfc="white", mec="black", mew=2.0)
ax.annotate("observed email\n$x_1{=}1,\\ x_2{=}1$:  $P(\\mathrm{spam}|\\mathbf{x})=0.941$",
            (1, 1), textcoords="offset points", xytext=(-40, 30),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.9))

# boundary intercepts
xs = np.array([-0.6, 1.6])
ys = -(w[0] * xs + w0) / w[1]
ax.plot(xs, ys, color="black", lw=2.0)

ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.6, 1.6)
ax.set_aspect("equal")
ax.set_xlabel(r"word 1 indicator $x_1$")
ax.set_ylabel(r"word 2 indicator $x_2$")
ax.set_title("Naive Bayes decision regions in the binary feature plane",
             fontsize=10)
cb = fig.colorbar(cf, ax=ax, fraction=0.046, pad=0.04)
cb.set_label(r"posterior $P(\mathrm{spam}\mid\mathbf{x})$", fontsize=9)
ax.grid(alpha=0.25)

fig.tight_layout()
fig.savefig("assets/figures/lec02-nb-spam-boundary.png", dpi=200)
print("saved lec02-nb-spam-boundary.png")
print("w", w.round(6), "w0", round(w0, 6))
for xv in (0, 1, 2):
    print("x1=", xv, "x2=", round(-(w[0] * xv + w0) / w[1], 6))
