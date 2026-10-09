"""Figure code: lec02-parameter-estimation-ml-bias.

Small-sample bias of the ML variance estimate.
E[sigma2_ML] = (N-1)/N * sigma2, so the bias is -sigma2/N.
Left: bias factor (N-1)/N against N; marks N=3 (0.6667) and N=20 (0.95).
Right: Monte Carlo histogram of the ML estimate at N=3 and N=20,
true variance sigma2 = 1 (standard normal samples).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

rng = np.random.default_rng(seed=0)
trials = 200000

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))

ax = axes[0]
n = np.linspace(2, 40, 400)
factor = (n - 1.0) / n
ax.plot(n, factor, color=c1, lw=2.2)
ax.axhline(1.0, color="#333333", ls="--", lw=1.2)
for nk, dy in ((3, 0.0), (20, 0.0)):
    fk = (nk - 1.0) / nk
    ax.plot([nk], [fk], "o", color=c2, ms=7, zorder=5)
    ax.annotate(f"$N={nk}$: {fk:.4f}", (nk, fk), textcoords="offset points",
                xytext=(8, -14), fontsize=9, color=c2)
ax.set_xlabel(r"sample size $N$")
ax.set_ylabel(r"$E[\hat{\sigma}^2_{ML}]/\sigma^2=(N-1)/N$")
ax.set_title(r"(a) expected value rises toward $1$", fontsize=10)
ax.set_xlim(2, 40)
ax.set_ylim(0.4, 1.05)
ax.grid(alpha=0.3)

ax = axes[1]
for nk, color, label in ((3, c1, r"$N=3$"), (20, c2, r"$N=20$")):
    s = rng.standard_normal((trials, nk))
    ml = ((s - s.mean(axis=1, keepdims=True)) ** 2).mean(axis=1)
    ax.hist(ml, bins=80, range=(0, 3), density=True, histtype="step", lw=2.0,
            color=color, label=f"{label}, theory {(nk - 1) / nk:.4f}")
ax.axvline(1.0, color="#333333", ls="--", lw=1.2)
ax.annotate(r"true $\sigma^2=1$", (1.0, 1.16), textcoords="offset points",
            xytext=(8, 0), fontsize=9)
ax.set_xlabel(r"ML estimate $\hat{\sigma}^2_{ML}$")
ax.set_ylabel("density")
ax.set_title(r"(b) $N=3$ peaks left of the truth", fontsize=10)
ax.set_xlim(0, 3)
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-parameter-estimation-ml-bias.png", dpi=200)
print("saved assets/figures/lec02-parameter-estimation-ml-bias.png")
for nk in (3, 20):
    print("N", nk, "factor", round((nk - 1) / nk, 6), "bias", round(-1.0 / nk, 6))
