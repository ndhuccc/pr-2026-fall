"""Figure code: lec02-risk-flip. The posterior favors omega_2, but the lowest-risk decision is omega_1.

Posterior P(w1|x)=0.25, P(w2|x)=0.75. Loss: lambda12=1 (true w2, decided w1), lambda21=5 (true w1,
decided w2), zero on the diagonal. Conditional risks: l1 = 0.75, l2 = 1.25 (lecture Section 3).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

post = np.array([0.25, 0.75])            # P(w1|x), P(w2|x)
loss = np.array([[0.0, 1.0],             # decide w1: lambda11, lambda12
                 [5.0, 0.0]])            # decide w2: lambda21, lambda22
risk = loss @ post                       # l1, l2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.6), sharey=False)
labels = [r"$\omega_1$", r"$\omega_2$"]
x = np.arange(2)

bars = ax1.bar(x, post, 0.5, color=[c1, c2], edgecolor="#333333", linewidth=0.6)
for b, v in zip(bars, post):
    ax1.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.2f}", ha="center", fontsize=10)
ax1.set_xticks(x, labels)
ax1.set_ylim(0, 1.0)
ax1.set_title("(a) posterior: $\\omega_2$ is favored", fontsize=10)
ax1.grid(axis="y", alpha=0.3)

names = [r"decide $\omega_1$", r"decide $\omega_2$"]
bars = ax2.bar(x, risk, 0.5, color=[c1, c2], edgecolor="#333333", linewidth=0.6)
for b, v in zip(bars, risk):
    ax2.text(b.get_x() + b.get_width() / 2, v + 0.03, f"{v:.2f}", ha="center", fontsize=10)
ax2.set_xticks(x, names)
ax2.set_ylim(0, 1.5)
ax2.set_title("(b) conditional risk: $\\omega_1$ is lower", fontsize=10)
ax2.grid(axis="y", alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-risk-flip.png", dpi=200)
print("saved assets/figures/lec02-risk-flip.png")
print("risk", risk.round(4), "decision", "w1" if risk.argmin() == 0 else "w2")
