"""Figure code: lec02-nonparametric-knn-classification.

k-nearest-neighbour density estimation used for classification.  The query
point is (0.7, 0.6) with k = 5.  Both classes are drawn around that point: the
five nearest red neighbours sit inside a circle of radius rho, the five
nearest black neighbours need a circle of radius 2*rho, so V2/V1 = 0.25.

The two clouds are placed so that the radii match the lecture example exactly:
five red points at distance rho, five black points at distance 2*rho.  The
background shading is the kNN density score (log ratio), computed from the
same radii rule.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C1 = "#333333"
C2 = "#dc2626"

query = np.array([0.7, 0.6])
k = 5
rho = 0.1 * np.sqrt(2)


def ring_points(center, radius, start_deg, count):
    ang = np.deg2rad(start_deg + np.arange(count) * 18.0)
    return np.column_stack([center[0] + radius * np.cos(ang),
                            center[1] + radius * np.sin(ang)])


# Five red points exactly on the radius-rho circle, five black on the 2*rho circle.
red = ring_points(query, rho, 10, k)
black = ring_points(query, 2 * rho, 100, k)
extra_red = np.array([[1.9, 1.7], [2.2, 0.9], [1.6, 0.2]])
extra_black = np.array([[-0.9, 1.6], [-0.4, 0.1], [-1.2, 0.6]])
red = np.vstack([red, extra_red])
black = np.vstack([black, extra_black])

fig, ax = plt.subplots(figsize=(7.2, 6.4))

xs = np.linspace(-2.6, 3.0, 400)
ys = np.linspace(-1.3, 2.6, 400)
XX, YY = np.meshgrid(xs, ys)
pts = np.column_stack([XX.ravel(), YY.ravel()])


def kth_radius(points, p):
    d = np.sqrt(((points - p) ** 2).sum(axis=1))
    return np.sort(d)[k - 1]


score = np.empty(len(pts))
for idx, p in enumerate(pts):
    r1 = kth_radius(black, p)
    r2 = kth_radius(red, p)
    score[idx] = np.log((k / (len(red) * np.pi * r2 ** 2)) /
                        (k / (len(black) * np.pi * r1 ** 2)))
score = score.reshape(XX.shape)
ax.contourf(XX, YY, score, levels=[-4, 0, 4], colors=["#f2c9c0", "#cfd9e6"], alpha=0.55)
ax.contour(XX, YY, score, levels=[0], colors="#333333", linewidths=1.6)

ax.scatter(black[:, 0], black[:, 1], s=55, c=C1, marker="o",
           edgecolor="white", linewidth=0.8, label=r"$\omega_1$ (black class)", zorder=3)
ax.scatter(red[:, 0], red[:, 1], s=55, c=C2, marker="o",
           edgecolor="white", linewidth=0.8, label=r"$\omega_2$ (red class)", zorder=3)
ax.plot(query[0], query[1], "*", ms=18, color="#f0b429", markeredgecolor="#333333",
        markeredgewidth=0.8, zorder=5, label="query $(0.7, 0.6)$")

th = np.linspace(0, 2 * np.pi, 300)
ax.plot(query[0] + rho * np.cos(th), query[1] + rho * np.sin(th),
        color=C2, lw=1.8, label=r"$V_2$: radius $\rho$")
ax.plot(query[0] + 2 * rho * np.cos(th), query[1] + 2 * rho * np.sin(th),
        color=C1, lw=1.8, ls="--", label=r"$V_1$: radius $2\rho$")

ax.annotate(r"$\rho$", (0.575, 0.545), fontsize=12, color=C2)
ax.annotate(r"$2\rho$", (0.60, 0.325), fontsize=12, color=C1)
ax.annotate(r"$V_2/V_1 = 0.25 < N_1/N_2 \approx 0.967$" + "\n" + r"decide $\omega_2$",
            (-2.5, -1.05), fontsize=10)

ax.set_xlim(-2.6, 3.0)
ax.set_ylim(-1.3, 2.6)
ax.set_aspect("equal")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("kNN density estimate with k = 5: smaller volume means denser class", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper left", ncol=2)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig("assets/figures/lec02-nonparametric-knn-classification.png", dpi=200)
print("saved assets/figures/lec02-nonparametric-knn-classification.png")
print("rho =", rho, "V2 =", np.pi * rho ** 2, "V1 =", 4 * np.pi * rho ** 2,
      "V2/V1 =", 0.25, "N1/N2 =", 1.0)
