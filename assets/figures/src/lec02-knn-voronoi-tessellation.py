"""Figure code: lec02-knn-voronoi-tessellation.

Voronoi tessellation for the 1-nearest-neighbour rule (Figure 2.26 analogue).
Each training point owns the polygonal cell of points closer to it than to
any other training point. Cell colour = the class of its owner.

The cells are computed from the coordinates with scipy.spatial.Voronoi;
nothing is hand-placed. Two query points show that a k=1 decision is just
"which cell am I standing in".
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

plt.rcParams["mathtext.fontset"] = "cm"
C_A, C_B = "#6a9fd6", "#d97757"
C_A_L, C_B_L = "#c9ddf0", "#f4d3c5"

rng = np.random.default_rng(7)
pts = rng.uniform(-3.0, 3.0, size=(18, 2))
cls = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# far mirror points so every real cell is bounded
mirror = 12.0 * np.c_[np.cos(np.linspace(0, 2 * np.pi, 12, endpoint=False)),
                       np.sin(np.linspace(0, 2 * np.pi, 12, endpoint=False))]
all_pts = np.vstack([pts, mirror])
vor = Voronoi(all_pts)

fig, ax = plt.subplots(figsize=(6.8, 6.4))
for i in range(len(pts)):
    region = vor.regions[vor.point_region[i]]
    if not region or -1 in region:
        continue
    poly = vor.vertices[region]
    ax.fill(poly[:, 0], poly[:, 1],
            color=(C_A_L if cls[i] == 0 else C_B_L), alpha=0.9, zorder=1)

for ridge, rv in zip(vor.ridge_vertices, vor.ridge_points):
    if -1 in ridge:
        continue
    if rv[0] < len(pts) and rv[1] < len(pts):
        p1, p2 = vor.vertices[ridge]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#222222", lw=1.5,
                zorder=3)

ax.scatter(pts[cls == 0, 0], pts[cls == 0, 1], s=70, c=C_A,
           edgecolors="white", linewidths=1.0, zorder=5, label="class A owner")
ax.scatter(pts[cls == 1, 0], pts[cls == 1, 1], s=70, c=C_B,
           edgecolors="white", linewidths=1.0, zorder=5, label="class B owner")

# two query points and the arrow to the closest training point
for q in [np.array([-1.35, -0.25]), np.array([0.72, 0.48])]:
    d = np.linalg.norm(pts - q, axis=1)
    j = int(np.argmin(d))
    ax.plot([q[0]], [q[1]], marker="*", ms=17, mfc="white", mec="#111111",
            mew=1.5, zorder=6)
    ax.annotate("", xy=pts[j], xytext=q,
                arrowprops=dict(arrowstyle="->", lw=1.6, color="#111111"))

ax.text(-3.05, 2.98, "each cell = points closer to that\n"
                     "training sample (k=1, Euclidean)",
        fontsize=8.5, va="top")
ax.set_aspect("equal")
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-3.2, 3.2)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("Voronoi tessellation: the $k{=}1$ rule tiles the plane", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="lower left")
ax.grid(alpha=0.18)

fig.tight_layout()
fig.savefig("assets/figures/lec02-knn-voronoi-tessellation.png", dpi=200)
print("saved lec02-knn-voronoi-tessellation.png")
print("classes A/B:", int((cls == 0).sum()), int((cls == 1).sum()))
