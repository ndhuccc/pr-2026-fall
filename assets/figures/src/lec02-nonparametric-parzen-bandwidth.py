"""Figure code: lec02-nonparametric-parzen-bandwidth.

Top row: Gaussian-kernel Parzen estimates on the same N=80 bimodal sample,
with a too-small, an optimal, and a too-large bandwidth b.
Bottom row: RMS error against b (log x-axis) for N=80 and N=320, with the
optimal b of each marked.  All curves are computed from the formulas in the
lecture; the optimal b is the argmin of the RMS curve.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_TRUE = "#555555"
C_RED = "#dc2626"
C_GRAY = "#8a8a8a"

LO, HI = -3.5, 4.0
GRID = np.linspace(LO, HI, 1200)
BS = np.geomspace(0.03, 1.5, 200)


def true_pdf(x):
    g1 = np.exp(-0.5 * ((x + 1.5) / 0.4) ** 2) / (np.sqrt(2 * np.pi) * 0.4)
    g2 = np.exp(-0.5 * ((x - 1.5) / 0.5) ** 2) / (np.sqrt(2 * np.pi) * 0.5)
    return 0.5 * g1 + 0.5 * g2


def parzen(x, xs, b):
    z = (x[:, None] - xs[None, :]) / b
    return np.exp(-0.5 * z ** 2).sum(axis=1) / (len(xs) * np.sqrt(2 * np.pi) * b)


def sample(n, seed):
    rng = np.random.default_rng(seed)
    comp = rng.random(n) < 0.5
    return np.where(comp, rng.normal(-1.5, 0.4, n), rng.normal(1.5, 0.5, n))


def rms_curve(xs):
    return np.array([np.sqrt(np.mean((parzen(GRID, xs, b) - true_pdf(GRID)) ** 2)) for b in BS])


xs80 = sample(80, 113)
xs320 = sample(320, 7)
r80, r320 = rms_curve(xs80), rms_curve(xs320)
i80, i320 = int(r80.argmin()), int(r320.argmin())

fig = plt.figure(figsize=(11.6, 6.6))
gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 1.05], hspace=0.55, wspace=0.22)

panel_b = [0.05, float(BS[i80]), 1.20]
labels = ["too small", "optimal", "too large"]
for j, b in enumerate(panel_b):
    ax = fig.add_subplot(gs[0, j])
    ax.plot(GRID, true_pdf(GRID), color=C_TRUE, ls="--", lw=1.6, label="true $p(x)$")
    ax.plot(GRID, parzen(GRID, xs80, b), color=C_RED, lw=1.8, label=r"$\hat{p}(x)$")
    ax.plot(xs80, np.full_like(xs80, -0.035), "|", color="#333333", ms=5)
    err = np.sqrt(np.mean((parzen(GRID, xs80, b) - true_pdf(GRID)) ** 2))
    tag = " (optimal)" if j == 1 else ""
    ax.set_title(f"$b$ = {b:.2f}{tag}\nRMS = {err:.3f}", fontsize=9.5)
    ax.set_xlim(LO, HI)
    ax.set_ylim(-0.05, 0.85)
    ax.set_xlabel("$x$")
    ax.grid(alpha=0.3)
    if j == 0:
        ax.set_ylabel("density")
        ax.legend(frameon=False, fontsize=8, loc="upper left")
    for bv in panel_b:
        ax.axvline(bv, color="#bbbbbb", lw=0.7, ls=":")

axb = fig.add_subplot(gs[1, :])
axb.plot(BS, r80, color=C_RED, lw=2.0, label="N = 80")
axb.plot(BS, r320, color=C_GRAY, lw=2.0, ls="--", label="N = 320")
axb.plot(BS[i80], r80[i80], "o", color=C_RED, ms=6)
axb.plot(BS[i320], r320[i320], "s", color=C_GRAY, ms=6)
axb.annotate(f"$b^*$ = {BS[i80]:.2f}\nRMS = {r80[i80]:.3f}",
             (BS[i80], r80[i80]), textcoords="offset points", xytext=(12, 40),
             fontsize=9, color=C_RED,
             arrowprops=dict(arrowstyle="-", color=C_RED, lw=0.8))
axb.annotate(f"$b^*$ = {BS[i320]:.2f}\nRMS = {r320[i320]:.3f}",
             (BS[i320], r320[i320]), textcoords="offset points", xytext=(-58, 18),
             fontsize=9, color=C_GRAY,
             arrowprops=dict(arrowstyle="-", color=C_GRAY, lw=0.8))
axb.annotate("noise region", (0.04, 0.145), fontsize=9, color="#333333")
axb.annotate("bias region", (0.72, 0.145), fontsize=9, color="#333333")
axb.axvline(BS[i80], color=C_RED, lw=0.8, ls=":")
axb.axvline(BS[i320], color=C_GRAY, lw=0.8, ls=":")
axb.set_xscale("log")
axb.set_xlim(BS[0], BS[-1])
axb.set_ylim(0, 0.17)
axb.set_xlabel("bandwidth $b$ (log scale)")
axb.set_ylabel("RMS error")
axb.legend(frameon=False, fontsize=9, loc="upper right")
axb.grid(alpha=0.3, which="both")
fig.suptitle("Gaussian-kernel Parzen estimate: bandwidth trades noise against bias", fontsize=11.5)
fig.savefig("assets/figures/lec02-nonparametric-parzen-bandwidth.png", dpi=200)
print("saved assets/figures/lec02-nonparametric-parzen-bandwidth.png")
print(f"N=80: b*={BS[i80]:.4f} RMS*={r80[i80]:.4f}")
print(f"N=320: b*={BS[i320]:.4f} RMS*={r320[i320]:.4f}")
for b in panel_b:
    print(f"  b={b:.2f}: RMS={np.sqrt(np.mean((parzen(GRID, xs80, b) - true_pdf(GRID)) ** 2)):.4f}")
