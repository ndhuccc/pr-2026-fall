"""Figure code: lec02-parameter-estimation-ml-peak.

The likelihood of the mean for five samples: x = [2.1, 2.7, 2.4, 2.8, 2.5].
Sample mean xbar = 2.5, S = sum (x_k - xbar)^2 = 0.30.
Likelihood L(mu) = prod_k N(x_k; mu, 1); log-likelihood L = -S/2 - N/2 ln(2 pi)
up to the constant; peaks at mu = 2.5.
The left panel shows the likelihood, the right panel the log-likelihood.
Both peak at the same mu, which is why taking logs is safe.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

x = np.array([2.1, 2.7, 2.4, 2.8, 2.5])
N = x.size
xbar = x.mean()

mu = np.linspace(1.0, 4.0, 800)
like = np.exp(-((x[None, :] - mu[:, None]) ** 2).sum(axis=1) / 2.0) / (2 * np.pi) ** (N / 2)
loglike = np.log(like)
# constant offset removed so the log panel shows a readable level
c = -N / 2.0 * np.log(2 * np.pi)
loglike_shift = loglike - c

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))

ax = axes[0]
ax.plot(mu, like, color=c1, lw=2.2)
ax.axvline(xbar, color="#333333", ls="--", lw=1.2)
ax.plot([xbar], [like.max()], "o", color=c2, ms=7, zorder=5)
ax.annotate(r"peak at $\bar{x}=\hat{\mu}_{ML}=2.5$", (xbar, like.max()),
            textcoords="offset points", xytext=(14, -42), fontsize=9, color=c2)
ax.set_xlabel(r"candidate mean $\mu$")
ax.set_ylabel(r"likelihood $L(\mu)$")
ax.set_title(r"(a) likelihood $L(\mu)=\prod_k p(x_k;\mu)$", fontsize=10)
ax.set_xlim(1.0, 4.0)
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(mu, loglike_shift, color=c2, lw=2.2)
ax.axvline(xbar, color="#333333", ls="--", lw=1.2)
ax.plot([xbar], [loglike_shift.max()], "o", color=c1, ms=7, zorder=5)
ax.annotate(r"same peak at $\mu=2.5$", (xbar, loglike_shift.max()),
            textcoords="offset points", xytext=(10, -22), fontsize=9, color=c1)
ax.set_xlabel(r"candidate mean $\mu$")
ax.set_ylabel(r"log-likelihood (offset)")
ax.set_title(r"(b) log-likelihood $\ln L(\mu)$", fontsize=10)
ax.set_xlim(1.0, 4.0)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-parameter-estimation-ml-peak.png", dpi=200)
print("saved assets/figures/lec02-parameter-estimation-ml-peak.png")
print("xbar", round(xbar, 4), "S", round(float(((x - xbar) ** 2).sum()), 4))
print("argmax mu", round(float(mu[loglike.argmax()]), 4))
for m in (2.0, 2.5, 3.0):
    ll = float(np.log(np.exp(-((x - m) ** 2).sum() / 2.0) / (2 * np.pi) ** (N / 2)))
    print("mu", m, "loglike", round(ll, 4), "like", round(float(np.exp(ll)), 6))
