"""Figure code: lec02-bayes-numbers. Prior, likelihood, product, and posterior for one observation.

Numbers: P(w1)=0.2, P(w2)=0.8, p(x|w1)=0.9, p(x|w2)=0.3 (illustrative values).
Products 0.18 and 0.24; evidence p(x)=0.42; posteriors 0.4286 and 0.5714.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

prior = np.array([0.2, 0.8])
like = np.array([0.9, 0.3])
prod = prior * like
evidence = prod.sum()
post = prod / evidence
classes = ["w1", "w2"]
x = np.arange(2)


def draw(ax, values, width, offset, color, alpha):
    bars = ax.bar(x + offset, values, width, color=color, alpha=alpha, edgecolor="#333333", linewidth=0.6)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.015, f"{v:.2f}", ha="center", va="bottom", fontsize=9)


fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), sharey=True)

ax = axes[0]
draw(ax, prior, 0.35, -0.18, c1, 1.0)
draw(ax, like, 0.35, 0.18, c1, 0.45)
ax.set_title("(a) prior (dark) and likelihood (light)", fontsize=10)

ax = axes[1]
draw(ax, prod, 0.5, 0.0, c2, 1.0)
ax.set_title("(b) product: prior x likelihood", fontsize=10)

ax = axes[2]
draw(ax, post, 0.5, 0.0, c2, 1.0)
ax.set_title("(c) posterior: product / evidence", fontsize=10)
ax.text(0.5, 0.92, f"evidence $p(x)$ = {evidence:.2f}", transform=ax.transAxes, ha="center", fontsize=9)

for ax in axes:
    ax.set_xticks(x, classes)
    ax.set_ylim(0, 1.0)
    ax.grid(axis="y", alpha=0.3)
axes[0].set_ylabel("value")

fig.tight_layout()
fig.savefig("assets/figures/lec02-bayes-numbers.png", dpi=200)
print("saved assets/figures/lec02-bayes-numbers.png")
print("products", prod.round(4), "evidence", round(evidence, 4), "posterior", post.round(4))
