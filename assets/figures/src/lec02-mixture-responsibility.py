"""Figure code: lec02-mixture-responsibility.

The E-step turns a hard "which component?" question into a soft probability.
One-dimensional two-component mixture: P1=0.5, p1=N(0,1), p2=N(1,1).
The responsibility curve r(x) = P(1|x) is computed from the formula, so its
crossing with 0.5 sits exactly at the midpoint x = 0.5.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def gauss(x, m, s):
    return np.exp(-(x - m) ** 2 / (2 * s * s)) / (np.sqrt(2 * np.pi) * s)


x = np.linspace(-4, 5, 900)
p1, p2 = gauss(x, 0.0, 1.0), gauss(x, 1.0, 1.0)
w1, w2 = 0.5 * p1, 0.5 * p2
r = w1 / (w1 + w2)
cross = 0.5 * (0.0 + 1.0)

x0 = np.array([-2.0, 0.5, 2.5])
p1a, p2a = gauss(x0, 0.0, 1.0), gauss(x0, 1.0, 1.0)
r0 = 0.5 * p1a / (0.5 * p1a + 0.5 * p2a)

fig, axes = plt.subplots(2, 1, figsize=(8.2, 6.4), sharex=True,
                          gridspec_kw=dict(height_ratios=[1.0, 1.0]))

ax = axes[0]
ax.plot(x, p1, color=c1, lw=2.0, label=r"$p_1=\mathcal{N}(0,1)$")
ax.plot(x, p2, color=c2, lw=2.0, label=r"$p_2=\mathcal{N}(1,1)$")
ax.axvline(cross, color="#888888", ls="--", lw=1.0)
ax.text(cross + 0.06, 0.378, "equal densities at $x=0.5$", fontsize=9, color="#555555")
ax.set_ylim(0, 0.44)
ax.set_ylabel("component density")
ax.set_title("Two overlapping components", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(x, r, color="#222222", lw=2.4)
ax.axhline(0.5, color="#888888", ls="--", lw=1.0)
ax.axvline(cross, color="#888888", ls="--", lw=1.0)
ax.scatter(x0, r0, s=42, color="#ffffff", edgecolor="#222222", zorder=5, linewidths=1.4)
for xi, ri in zip(x0, r0):
    ax.annotate(f"{ri:.3f}", (xi, ri), textcoords="offset points",
                xytext=(6, 8 if ri < 0.5 else -14), fontsize=9, color="#222222")
ax.text(-3.9, 0.83, "soft: near 0.5\nwhen unsure", fontsize=9, color="#555555")
ax.set_xlim(-4, 5)
ax.set_ylim(-0.03, 1.06)
ax.set_xlabel("feature $x$")
ax.set_ylabel(r"responsibility $P(1\mid x)$")
ax.set_title("E-step output: a soft assignment, not a hard label", fontsize=10)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-mixture-responsibility.png", dpi=200)
print("saved assets/figures/lec02-mixture-responsibility.png")
print("crossing x", cross, "r there", round(float(r[np.argmin(abs(x - cross))]), 4))
for xi, ri in zip(x0, r0):
    print(f"x={xi:+.1f}  r = {ri:.4f}")
