"""Figure code for lec02-perceptron-mlp, KP1 (biological neuron and McCulloch-Pitts neuron).
Draws three figures. Labels are English only.
  lec02-perceptron-mlp-neuron-anatomy : biological neuron, parts and the sum-then-threshold mechanism
  lec02-perceptron-mlp-mp-threshold   : worked example x=(1,0,1), z=2, thresholds 1, 2, 3
  lec02-perceptron-mlp-mp-gates       : AND (theta=2), OR (theta=1), NOT (w=-1, w0=0.5) as one neuron
Light PNG (dpi 200) goes to assets/figures/. If env DECK_WORK is set, a dark SVG for the slides goes to $DECK_WORK/assets/figures/.
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))
THEMES = {
    "light": dict(text="#222222", muted="#666666", main="#c2410c", ref="#1d6fb8", aux="#0f766e", warn="#b91c1c",
                  ok="#2f855a", edge="#b7791f", soft="#f1f5f9", onfill="white"),
    "dark": dict(text="#f2ede4", muted="#b7b0a5", main="#d97757", ref="#6a9fd6", aux="#5fb8a8", warn="#e07a70",
                 ok="#7dbb8c", edge="#e0995f", soft="#2a241d", onfill="#1c1712"),
}


def setup(theme, w, h):
    t = THEMES[theme]
    plt.rcParams.update({"mathtext.fontset": "cm", "svg.fonttype": "path", "text.color": t["text"],
                         "axes.labelcolor": t["text"], "axes.edgecolor": t["muted"],
                         "xtick.color": t["muted"], "ytick.color": t["muted"]})
    fig = plt.figure(figsize=(w / 100, h / 100))
    fig.patch.set_facecolor("none" if theme == "dark" else "white")
    return fig, t


FM = 1.0   # font multiplier: the dark slide version is shown at ~60% size, so its text is enlarged to stay readable


def px(size_px):
    """Font size in node px -> points (1 inch == 100 px)."""
    return size_px * 0.72 * FM


def save(fig, name, theme):
    if theme == "light":
        fig.savefig(os.path.join(OUT, name + ".png"), dpi=200, facecolor="white")
    else:
        d = os.environ.get("DECK_WORK")
        if d:
            os.makedirs(os.path.join(d, "assets", "figures"), exist_ok=True)
            fig.savefig(os.path.join(d, "assets", "figures", name + ".svg"), transparent=True)
    plt.close(fig)


def arrow(ax, p, q, color, lw=2.4, ms=18):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw))


def anatomy(theme):
    global FM
    FM = 1.75 if theme == "dark" else 1.0
    W, H = 1100, 440
    fig, t = setup(theme, W, H)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    fs = px(20)
    sx, sy = 430, 170
    # three dendrite branches converge on the soma; arrows show incoming signals
    for y0, yb in [(300, 215), (170, 170), (50, 125)]:
        ax.plot([90, 200, 320], [y0, y0 + (yb - y0) * 0.4, yb], color=t["ref"], lw=3.4, solid_capstyle="round")
        ax.plot([90, 55], [y0, y0 + 22], color=t["ref"], lw=2.4)
        ax.plot([90, 55], [y0, y0 - 22], color=t["ref"], lw=2.4)
        arrow(ax, (14, y0), (50, y0), t["muted"], lw=1.8, ms=14)
    ax.add_patch(Ellipse((sx, sy), 220, 150, fc=t["soft"], ec=t["main"], lw=3.4, zorder=2))
    ax.add_patch(Circle((sx, sy), 34, fc="none", ec=t["edge"], lw=2.6, zorder=3))
    ax.plot([540, 760], [170, 170], color=t["aux"], lw=7, solid_capstyle="round")
    arrow(ax, (620, 200), (720, 200), t["aux"], lw=3, ms=22)
    for dy in (-34, 0, 34):
        ax.plot([760, 800], [170, 170 + dy], color=t["aux"], lw=3.4)
        ax.add_patch(Circle((806, 170 + dy), 9, fc=t["aux"], ec=t["aux"]))
    ax.plot([826, 880], [170, 170], color=t["edge"], lw=3, ls=(0, (3, 3)))
    ax.text(853, 200, r"$\rightleftarrows$", ha="center", va="center", fontsize=fs, color=t["edge"])
    ax.add_patch(Ellipse((985, 170), 150, 110, fc=t["soft"], ec=t["muted"], lw=2.4))
    ax.text(985, 170, "next\nneuron", ha="center", va="center", fontsize=px(18), color=t["muted"])
    kw = dict(fontsize=fs, ha="center", va="center")
    dark = theme == "dark"
    ax.text(150, 385, "Dendrites" if dark else "Dendrites\n(receive signals)", color=t["ref"], **kw)
    ax.text(430, 385, "Soma" if dark else "Soma\n(adds signals up)", color=t["main"], **kw)
    ax.text(430, 226, "Nucleus", color=t["edge"], fontsize=px(15), ha="center", va="center", zorder=4)
    ax.text(650, 112, "Axon" if dark else "Axon\n(carries the pulse)", color=t["aux"], **kw)
    ax.text(880, 262, "Synapse" if dark else "Synapse\n(chemical gap)", color=t["edge"], **kw)
    if theme == "dark":
        ax.text(550, 32, "add up  →  ≥ threshold ?  →  fire / silent", ha="center", va="center", fontsize=px(22), color=t["text"])
        save(fig, "lec02-perceptron-mlp-neuron-anatomy", theme)
        return
    ax.text(550, 32, "many inputs add up  →  total ≥ threshold ?  →  fire / stay silent", ha="center", va="center",
            fontsize=px(22), color=t["text"])
    save(fig, "lec02-perceptron-mlp-neuron-anatomy", theme)


def threshold(theme):
    global FM
    FM = 1.65 if theme == "dark" else 1.0
    W, H = 1100, 440
    fig, t = setup(theme, W, H)
    ax = fig.add_axes([0.04, 0.2, 0.92, 0.7])
    x = np.array([1, 0, 1])
    z = int(x.sum())
    left = 0
    cols = [t["ref"], t["muted"], t["aux"]]
    for i, v in enumerate(x):
        if v:
            ax.barh(0, v, left=left, height=0.5, color=cols[i], ec=t["text"], lw=1.5)
            ax.text(left + v / 2, 0, rf"$x_{i + 1}=1$", ha="center", va="center", color=t["onfill"], fontsize=px(22),
                    fontweight="bold")
            left += v
    ax.text(0.5, -0.43, (r"$x_2=0$" if theme == "dark" else r"$x_2=0$ adds nothing"), ha="center", va="center", color=t["muted"], fontsize=px(18))
    for th, ok in [(1, True), (2, True), (3, False)]:
        c = t["ok"] if ok else t["warn"]
        ax.plot([th, th], [-0.3, 0.45], color=c, lw=3, ls="--")
        ax.text(th, 0.5, rf"$\theta={th}$" + "\n" + (r"$o=1$ fires" if ok else r"$o=0$ silent"), ha="center", va="bottom",
                color=c, fontsize=px(20), fontweight="bold")
    ax.set_xlim(-0.05, 3.5)
    ax.set_ylim(-0.55, 1.0)
    ax.set_yticks([])
    ax.set_xticks([0, 1, 2, 3])
    ax.tick_params(labelsize=px(20))
    ax.set_xlabel((r"total  $z=x_1+x_2+x_3=2$" if theme == "dark" else r"accumulated total  $z=x_1+x_2+x_3$  (here $z=2$)"), fontsize=px(20))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_facecolor("none")
    save(fig, "lec02-perceptron-mlp-mp-threshold", theme)


def gates(theme):
    global FM
    FM = 1.3 if theme == "dark" else 1.0
    W, H = 1160, 400
    fig, t = setup(theme, W, H)
    fs = px(19)

    def dots(ax, pts, y_of=lambda p: p[1]):
        for p in pts:
            o = p[-1]
            ax.scatter([p[0]], [y_of(p)], s=300, color=t["main"] if o else "none", edgecolor=t["main"] if o else t["ref"],
                       lw=2.8, zorder=3)

    def plane(rect, title, pts, theta):
        ax = fig.add_axes(rect)
        ax.set_facecolor("none")
        xs = np.linspace(-0.4, 1.4, 50)
        ax.fill_between(xs, theta - xs, 1.5, color=t["main"], alpha=0.14)
        ax.plot(xs, theta - xs, color=t["edge"], lw=3)
        dots(ax, pts)
        ax.set_xlim(-0.4, 1.4)
        ax.set_ylim(-0.4, 1.4)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xlabel(r"$x_1$", fontsize=fs)
        ax.set_ylabel(r"$x_2$", fontsize=fs)
        ax.set_title(title, fontsize=fs, pad=8)
        ax.tick_params(labelsize=fs)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    plane([0.07, 0.29, 0.24, 0.51], r"AND:  $\theta=2$", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)], 2)
    plane([0.40, 0.29, 0.24, 0.51], r"OR:  $\theta=1$", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)], 1)
    n = fig.add_axes([0.73, 0.29, 0.24, 0.51])
    n.set_facecolor("none")
    n.axvspan(-0.4, 0.5, color=t["main"], alpha=0.14)
    n.axvline(0.5, color=t["edge"], lw=3)
    for xv, ov in [(0, 1), (1, 0)]:
        n.scatter([xv], [0], s=300, color=t["main"] if ov else "none", edgecolor=t["main"] if ov else t["ref"], lw=2.8, zorder=3)
    n.set_xlim(-0.4, 1.4)
    n.set_ylim(-0.6, 0.6)
    n.set_yticks([])
    n.set_xticks([0, 1])
    n.set_xlabel(r"$x$", fontsize=fs)
    n.tick_params(labelsize=fs)
    n.set_title(r"NOT:  $w=-1,\ w_0=0.5$", fontsize=fs, pad=8)
    for s in ("top", "right", "left"):
        n.spines[s].set_visible(False)
    fig.text(0.5, 0.025, "filled = output 1,  open = output 0;  shaded side = where the neuron fires", ha="center", va="center",
             fontsize=px(19), color=t["muted"])
    save(fig, "lec02-perceptron-mlp-mp-gates", theme)


if __name__ == "__main__":
    for th in ("light", "dark"):
        anatomy(th)
        threshold(th)
        gates(th)
    print("ok")
