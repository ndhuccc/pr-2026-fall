"""Lecture 01, Figure 1: a 2-D feature plane with simulated data (not from the textbook).

Each point is one region of interest: x = [mean gray level, gray-level std]^T.
Class A and class B are simulated with a fixed random seed. The decision rule is the
perpendicular bisector of the two class means (a linear rule), so the line is
computed from the data, not drawn by hand.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
rng = np.random.default_rng(7)

A = rng.multivariate_normal([100, 18], [[90, 10], [10, 25]], 30)   # class A (simulated)
B = rng.multivariate_normal([128, 36], [[140, 30], [30, 110]], 30)  # class B (simulated)

mA, mB = A.mean(axis=0), B.mean(axis=0)
w = mB - mA                       # direction from class A mean to class B mean
mid = (mA + mB) / 2               # midpoint between the two means
new = np.array([118.0, 30.0])     # unknown sample (star)

def decide(x):
    return "B" if (x - mid) @ w > 0 else "A"

accA = np.mean([decide(x) == "A" for x in A])
accB = np.mean([decide(x) == "B" for x in B])
print(f"accuracy on the 60 simulated samples: A {accA:.2f}, B {accB:.2f}")
print(f"new sample {new} -> class {decide(new)}")

# boundary: points x with (x - mid) . w = 0
t = np.linspace(60, 170, 200)
direction = np.array([-w[1], w[0]])
direction = direction / np.linalg.norm(direction)
line = mid + np.outer(t - mid[0], direction / direction[0])

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.scatter(A[:, 0], A[:, 1], marker="o", color="#6a9fd6", label="class A (simulated)")
ax.scatter(B[:, 0], B[:, 1], marker="x", color="#d97757", label="class B (simulated)")
ax.plot(line[:, 0], line[:, 1], color="#333333", lw=1.6, label="decision line")
ax.scatter([new[0]], [new[1]], marker="*", s=220, color="#f2c94c", edgecolor="#333333", zorder=5,
           label="unknown sample")
ax.set_xlim(60, 170)
ax.set_ylim(0, 75)
ax.set_xlabel(r"mean gray level $x_1$")
ax.set_ylabel(r"gray-level std $x_2$")
ax.grid(alpha=0.3)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig("assets/figures/lec01_fig1.png", dpi=200)
print("saved assets/figures/lec01_fig1.png")
