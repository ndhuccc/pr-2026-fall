"""Figure code: lec02-maxent-constraints. The same maximum-entropy recipe gives
different answers for different constraints.

Panel (a): support [-1, 1] only           -> uniform,  H = ln 2   = 0.693
Panel (b): support x >= 0 and mean 1     -> exponential e^{-x}, H = 1 + ln 1 = 1.000
Panel (c): mean 0 and variance 1         -> Gaussian,   H = 0.5 ln(2 pi e) = 1.419
Entropies are computed numerically on the same kind of grid; the values are not
compared across panels because the supports differ.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"


def entropy_on_grid(x, f):
    dx = x[1] - x[0]
    f = np.clip(f, 0.0, None)
    m = f > 0
    return -np.sum(f[m] * np.log(f[m])) * dx


fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.8))

# (a) uniform on [0, 2]
xg = np.linspace(0.0, 2.0, 4001)
fg = np.full_like(xg, 0.5)
H_uniform = entropy_on_grid(xg, fg)
x = xg
f = fg
axes[0].plot(x, f, color="#d62728", lw=2.4)
axes[0].fill_between(x, f, color="#d62728", alpha=0.20)
axes[0].text(0.08, 0.62, r"$p(x)=\frac{1}{2}$", fontsize=11)
axes[0].text(0.08, 0.53, rf"$H=\ln 2={H_uniform:.3f}$", fontsize=9)
axes[0].set_title(r"(a) support $[0,2]$ only", fontsize=10)
axes[0].set_xlim(-0.15, 2.15)
axes[0].set_ylim(0, 0.72)

# (b) exponential on x >= 0 with mean 1: entropy on a wide grid, display cropped
xg = np.linspace(0.0, 60.0, 600001)
fg = np.exp(-xg)
H_exp = entropy_on_grid(xg, fg)
x = np.linspace(0.0, 6.0, 4001)
f = np.exp(-x)
axes[1].plot(x, f, color="#e0a24d", lw=2.4)
axes[1].fill_between(x, f, color="#e0a24d", alpha=0.20)
axes[1].annotate(r"$p(x)=e^{-x}$" "\n" rf"$H=1+\ln 1={H_exp:.3f}$",
                 xy=(1.0, np.exp(-1.0)), xytext=(1.6, 0.60), fontsize=9,
                 arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0))
axes[1].set_title(r"(b) support $x\geq 0$, mean $=1$", fontsize=10)
axes[1].set_xlim(0, 6)
axes[1].set_ylim(0, 1.12)

# (c) Gaussian with mean 0 and variance 1
xg = np.linspace(-30.0, 30.0, 600001)
fg = np.exp(-xg ** 2 / 2) / np.sqrt(2 * np.pi)
H_gauss = entropy_on_grid(xg, fg)
x = np.linspace(-4.0, 4.0, 4001)
f = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)
axes[2].plot(x, f, color="#6a4c9c", lw=2.4)
axes[2].fill_between(x, f, color="#6a4c9c", alpha=0.20)
axes[2].text(-3.7, 0.32, r"$p(x)=\mathcal{N}(0,1)$", fontsize=10)
axes[2].text(-3.7, 0.26, rf"$H=\frac{{1}}{{2}}\ln(2\pi e)={H_gauss:.3f}$",
             fontsize=9)
axes[2].set_title(r"(c) mean $0$, variance $1$", fontsize=10)
axes[2].set_xlim(-4, 4)
axes[2].set_ylim(0, 0.46)

for ax, xl in zip(axes, [r"$x$", r"$x$", r"$x$"]):
    ax.set_xlabel(xl)
    ax.grid(alpha=0.3)
axes[0].set_ylabel(r"density $p(x)$")

fig.suptitle("Same recipe, different constraints, different answers", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("assets/figures/lec02-maxent-constraints.png", dpi=200)
print("saved assets/figures/lec02-maxent-constraints.png")
print(f"uniform[0,2] H={H_uniform:.4f}")
print(f"exp mean1     H={H_exp:.4f}")
print(f"gauss(0,1)    H={H_gauss:.4f}")
print("closed forms:", np.log(2), 1 + np.log(1), 0.5 * np.log(2 * np.pi * np.e))
