"""Figure code: lec02-bn-inference-complexity.

Tree network with seven binary/ L-valued nodes (s, u, v, x, y, w, z).
Brute force marginalizes out five variables to get P(s | z = z0), costing
L^5 operations when each variable takes L values. Factoring the sum inward
along the graph structure brings this down to the L^2 order.

The two curves are the analytic expressions L^5 and L^2; no point is placed
by hand. Annotation values are read off the curves at L = 10.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
brute_c = "#c0392b"
fact_c = "#2b5fa5"

L = np.linspace(1.0, 12.0, 600)
brute = L ** 5
fact = L ** 2

fig, ax = plt.subplots(figsize=(8.4, 5.4))
ax.plot(L, brute, color=brute_c, lw=2.4, label=r"brute force: $L^5$")
ax.plot(L, fact, color=fact_c, lw=2.4, label=r"factored message passing: $L^2$")

L0 = 10.0
b0, f0 = L0 ** 5, L0 ** 2
ax.plot([L0, L0], [f0, b0], color="#888888", ls=":", lw=1.4, zorder=1)
ax.plot([L0], [b0], "o", color=brute_c, ms=6, zorder=3)
ax.plot([L0], [f0], "o", color=fact_c, ms=6, zorder=3)
ax.annotate(rf"$L=10$: ${b0:.0f}$ ops", (L0, b0), textcoords="offset points",
            xytext=(-14, 12), fontsize=9.5, color=brute_c, ha="right")
ax.annotate(rf"$L=10$: ${f0:.0f}$ ops", (L0, f0), textcoords="offset points",
            xytext=(-14, -16), fontsize=9.5, color=fact_c, ha="right")
ax.annotate("", xy=(L0 + 0.35, b0), xytext=(L0 + 0.35, f0),
            arrowprops=dict(arrowstyle="<|-|>", color="#555555", lw=1.2))
ax.text(L0 + 0.55, np.sqrt(b0 * f0), "factor\n1000", fontsize=9,
        color="#555555", va="center")

ax.set_yscale("log")
ax.set_xlim(1, 12)
ax.set_ylim(1, brute[-1] * 1.6)
ax.set_xlabel(r"number of values per variable, $L$")
ax.set_ylabel("number of operations (log scale)")
ax.set_title("Factoring the sum inward: a tree inference cost drops from $L^5$ to the $L^2$ order",
             fontsize=10.5)
ax.legend(frameon=False, fontsize=9.5, loc="upper left")
ax.grid(alpha=0.3, which="both")

fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-inference-complexity.png", dpi=200)
print("saved assets/figures/lec02-bn-inference-complexity.png")
print("L=10 brute", b0, "factored", f0, "ratio", b0 / f0)
