"""Figure code: lec02-nonparametric-dimensionality-curse.

Top: the mean nearest-neighbour distance d(l, N) against the dimension l, from
the formula d(l, N) = 2 * (l * Gamma(l/2) / (2 * pi^(l/2) * N))^(1/l), for
N = 1e10 and N = 1e7.
Bottom: the distance of a uniform point from the origin in the unit cube,
||x||, for l = 2, 10 and 40.  In high dimensions the points pile up on a thin
shell; the shell radius for l = 40 is 1.83, the same size as the mean NN
distance in the top panel.  All values are computed, none are typed in.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

plt.rcParams["mathtext.fontset"] = "cm"
C_RED = "#dc2626"
C_GRAY = "#8a8a8a"
C_BLUE = "#6a9fd6"


def log_d(l, N):
    return np.log(2) + (1.0 / l) * (np.log(l) + gammaln(l / 2)
                                    - np.log(2) - (l / 2) * np.log(np.pi) - np.log(N))


L = np.arange(1, 46)
d10 = np.exp(log_d(L, 1e10))
d7 = np.exp(log_d(L, 1e7))

fig = plt.figure(figsize=(12.4, 7.6))
gs = fig.add_gridspec(2, 3, height_ratios=[1.5, 1.0], hspace=0.5, wspace=0.38)

ax = fig.add_subplot(gs[0, :])
ax.plot(L, d10, color=C_RED, lw=2.2, label=r"$N = 10^{10}$")
ax.plot(L, d7, color=C_GRAY, lw=2.2, ls="--", label=r"$N = 10^{7}$")
ax.axhline(1.0, color="#bbbbbb", lw=1.0, ls=":")
ax.annotate("unit cube edge = 1", (6.2, 1.18), fontsize=9, color="#555555")
marks = [(2, r"$1.13\times 10^{-5}$", (10, -14)),
         (10, "0.18", (10, -16)),
         (20, "0.76", (10, -16)),
         (40, "1.83", (6, 12))]
for l, txt, off in marks:
    val = float(np.exp(log_d(l, 1e10)))
    ax.plot(l, val, "o", color=C_RED, ms=6, zorder=5)
    ax.annotate(txt, (l, val), textcoords="offset points", xytext=off,
                fontsize=9.5, color=C_RED, zorder=6)
ax.annotate("1000x more samples:\n2-D distance shrinks 31.6x,\n40-D distance shrinks only 1.19x",
            (21.5, 0.010), fontsize=9.5, color="#333333")
ax.set_yscale("log")
ax.set_xlim(1, 45)
ax.set_ylim(1e-6, 5)
ax.set_xlabel("dimension $l$")
ax.set_ylabel("mean nearest-neighbour distance $d(l,N)$")
ax.set_title("Curse of dimensionality: the same sample count fills low dimensions but not high ones",
             fontsize=11)
ax.legend(frameon=False, fontsize=9.5, loc="lower right")
ax.grid(alpha=0.3, which="both")

rng = np.random.default_rng(11)
for j, l in enumerate([2, 10, 40]):
    axs = fig.add_subplot(gs[1, j])
    X = rng.random((3000, l))
    rad = np.sqrt(((X - 0.5) ** 2).sum(axis=1))
    mean_r = float(rad.mean())
    shell = float(np.sqrt(l / 12.0))
    axs.hist(rad, bins=40, color=C_BLUE, alpha=0.75, edgecolor="#333333", linewidth=0.4)
    axs.axvline(shell, color=C_RED, lw=1.8,
                label=r"shell radius $\sqrt{l/12}$ = %.2f" % shell)
    axs.set_title(f"$l$ = {l}: mean = {mean_r:.2f}", fontsize=9.5)
    axs.set_xlabel(r"distance from cube centre")
    axs.grid(alpha=0.3)
    if j == 0:
        axs.set_ylabel("count")
    axs.legend(frameon=False, fontsize=8.0, loc="upper right")
    if l == 40:
        axs.annotate("thin shell at r = 1.83", (0.02, 0.10),
                     xycoords="axes fraction", fontsize=8.5, color=C_RED)

fig.suptitle("Parzen and kNN estimates fail in high dimensions", fontsize=12)
fig.savefig("assets/figures/lec02-nonparametric-dimensionality-curse.png", dpi=200)
print("saved assets/figures/lec02-nonparametric-dimensionality-curse.png")
for l in [1, 2, 10, 20, 30, 40, 45]:
    print(f"l={l}: d(1e10)={np.exp(log_d(l,1e10)):.6g}  d(1e7)={np.exp(log_d(l,1e7)):.6g}")
print("shell radius l=40:", np.sqrt(40 / 12), " l=2:", np.sqrt(2 / 12), " l=10:", np.sqrt(10 / 12))
print("ratio 2-D", float(np.exp(log_d(2, 1e7)) / np.exp(log_d(2, 1e10))))
print("ratio 40-D", float(np.exp(log_d(40, 1e7)) / np.exp(log_d(40, 1e10))))
