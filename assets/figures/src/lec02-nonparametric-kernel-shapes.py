"""Figure code: lec02-nonparametric-kernel-shapes.

Left: the two kernel choices, the box kernel of side b = 1.0 and the standard
Gaussian kernel, both drawn as densities.
Right: the Parzen estimate for b = 1.0 built from the five sample points
-1.5, -0.5, 0.5, 1.5, 2.5.  Each thin curve is one kernel 1/(N*b) * phi((x_i-x)/b);
the thick curve is their sum, which is p_hat(x).  The value at x = 0 is 0.1961.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_BOX = "#6a9fd6"
C_GAUSS = "#dc2626"
C_THIN = "#bbbbbb"


def phi(z):
    return np.exp(-0.5 * z ** 2) / np.sqrt(2 * np.pi)


b = 1.0
samples = np.array([-1.5, -0.5, 0.5, 1.5, 2.5])
n = len(samples)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.6, 4.4))

# --- left: kernel shapes ---
u = np.linspace(-3, 3, 800)
box = np.where(np.abs(u) <= b / 2, 1.0 / b, 0.0)
axL.plot(u, box, color=C_BOX, lw=2.2, label=r"box kernel, side $b=1.0$")
axL.plot(u, phi(u), color=C_GAUSS, lw=2.2, label=r"Gaussian kernel $\mathcal{N}(0,1)$")
axL.fill_between(u, 0, box, color=C_BOX, alpha=0.15)
axL.axvline(-b / 2, color="#888888", ls=":", lw=1.0)
axL.axvline(b / 2, color="#888888", ls=":", lw=1.0)
axL.annotate(r"$b/2$", (b / 2, 0.62), textcoords="offset points", xytext=(4, 0), fontsize=9)
axL.annotate(r"$-b/2$", (-b / 2, 0.62), textcoords="offset points", xytext=(-30, 0), fontsize=9)
axL.set_xlim(-3, 3)
axL.set_ylim(0, 1.25)
axL.set_xlabel("$u$")
axL.set_ylabel(r"kernel $\phi(u)$")
axL.set_title("(a) box kernel vs Gaussian kernel", fontsize=10)
axL.legend(frameon=False, fontsize=9, loc="upper right")
axL.grid(alpha=0.3)

# --- right: Parzen sum for b = 1.0 ---
x = np.linspace(-4, 5, 1000)
acc = np.zeros_like(x)
for xi in samples:
    k = phi((xi - x) / b) / (n * b)
    acc += k
    axR.plot(x, k, color=C_THIN, lw=1.0)
axR.plot(x, acc, color=C_GAUSS, lw=2.4, label=r"$\hat{p}(x)$, the average")
axR.plot(samples, np.full_like(samples, -0.007), "|", color="#333333", ms=9)
axR.plot(0.0, float(np.mean(phi((samples - 0.0) / b)) / b), "o", color=C_GAUSS, ms=7)
axR.annotate(r"$\hat{p}(0)=0.196$", (0.0, 0.196), textcoords="offset points",
             xytext=(14, 30), fontsize=9.5, color=C_GAUSS,
             arrowprops=dict(arrowstyle="-", color=C_GAUSS, lw=0.9))
axR.set_xlim(-4, 5)
axR.set_ylim(-0.02, 0.32)
axR.set_xlabel("$x$")
axR.set_ylabel(r"density estimate $\hat{p}(x)$")
axR.set_title(r"(b) Parzen estimate, $b=1.0$, $N=5$", fontsize=10)
axR.legend(frameon=False, fontsize=9, loc="upper left")
axR.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-nonparametric-kernel-shapes.png", dpi=200)
print("saved assets/figures/lec02-nonparametric-kernel-shapes.png")
print("kernel values at x=0:", np.round(phi((samples - 0.0) / b), 4))
print("sum:", round(float(phi((samples - 0.0) / b).sum()), 4),
      "phat(0):", round(float(np.mean(phi((samples - 0.0) / b)) / b), 4))
