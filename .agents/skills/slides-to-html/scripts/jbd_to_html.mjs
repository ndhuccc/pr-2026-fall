#!/usr/bin/env node
// 把 JianBauDau 投影片(.jbd.json,schemaVersion 3)轉成「單檔、離線可開」的 HTML。
//
// 用法:
//   node jbd_to_html.mjs --out-dir <輸出資料夾> <檔案.jbd.json> [更多檔案...]
//   加 --strict:任何一份轉換失敗就以非 0 結束(預設只印警告並略過該份)。
//
// 輸出檔名 = 輸入檔名去掉 `.jbd.json` 再加 `.html`。
// 公式在轉換時就用 KaTeX 排好(靜態 HTML),圖片、音檔、字型全部內嵌,不需要網路與 JavaScript 函式庫。
// 畫面規則依 JianBauDau 原始碼(連接點、曲線、箭頭、文字樣式等)還原;細節見 ../SKILL.md。
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(here, '..', 'package.json'));
let katex, Marked;
try {
  katex = require('katex');
  ({ Marked } = require('marked'));
} catch (e) {
  console.error('[錯誤] 找不到 katex / marked。請先在 .agents/skills/slides-to-html 執行:npm ci');
  process.exit(2);
}

const KDIST = path.join(path.dirname(require.resolve('katex/package.json')), 'dist');

// ---------- KaTeX 樣式(字型以 base64 內嵌,只留 woff2) ----------
function katexCss() {
  let css = fs.readFileSync(path.join(KDIST, 'katex.min.css'), 'utf8');
  css = css.replace(
    /url\(fonts\/([^)]+?)\.woff2\) format\("woff2"\),url\(fonts\/[^)]+?\.woff\) format\("woff"\),url\(fonts\/[^)]+?\.ttf\) format\("truetype"\)/g,
    (_, name) => `url(data:font/woff2;base64,${fs.readFileSync(path.join(KDIST, 'fonts', name + '.woff2')).toString('base64')}) format("woff2")`,
  );
  if (/url\(fonts\//.test(css)) throw new Error('KaTeX 字型內嵌失敗(版本與預期不同)');
  return css;
}
const KCSS = katexCss();

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const escAttr = (s) => esc(s).replace(/"/g, '&quot;');
const num = (v) => (Number.isInteger(v) ? String(v) : String(Math.round(v * 1000) / 1000));

// ---------- Markdown(單換行 = 換行;不允許原始 HTML;連結只留 http/https/mailto) ----------
const md = new Marked({
  gfm: true,
  breaks: true,
  renderer: {
    html(t) { return esc(typeof t === 'string' ? t : t.text); },
    image(_h, _t, text) { return esc(text || ''); },
    link(href, _title, text) {
      return /^(https?:|mailto:|#)/i.test(href || '')
        ? `<a href="${escAttr(href)}" target="_blank" rel="noopener noreferrer">${text}</a>` : text;
    },
  },
});

const FONT_SLUGS = { inter: 'Inter', 'avenir-next': "'Avenir Next'", georgia: 'Georgia', 'courier-new': "'Courier New'", impact: 'Impact' };

// 文字 → HTML。順序:先保護公式與程式碼,再處理 {color=…} 等字元格式,最後交給 Markdown。
function renderMarkdown(raw, { inline = false } = {}) {
  const holes = [];
  const hold = (html) => { holes.push(html); return `${holes.length - 1}`; };
  const tex = (f, display) => hold(katex.renderToString(display ? f.replace(/^\r?\n|\r?\n$/g, '') : f, { displayMode: display, throwOnError: false, strict: 'ignore', trust: false }));

  // 配對規則與 JianBauDau 相同(src/model/math.ts):
  //  - `$$` 前後不可再緊鄰 `$`;`$$...$$` 為區塊公式。
  //  - `$...$` 的結尾是下一個「未跳脫、前後都不緊鄰 `$`」的 `$`(可含空白與換行)。
  const escaped = (s, i) => { let n = 0; for (let k = i - 1; k >= 0 && s[k] === '\\'; k--) n++; return n % 2 === 1; };
  const isDouble = (s, i) => s.startsWith('$$', i) && !escaped(s, i) && s[i - 1] !== '$' && s[i + 2] !== '$';
  const closeInline = (s, i) => {
    for (let k = i + 1; k < s.length; k++) {
      if (s[k] !== '$' || escaped(s, k) || s[k - 1] === '$' || s[k + 1] === '$') continue;
      return k;
    }
    return -1;
  };

  let out = '', i = 0, code = null;
  const s = raw;
  while (i < s.length) {
    const ch = s[i];
    if (code) {
      if (s.startsWith(code, i)) { out += code; i += code.length; code = null; } else { out += ch; i++; }
      continue;
    }
    if (ch === '`' && !escaped(s, i)) { let n = 1; while (s[i + n] === '`') n++; code = '`'.repeat(n); out += code; i += n; continue; }
    if (ch === '\\') { out += ch + (s[i + 1] ?? ''); i += 2; continue; }
    if (isDouble(s, i)) {
      let end = -1;
      for (let k = i + 2; k < s.length; k++) { if (isDouble(s, k)) { end = k; break; } }
      if (end > 0) { out += hold(`<div class="math-block">${tex(s.slice(i + 2, end), true).replace(/\uE000(\d+)\uE001/g, (_, n) => holes[n])}</div>`); i = end + 2; continue; }
      out += '$$'; i += 2; continue;
    }
    if (ch === '$' && s[i + 1] !== '$') {
      const j = closeInline(s, i);
      if (j > 0) { out += tex(s.slice(i + 1, j), false); i = j + 1; continue; }
    }
    out += ch; i++;
  }

  // {color=#rrggbb}…{/color}、{size=N}…{/size}、{font=slug}…{/font}
  let s2 = out;
  for (let pass = 0; pass < 4; pass++) {
    const next = s2.replace(/\{(color|size|font)=([^}\n]+)\}([\s\S]*?)\{\/\1\}/g, (m, kind, val, body) => {
      let style = '';
      if (kind === 'color' && /^#[0-9a-f]{3}(?:[0-9a-f]{3})?$/i.test(val.trim())) style = `color:${val.trim()}`;
      else if (kind === 'size' && Number.isFinite(Number(val))) style = `font-size:${Math.max(10, Math.min(120, Number(val)))}px`;
      else if (kind === 'font' && FONT_SLUGS[val.trim().toLowerCase()]) style = `font-family:${FONT_SLUGS[val.trim().toLowerCase()]}`;
      return style ? hold(`<span style="${style}">`) + body + hold('</span>') : m;
    });
    if (next === s2) break;
    s2 = next;
  }

  let html = inline ? md.parseInline(s2) : md.parse(s2);
  html = html.replace(/>\n</g, '><').replace(/\n$/, '');
  return html.replace(/(\d+)/g, (_, n) => holes[n]);
}

// ---------- 版面常數(來自 JianBauDau 原始碼) ----------
const HOOKS = 16, CURVE_OFFSET = 0.18, LABEL_OFFSET = 12, ARROW_ASPECT = 1.35;
const ARROW_MULT = { small: 5, medium: 8, large: 12 };

// ---- 填色透明度、漸層、陰影、多邊形/折線(JianBauDau 新增的繪圖效果)----
function colorA(c, a) {
  if (a === undefined || a >= 1 || !c || c === 'transparent') return c;
  let m = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(c.trim());
  if (m) { let h = m[1]; if (h.length === 3) h = [...h].map((x) => x + x).join(''); return `rgba(${parseInt(h.slice(0, 2), 16)},${parseInt(h.slice(2, 4), 16)},${parseInt(h.slice(4, 6), 16)},${a})`; }
  m = /^rgba?\(([^)]+)\)$/i.exec(c.trim());
  if (m) { const p = m[1].split(',').map((x) => x.trim()); return `rgba(${p[0]},${p[1]},${p[2]},${num((p[3] === undefined ? 1 : parseFloat(p[3])) * a)})`; }
  return c;
}
const hasGrad = (st) => typeof st.gradientTo === 'string' && st.gradientTo !== '';
function gradStops(st) {
  const op = st.fillOpacity ?? 1;
  const mid = (Array.isArray(st.gradientStops) ? st.gradientStops : []).filter((g) => Number.isFinite(g.offset) && g.color)
    .map((g) => ({ o: Math.min(0.99, Math.max(0.01, g.offset)), c: g.color })).sort((a, b) => a.o - b.o).slice(0, 8);
  return [{ o: 0, c: st.fill || '#ffffff' }, ...mid, { o: 1, c: st.gradientTo }].map((g) => ({ o: g.o, c: colorA(g.c, op) }));
}
// CSS 背景(矩形、文字卡片):漸層或帶透明度的純色
function bgCss(st) {
  if (hasGrad(st)) {
    const stops = gradStops(st).map((g) => `${g.c} ${num(g.o * 100)}%`).join(',');
    return st.gradientType === 'radial' ? `radial-gradient(ellipse closest-side,${stops})` : `linear-gradient(${st.gradientAngle ?? 180}deg,${stops})`;
  }
  return st.fill && st.fill !== 'transparent' ? colorA(st.fill, st.fillOpacity) : null;
}
function shadowCss(st) {
  if (!st.shadowColor) return null;
  return `filter:drop-shadow(${st.shadowOffsetX ?? 0}px ${st.shadowOffsetY ?? 4}px ${Math.max(0, st.shadowBlur ?? 8)}px ${colorA(st.shadowColor, st.shadowOpacity)})`;
}
// SVG 填色:漸層放進 <defs>,回傳 { fill, defs }
let gradSeq = 0;
function svgFill(st) {
  if (hasGrad(st)) {
    const id = `g${++gradSeq}`, stops = gradStops(st).map((g) => `<stop offset="${num(g.o)}" stop-color="${g.c.startsWith('rgba') ? g.c.replace(/rgba\(([^,]+),([^,]+),([^,]+),([^)]+)\)/, 'rgb($1,$2,$3)') : g.c}" stop-opacity="${g.c.startsWith('rgba') ? g.c.replace(/.*,([^)]+)\)$/, '$1') : 1}"/>`).join('');
    if (st.gradientType === 'radial') return { fill: `url(#${id})`, defs: `<defs><radialGradient id="${id}" cx="0.5" cy="0.5" r="0.5">${stops}</radialGradient></defs>` };
    const a = ((st.gradientAngle ?? 180) * Math.PI) / 180, dx = Math.sin(a), dy = -Math.cos(a);
    return { fill: `url(#${id})`, defs: `<defs><linearGradient id="${id}" x1="${num(0.5 - dx / 2)}" y1="${num(0.5 - dy / 2)}" x2="${num(0.5 + dx / 2)}" y2="${num(0.5 + dy / 2)}">${stops}</linearGradient></defs>` };
  }
  return { fill: st.fill && st.fill !== 'transparent' ? colorA(st.fill, st.fillOpacity) : 'none', defs: '' };
}
// polygon / polyline 的路徑:座標 0~100;smooth 的點用 Catmull-Rom 曲線穿過,其餘為尖角
function pathD(pts, closed) {
  const n = pts.length, P = (i) => (closed ? pts[(i + n) % n] : pts[Math.min(n - 1, Math.max(0, i))]);
  let d = `M${num(pts[0].x)} ${num(pts[0].y)}`;
  const segs = closed ? n : n - 1;
  for (let i = 0; i < segs; i++) {
    const p0 = P(i - 1), p1 = P(i), p2 = P(i + 1), p3 = P(i + 2);
    const c1 = pts[i % n].smooth ? { x: p1.x + (p2.x - p0.x) / 6, y: p1.y + (p2.y - p0.y) / 6 } : p1;
    const c2 = P(i + 1).smooth ? { x: p2.x - (p3.x - p1.x) / 6, y: p2.y - (p3.y - p1.y) / 6 } : p2;
    d += (!pts[i % n].smooth && !P(i + 1).smooth) ? ` L${num(p2.x)} ${num(p2.y)}` : ` C${num(c1.x)} ${num(c1.y)} ${num(c2.x)} ${num(c2.y)} ${num(p2.x)} ${num(p2.y)}`;
  }
  return d + (closed ? ' Z' : '');
}
const SHAPES = {
  triangle: '50,4 96,94 4,94', diamond: '50,3 97,50 50,97 3,50', pentagon: '50,3 97,37 79,95 21,95 3,37',
  star: '50,3 61,35 97,35 68,56 79,93 50,70 21,93 32,56 3,35 39,35', arrow: '3,27 61,27 61,5 97,50 61,95 61,73 3,73',
};
const DASH = { dashed: '8 5', dotted: '1 5' };
// 會放進 style="…" 屬性,所以字型名稱一律用單引號(雙引號會把屬性提早截斷,導致字級、粗細、顏色全部失效)
const DEFAULT_FONT = "'Avenir Next','Segoe UI',system-ui,'Noto Sans TC','Microsoft JhengHei','PingFang TC',sans-serif";

function hookPoint(n, hook) {
  const a = -Math.PI / 2 + (((Math.trunc(hook) % HOOKS) + HOOKS) % HOOKS) * (Math.PI * 2) / HOOKS;
  const dx = Math.cos(a), dy = Math.sin(a), hw = n.width / 2, hh = n.height / 2;
  const d = Math.min(Math.abs(dx) > 1e-10 ? hw / Math.abs(dx) : Infinity, Math.abs(dy) > 1e-10 ? hh / Math.abs(dy) : Infinity);
  return { x: n.transform.x + hw + dx * d, y: n.transform.y + hh + dy * d };
}

function pathPointAt(pts, t) {
  const lens = pts.slice(0, -1).map((p, i) => Math.hypot(pts[i + 1].x - p.x, pts[i + 1].y - p.y));
  const total = lens.reduce((a, b) => a + b, 0);
  if (total < 1e-9) return { p: pts[0], tan: { x: 1, y: 0 } };
  let dist = Math.max(0, Math.min(1, t)) * total;
  for (let i = 0; i < lens.length; i++) {
    if (lens[i] < 1e-9) continue;
    if (dist <= lens[i] || i === lens.length - 1) {
      const f = Math.max(0, Math.min(1, dist / lens[i]));
      return { p: { x: pts[i].x + (pts[i + 1].x - pts[i].x) * f, y: pts[i].y + (pts[i + 1].y - pts[i].y) * f }, tan: { x: pts[i + 1].x - pts[i].x, y: pts[i + 1].y - pts[i].y } };
    }
    dist -= lens[i];
  }
  return { p: pts[0], tan: { x: 1, y: 0 } };
}

function connectorSvg(n, byId, labels) {
  const c = n.connector;
  const a = byId[c.sourceNodeId], b = byId[c.targetNodeId];
  if (!a || !b) return '';
  const src = hookPoint(a, c.sourceHook), dst = hookPoint(b, c.targetHook);
  const st = n.style || {};
  const col = st.stroke || '#aaa', bw = Math.max(1, st.borderWidth ?? 3);
  const dash = DASH[st.borderStyle];
  const mult = ARROW_MULT[c.arrowSize] ?? ARROW_MULT.medium;
  const alen = bw * mult, ahei = alen / ARROW_ASPECT;
  let d, polyline = null, ctrl = null;
  if (c.waypoints?.length) {
    polyline = [src, ...c.waypoints, dst];
    d = polyline.map((p, i) => `${i ? 'L' : 'M'}${num(p.x)} ${num(p.y)}`).join(' ');
  } else if (c.curve) {
    const dx = dst.x - src.x, dy = dst.y - src.y, len = Math.hypot(dx, dy);
    const mid = { x: (src.x + dst.x) / 2, y: (src.y + dst.y) / 2 };
    ctrl = len < 1e-9 ? mid : { x: mid.x - (dy / len) * len * CURVE_OFFSET, y: mid.y + (dx / len) * len * CURVE_OFFSET };
    d = `M${num(src.x)} ${num(src.y)} Q${num(ctrl.x)} ${num(ctrl.y)} ${num(dst.x)} ${num(dst.y)}`;
  } else {
    d = `M${num(src.x)} ${num(src.y)} L${num(dst.x)} ${num(dst.y)}`;
  }
  // 箭頭:沿終點切線方向;線段略為縮短避免筆畫穿出箭頭尖端
  const dir = c.direction ?? 'forward';
  const endTan = (from, to, ctl, poly, atEnd) => {
    if (poly) { const p = atEnd ? poly[poly.length - 1] : poly[0], q = atEnd ? poly[poly.length - 2] : poly[1]; return { x: p.x - q.x, y: p.y - q.y }; }
    if (ctl) return atEnd ? { x: to.x - ctl.x, y: to.y - ctl.y } : { x: from.x - ctl.x, y: from.y - ctl.y };
    return atEnd ? { x: to.x - from.x, y: to.y - from.y } : { x: from.x - to.x, y: from.y - to.y };
  };
  const head = (tip, tan) => {
    const l = Math.hypot(tan.x, tan.y) || 1, ux = tan.x / l, uy = tan.y / l;
    const bx = tip.x - ux * alen, by = tip.y - uy * alen, px = -uy * ahei / 2, py = ux * ahei / 2;
    return `<polygon points="${num(tip.x)},${num(tip.y)} ${num(bx + px)},${num(by + py)} ${num(bx - px)},${num(by - py)}" fill="${col}"/>`;
  };
  let svg = `<path d="${d}" fill="none" stroke="${col}" stroke-width="${bw}" stroke-linecap="round" stroke-linejoin="round"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`;
  if (dir === 'forward' || dir === 'both') svg += head(dst, endTan(src, dst, ctrl, polyline, true));
  if (dir === 'backward' || dir === 'both') svg += head(src, endTan(src, dst, ctrl, polyline, false));

  if (c.label?.text) {
    const pts = polyline ?? (ctrl ? null : [src, dst]);
    let p, tan;
    const t = Math.max(0, Math.min(1, c.label.t ?? 0.5));
    if (pts) ({ p, tan } = pathPointAt(pts, t));
    else {
      const u = 1 - t;
      p = { x: u * u * src.x + 2 * u * t * ctrl.x + t * t * dst.x, y: u * u * src.y + 2 * u * t * ctrl.y + t * t * dst.y };
      tan = { x: 2 * (u * (ctrl.x - src.x) + t * (dst.x - ctrl.x)), y: 2 * (u * (ctrl.y - src.y) + t * (dst.y - ctrl.y)) };
    }
    const l = Math.hypot(tan.x, tan.y);
    if (c.label.offset !== 'on' && l > 1e-9) {
      const sgn = c.label.offset === 'above' ? -1 : 1;
      p = { x: p.x + (-tan.y / l) * LABEL_OFFSET * sgn, y: p.y + (tan.x / l) * LABEL_OFFSET * sgn };
    }
    labels.push(`<div class="clabel" style="left:${num(p.x)}px;top:${num(p.y)}px">${renderMarkdown(c.label.text, { inline: true })}</div>`);
  }
  return svg;
}

// ---------- 單一文件轉換 ----------
function convert(file, outFile) {
  const d = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (d.schemaVersion !== 3) throw new Error(`不支援的 schemaVersion ${d.schemaVersion}(僅支援 3)`);
  const nodes = d.nodes, scenes = d.scenes;
  const steps = [...d.steps].sort((a, b) => a.order - b.order);
  const warn = new Set();

  // 圖片與音檔各存一份在 JavaScript 陣列,畫面用索引取用(同一張圖出現在多處也不會讓檔案變大)
  const imgs = [], imgIdx = new Map();
  const imgRef = (src) => { if (!imgIdx.has(src)) { imgIdx.set(src, imgs.length); imgs.push(src); } return imgIdx.get(src); };

  const byScene = new Map();
  for (const n of Object.values(nodes)) { if (!byScene.has(n.sceneId)) byScene.set(n.sceneId, []); byScene.get(n.sceneId).push(n); }

  const cam = (c, w, h) => `translate(${num(w / 2)}px,${num(h / 2)}px) rotate(${c.rotation || 0}deg) scale(${num(c.zoom)}) translate(${num(-c.x)}px,${num(-c.y)}px)`;

  function boxCss(n) {
    const st = n.style || {}, t = n.transform;
    const css = [`left:${num(t.x)}px`, `top:${num(t.y)}px`, `width:${num(n.width)}px`, `height:${num(n.height)}px`, `z-index:${n.zIndex ?? 1}`];
    if (t.rotation || t.scaleX !== 1 || t.scaleY !== 1) css.push(`transform:rotate(${t.rotation || 0}deg) scale(${t.scaleX ?? 1},${t.scaleY ?? 1})`);
    return { css, st };
  }
  function copyCss(n, isShape) {
    const st = n.style || {};
    return [
      `font-family:${st.fontFamily ? `${st.fontFamily},` : ''}${DEFAULT_FONT}`,
      `font-size:${st.fontSize ?? 20}px`,
      `font-weight:${st.fontWeight ?? (isShape ? 720 : 400)}`,
      `font-style:${st.fontStyle ?? 'normal'}`,
      `text-align:${st.textAlign ?? (isShape ? 'center' : 'left')}`,
      `line-height:${st.lineHeight ?? (isShape ? 1.05 : 1.13)}`,
      `letter-spacing:${st.letterSpacing === undefined ? (isShape ? '-0.02em' : '0px') : `${st.letterSpacing}px`}`,
      `color:${st.textColor || '#f2ede4'}`,
    ].join(';');
  }

  function sceneInner(sceneId, depth, seen) {
    const list = (byScene.get(sceneId) || []).filter((n) => n.type !== 'connector').sort((a, b) => (a.zIndex ?? 0) - (b.zIndex ?? 0));
    const wires = [], labels = [], parts = [];
    const push = (n, h) => parts.push(n.initiallyHidden ? h.replace('class="n ', 'class="n hid ') : h);
    for (const n of byScene.get(sceneId) || []) if (n.type === 'connector') wires.push(connectorSvg(n, nodes, labels));
    for (const n of list) {
      const { css, st } = boxCss(n);
      const bgc = n.type !== 'frame' ? bgCss(st) : null;
      if (bgc) css.push(`background:${bgc}`);
      const shc = shadowCss(st);
      if (shc) css.push(shc);
      const bwid = st.borderWidth ?? 1;
      if (st.stroke && st.stroke !== 'transparent' && (n.type !== 'text')) css.push(`border:${bwid}px ${st.borderStyle || 'solid'} ${st.stroke}`);
      if (st.radius) css.push(`border-radius:${st.radius}px`);
      if (n.type === 'text') {
        push(n, `<div class="n text" data-n="${escAttr(n.id)}" style="${css.join(';')}"><div class="copy" style="${escAttr(copyCss(n, false))}">${renderMarkdown(n.text || '')}</div></div>`);
      } else if (n.type === 'shape') {
        const kind = n.shapeKind || 'rectangle';
        if (kind === 'rectangle') {
          if (!shc) css.push('box-shadow:0 18px 30px rgba(106,64,46,.16)');
          push(n, `<div class="n shape" data-n="${escAttr(n.id)}" style="${css.join(';')}"><div class="copy shape-label" style="${escAttr(copyCss(n, true))}">${renderMarkdown(n.text || '')}</div></div>`);
        } else {
          const bg = css.filter((c) => !/^(background|border|box-shadow)/.test(c));
          const stroke = st.stroke && st.stroke !== 'transparent' ? st.stroke : 'none';
          const sw = Math.max(1, st.borderWidth ?? 1);
          const dash = DASH[st.borderStyle] ? ` stroke-dasharray="${DASH[st.borderStyle]}"` : '';
          const sf = svgFill(st), sattr = `stroke="${stroke}" stroke-width="${sw}" vector-effect="non-scaling-stroke"${dash}`;
          let shapeSvg = '', vb = '0 0 100 100';
          if (kind === 'ellipse') shapeSvg = `<ellipse cx="50" cy="50" rx="47" ry="47" fill="${sf.fill}" ${sattr}/>`;
          else if (kind === 'polygon' || kind === 'polyline') {
            const pts = n.polygonPoints;
            const ok = Array.isArray(pts) && pts.length >= (kind === 'polygon' ? 3 : 2) && pts.length <= 200 && pts.every((q) => Number.isFinite(q.x) && Number.isFinite(q.y));
            if (ok) {
              // 用節點自己的像素當座標系,線寬才會跟著畫面縮放、不被拉扁
              vb = `0 0 ${num(n.width)} ${num(n.height)}`;
              const px = pts.map((q) => ({ x: q.x * n.width / 100, y: q.y * n.height / 100, smooth: q.smooth === true }));
              shapeSvg = `<path d="${pathD(px, kind === 'polygon')}" fill="${kind === 'polyline' && !(st.fill && st.fill !== 'transparent') ? 'none' : sf.fill}" stroke="${stroke}" stroke-width="${st.borderWidth ?? 1}"${dash} stroke-linecap="round" stroke-linejoin="round"/>`;
            }
            else warn.add(`${kind} 頂點不合規格(退回矩形):${n.id}`);
          } else if (SHAPES[kind]) shapeSvg = `<polygon points="${SHAPES[kind]}" fill="${sf.fill}" ${sattr}/>`;
          shapeSvg = sf.defs + shapeSvg;
          push(n, `<div class="n shape" data-n="${escAttr(n.id)}" style="${bg.join(';')}"><svg class="shape-visual" viewBox="${vb}" preserveAspectRatio="none">${shapeSvg}</svg><div class="copy shape-label" style="${escAttr(copyCss(n, true))}">${renderMarkdown(n.text || '')}</div></div>`);
        }
      } else if (n.type === 'image') {
        const src = n.image?.src || '';
        if (!/^(data:|https?:)/.test(src)) { warn.add('有圖片參照 asset: 或相對路徑,無法內嵌,已略過'); continue; }
        const inner = src.startsWith('data:') ? `<img data-i="${imgRef(src)}" alt="${escAttr(n.image.alt || '')}" style="object-fit:${n.image.fit || 'contain'}">` : `<img src="${escAttr(src)}" alt="${escAttr(n.image.alt || '')}" style="object-fit:${n.image.fit || 'contain'}">`;
        push(n, `<div class="n img" data-n="${escAttr(n.id)}" style="${css.join(';')}">${inner}</div>`);
      } else if (n.type === 'frame') {
        const f = n.frame || {};
        const pad = f.padding ?? 18;
        const child = scenes[f.childSceneId];
        const fcss = css.filter((c) => !/^background/.test(c));
        fcss.push(`background:${st.fill || 'transparent'}`, 'box-shadow:0 38px 76px rgba(54,48,39,.52),0 14px 32px rgba(157,180,123,.44)');
        let prev = '';
        if (child && f.previewMode !== 'off' && depth < 4 && !seen.has(f.childSceneId)) {
          const pw = Math.max(1, n.width - pad * 2), ph = Math.max(1, n.height - pad * 2 - 10);
          const inner = sceneInner(f.childSceneId, depth + 1, new Set([...seen, f.childSceneId]));
          prev = `<div class="fprev" style="left:${pad}px;top:${pad}px;width:${num(pw)}px;height:${num(ph)}px;${f.clip === false ? '' : 'overflow:hidden'}"><div class="world" style="transform:${cam(child.camera, pw, ph)}">${inner}</div></div>`;
        }
        push(n, `<div class="n frame" data-n="${escAttr(n.id)}" style="${fcss.join(';')}">${prev}<div class="flabel" style="color:${st.textColor || '#f2ede4'};font-size:${st.fontSize ?? 22}px">${esc(n.text || '').replace(/\n/g, '<br>')}</div></div>`);
      } else {
        warn.add(`略過不支援的節點類型:${n.type}`);
      }
    }
    return `<svg class="wires">${wires.join('')}</svg>${parts.join('')}${labels.join('')}`;
  }

  // 步驟實際前往的畫布:enter-frame 前往框的子畫布,其餘為 target.sceneId
  const destScene = (s) => {
    const t = s.target;
    if (t.kind === 'enter-frame') { const f = nodes[t.frameId]; return f?.frame?.childSceneId || t.sceneId; }
    return t.sceneId;
  };
  const layerIds = [];
  for (const s of steps) { const id = destScene(s); if (!layerIds.includes(id)) layerIds.push(id); }
  const layersHtml = layerIds.map((id, i) => `<div class="layer" id="L${i}"><div class="world">${sceneInner(id, 0, new Set([id]))}</div></div>`).join('\n');

  // 自動框景(scene-overview / focus-node):算出涵蓋範圍,留邊距後換成「中心點 + 縮放」
  const frameBox = (list) => {
    if (!list.length) return null;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const n of list) { x0 = Math.min(x0, n.transform.x); y0 = Math.min(y0, n.transform.y); x1 = Math.max(x1, n.transform.x + n.width); y1 = Math.max(y1, n.transform.y + n.height); }
    return { x: (x0 + x1) / 2, y: (y0 + y1) / 2, z: Math.min(1280 / Math.max(1, x1 - x0), 720 / Math.max(1, y1 - y0)) * 0.88 };
  };

  const auds = [];
  const stepData = steps.map((s) => {
    const t = s.target, destId = destScene(s);
    const sc = scenes[destId];
    let p = t.point || sc?.camera || { x: 0, y: 0 }, zoom = t.zoom ?? sc?.camera?.zoom ?? 1;
    if (t.kind === 'scene-overview') {
      const b = frameBox((byScene.get(destId) || []).filter((n) => n.type !== 'connector' && !n.initiallyHidden));
      if (b) { p = { x: b.x, y: b.y }; zoom = b.z; }
    } else if (t.kind === 'focus-node') {
      const b = nodes[t.nodeId] ? frameBox([nodes[t.nodeId]]) : null;
      if (b) { p = { x: b.x, y: b.y }; zoom = b.z; } else warn.add(`focus-node 找不到節點 ${t.nodeId},以預設鏡頭顯示`);
    } else if (t.kind === 'enter-frame') {
      p = sc?.camera || { x: 0, y: 0 }; zoom = sc?.camera?.zoom ?? 1;
    } else if (t.kind !== 'scene-point') warn.add(`步驟目標類型 ${t.kind} 未支援,以預設鏡頭顯示`);
    let aud = -1;
    if (s.narration?.src && s.narration.src.startsWith('data:')) { aud = auds.length; auds.push(s.narration.src); }
    else if (s.narration?.src) warn.add('有語音參照 asset: 或網址,無法內嵌,已略過');
    const rv = s.reveal;
    return {
      label: s.label || '', notes: s.speakerNotes || '', tr: s.narration?.transcript || '', aud,
      layer: layerIds.indexOf(destId),
      x: p.x, y: p.y, z: zoom, r: t.rotation ?? 0,
      vw: t.referenceViewport?.width || 1280, vh: t.referenceViewport?.height || 720,
      ms: s.durationMs ?? 900, ease: s.easing || 'smooth',
      rv: rv ? { after: rv.timing !== 'with-camera', enter: (rv.enter || []).map((e) => ({ id: e.nodeId, fx: e.effect || 'fade', dl: e.delayMs || 0, du: e.durationMs ?? 400 })), exit: rv.exitNodeIds || [] } : null,
    };
  });
  if (!stepData.length) throw new Error('簡報沒有任何步驟');

  const title = d.metadata?.title || path.basename(file).replace(/\.jbd\.json$/, '');
  const json = (o) => JSON.stringify(o).replace(/</g, '\\u003c');
  const hasAudio = auds.length > 0;

  const html = `<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<style>${KCSS}</style>
<style>
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:#0f0f0d;color:#f2ede4;font-family:${DEFAULT_FONT};overflow:hidden}
#app{position:fixed;inset:0;display:flex;flex-direction:column}
#stagewrap{flex:1;min-height:0;position:relative}
#stage{position:absolute;left:0;top:0;width:1280px;height:720px;background:#1b1b18;overflow:hidden;transform-origin:0 0;box-shadow:0 0 0 1px #34342d}
.layer{position:absolute;inset:0;opacity:0;pointer-events:none;transition:opacity .45s}
.layer.on{opacity:1}
.world{position:absolute;left:0;top:0;transform-origin:0 0;will-change:transform}
.wires{position:absolute;left:0;top:0;width:1px;height:1px;overflow:visible;z-index:1}
.n{position:absolute;display:flex;border:1px solid transparent}
.n.hid{opacity:0;visibility:hidden}
.n.text{align-items:flex-start;justify-content:flex-start}
.n.shape{align-items:center;justify-content:center}
.n.img{overflow:hidden}.n.img img{width:100%;height:100%;display:block}
.n.frame{align-items:flex-start;justify-content:flex-end;overflow:visible}
.fprev{position:absolute}
.flabel{position:absolute;left:0;bottom:100%;margin-bottom:6px;white-space:nowrap;font-weight:600;opacity:.9}
.shape-visual{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.copy{min-width:0;max-width:100%;overflow:hidden;overflow-wrap:anywhere}
.n.text>.copy{display:block;width:100%}
.shape-label{position:relative;width:100%;height:100%;padding:12px;display:flex;flex-direction:column;justify-content:center;gap:3px}
.copy p{margin:0}.copy p+p{margin-top:.35em}
.copy ul,.copy ol{margin:.15em 0;padding-left:1.25em}.copy li{padding-left:.1em}
.copy a{color:inherit;text-decoration:underline}
.copy code{padding:.05em .22em;border-radius:3px;background:rgba(0,0,0,.16);font-family:"Courier New",ui-monospace,monospace;font-size:.9em}
.copy pre{margin:.3em 0;overflow:hidden}.copy pre code{background:none;padding:0}
.copy h1,.copy h2,.copy h3,.copy h4,.copy h5,.copy h6{margin:.15em 0;line-height:1.1;font-size:1em}
.copy h1{font-size:1.35em}.copy h2{font-size:1.22em}.copy h3{font-size:1.12em}
.copy blockquote{margin:.25em 0;padding-left:.65em;border-left:2px solid currentColor;opacity:.82}
.copy hr{margin:.45em 0;border:0;border-top:1px solid currentColor;opacity:.45}
.copy table{display:block;width:max-content;max-width:100%;border-collapse:collapse}
.copy th,.copy td{padding:.12em .35em;border:1px solid currentColor}
.math-block{display:block;max-width:100%;overflow:hidden}
.math-block .katex-display{margin:0;min-width:max-content}
.katex{font-size:1.08em}
.clabel{position:absolute;z-index:3;min-width:12px;max-width:320px;padding:3px 7px;overflow:hidden;border:1px solid rgba(54,48,39,.28);border-radius:5px;background:rgba(255,255,255,.94);color:#211913;font-size:32px;font-weight:600;line-height:1.15;white-space:nowrap;text-overflow:ellipsis;transform:translate(-50%,-50%)}
#notes{position:absolute;left:0;right:0;bottom:0;max-height:38%;overflow:auto;background:rgba(15,15,13,.95);color:#e8e1d4;font-size:15px;line-height:1.65;padding:12px 18px;border-top:1px solid #3a3a32;display:none;z-index:9;white-space:pre-wrap}
#notes.on{display:block}
#notes h4{margin:.6em 0 .2em;font-size:13px;color:#a8a08f;font-weight:600}
#bar{display:flex;align-items:center;gap:10px;padding:8px 14px;background:#0f0f0d;border-top:1px solid #2a2a24;font-size:14px;color:#b9b2a2}
#bar button{background:#2a2a24;color:#f2ede4;border:1px solid #4a4a40;border-radius:6px;padding:5px 12px;font:inherit;cursor:pointer}
#bar button:hover{background:#3a3a32}#bar button.on{background:#4b6a3e;border-color:#6d9a5b}
#lab{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:center}
#cnt{min-width:64px;text-align:center;color:#f2ede4}
</style>
</head>
<body>
<div id="app">
 <div id="stagewrap"><div id="stage">
${layersHtml}
  <div id="notes"></div>
 </div></div>
 <div id="bar">
  <button id="prev" title="上一頁(←)">◀</button><span id="cnt"></span><button id="next" title="下一頁(→、空白鍵)">▶</button>
  <span id="lab"></span>
  ${hasAudio ? '<button id="voice" title="播放這一頁的語音(V)">語音</button><button id="auto" title="換頁時自動播放語音">自動</button>' : ''}
  <button id="nb" title="講者備註與逐字稿(N)">備註</button><button id="fs" title="全螢幕(F)">全螢幕</button>
 </div>
</div>
<script>
const STEPS=${json(stepData)};
const IMGS=${json(imgs)};
const AUD=${json(auds)};
const EASE={smooth:'cubic-bezier(.4,0,.2,1)',easeInOut:'ease-in-out',linear:'linear'};
const stage=document.getElementById('stage'),wrap=document.getElementById('stagewrap'),notes=document.getElementById('notes');
const cnt=document.getElementById('cnt'),lab=document.getElementById('lab');
const layers=[...document.querySelectorAll('.layer')];
document.querySelectorAll('img[data-i]').forEach(i=>{i.src=IMGS[i.dataset.i]});
let cur=-1,audio=null,auto=false;
function fit(){
  const s=Math.min(wrap.clientWidth/1280,wrap.clientHeight/720);
  stage.style.transform='scale('+s+')';
  stage.style.left=((wrap.clientWidth-1280*s)/2)+'px';
  stage.style.top=((wrap.clientHeight-720*s)/2)+'px';
}
function stopAudio(){if(audio){audio.pause();audio=null}const v=document.getElementById('voice');if(v)v.classList.remove('on')}
function playAudio(){
  const s=STEPS[cur];if(s.aud<0)return;stopAudio();
  audio=new Audio(AUD[s.aud]);const v=document.getElementById('voice');if(v)v.classList.add('on');
  audio.onended=()=>{if(v)v.classList.remove('on')};audio.play().catch(()=>{if(v)v.classList.remove('on')});
}
function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
// 逐項揭示:initiallyHidden 的節點,依 0..i 步驟(同一畫布)的 reveal.enter / exitNodeIds 累計出可見集合
const HID=new Set([...document.querySelectorAll('.n.hid[data-n]')].map(e=>e.dataset.n));
const TRK=new Set(HID);STEPS.forEach(t=>t.rv&&t.rv.exit.forEach(id=>TRK.add(id)));
function reveal(i,animate){
  if(!TRK.size)return;
  const s=STEPS[i],shown=new Set([...TRK].filter(id=>!HID.has(id)));
  for(let k=0;k<=i;k++){const r=STEPS[k].rv;if(!r||STEPS[k].layer!==s.layer)continue;r.enter.forEach(e=>shown.add(e.id));r.exit.forEach(id=>shown.delete(id))}
  const ent=new Map((animate&&s.rv?s.rv.enter:[]).map(e=>[e.id,e]));
  layers[s.layer].querySelectorAll('.n[data-n]').forEach(el=>{
    const id=el.dataset.n;if(!TRK.has(id))return;
    el.getAnimations().forEach(a=>a.cancel());
    if(shown.has(id)){
      el.classList.remove('hid');
      const e=ent.get(id);
      if(e&&e.fx!=='none'){
        const base=(s.rv.after?s.ms:0)+e.dl;
        el.animate(e.fx==='scale'?[{opacity:0,transform:'scale(.6)'},{opacity:1,transform:'scale(1)'}]:[{opacity:0},{opacity:1}],{duration:e.du,delay:base,fill:'backwards',easing:'ease-out'});
      }
    }else el.classList.add('hid');
  });
}
function go(i,instant){
  i=Math.max(0,Math.min(STEPS.length-1,i));
  const s=STEPS[i],prev=cur>=0?STEPS[cur]:null;
  const k=Math.min(1280/s.vw,720/s.vh);
  const t='translate(640px,360px) rotate('+s.r+'deg) scale('+(s.z*k)+') translate('+(-s.x)+'px,'+(-s.y)+'px)';
  const w=layers[s.layer].firstElementChild;
  if(instant||!prev||prev.layer!==s.layer){w.style.transition='none';w.style.transform=t;void w.offsetWidth}
  else{w.style.transition='transform '+s.ms+'ms '+(EASE[s.ease]||EASE.smooth);w.style.transform=t}
  layers.forEach((l,j)=>l.classList.toggle('on',j===s.layer));
  reveal(i,!instant&&prev&&i===cur+1);
  cur=i;stopAudio();
  cnt.textContent=(i+1)+' / '+STEPS.length;lab.textContent=s.label;
  notes.innerHTML=(s.notes?'<h4>講者備註</h4>'+esc(s.notes):'')+(s.tr?'<h4>語音逐字稿</h4>'+esc(s.tr):'');
  const v=document.getElementById('voice');if(v)v.disabled=s.aud<0;
  history.replaceState(null,'','#'+(i+1));
  if(auto&&s.aud>=0&&!instant)playAudio();
}
// 方框固定大小的圖形:文字超出時縮小字級(最小 60%),避免被截掉
function shrink(){
  document.querySelectorAll('.shape-label').forEach(el=>{
    // 以節點自己的字級(px)為基準縮放;只在超出超過 6px 時才縮,避免內距差幾像素就縮字
    const base=parseFloat(getComputedStyle(el).fontSize);let f=1;
    while(el.scrollHeight>el.clientHeight+6&&f>0.6){f-=0.04;el.style.fontSize=(base*f)+'px'}
    if(f<1)el.dataset.shrunk=f.toFixed(2);
  });
}
document.getElementById('prev').onclick=()=>go(cur-1);
document.getElementById('next').onclick=()=>go(cur+1);
document.getElementById('nb').onclick=()=>notes.classList.toggle('on');
document.getElementById('fs').onclick=()=>{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()};
const vb=document.getElementById('voice');
if(vb){vb.onclick=()=>{audio&&!audio.paused?stopAudio():playAudio()};
  document.getElementById('auto').onclick=function(){auto=!auto;this.classList.toggle('on',auto);if(auto)playAudio()}}
addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){go(cur+1);e.preventDefault()}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){go(cur-1);e.preventDefault()}
  else if(e.key==='Home')go(0);else if(e.key==='End')go(STEPS.length-1);
  else if(e.key==='n'||e.key==='N')notes.classList.toggle('on');
  else if(e.key==='f'||e.key==='F')document.getElementById('fs').click();
  else if((e.key==='v'||e.key==='V')&&vb)vb.click();
});
stage.addEventListener('click',e=>{if(!notes.contains(e.target))go(cur+1)});
addEventListener('resize',fit);
fit();
go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1),true);
(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(shrink);
</script>
</body>
</html>
`;
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, html);
  return { steps: stepData.length, bytes: Buffer.byteLength(html), warn: [...warn] };
}

// ---------- 命令列 ----------
const args = process.argv.slice(2);
let outDir = null, strict = false;
const inputs = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--out-dir') outDir = args[++i];
  else if (args[i] === '--strict') strict = true;
  else inputs.push(args[i]);
}
if (!outDir || !inputs.length) {
  console.error('用法:node jbd_to_html.mjs --out-dir <資料夾> [--strict] <檔案.jbd.json> ...');
  process.exit(2);
}
let failed = 0;
for (const f of inputs) {
  const out = path.join(outDir, path.basename(f).replace(/\.jbd\.json$/, '') + '.html');
  try {
    const r = convert(f, out);
    console.log(`${path.basename(out)}  ${r.steps} 頁  ${(r.bytes / 1e6).toFixed(1)} MB`);
    for (const w of r.warn) console.error(`[警告] ${path.basename(f)}:${w}`);
  } catch (e) {
    failed++;
    console.error(`[警告] ${path.basename(f)}:轉換失敗,已略過(${e.message})`);
  }
}
process.exit(strict && failed ? 1 : 0);
