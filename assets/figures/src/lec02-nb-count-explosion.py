"""Figure code: lec02-nb-count-explosion.

Naive Bayes: the number of probability values to estimate explodes with the
number of binary features l when independence is not assumed.

Numbers (computed here, not hand-filled):
  no-independence : 2^l - 1
  independence    : 2 l
  l=6  -> 63 vs 12   (5.25x)
  l=10 -> 1023 vs 20 (51.15x)
  l=20 -> 1048575 vs 40 (26214.4x)
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
RED = "#dc2626"
GREY = "#555555"

l = np.arange(1, 21)
full = 2.0 ** l - 1.0
indep = 2.0 * l

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))

ax = axes[0]
ax.semilogy(l, full, "-o", color=GREY, lw=2.0, ms=4.5,
            label=r"no independence: $2^l-1$")
ax.semilogy(l, indep, "-s", color=RED, lw=2.2, ms=4.5,
            label=r"independence: $2l$")
for lv, dx, dy in [(20, -46, -4), (10, 5, 12), (6, 6, 14)]:
    fv, iv = 2 ** lv - 1, 2 * lv
    ax.annotate(f"{fv:,}", (lv, fv), textcoords="offset points",
                xytext=(dx, dy), fontsize=9, color=GREY)
for lv, dx, dy in [(20, -18, -14), (10, 5, -14)]:
    iv = 2 * lv
    ax.annotate(f"{iv:,}", (lv, iv), textcoords="offset points",
                xytext=(dx, dy), fontsize=9, color=RED)
ax.annotate("l=6: 63 vs 12\n(5.25x)", (6, 63), textcoords="offset points",
            xytext=(-14, 36), fontsize=8.5, color=GREY,
            arrowprops=dict(arrowstyle="->", color=GREY, lw=0.9))
ax.annotate("l=10: 1023 vs 20\n(51.2x)", (10.6, 260), fontsize=8.5, color=RED)
ax.annotate(r"the two lines nearly meet at $l\approx1$; the" "\n"
            r"exponential line pulls away from $l\approx3$",
            (1.3, 1.0), fontsize=8.0, color="#333333")
ax.set_xlim(0.5, 20.5)
ax.set_ylim(0.5, 5e7)
ax.set_xlabel("number of binary features $l$")
ax.set_ylabel("probability values to estimate")
ax.set_title("(a) counts on a log scale", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.grid(alpha=0.3, which="both")

ax = axes[1]
vals = [2 ** 10 - 1, 2 * 10]
labels = ["no independence\n$2^{10}-1$", "independence\n$2\\times10$"]
bars = ax.bar([0, 1], vals, width=0.55, color=[GREY, RED],
              edgecolor="#333333", linewidth=0.6)
ax.set_yscale("log")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v * 1.25, f"{v:,}",
            ha="center", fontsize=10)
ax.set_xticks([0, 1], labels)
ax.set_ylim(1, 3e5)
ax.set_ylabel("probability values to estimate")
ax.set_title("(b) fixed $l=10$: 1023 vs 20 (51.2x fewer)", fontsize=10)
ax.annotate("data demand drops from\n$N^{10}$ to about $20N$", (0.5, 4000),
            ha="center", fontsize=8.5, color="#333333")
ax.grid(axis="y", alpha=0.3, which="both")

fig.tight_layout()
fig.savefig("assets/figures/lec02-nb-count-explosion.png", dpi=200)
print("saved lec02-nb-count-explosion.png")
for lv in (6, 10, 20):
    print(lv, 2 ** lv - 1, 2 * lv, round((2 ** lv - 1) / (2 * lv), 2))
