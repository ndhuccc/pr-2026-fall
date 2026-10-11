#!/usr/bin/env python3
"""audit_deck.py -- automatic audit of a JianBauDau deck (slides/lecNN.jbd.json) for the checks a program can do.

    py .agents/skills/view-from-text/tools/audit_deck.py slides/lec03.jbd.json            # bilingual course deck (default)
    py .agents/skills/view-from-text/tools/audit_deck.py slides/lec03.jbd.json --monolingual

Covers AUDIT_CHECKLIST.md: A (format), B (cameras, connector colours, FRAME STYLE), E10 (contrast incl. frame titles),
D (fonts, titles), H5 (step / reticle structure), G14 (image alt), L (bilingual layout).
It does NOT replace the visual checks: run preview_deck.py and look at the contact sheets, then open the deck in JianBauDau.
Exit code 1 when there is any FAIL.
"""
import argparse
import json
import math
import re
import sys

W, H, HEADROOM, PITCH = 1280, 720, 100, 1440
STD_FRAME_STYLE = {"fill": "transparent", "stroke": "transparent", "textColor": "#f2ede4", "fontSize": 22, "radius": 0}
STD_FRAME_KEYS = {"childSceneId", "previewMode", "padding", "clip"}
CJK = re.compile(r"[㐀-鿿豈-﫿]")
MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$", re.S)


def en_words(text):
    """Number of English words (2+ letters) outside formulas. A text block counts as bilingual with at least 3."""
    return len(re.findall(r"[A-Za-z]{2,}", MATH.sub(" ", text)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--monolingual", action="store_true", help="skip the bilingual checks (only when the teacher asked for Chinese only)")
    args = ap.parse_args()
    doc = json.load(open(args.deck, encoding="utf-8"))
    S, N, ST = doc["scenes"], doc["nodes"], doc["steps"]
    fails, warns = [], []
    F = lambda code, msg: fails.append(f"{code} {msg}")
    Wn = lambda code, msg: warns.append(f"{code} {msg}")

    # ------------------------------------------------------------ A: format
    root = doc.get("rootSceneId")
    if doc.get("schemaVersion") != 3: F("A1", "schemaVersion must be 3")
    if root not in S or S[root].get("parentFrameId") is not None: F("A1", "root scene")
    claimed = {}
    for sid, sc in S.items():
        if sc["id"] != sid: F("A3", f"scene id mismatch {sid}")
        cam = sc["camera"]
        if not (cam["zoom"] > 0 and all(math.isfinite(cam[k]) for k in ("x", "y", "rotation"))): F("A2", sid)
        for nid in sc["nodeIds"]:
            if nid not in N: F("A3", f"{sid} lists missing node {nid}"); continue
            if N[nid]["sceneId"] != sid: F("A3", f"{nid}.sceneId != {sid}")
            if nid in claimed: F("A4", f"{nid} listed by two scenes")
            claimed[nid] = sid
    for nid, n in N.items():
        if nid not in claimed: F("A4", f"orphan node {nid}")
        t = n["transform"]
        if not all(math.isfinite(t[k]) for k in ("x", "y", "scaleX", "scaleY", "rotation")) or t["scaleX"] == 0 or t["scaleY"] == 0: F("A5", nid)
        if not (n["width"] > 0 and n["height"] > 0): F("A5", f"{nid} size")
        if n["type"] == "frame":
            cs = n["frame"]["childSceneId"]
            if cs not in S or S[cs]["parentFrameId"] != nid: F("A6", f"frame {nid}")
        if n["type"] == "image" and not n.get("image", {}).get("src"): F("A7", nid)
        if n["type"] == "connector":
            c = n["connector"]
            a, b = c["sourceNodeId"], c["targetNodeId"]
            if a not in N or b not in N or N[a]["sceneId"] != n["sceneId"] or N[b]["sceneId"] != n["sceneId"] or a == b \
                    or N[a]["type"] == "connector" or N[b]["type"] == "connector":
                F("A8", f"connector {nid}")
            for hk in (c["sourceHook"], c["targetHook"]):
                if not (isinstance(hk, int) and 0 <= hk <= 15): F("A8", f"hook {nid}")
            if n["style"]["textColor"].lower() != "#1c1712": F("B1", f"connector label colour {nid}")
            if n["style"].get("stroke") in (None, "transparent") or n["style"].get("borderWidth", 0) < 3: F("B8", f"connector stroke/width {nid}")
    seen_ids = set()
    for i, s in enumerate(ST):
        if s["id"] in seen_ids: F("A10", f"duplicate step id {s['id']}")
        seen_ids.add(s["id"])
        if s["order"] != i: F("K8", "step order must be 0..n-1")
        if not (180 <= s["durationMs"] <= 10000 and 0 <= s["holdMs"] <= 30000 and s["easing"] in ("linear", "easeInOut", "smooth")): F("A10", s["id"])
        if len(s["label"]) > 20: Wn("D3", f"step label longer than 20 chars: {s['label']!r}")
        if re.match(r"^\s*\d+[\s.、)]", s["label"]): F("D3", f"step label starts with a number: {s['label']!r}")
        if "speakerNotes" in s: Wn("J3", "speaker notes present (they are public)")
        t = s["target"]
        if t["sceneId"] not in S: F("A11", s["id"])
        if t["kind"] in ("enter-frame", "scene-overview"): F("H5", f"{t['kind']} must not be used ({s['id']})")
        if t["kind"] == "scene-point" and t.get("referenceViewport") != {"width": W, "height": H}: F("B5", f"referenceViewport {s['id']}")
    if doc["metadata"].get("aspectRatio") != "16:9": Wn("B4", "aspectRatio is not 16:9 (check pitch/zoom constants)")

    # ------------------------------------------------------------ H5 structure + cameras
    frames = {n["id"]: n for n in N.values() if n["type"] == "frame"}
    root_steps = [s for s in ST if s["target"]["sceneId"] == root]
    if len(root_steps) != len(frames): F("H5", f"root scene has {len(root_steps)} steps for {len(frames)} frames")
    for fid, fr in frames.items():
        cx, cy = fr["transform"]["x"] + fr["width"] / 2, fr["transform"]["y"] + fr["height"] / 2
        m = [s for s in root_steps if abs(s["target"]["point"]["x"] - cx) < 1 and abs(s["target"]["point"]["y"] - cy) < 1]
        if len(m) != 1: F("H5", f"frame {fid} has {len(m)} steps (must be exactly 1)")
        pages = [s for s in ST if s["target"]["sceneId"] == fr["frame"]["childSceneId"]]
        if len(pages) < 2: Wn("C5", f"{fr['frame']['childSceneId']} has only {len(pages)} page(s)")
    for s in ST:
        t = s["target"]
        if t["sceneId"] != root and t["kind"] == "scene-point":
            idx = round((t["point"]["x"] - W / 2) / PITCH)
            if abs(t["point"]["x"] - (idx * PITCH + W / 2)) > 0.5 or abs(t["point"]["y"] - (H / 2 - HEADROOM / 2)) > 0.5 or abs(t["zoom"] - H / (H + HEADROOM)) > 1e-6:
                F("B6", f"camera of {s['id']} does not follow the page formula")
    for sid, sc in S.items():
        if sid == root: continue
        for nid in sc["nodeIds"]:
            n = N[nid]
            if n["type"] == "connector": continue
            y, h = n["transform"]["y"], n["height"]
            if y < 0: F("B6", f"{nid} sits in the title-bar headroom (y<0)")
            if y + h > H + 1: F("B3", f"{nid} extends below the page ({y + h:.0f}>720)")
            x = n["transform"]["x"] % PITCH
            if x + n["width"] > W + 1: F("B3", f"{nid} extends past the page width")

    # ------------------------------------------------------------ B9 frame style (the legibility rule)
    for fid, fr in frames.items():
        st = fr["style"]
        std = {k: st.get(k) for k in STD_FRAME_STYLE}
        if {k: (v.lower() if isinstance(v, str) else v) for k, v in std.items()} != STD_FRAME_STYLE or set(st) - set(STD_FRAME_STYLE):
            F("B9", f"frame {fid} style differs from the standard (transparent fill/stroke, textColor #f2ede4, fontSize 22, radius 0): {st}")
        extra = set(fr["frame"]) - STD_FRAME_KEYS
        if extra: F("B9", f"frame {fid} sets {sorted(extra)}; do not set title colours/sizes (the title bar background is not under our control)")
        if "\n" in fr["text"] or len(fr["text"]) > 16: Wn("B9", f"frame title should be one short line (<=16 chars): {fr['text']!r}")

    # ------------------------------------------------------------ E10 contrast
    def parse(c):
        if c == "transparent": return None
        m = re.match(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", c)
        if m: return (int(m[1]), int(m[2]), int(m[3]), float(m[4]) if m[4] else 1.0)
        h = c.lstrip("#")
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)

    def over(fg, bg):
        a = fg[3]
        return tuple(round(fg[i] * a + bg[i] * (1 - a)) for i in range(3)) + (1.0,)

    def lum(c):
        f = lambda v: (v / 255 / 12.92) if v / 255 <= 0.03928 else ((v / 255 + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])

    def cr(a, b):
        la, lb = sorted((lum(a), lum(b)), reverse=True)
        return (la + 0.05) / (lb + 0.05)

    canvas = parse("#151513")
    for nid, n in N.items():
        if n["type"] not in ("text", "shape", "frame"): continue
        st = n["style"]
        bg = canvas
        f = parse(st["fill"])
        if f: bg = over(f, canvas)
        r = cr(parse(st["textColor"]), bg)
        if r < 4.5: F("E10", f"contrast {r:.2f} on {nid}")
        if st["fontSize"] < 16: F("D4", f"font {st['fontSize']}px on {nid}")

    # ------------------------------------------------------------ pages: titles, fonts, bilingual layout
    pages = {}
    for sid, sc in S.items():
        if sid == root: continue
        for nid in sc["nodeIds"]:
            n = N[nid]
            if n["type"] == "connector": continue
            pages.setdefault((sid, int((n["transform"]["x"] + n["width"] / 2) // PITCH)), []).append(n)
    no_en_nodes = total_nodes = 0
    for (sid, idx), ns in sorted(pages.items()):
        tag = f"{sid}#p{idx + 1}"
        title = [n for n in ns if n["type"] == "text" and n["style"]["fontSize"] >= 40 and n["transform"]["y"] < 120]
        if len(title) != 1: Wn("D2", f"{tag}: expected one page title (font >= 40, y < 120), found {len(title)}"); continue
        t = title[0]
        if "$" in t["text"]: F("D2", f"{tag}: math in the page title (KaTeX line height makes it collide with the subtitle): {t['text']!r}")
        if not (6 <= len(re.sub(r"\s", "", t["text"])) <= 26): Wn("D2", f"{tag}: title length: {t['text']!r}")
        if not args.monolingual:
            sub = [n for n in ns if n["type"] == "text" and n["style"]["fontSize"] < 40 and n["transform"]["y"] < 130 and n is not t
                   and not CJK.search(n["text"]) and en_words(n["text"]) >= 3]
            if not sub: F("L1", f"{tag}: no English subtitle under the page title")
        for n in ns:
            if n["type"] not in ("text", "shape") or n is t: continue
            fs = n["style"]["fontSize"]
            if fs < 22 and CJK.search(n["text"]): Wn("D4", f"{tag}: body text {fs}px < 22 ({n['id']})")
            if not args.monolingual and len(CJK.findall(re.sub(r"\$[^$]*\$", "", n["text"]))) >= 8:
                total_nodes += 1
                if en_words(n["text"]) < 3:
                    no_en_nodes += 1
                    Wn("L1", f"{tag}: no English line in {n['id']}: {n['text'][:24]!r}")
                elif "*" not in n["text"]:
                    Wn("L2", f"{tag}: English line is not italic (*...*) in {n['id']}")
    if not args.monolingual and total_nodes and no_en_nodes / total_nodes > 0.1:
        F("L1", f"{no_en_nodes}/{total_nodes} text blocks have no English line (more than 10%)")
    for nid, n in N.items():
        if n["type"] == "image":
            if len(n["image"]["alt"].strip()) < 12: F("G14", f"image alt too short: {nid}")
            if n["image"].get("fit") != "contain": F("G14", f"image fit must be 'contain': {nid}")
            if len(n["image"]["src"]) > 340_000: F("G13", f"embedded SVG too large: {nid}")

    print(f"audit_deck: {args.deck}  | scenes {len(S)}  nodes {len(N)}  steps {len(ST)}  frames {len(frames)}  pages {len(pages)}  "
          f"{'monolingual' if args.monolingual else 'bilingual'}")
    print(f"FAIL {len(fails)}")
    for x in fails: print("  FAIL", x)
    print(f"WARN {len(warns)}")
    for x in warns[:40]: print("  WARN", x)
    if len(warns) > 40: print(f"  ... {len(warns) - 40} more")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
