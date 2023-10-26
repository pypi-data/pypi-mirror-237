const {
  SvelteComponent: xi,
  assign: Ri,
  create_slot: Fi,
  detach: Ui,
  element: Gi,
  get_all_dirty_from_scope: Vi,
  get_slot_changes: ji,
  get_spread_update: Xi,
  init: Wi,
  insert: Yi,
  safe_not_equal: qi,
  set_dynamic_element_data: Yt,
  set_style: $,
  toggle_class: ge,
  transition_in: ti,
  transition_out: ni,
  update_slot_base: zi
} = window.__gradio__svelte__internal;
function Zi(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[17].default
  ), l = Fi(
    r,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let s = [
    { "data-testid": (
      /*test_id*/
      e[7]
    ) },
    { id: (
      /*elem_id*/
      e[2]
    ) },
    {
      class: n = "block " + /*elem_classes*/
      e[3].join(" ") + " svelte-1t38q2d"
    }
  ], a = {};
  for (let u = 0; u < s.length; u += 1)
    a = Ri(a, s[u]);
  return {
    c() {
      t = Gi(
        /*tag*/
        e[14]
      ), l && l.c(), Yt(
        /*tag*/
        e[14]
      )(t, a), ge(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), ge(
        t,
        "padded",
        /*padding*/
        e[6]
      ), ge(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), ge(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), $(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), $(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), $(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), $(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), $(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), $(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), $(t, "border-width", "var(--block-border-width)");
    },
    m(u, o) {
      Yi(u, t, o), l && l.m(t, null), i = !0;
    },
    p(u, o) {
      l && l.p && (!i || o & /*$$scope*/
      65536) && zi(
        l,
        r,
        u,
        /*$$scope*/
        u[16],
        i ? ji(
          r,
          /*$$scope*/
          u[16],
          o,
          null
        ) : Vi(
          /*$$scope*/
          u[16]
        ),
        null
      ), Yt(
        /*tag*/
        u[14]
      )(t, a = Xi(s, [
        (!i || o & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          u[7]
        ) },
        (!i || o & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          u[2]
        ) },
        (!i || o & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        u[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), ge(
        t,
        "hidden",
        /*visible*/
        u[10] === !1
      ), ge(
        t,
        "padded",
        /*padding*/
        u[6]
      ), ge(
        t,
        "border_focus",
        /*border_mode*/
        u[5] === "focus"
      ), ge(t, "hide-container", !/*explicit_call*/
      u[8] && !/*container*/
      u[9]), o & /*height*/
      1 && $(t, "height", typeof /*height*/
      u[0] == "number" ? (
        /*height*/
        u[0] + "px"
      ) : void 0), o & /*width*/
      2 && $(t, "width", typeof /*width*/
      u[1] == "number" ? `calc(min(${/*width*/
      u[1]}px, 100%))` : void 0), o & /*variant*/
      16 && $(
        t,
        "border-style",
        /*variant*/
        u[4]
      ), o & /*allow_overflow*/
      2048 && $(
        t,
        "overflow",
        /*allow_overflow*/
        u[11] ? "visible" : "hidden"
      ), o & /*scale*/
      4096 && $(
        t,
        "flex-grow",
        /*scale*/
        u[12]
      ), o & /*min_width*/
      8192 && $(t, "min-width", `calc(min(${/*min_width*/
      u[13]}px, 100%))`);
    },
    i(u) {
      i || (ti(l, u), i = !0);
    },
    o(u) {
      ni(l, u), i = !1;
    },
    d(u) {
      u && Ui(t), l && l.d(u);
    }
  };
}
function Qi(e) {
  let t, n = (
    /*tag*/
    e[14] && Zi(e)
  );
  return {
    c() {
      n && n.c();
    },
    m(i, r) {
      n && n.m(i, r), t = !0;
    },
    p(i, [r]) {
      /*tag*/
      i[14] && n.p(i, r);
    },
    i(i) {
      t || (ti(n, i), t = !0);
    },
    o(i) {
      ni(n, i), t = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function Ji(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t, { height: l = void 0 } = t, { width: s = void 0 } = t, { elem_id: a = "" } = t, { elem_classes: u = [] } = t, { variant: o = "solid" } = t, { border_mode: f = "base" } = t, { padding: _ = !0 } = t, { type: h = "normal" } = t, { test_id: d = void 0 } = t, { explicit_call: y = !1 } = t, { container: m = !0 } = t, { visible: v = !0 } = t, { allow_overflow: E = !0 } = t, { scale: A = null } = t, { min_width: p = 0 } = t, S = h === "fieldset" ? "fieldset" : "div";
  return e.$$set = (H) => {
    "height" in H && n(0, l = H.height), "width" in H && n(1, s = H.width), "elem_id" in H && n(2, a = H.elem_id), "elem_classes" in H && n(3, u = H.elem_classes), "variant" in H && n(4, o = H.variant), "border_mode" in H && n(5, f = H.border_mode), "padding" in H && n(6, _ = H.padding), "type" in H && n(15, h = H.type), "test_id" in H && n(7, d = H.test_id), "explicit_call" in H && n(8, y = H.explicit_call), "container" in H && n(9, m = H.container), "visible" in H && n(10, v = H.visible), "allow_overflow" in H && n(11, E = H.allow_overflow), "scale" in H && n(12, A = H.scale), "min_width" in H && n(13, p = H.min_width), "$$scope" in H && n(16, r = H.$$scope);
  }, [
    l,
    s,
    a,
    u,
    o,
    f,
    _,
    d,
    y,
    m,
    v,
    E,
    A,
    p,
    S,
    h,
    r,
    i
  ];
}
class Ki extends xi {
  constructor(t) {
    super(), Wi(this, t, Ji, Qi, qi, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 15,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const $i = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], qt = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
$i.reduce(
  (e, { color: t, primary: n, secondary: i }) => ({
    ...e,
    [t]: {
      primary: qt[t][n],
      secondary: qt[t][i]
    }
  }),
  {}
);
function Te() {
}
function er(e) {
  return e();
}
function tr(e) {
  e.forEach(er);
}
function nr(e) {
  return typeof e == "function";
}
function ir(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function ii(e, ...t) {
  if (e == null) {
    for (const i of t)
      i(void 0);
    return Te;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function rr(e) {
  let t;
  return ii(e, (n) => t = n)(), t;
}
function zt(e) {
  const t = typeof e == "string" && e.match(/^\s*(-?[\d.]+)([^\s]*)\s*$/);
  return t ? [parseFloat(t[1]), t[2] || "px"] : [
    /** @type {number} */
    e,
    "px"
  ];
}
const ri = typeof window < "u";
let Zt = ri ? () => window.performance.now() : () => Date.now(), li = ri ? (e) => requestAnimationFrame(e) : Te;
const Ne = /* @__PURE__ */ new Set();
function si(e) {
  Ne.forEach((t) => {
    t.c(e) || (Ne.delete(t), t.f());
  }), Ne.size !== 0 && li(si);
}
function lr(e) {
  let t;
  return Ne.size === 0 && li(si), {
    promise: new Promise((n) => {
      Ne.add(t = { c: e, f: n });
    }),
    abort() {
      Ne.delete(t);
    }
  };
}
function sr(e) {
  return e < 0.5 ? 4 * e * e * e : 0.5 * Math.pow(2 * e - 2, 3) + 1;
}
function or(e) {
  const t = e - 1;
  return t * t * t + 1;
}
function ar(e, { delay: t = 0, duration: n = 400, easing: i = or, x: r = 0, y: l = 0, opacity: s = 0 } = {}) {
  const a = getComputedStyle(e), u = +a.opacity, o = a.transform === "none" ? "" : a.transform, f = u * (1 - s), [_, h] = zt(r), [d, y] = zt(l);
  return {
    delay: t,
    duration: n,
    easing: i,
    css: (m, v) => `
			transform: ${o} translate(${(1 - m) * _}${h}, ${(1 - m) * d}${y});
			opacity: ${u - f * v}`
  };
}
const Be = [];
function ur(e, t) {
  return {
    subscribe: Re(e, t).subscribe
  };
}
function Re(e, t = Te) {
  let n;
  const i = /* @__PURE__ */ new Set();
  function r(a) {
    if (ir(e, a) && (e = a, n)) {
      const u = !Be.length;
      for (const o of i)
        o[1](), Be.push(o, e);
      if (u) {
        for (let o = 0; o < Be.length; o += 2)
          Be[o][0](Be[o + 1]);
        Be.length = 0;
      }
    }
  }
  function l(a) {
    r(a(e));
  }
  function s(a, u = Te) {
    const o = [a, u];
    return i.add(o), i.size === 1 && (n = t(r, l) || Te), a(e), () => {
      i.delete(o), i.size === 0 && n && (n(), n = null);
    };
  }
  return { set: r, update: l, subscribe: s };
}
function Fe(e, t, n) {
  const i = !Array.isArray(e), r = i ? [e] : e;
  if (!r.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const l = t.length < 2;
  return ur(n, (s, a) => {
    let u = !1;
    const o = [];
    let f = 0, _ = Te;
    const h = () => {
      if (f)
        return;
      _();
      const y = t(i ? o[0] : o, s, a);
      l ? s(y) : _ = nr(y) ? y : Te;
    }, d = r.map(
      (y, m) => ii(
        y,
        (v) => {
          o[m] = v, f &= ~(1 << m), u && h();
        },
        () => {
          f |= 1 << m;
        }
      )
    );
    return u = !0, h(), function() {
      tr(d), _(), u = !1;
    };
  });
}
function Qt(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Et(e, t, n, i) {
  if (typeof n == "number" || Qt(n)) {
    const r = i - n, l = (n - t) / (e.dt || 1 / 60), s = e.opts.stiffness * r, a = e.opts.damping * l, u = (s - a) * e.inv_mass, o = (l + u) * e.dt;
    return Math.abs(o) < e.opts.precision && Math.abs(r) < e.opts.precision ? i : (e.settled = !1, Qt(n) ? new Date(n.getTime() + o) : n + o);
  } else {
    if (Array.isArray(n))
      return n.map(
        (r, l) => Et(e, t[l], n[l], i[l])
      );
    if (typeof n == "object") {
      const r = {};
      for (const l in n)
        r[l] = Et(e, t[l], n[l], i[l]);
      return r;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function Jt(e, t = {}) {
  const n = Re(e), { stiffness: i = 0.15, damping: r = 0.8, precision: l = 0.01 } = t;
  let s, a, u, o = e, f = e, _ = 1, h = 0, d = !1;
  function y(v, E = {}) {
    f = v;
    const A = u = {};
    return e == null || E.hard || m.stiffness >= 1 && m.damping >= 1 ? (d = !0, s = Zt(), o = v, n.set(e = f), Promise.resolve()) : (E.soft && (h = 1 / ((E.soft === !0 ? 0.5 : +E.soft) * 60), _ = 0), a || (s = Zt(), d = !1, a = lr((p) => {
      if (d)
        return d = !1, a = null, !1;
      _ = Math.min(_ + h, 1);
      const S = {
        inv_mass: _,
        opts: m,
        settled: !0,
        dt: (p - s) * 60 / 1e3
      }, H = Et(S, o, e, f);
      return s = p, o = e, n.set(e = H), S.settled && (a = null), !S.settled;
    })), new Promise((p) => {
      a.promise.then(() => {
        A === u && p();
      });
    }));
  }
  const m = {
    set: y,
    update: (v, E) => y(v(f, e), E),
    subscribe: n.subscribe,
    stiffness: i,
    damping: r,
    precision: l
  };
  return m;
}
function fr(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var hr = function(t) {
  return cr(t) && !_r(t);
};
function cr(e) {
  return !!e && typeof e == "object";
}
function _r(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || gr(e);
}
var mr = typeof Symbol == "function" && Symbol.for, dr = mr ? Symbol.for("react.element") : 60103;
function gr(e) {
  return e.$$typeof === dr;
}
function br(e) {
  return Array.isArray(e) ? [] : {};
}
function We(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? Ie(br(e), e, t) : e;
}
function pr(e, t, n) {
  return e.concat(t).map(function(i) {
    return We(i, n);
  });
}
function vr(e, t) {
  if (!t.customMerge)
    return Ie;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : Ie;
}
function yr(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function Kt(e) {
  return Object.keys(e).concat(yr(e));
}
function oi(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function wr(e, t) {
  return oi(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function Er(e, t, n) {
  var i = {};
  return n.isMergeableObject(e) && Kt(e).forEach(function(r) {
    i[r] = We(e[r], n);
  }), Kt(t).forEach(function(r) {
    wr(e, r) || (oi(e, r) && n.isMergeableObject(t[r]) ? i[r] = vr(r, n)(e[r], t[r], n) : i[r] = We(t[r], n));
  }), i;
}
function Ie(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || pr, n.isMergeableObject = n.isMergeableObject || hr, n.cloneUnlessOtherwiseSpecified = We;
  var i = Array.isArray(t), r = Array.isArray(e), l = i === r;
  return l ? i ? n.arrayMerge(e, t, n) : Er(e, t, n) : We(t, n);
}
Ie.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(i, r) {
    return Ie(i, r, n);
  }, {});
};
var Tr = Ie, Sr = Tr;
const Hr = /* @__PURE__ */ fr(Sr);
var Tt = function(e, t) {
  return Tt = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, i) {
    n.__proto__ = i;
  } || function(n, i) {
    for (var r in i)
      Object.prototype.hasOwnProperty.call(i, r) && (n[r] = i[r]);
  }, Tt(e, t);
};
function ot(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  Tt(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var x = function() {
  return x = Object.assign || function(t) {
    for (var n, i = 1, r = arguments.length; i < r; i++) {
      n = arguments[i];
      for (var l in n)
        Object.prototype.hasOwnProperty.call(n, l) && (t[l] = n[l]);
    }
    return t;
  }, x.apply(this, arguments);
};
function ht(e, t, n) {
  if (n || arguments.length === 2)
    for (var i = 0, r = t.length, l; i < r; i++)
      (l || !(i in t)) && (l || (l = Array.prototype.slice.call(t, 0, i)), l[i] = t[i]);
  return e.concat(l || Array.prototype.slice.call(t));
}
var N;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(N || (N = {}));
var F;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(F || (F = {}));
var Le;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(Le || (Le = {}));
function $t(e) {
  return e.type === F.literal;
}
function Ar(e) {
  return e.type === F.argument;
}
function ai(e) {
  return e.type === F.number;
}
function ui(e) {
  return e.type === F.date;
}
function fi(e) {
  return e.type === F.time;
}
function hi(e) {
  return e.type === F.select;
}
function ci(e) {
  return e.type === F.plural;
}
function Br(e) {
  return e.type === F.pound;
}
function _i(e) {
  return e.type === F.tag;
}
function mi(e) {
  return !!(e && typeof e == "object" && e.type === Le.number);
}
function St(e) {
  return !!(e && typeof e == "object" && e.type === Le.dateTime);
}
var di = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, Pr = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function Mr(e) {
  var t = {};
  return e.replace(Pr, function(n) {
    var i = n.length;
    switch (n[0]) {
      case "G":
        t.era = i === 4 ? "long" : i === 5 ? "narrow" : "short";
        break;
      case "y":
        t.year = i === 2 ? "2-digit" : "numeric";
        break;
      case "Y":
      case "u":
      case "U":
      case "r":
        throw new RangeError("`Y/u/U/r` (year) patterns are not supported, use `y` instead");
      case "q":
      case "Q":
        throw new RangeError("`q/Q` (quarter) patterns are not supported");
      case "M":
      case "L":
        t.month = ["numeric", "2-digit", "short", "long", "narrow"][i - 1];
        break;
      case "w":
      case "W":
        throw new RangeError("`w/W` (week) patterns are not supported");
      case "d":
        t.day = ["numeric", "2-digit"][i - 1];
        break;
      case "D":
      case "F":
      case "g":
        throw new RangeError("`D/F/g` (day) patterns are not supported, use `d` instead");
      case "E":
        t.weekday = i === 4 ? "short" : i === 5 ? "narrow" : "short";
        break;
      case "e":
        if (i < 4)
          throw new RangeError("`e..eee` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "c":
        if (i < 4)
          throw new RangeError("`c..ccc` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "a":
        t.hour12 = !0;
        break;
      case "b":
      case "B":
        throw new RangeError("`b/B` (period) patterns are not supported, use `a` instead");
      case "h":
        t.hourCycle = "h12", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "H":
        t.hourCycle = "h23", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "K":
        t.hourCycle = "h11", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "k":
        t.hourCycle = "h24", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "j":
      case "J":
      case "C":
        throw new RangeError("`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead");
      case "m":
        t.minute = ["numeric", "2-digit"][i - 1];
        break;
      case "s":
        t.second = ["numeric", "2-digit"][i - 1];
        break;
      case "S":
      case "A":
        throw new RangeError("`S/A` (second) patterns are not supported, use `s` instead");
      case "z":
        t.timeZoneName = i < 4 ? "short" : "long";
        break;
      case "Z":
      case "O":
      case "v":
      case "V":
      case "X":
      case "x":
        throw new RangeError("`Z/O/v/V/X/x` (timeZone) patterns are not supported, use `z` instead");
    }
    return "";
  }), t;
}
var Nr = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function Ir(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(Nr).filter(function(h) {
    return h.length > 0;
  }), n = [], i = 0, r = t; i < r.length; i++) {
    var l = r[i], s = l.split("/");
    if (s.length === 0)
      throw new Error("Invalid number skeleton");
    for (var a = s[0], u = s.slice(1), o = 0, f = u; o < f.length; o++) {
      var _ = f[o];
      if (_.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: a, options: u });
  }
  return n;
}
function Lr(e) {
  return e.replace(/^(.*?)-/, "");
}
var en = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, gi = /^(@+)?(\+|#+)?[rs]?$/g, Or = /(\*)(0+)|(#+)(0+)|(0+)/g, bi = /^(0+)$/;
function tn(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(gi, function(n, i, r) {
    return typeof r != "string" ? (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length) : r === "+" ? t.minimumSignificantDigits = i.length : i[0] === "#" ? t.maximumSignificantDigits = i.length : (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length + (typeof r == "string" ? r.length : 0)), "";
  }), t;
}
function pi(e) {
  switch (e) {
    case "sign-auto":
      return {
        signDisplay: "auto"
      };
    case "sign-accounting":
    case "()":
      return {
        currencySign: "accounting"
      };
    case "sign-always":
    case "+!":
      return {
        signDisplay: "always"
      };
    case "sign-accounting-always":
    case "()!":
      return {
        signDisplay: "always",
        currencySign: "accounting"
      };
    case "sign-except-zero":
    case "+?":
      return {
        signDisplay: "exceptZero"
      };
    case "sign-accounting-except-zero":
    case "()?":
      return {
        signDisplay: "exceptZero",
        currencySign: "accounting"
      };
    case "sign-never":
    case "+_":
      return {
        signDisplay: "never"
      };
  }
}
function kr(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !bi.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function nn(e) {
  var t = {}, n = pi(e);
  return n || t;
}
function Cr(e) {
  for (var t = {}, n = 0, i = e; n < i.length; n++) {
    var r = i[n];
    switch (r.stem) {
      case "percent":
      case "%":
        t.style = "percent";
        continue;
      case "%x100":
        t.style = "percent", t.scale = 100;
        continue;
      case "currency":
        t.style = "currency", t.currency = r.options[0];
        continue;
      case "group-off":
      case ",_":
        t.useGrouping = !1;
        continue;
      case "precision-integer":
      case ".":
        t.maximumFractionDigits = 0;
        continue;
      case "measure-unit":
      case "unit":
        t.style = "unit", t.unit = Lr(r.options[0]);
        continue;
      case "compact-short":
      case "K":
        t.notation = "compact", t.compactDisplay = "short";
        continue;
      case "compact-long":
      case "KK":
        t.notation = "compact", t.compactDisplay = "long";
        continue;
      case "scientific":
        t = x(x(x({}, t), { notation: "scientific" }), r.options.reduce(function(u, o) {
          return x(x({}, u), nn(o));
        }, {}));
        continue;
      case "engineering":
        t = x(x(x({}, t), { notation: "engineering" }), r.options.reduce(function(u, o) {
          return x(x({}, u), nn(o));
        }, {}));
        continue;
      case "notation-simple":
        t.notation = "standard";
        continue;
      case "unit-width-narrow":
        t.currencyDisplay = "narrowSymbol", t.unitDisplay = "narrow";
        continue;
      case "unit-width-short":
        t.currencyDisplay = "code", t.unitDisplay = "short";
        continue;
      case "unit-width-full-name":
        t.currencyDisplay = "name", t.unitDisplay = "long";
        continue;
      case "unit-width-iso-code":
        t.currencyDisplay = "symbol";
        continue;
      case "scale":
        t.scale = parseFloat(r.options[0]);
        continue;
      case "integer-width":
        if (r.options.length > 1)
          throw new RangeError("integer-width stems only accept a single optional option");
        r.options[0].replace(Or, function(u, o, f, _, h, d) {
          if (o)
            t.minimumIntegerDigits = f.length;
          else {
            if (_ && h)
              throw new Error("We currently do not support maximum integer digits");
            if (d)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (bi.test(r.stem)) {
      t.minimumIntegerDigits = r.stem.length;
      continue;
    }
    if (en.test(r.stem)) {
      if (r.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      r.stem.replace(en, function(u, o, f, _, h, d) {
        return f === "*" ? t.minimumFractionDigits = o.length : _ && _[0] === "#" ? t.maximumFractionDigits = _.length : h && d ? (t.minimumFractionDigits = h.length, t.maximumFractionDigits = h.length + d.length) : (t.minimumFractionDigits = o.length, t.maximumFractionDigits = o.length), "";
      });
      var l = r.options[0];
      l === "w" ? t = x(x({}, t), { trailingZeroDisplay: "stripIfInteger" }) : l && (t = x(x({}, t), tn(l)));
      continue;
    }
    if (gi.test(r.stem)) {
      t = x(x({}, t), tn(r.stem));
      continue;
    }
    var s = pi(r.stem);
    s && (t = x(x({}, t), s));
    var a = kr(r.stem);
    a && (t = x(x({}, t), a));
  }
  return t;
}
var Qe = {
  AX: [
    "H"
  ],
  BQ: [
    "H"
  ],
  CP: [
    "H"
  ],
  CZ: [
    "H"
  ],
  DK: [
    "H"
  ],
  FI: [
    "H"
  ],
  ID: [
    "H"
  ],
  IS: [
    "H"
  ],
  ML: [
    "H"
  ],
  NE: [
    "H"
  ],
  RU: [
    "H"
  ],
  SE: [
    "H"
  ],
  SJ: [
    "H"
  ],
  SK: [
    "H"
  ],
  AS: [
    "h",
    "H"
  ],
  BT: [
    "h",
    "H"
  ],
  DJ: [
    "h",
    "H"
  ],
  ER: [
    "h",
    "H"
  ],
  GH: [
    "h",
    "H"
  ],
  IN: [
    "h",
    "H"
  ],
  LS: [
    "h",
    "H"
  ],
  PG: [
    "h",
    "H"
  ],
  PW: [
    "h",
    "H"
  ],
  SO: [
    "h",
    "H"
  ],
  TO: [
    "h",
    "H"
  ],
  VU: [
    "h",
    "H"
  ],
  WS: [
    "h",
    "H"
  ],
  "001": [
    "H",
    "h"
  ],
  AL: [
    "h",
    "H",
    "hB"
  ],
  TD: [
    "h",
    "H",
    "hB"
  ],
  "ca-ES": [
    "H",
    "h",
    "hB"
  ],
  CF: [
    "H",
    "h",
    "hB"
  ],
  CM: [
    "H",
    "h",
    "hB"
  ],
  "fr-CA": [
    "H",
    "h",
    "hB"
  ],
  "gl-ES": [
    "H",
    "h",
    "hB"
  ],
  "it-CH": [
    "H",
    "h",
    "hB"
  ],
  "it-IT": [
    "H",
    "h",
    "hB"
  ],
  LU: [
    "H",
    "h",
    "hB"
  ],
  NP: [
    "H",
    "h",
    "hB"
  ],
  PF: [
    "H",
    "h",
    "hB"
  ],
  SC: [
    "H",
    "h",
    "hB"
  ],
  SM: [
    "H",
    "h",
    "hB"
  ],
  SN: [
    "H",
    "h",
    "hB"
  ],
  TF: [
    "H",
    "h",
    "hB"
  ],
  VA: [
    "H",
    "h",
    "hB"
  ],
  CY: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  GR: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  CO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  DO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KP: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  NA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  VE: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  AC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  AI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BW: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BZ: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  DG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  FK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GB: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IM: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IO: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  JE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  LT: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MS: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NF: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NR: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NU: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  PN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SH: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  TA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  ZA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  "af-ZA": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  AR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CL: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CU: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  EA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BO": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BR": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-EC": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-ES": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-GQ": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-PE": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  GT: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  HN: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  IC: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KG: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KM: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  LK: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MX: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  NI: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  PY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  SV: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  UY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  JP: [
    "H",
    "h",
    "K"
  ],
  AD: [
    "H",
    "hB"
  ],
  AM: [
    "H",
    "hB"
  ],
  AO: [
    "H",
    "hB"
  ],
  AT: [
    "H",
    "hB"
  ],
  AW: [
    "H",
    "hB"
  ],
  BE: [
    "H",
    "hB"
  ],
  BF: [
    "H",
    "hB"
  ],
  BJ: [
    "H",
    "hB"
  ],
  BL: [
    "H",
    "hB"
  ],
  BR: [
    "H",
    "hB"
  ],
  CG: [
    "H",
    "hB"
  ],
  CI: [
    "H",
    "hB"
  ],
  CV: [
    "H",
    "hB"
  ],
  DE: [
    "H",
    "hB"
  ],
  EE: [
    "H",
    "hB"
  ],
  FR: [
    "H",
    "hB"
  ],
  GA: [
    "H",
    "hB"
  ],
  GF: [
    "H",
    "hB"
  ],
  GN: [
    "H",
    "hB"
  ],
  GP: [
    "H",
    "hB"
  ],
  GW: [
    "H",
    "hB"
  ],
  HR: [
    "H",
    "hB"
  ],
  IL: [
    "H",
    "hB"
  ],
  IT: [
    "H",
    "hB"
  ],
  KZ: [
    "H",
    "hB"
  ],
  MC: [
    "H",
    "hB"
  ],
  MD: [
    "H",
    "hB"
  ],
  MF: [
    "H",
    "hB"
  ],
  MQ: [
    "H",
    "hB"
  ],
  MZ: [
    "H",
    "hB"
  ],
  NC: [
    "H",
    "hB"
  ],
  NL: [
    "H",
    "hB"
  ],
  PM: [
    "H",
    "hB"
  ],
  PT: [
    "H",
    "hB"
  ],
  RE: [
    "H",
    "hB"
  ],
  RO: [
    "H",
    "hB"
  ],
  SI: [
    "H",
    "hB"
  ],
  SR: [
    "H",
    "hB"
  ],
  ST: [
    "H",
    "hB"
  ],
  TG: [
    "H",
    "hB"
  ],
  TR: [
    "H",
    "hB"
  ],
  WF: [
    "H",
    "hB"
  ],
  YT: [
    "H",
    "hB"
  ],
  BD: [
    "h",
    "hB",
    "H"
  ],
  PK: [
    "h",
    "hB",
    "H"
  ],
  AZ: [
    "H",
    "hB",
    "h"
  ],
  BA: [
    "H",
    "hB",
    "h"
  ],
  BG: [
    "H",
    "hB",
    "h"
  ],
  CH: [
    "H",
    "hB",
    "h"
  ],
  GE: [
    "H",
    "hB",
    "h"
  ],
  LI: [
    "H",
    "hB",
    "h"
  ],
  ME: [
    "H",
    "hB",
    "h"
  ],
  RS: [
    "H",
    "hB",
    "h"
  ],
  UA: [
    "H",
    "hB",
    "h"
  ],
  UZ: [
    "H",
    "hB",
    "h"
  ],
  XK: [
    "H",
    "hB",
    "h"
  ],
  AG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  AU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  CA: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  DM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  "en-001": [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FJ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GD: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  JM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KN: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LR: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MH: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MP: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MW: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  NZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SL: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TT: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  UM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  US: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  ZM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BO: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  EC: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  ES: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  GQ: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  PE: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  AE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  "ar-001": [
    "h",
    "hB",
    "hb",
    "H"
  ],
  BH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  DZ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EG: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  HK: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  IQ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  JO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  KW: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LB: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MR: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  OM: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PS: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  QA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SD: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  TN: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  YE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  AF: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  LA: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  CN: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  LV: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  TL: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  "zu-ZA": [
    "H",
    "hB",
    "hb",
    "h"
  ],
  CD: [
    "hB",
    "H"
  ],
  IR: [
    "hB",
    "H"
  ],
  "hi-IN": [
    "hB",
    "h",
    "H"
  ],
  "kn-IN": [
    "hB",
    "h",
    "H"
  ],
  "ml-IN": [
    "hB",
    "h",
    "H"
  ],
  "te-IN": [
    "hB",
    "h",
    "H"
  ],
  KH: [
    "hB",
    "h",
    "H",
    "hb"
  ],
  "ta-IN": [
    "hB",
    "h",
    "hb",
    "H"
  ],
  BN: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  MY: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  ET: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "gu-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "mr-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "pa-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  TW: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  KE: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  MM: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  TZ: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  UG: [
    "hB",
    "hb",
    "H",
    "h"
  ]
};
function Dr(e, t) {
  for (var n = "", i = 0; i < e.length; i++) {
    var r = e.charAt(i);
    if (r === "j") {
      for (var l = 0; i + 1 < e.length && e.charAt(i + 1) === r; )
        l++, i++;
      var s = 1 + (l & 1), a = l < 2 ? 1 : 3 + (l >> 1), u = "a", o = xr(t);
      for ((o == "H" || o == "k") && (a = 0); a-- > 0; )
        n += u;
      for (; s-- > 0; )
        n = o + n;
    } else
      r === "J" ? n += "H" : n += r;
  }
  return n;
}
function xr(e) {
  var t = e.hourCycle;
  if (t === void 0 && // @ts-ignore hourCycle(s) is not identified yet
  e.hourCycles && // @ts-ignore
  e.hourCycles.length && (t = e.hourCycles[0]), t)
    switch (t) {
      case "h24":
        return "k";
      case "h23":
        return "H";
      case "h12":
        return "h";
      case "h11":
        return "K";
      default:
        throw new Error("Invalid hourCycle");
    }
  var n = e.language, i;
  n !== "root" && (i = e.maximize().region);
  var r = Qe[i || ""] || Qe[n || ""] || Qe["".concat(n, "-001")] || Qe["001"];
  return r[0];
}
var ct, Rr = new RegExp("^".concat(di.source, "*")), Fr = new RegExp("".concat(di.source, "*$"));
function L(e, t) {
  return { start: e, end: t };
}
var Ur = !!String.prototype.startsWith, Gr = !!String.fromCodePoint, Vr = !!Object.fromEntries, jr = !!String.prototype.codePointAt, Xr = !!String.prototype.trimStart, Wr = !!String.prototype.trimEnd, Yr = !!Number.isSafeInteger, qr = Yr ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, Ht = !0;
try {
  var zr = yi("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Ht = ((ct = zr.exec("a")) === null || ct === void 0 ? void 0 : ct[0]) === "a";
} catch {
  Ht = !1;
}
var rn = Ur ? (
  // Native
  function(t, n, i) {
    return t.startsWith(n, i);
  }
) : (
  // For IE11
  function(t, n, i) {
    return t.slice(i, i + n.length) === n;
  }
), At = Gr ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var i = "", r = t.length, l = 0, s; r > l; ) {
      if (s = t[l++], s > 1114111)
        throw RangeError(s + " is not a valid code point");
      i += s < 65536 ? String.fromCharCode(s) : String.fromCharCode(((s -= 65536) >> 10) + 55296, s % 1024 + 56320);
    }
    return i;
  }
), ln = (
  // native
  Vr ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, i = 0, r = t; i < r.length; i++) {
        var l = r[i], s = l[0], a = l[1];
        n[s] = a;
      }
      return n;
    }
  )
), vi = jr ? (
  // Native
  function(t, n) {
    return t.codePointAt(n);
  }
) : (
  // IE 11
  function(t, n) {
    var i = t.length;
    if (!(n < 0 || n >= i)) {
      var r = t.charCodeAt(n), l;
      return r < 55296 || r > 56319 || n + 1 === i || (l = t.charCodeAt(n + 1)) < 56320 || l > 57343 ? r : (r - 55296 << 10) + (l - 56320) + 65536;
    }
  }
), Zr = Xr ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Rr, "");
  }
), Qr = Wr ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Fr, "");
  }
);
function yi(e, t) {
  return new RegExp(e, t);
}
var Bt;
if (Ht) {
  var sn = yi("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Bt = function(t, n) {
    var i;
    sn.lastIndex = n;
    var r = sn.exec(t);
    return (i = r[1]) !== null && i !== void 0 ? i : "";
  };
} else
  Bt = function(t, n) {
    for (var i = []; ; ) {
      var r = vi(t, n);
      if (r === void 0 || wi(r) || el(r))
        break;
      i.push(r), n += r >= 65536 ? 2 : 1;
    }
    return At.apply(void 0, i);
  };
var Jr = (
  /** @class */
  function() {
    function e(t, n) {
      n === void 0 && (n = {}), this.message = t, this.position = { offset: 0, line: 1, column: 1 }, this.ignoreTag = !!n.ignoreTag, this.locale = n.locale, this.requiresOtherClause = !!n.requiresOtherClause, this.shouldParseSkeletons = !!n.shouldParseSkeletons;
    }
    return e.prototype.parse = function() {
      if (this.offset() !== 0)
        throw Error("parser can only be used once");
      return this.parseMessage(0, "", !1);
    }, e.prototype.parseMessage = function(t, n, i) {
      for (var r = []; !this.isEOF(); ) {
        var l = this.char();
        if (l === 123) {
          var s = this.parseArgument(t, i);
          if (s.err)
            return s;
          r.push(s.val);
        } else {
          if (l === 125 && t > 0)
            break;
          if (l === 35 && (n === "plural" || n === "selectordinal")) {
            var a = this.clonePosition();
            this.bump(), r.push({
              type: F.pound,
              location: L(a, this.clonePosition())
            });
          } else if (l === 60 && !this.ignoreTag && this.peek() === 47) {
            if (i)
              break;
            return this.error(N.UNMATCHED_CLOSING_TAG, L(this.clonePosition(), this.clonePosition()));
          } else if (l === 60 && !this.ignoreTag && Pt(this.peek() || 0)) {
            var s = this.parseTag(t, n);
            if (s.err)
              return s;
            r.push(s.val);
          } else {
            var s = this.parseLiteral(t, n);
            if (s.err)
              return s;
            r.push(s.val);
          }
        }
      }
      return { val: r, err: null };
    }, e.prototype.parseTag = function(t, n) {
      var i = this.clonePosition();
      this.bump();
      var r = this.parseTagName();
      if (this.bumpSpace(), this.bumpIf("/>"))
        return {
          val: {
            type: F.literal,
            value: "<".concat(r, "/>"),
            location: L(i, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var l = this.parseMessage(t + 1, n, !0);
        if (l.err)
          return l;
        var s = l.val, a = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !Pt(this.char()))
            return this.error(N.INVALID_TAG, L(a, this.clonePosition()));
          var u = this.clonePosition(), o = this.parseTagName();
          return r !== o ? this.error(N.UNMATCHED_CLOSING_TAG, L(u, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: F.tag,
              value: r,
              children: s,
              location: L(i, this.clonePosition())
            },
            err: null
          } : this.error(N.INVALID_TAG, L(a, this.clonePosition())));
        } else
          return this.error(N.UNCLOSED_TAG, L(i, this.clonePosition()));
      } else
        return this.error(N.INVALID_TAG, L(i, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && $r(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var i = this.clonePosition(), r = ""; ; ) {
        var l = this.tryParseQuote(n);
        if (l) {
          r += l;
          continue;
        }
        var s = this.tryParseUnquoted(t, n);
        if (s) {
          r += s;
          continue;
        }
        var a = this.tryParseLeftAngleBracket();
        if (a) {
          r += a;
          continue;
        }
        break;
      }
      var u = L(i, this.clonePosition());
      return {
        val: { type: F.literal, value: r, location: u },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !Kr(this.peek() || 0)) ? (this.bump(), "<") : null;
    }, e.prototype.tryParseQuote = function(t) {
      if (this.isEOF() || this.char() !== 39)
        return null;
      switch (this.peek()) {
        case 39:
          return this.bump(), this.bump(), "'";
        case 123:
        case 60:
        case 62:
        case 125:
          break;
        case 35:
          if (t === "plural" || t === "selectordinal")
            break;
          return null;
        default:
          return null;
      }
      this.bump();
      var n = [this.char()];
      for (this.bump(); !this.isEOF(); ) {
        var i = this.char();
        if (i === 39)
          if (this.peek() === 39)
            n.push(39), this.bump();
          else {
            this.bump();
            break;
          }
        else
          n.push(i);
        this.bump();
      }
      return At.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var i = this.char();
      return i === 60 || i === 123 || i === 35 && (n === "plural" || n === "selectordinal") || i === 125 && t > 0 ? null : (this.bump(), At(i));
    }, e.prototype.parseArgument = function(t, n) {
      var i = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(N.EMPTY_ARGUMENT, L(i, this.clonePosition()));
      var r = this.parseIdentifierIfPossible().value;
      if (!r)
        return this.error(N.MALFORMED_ARGUMENT, L(i, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: F.argument,
              // value does not include the opening and closing braces.
              value: r,
              location: L(i, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition())) : this.parseArgumentOptions(t, n, r, i);
        default:
          return this.error(N.MALFORMED_ARGUMENT, L(i, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), i = Bt(this.message, n), r = n + i.length;
      this.bumpTo(r);
      var l = this.clonePosition(), s = L(t, l);
      return { value: i, location: s };
    }, e.prototype.parseArgumentOptions = function(t, n, i, r) {
      var l, s = this.clonePosition(), a = this.parseIdentifierIfPossible().value, u = this.clonePosition();
      switch (a) {
        case "":
          return this.error(N.EXPECT_ARGUMENT_TYPE, L(s, u));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var o = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), _ = this.parseSimpleArgStyleIfPossible();
            if (_.err)
              return _;
            var h = Qr(_.val);
            if (h.length === 0)
              return this.error(N.EXPECT_ARGUMENT_STYLE, L(this.clonePosition(), this.clonePosition()));
            var d = L(f, this.clonePosition());
            o = { style: h, styleLocation: d };
          }
          var y = this.tryParseArgumentClose(r);
          if (y.err)
            return y;
          var m = L(r, this.clonePosition());
          if (o && rn(o == null ? void 0 : o.style, "::", 0)) {
            var v = Zr(o.style.slice(2));
            if (a === "number") {
              var _ = this.parseNumberSkeletonFromString(v, o.styleLocation);
              return _.err ? _ : {
                val: { type: F.number, value: i, location: m, style: _.val },
                err: null
              };
            } else {
              if (v.length === 0)
                return this.error(N.EXPECT_DATE_TIME_SKELETON, m);
              var E = v;
              this.locale && (E = Dr(v, this.locale));
              var h = {
                type: Le.dateTime,
                pattern: E,
                location: o.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? Mr(E) : {}
              }, A = a === "date" ? F.date : F.time;
              return {
                val: { type: A, value: i, location: m, style: h },
                err: null
              };
            }
          }
          return {
            val: {
              type: a === "number" ? F.number : a === "date" ? F.date : F.time,
              value: i,
              location: m,
              style: (l = o == null ? void 0 : o.style) !== null && l !== void 0 ? l : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var p = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(N.EXPECT_SELECT_ARGUMENT_OPTIONS, L(p, x({}, p)));
          this.bumpSpace();
          var S = this.parseIdentifierIfPossible(), H = 0;
          if (a !== "select" && S.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(N.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, L(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var _ = this.tryParseDecimalInteger(N.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, N.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (_.err)
              return _;
            this.bumpSpace(), S = this.parseIdentifierIfPossible(), H = _.val;
          }
          var I = this.tryParsePluralOrSelectOptions(t, a, n, S);
          if (I.err)
            return I;
          var y = this.tryParseArgumentClose(r);
          if (y.err)
            return y;
          var Y = L(r, this.clonePosition());
          return a === "select" ? {
            val: {
              type: F.select,
              value: i,
              options: ln(I.val),
              location: Y
            },
            err: null
          } : {
            val: {
              type: F.plural,
              value: i,
              options: ln(I.val),
              offset: H,
              pluralType: a === "plural" ? "cardinal" : "ordinal",
              location: Y
            },
            err: null
          };
        }
        default:
          return this.error(N.INVALID_ARGUMENT_TYPE, L(s, u));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, L(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var i = this.char();
        switch (i) {
          case 39: {
            this.bump();
            var r = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(N.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, L(r, this.clonePosition()));
            this.bump();
            break;
          }
          case 123: {
            t += 1, this.bump();
            break;
          }
          case 125: {
            if (t > 0)
              t -= 1;
            else
              return {
                val: this.message.slice(n.offset, this.offset()),
                err: null
              };
            break;
          }
          default:
            this.bump();
            break;
        }
      }
      return {
        val: this.message.slice(n.offset, this.offset()),
        err: null
      };
    }, e.prototype.parseNumberSkeletonFromString = function(t, n) {
      var i = [];
      try {
        i = Ir(t);
      } catch {
        return this.error(N.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: Le.number,
          tokens: i,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? Cr(i) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, i, r) {
      for (var l, s = !1, a = [], u = /* @__PURE__ */ new Set(), o = r.value, f = r.location; ; ) {
        if (o.length === 0) {
          var _ = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var h = this.tryParseDecimalInteger(N.EXPECT_PLURAL_ARGUMENT_SELECTOR, N.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (h.err)
              return h;
            f = L(_, this.clonePosition()), o = this.message.slice(_.offset, this.offset());
          } else
            break;
        }
        if (u.has(o))
          return this.error(n === "select" ? N.DUPLICATE_SELECT_ARGUMENT_SELECTOR : N.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        o === "other" && (s = !0), this.bumpSpace();
        var d = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? N.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : N.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, L(this.clonePosition(), this.clonePosition()));
        var y = this.parseMessage(t + 1, n, i);
        if (y.err)
          return y;
        var m = this.tryParseArgumentClose(d);
        if (m.err)
          return m;
        a.push([
          o,
          {
            value: y.val,
            location: L(d, this.clonePosition())
          }
        ]), u.add(o), this.bumpSpace(), l = this.parseIdentifierIfPossible(), o = l.value, f = l.location;
      }
      return a.length === 0 ? this.error(n === "select" ? N.EXPECT_SELECT_ARGUMENT_SELECTOR : N.EXPECT_PLURAL_ARGUMENT_SELECTOR, L(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !s ? this.error(N.MISSING_OTHER_CLAUSE, L(this.clonePosition(), this.clonePosition())) : { val: a, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var i = 1, r = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (i = -1);
      for (var l = !1, s = 0; !this.isEOF(); ) {
        var a = this.char();
        if (a >= 48 && a <= 57)
          l = !0, s = s * 10 + (a - 48), this.bump();
        else
          break;
      }
      var u = L(r, this.clonePosition());
      return l ? (s *= i, qr(s) ? { val: s, err: null } : this.error(n, u)) : this.error(t, u);
    }, e.prototype.offset = function() {
      return this.position.offset;
    }, e.prototype.isEOF = function() {
      return this.offset() === this.message.length;
    }, e.prototype.clonePosition = function() {
      return {
        offset: this.position.offset,
        line: this.position.line,
        column: this.position.column
      };
    }, e.prototype.char = function() {
      var t = this.position.offset;
      if (t >= this.message.length)
        throw Error("out of bound");
      var n = vi(this.message, t);
      if (n === void 0)
        throw Error("Offset ".concat(t, " is at invalid UTF-16 code unit boundary"));
      return n;
    }, e.prototype.error = function(t, n) {
      return {
        val: null,
        err: {
          kind: t,
          message: this.message,
          location: n
        }
      };
    }, e.prototype.bump = function() {
      if (!this.isEOF()) {
        var t = this.char();
        t === 10 ? (this.position.line += 1, this.position.column = 1, this.position.offset += 1) : (this.position.column += 1, this.position.offset += t < 65536 ? 1 : 2);
      }
    }, e.prototype.bumpIf = function(t) {
      if (rn(this.message, t, this.offset())) {
        for (var n = 0; n < t.length; n++)
          this.bump();
        return !0;
      }
      return !1;
    }, e.prototype.bumpUntil = function(t) {
      var n = this.offset(), i = this.message.indexOf(t, n);
      return i >= 0 ? (this.bumpTo(i), !0) : (this.bumpTo(this.message.length), !1);
    }, e.prototype.bumpTo = function(t) {
      if (this.offset() > t)
        throw Error("targetOffset ".concat(t, " must be greater than or equal to the current offset ").concat(this.offset()));
      for (t = Math.min(t, this.message.length); ; ) {
        var n = this.offset();
        if (n === t)
          break;
        if (n > t)
          throw Error("targetOffset ".concat(t, " is at invalid UTF-16 code unit boundary"));
        if (this.bump(), this.isEOF())
          break;
      }
    }, e.prototype.bumpSpace = function() {
      for (; !this.isEOF() && wi(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), i = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return i ?? null;
    }, e;
  }()
);
function Pt(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Kr(e) {
  return Pt(e) || e === 47;
}
function $r(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function wi(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function el(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function Mt(e) {
  e.forEach(function(t) {
    if (delete t.location, hi(t) || ci(t))
      for (var n in t.options)
        delete t.options[n].location, Mt(t.options[n].value);
    else
      ai(t) && mi(t.style) || (ui(t) || fi(t)) && St(t.style) ? delete t.style.location : _i(t) && Mt(t.children);
  });
}
function tl(e, t) {
  t === void 0 && (t = {}), t = x({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new Jr(e, t).parse();
  if (n.err) {
    var i = SyntaxError(N[n.err.kind]);
    throw i.location = n.err.location, i.originalMessage = n.err.message, i;
  }
  return t != null && t.captureLocation || Mt(n.val), n.val;
}
function _t(e, t) {
  var n = t && t.cache ? t.cache : ol, i = t && t.serializer ? t.serializer : sl, r = t && t.strategy ? t.strategy : il;
  return r(e, {
    cache: n,
    serializer: i
  });
}
function nl(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function Ei(e, t, n, i) {
  var r = nl(i) ? i : n(i), l = t.get(r);
  return typeof l > "u" && (l = e.call(this, i), t.set(r, l)), l;
}
function Ti(e, t, n) {
  var i = Array.prototype.slice.call(arguments, 3), r = n(i), l = t.get(r);
  return typeof l > "u" && (l = e.apply(this, i), t.set(r, l)), l;
}
function Vt(e, t, n, i, r) {
  return n.bind(t, e, i, r);
}
function il(e, t) {
  var n = e.length === 1 ? Ei : Ti;
  return Vt(e, this, n, t.cache.create(), t.serializer);
}
function rl(e, t) {
  return Vt(e, this, Ti, t.cache.create(), t.serializer);
}
function ll(e, t) {
  return Vt(e, this, Ei, t.cache.create(), t.serializer);
}
var sl = function() {
  return JSON.stringify(arguments);
};
function jt() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
jt.prototype.get = function(e) {
  return this.cache[e];
};
jt.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var ol = {
  create: function() {
    return new jt();
  }
}, mt = {
  variadic: rl,
  monadic: ll
}, Oe;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(Oe || (Oe = {}));
var at = (
  /** @class */
  function(e) {
    ot(t, e);
    function t(n, i, r) {
      var l = e.call(this, n) || this;
      return l.code = i, l.originalMessage = r, l;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), on = (
  /** @class */
  function(e) {
    ot(t, e);
    function t(n, i, r, l) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(i, '". Options are "').concat(Object.keys(r).join('", "'), '"'), Oe.INVALID_VALUE, l) || this;
    }
    return t;
  }(at)
), al = (
  /** @class */
  function(e) {
    ot(t, e);
    function t(n, i, r) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(i), Oe.INVALID_VALUE, r) || this;
    }
    return t;
  }(at)
), ul = (
  /** @class */
  function(e) {
    ot(t, e);
    function t(n, i) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(i, '"'), Oe.MISSING_VALUE, i) || this;
    }
    return t;
  }(at)
), J;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(J || (J = {}));
function fl(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var i = t[t.length - 1];
    return !i || i.type !== J.literal || n.type !== J.literal ? t.push(n) : i.value += n.value, t;
  }, []);
}
function hl(e) {
  return typeof e == "function";
}
function tt(e, t, n, i, r, l, s) {
  if (e.length === 1 && $t(e[0]))
    return [
      {
        type: J.literal,
        value: e[0].value
      }
    ];
  for (var a = [], u = 0, o = e; u < o.length; u++) {
    var f = o[u];
    if ($t(f)) {
      a.push({
        type: J.literal,
        value: f.value
      });
      continue;
    }
    if (Br(f)) {
      typeof l == "number" && a.push({
        type: J.literal,
        value: n.getNumberFormat(t).format(l)
      });
      continue;
    }
    var _ = f.value;
    if (!(r && _ in r))
      throw new ul(_, s);
    var h = r[_];
    if (Ar(f)) {
      (!h || typeof h == "string" || typeof h == "number") && (h = typeof h == "string" || typeof h == "number" ? String(h) : ""), a.push({
        type: typeof h == "string" ? J.literal : J.object,
        value: h
      });
      continue;
    }
    if (ui(f)) {
      var d = typeof f.style == "string" ? i.date[f.style] : St(f.style) ? f.style.parsedOptions : void 0;
      a.push({
        type: J.literal,
        value: n.getDateTimeFormat(t, d).format(h)
      });
      continue;
    }
    if (fi(f)) {
      var d = typeof f.style == "string" ? i.time[f.style] : St(f.style) ? f.style.parsedOptions : i.time.medium;
      a.push({
        type: J.literal,
        value: n.getDateTimeFormat(t, d).format(h)
      });
      continue;
    }
    if (ai(f)) {
      var d = typeof f.style == "string" ? i.number[f.style] : mi(f.style) ? f.style.parsedOptions : void 0;
      d && d.scale && (h = h * (d.scale || 1)), a.push({
        type: J.literal,
        value: n.getNumberFormat(t, d).format(h)
      });
      continue;
    }
    if (_i(f)) {
      var y = f.children, m = f.value, v = r[m];
      if (!hl(v))
        throw new al(m, "function", s);
      var E = tt(y, t, n, i, r, l), A = v(E.map(function(H) {
        return H.value;
      }));
      Array.isArray(A) || (A = [A]), a.push.apply(a, A.map(function(H) {
        return {
          type: typeof H == "string" ? J.literal : J.object,
          value: H
        };
      }));
    }
    if (hi(f)) {
      var p = f.options[h] || f.options.other;
      if (!p)
        throw new on(f.value, h, Object.keys(f.options), s);
      a.push.apply(a, tt(p.value, t, n, i, r));
      continue;
    }
    if (ci(f)) {
      var p = f.options["=".concat(h)];
      if (!p) {
        if (!Intl.PluralRules)
          throw new at(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, Oe.MISSING_INTL_API, s);
        var S = n.getPluralRules(t, { type: f.pluralType }).select(h - (f.offset || 0));
        p = f.options[S] || f.options.other;
      }
      if (!p)
        throw new on(f.value, h, Object.keys(f.options), s);
      a.push.apply(a, tt(p.value, t, n, i, r, h - (f.offset || 0)));
      continue;
    }
  }
  return fl(a);
}
function cl(e, t) {
  return t ? x(x(x({}, e || {}), t || {}), Object.keys(e).reduce(function(n, i) {
    return n[i] = x(x({}, e[i]), t[i] || {}), n;
  }, {})) : e;
}
function _l(e, t) {
  return t ? Object.keys(e).reduce(function(n, i) {
    return n[i] = cl(e[i], t[i]), n;
  }, x({}, e)) : e;
}
function dt(e) {
  return {
    create: function() {
      return {
        get: function(t) {
          return e[t];
        },
        set: function(t, n) {
          e[t] = n;
        }
      };
    }
  };
}
function ml(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: _t(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.NumberFormat).bind.apply(t, ht([void 0], n, !1)))();
    }, {
      cache: dt(e.number),
      strategy: mt.variadic
    }),
    getDateTimeFormat: _t(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, ht([void 0], n, !1)))();
    }, {
      cache: dt(e.dateTime),
      strategy: mt.variadic
    }),
    getPluralRules: _t(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.PluralRules).bind.apply(t, ht([void 0], n, !1)))();
    }, {
      cache: dt(e.pluralRules),
      strategy: mt.variadic
    })
  };
}
var dl = (
  /** @class */
  function() {
    function e(t, n, i, r) {
      var l = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(s) {
        var a = l.formatToParts(s);
        if (a.length === 1)
          return a[0].value;
        var u = a.reduce(function(o, f) {
          return !o.length || f.type !== J.literal || typeof o[o.length - 1] != "string" ? o.push(f.value) : o[o.length - 1] += f.value, o;
        }, []);
        return u.length <= 1 ? u[0] || "" : u;
      }, this.formatToParts = function(s) {
        return tt(l.ast, l.locales, l.formatters, l.formats, s, void 0, l.message);
      }, this.resolvedOptions = function() {
        return {
          locale: l.resolvedLocale.toString()
        };
      }, this.getAst = function() {
        return l.ast;
      }, this.locales = n, this.resolvedLocale = e.resolveLocale(n), typeof t == "string") {
        if (this.message = t, !e.__parse)
          throw new TypeError("IntlMessageFormat.__parse must be set to process `message` of type `string`");
        this.ast = e.__parse(t, {
          ignoreTag: r == null ? void 0 : r.ignoreTag,
          locale: this.resolvedLocale
        });
      } else
        this.ast = t;
      if (!Array.isArray(this.ast))
        throw new TypeError("A message must be provided as a String or AST.");
      this.formats = _l(e.formats, i), this.formatters = r && r.formatters || ml(this.formatterCache);
    }
    return Object.defineProperty(e, "defaultLocale", {
      get: function() {
        return e.memoizedDefaultLocale || (e.memoizedDefaultLocale = new Intl.NumberFormat().resolvedOptions().locale), e.memoizedDefaultLocale;
      },
      enumerable: !1,
      configurable: !0
    }), e.memoizedDefaultLocale = null, e.resolveLocale = function(t) {
      var n = Intl.NumberFormat.supportedLocalesOf(t);
      return n.length > 0 ? new Intl.Locale(n[0]) : new Intl.Locale(typeof t == "string" ? t : t[0]);
    }, e.__parse = tl, e.formats = {
      number: {
        integer: {
          maximumFractionDigits: 0
        },
        currency: {
          style: "currency"
        },
        percent: {
          style: "percent"
        }
      },
      date: {
        short: {
          month: "numeric",
          day: "numeric",
          year: "2-digit"
        },
        medium: {
          month: "short",
          day: "numeric",
          year: "numeric"
        },
        long: {
          month: "long",
          day: "numeric",
          year: "numeric"
        },
        full: {
          weekday: "long",
          month: "long",
          day: "numeric",
          year: "numeric"
        }
      },
      time: {
        short: {
          hour: "numeric",
          minute: "numeric"
        },
        medium: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric"
        },
        long: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        },
        full: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        }
      }
    }, e;
  }()
);
function gl(e, t) {
  if (t == null)
    return;
  if (t in e)
    return e[t];
  const n = t.split(".");
  let i = e;
  for (let r = 0; r < n.length; r++)
    if (typeof i == "object") {
      if (r > 0) {
        const l = n.slice(r, n.length).join(".");
        if (l in i) {
          i = i[l];
          break;
        }
      }
      i = i[n[r]];
    } else
      i = void 0;
  return i;
}
const pe = {}, bl = (e, t, n) => n && (t in pe || (pe[t] = {}), e in pe[t] || (pe[t][e] = n), n), Si = (e, t) => {
  if (t == null)
    return;
  if (t in pe && e in pe[t])
    return pe[t][e];
  const n = ut(t);
  for (let i = 0; i < n.length; i++) {
    const r = n[i], l = vl(r, e);
    if (l)
      return bl(e, t, l);
  }
};
let Xt;
const ze = Re({});
function pl(e) {
  return Xt[e] || null;
}
function Hi(e) {
  return e in Xt;
}
function vl(e, t) {
  if (!Hi(e))
    return null;
  const n = pl(e);
  return gl(n, t);
}
function yl(e) {
  if (e == null)
    return;
  const t = ut(e);
  for (let n = 0; n < t.length; n++) {
    const i = t[n];
    if (Hi(i))
      return i;
  }
}
function wl(e, ...t) {
  delete pe[e], ze.update((n) => (n[e] = Hr.all([n[e] || {}, ...t]), n));
}
Fe(
  [ze],
  ([e]) => Object.keys(e)
);
ze.subscribe((e) => Xt = e);
const nt = {};
function El(e, t) {
  nt[e].delete(t), nt[e].size === 0 && delete nt[e];
}
function Ai(e) {
  return nt[e];
}
function Tl(e) {
  return ut(e).map((t) => {
    const n = Ai(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function Nt(e) {
  return e == null ? !1 : ut(e).some(
    (t) => {
      var n;
      return (n = Ai(t)) == null ? void 0 : n.size;
    }
  );
}
function Sl(e, t) {
  return Promise.all(
    t.map((i) => (El(e, i), i().then((r) => r.default || r)))
  ).then((i) => wl(e, ...i));
}
const Ve = {};
function Bi(e) {
  if (!Nt(e))
    return e in Ve ? Ve[e] : Promise.resolve();
  const t = Tl(e);
  return Ve[e] = Promise.all(
    t.map(
      ([n, i]) => Sl(n, i)
    )
  ).then(() => {
    if (Nt(e))
      return Bi(e);
    delete Ve[e];
  }), Ve[e];
}
const Hl = {
  number: {
    scientific: { notation: "scientific" },
    engineering: { notation: "engineering" },
    compactLong: { notation: "compact", compactDisplay: "long" },
    compactShort: { notation: "compact", compactDisplay: "short" }
  },
  date: {
    short: { month: "numeric", day: "numeric", year: "2-digit" },
    medium: { month: "short", day: "numeric", year: "numeric" },
    long: { month: "long", day: "numeric", year: "numeric" },
    full: { weekday: "long", month: "long", day: "numeric", year: "numeric" }
  },
  time: {
    short: { hour: "numeric", minute: "numeric" },
    medium: { hour: "numeric", minute: "numeric", second: "numeric" },
    long: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    },
    full: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    }
  }
}, Al = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: Hl,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, Bl = Al;
function ke() {
  return Bl;
}
const gt = Re(!1);
var Pl = Object.defineProperty, Ml = Object.defineProperties, Nl = Object.getOwnPropertyDescriptors, an = Object.getOwnPropertySymbols, Il = Object.prototype.hasOwnProperty, Ll = Object.prototype.propertyIsEnumerable, un = (e, t, n) => t in e ? Pl(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, Ol = (e, t) => {
  for (var n in t || (t = {}))
    Il.call(t, n) && un(e, n, t[n]);
  if (an)
    for (var n of an(t))
      Ll.call(t, n) && un(e, n, t[n]);
  return e;
}, kl = (e, t) => Ml(e, Nl(t));
let It;
const rt = Re(null);
function fn(e) {
  return e.split("-").map((t, n, i) => i.slice(0, n + 1).join("-")).reverse();
}
function ut(e, t = ke().fallbackLocale) {
  const n = fn(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...fn(t)])] : n;
}
function Se() {
  return It ?? void 0;
}
rt.subscribe((e) => {
  It = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const Cl = (e) => {
  if (e && yl(e) && Nt(e)) {
    const { loadingDelay: t } = ke();
    let n;
    return typeof window < "u" && Se() != null && t ? n = window.setTimeout(
      () => gt.set(!0),
      t
    ) : gt.set(!0), Bi(e).then(() => {
      rt.set(e);
    }).finally(() => {
      clearTimeout(n), gt.set(!1);
    });
  }
  return rt.set(e);
}, Ze = kl(Ol({}, rt), {
  set: Cl
}), ft = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (i) => {
    const r = JSON.stringify(i);
    return r in t ? t[r] : t[r] = e(i);
  };
};
var Dl = Object.defineProperty, lt = Object.getOwnPropertySymbols, Pi = Object.prototype.hasOwnProperty, Mi = Object.prototype.propertyIsEnumerable, hn = (e, t, n) => t in e ? Dl(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, Wt = (e, t) => {
  for (var n in t || (t = {}))
    Pi.call(t, n) && hn(e, n, t[n]);
  if (lt)
    for (var n of lt(t))
      Mi.call(t, n) && hn(e, n, t[n]);
  return e;
}, Ue = (e, t) => {
  var n = {};
  for (var i in e)
    Pi.call(e, i) && t.indexOf(i) < 0 && (n[i] = e[i]);
  if (e != null && lt)
    for (var i of lt(e))
      t.indexOf(i) < 0 && Mi.call(e, i) && (n[i] = e[i]);
  return n;
};
const Ye = (e, t) => {
  const { formats: n } = ke();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, xl = ft(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ue(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return i && (r = Ye("number", i)), new Intl.NumberFormat(n, r);
  }
), Rl = ft(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ue(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return i ? r = Ye("date", i) : Object.keys(r).length === 0 && (r = Ye("date", "short")), new Intl.DateTimeFormat(n, r);
  }
), Fl = ft(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ue(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return i ? r = Ye("time", i) : Object.keys(r).length === 0 && (r = Ye("time", "short")), new Intl.DateTimeFormat(n, r);
  }
), Ul = (e = {}) => {
  var t = e, {
    locale: n = Se()
  } = t, i = Ue(t, [
    "locale"
  ]);
  return xl(Wt({ locale: n }, i));
}, Gl = (e = {}) => {
  var t = e, {
    locale: n = Se()
  } = t, i = Ue(t, [
    "locale"
  ]);
  return Rl(Wt({ locale: n }, i));
}, Vl = (e = {}) => {
  var t = e, {
    locale: n = Se()
  } = t, i = Ue(t, [
    "locale"
  ]);
  return Fl(Wt({ locale: n }, i));
}, jl = ft(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = Se()) => new dl(e, t, ke().formats, {
    ignoreTag: ke().ignoreTag
  })
), Xl = (e, t = {}) => {
  var n, i, r, l;
  let s = t;
  typeof e == "object" && (s = e, e = s.id);
  const {
    values: a,
    locale: u = Se(),
    default: o
  } = s;
  if (u == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = Si(e, u);
  if (!f)
    f = (l = (r = (i = (n = ke()).handleMissingMessage) == null ? void 0 : i.call(n, { locale: u, id: e, defaultValue: o })) != null ? r : o) != null ? l : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!a)
    return f;
  let _ = f;
  try {
    _ = jl(f, u).format(a);
  } catch (h) {
    h instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      h.message
    );
  }
  return _;
}, Wl = (e, t) => Vl(t).format(e), Yl = (e, t) => Gl(t).format(e), ql = (e, t) => Ul(t).format(e), zl = (e, t = Se()) => Si(e, t), Zl = Fe([Ze, ze], () => Xl);
Fe([Ze], () => Wl);
Fe([Ze], () => Yl);
Fe([Ze], () => ql);
Fe([Ze, ze], () => zl);
rr(Zl);
function Pe(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let i = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + i;
}
const {
  SvelteComponent: Ql,
  append: re,
  attr: O,
  component_subscribe: cn,
  detach: Jl,
  element: Kl,
  init: $l,
  insert: es,
  noop: _n,
  safe_not_equal: ts,
  set_style: Je,
  svg_element: le,
  toggle_class: mn
} = window.__gradio__svelte__internal, { onMount: ns } = window.__gradio__svelte__internal;
function is(e) {
  let t, n, i, r, l, s, a, u, o, f, _, h;
  return {
    c() {
      t = Kl("div"), n = le("svg"), i = le("g"), r = le("path"), l = le("path"), s = le("path"), a = le("path"), u = le("g"), o = le("path"), f = le("path"), _ = le("path"), h = le("path"), O(r, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), O(r, "fill", "#FF7C00"), O(r, "fill-opacity", "0.4"), O(r, "class", "svelte-43sxxs"), O(l, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), O(l, "fill", "#FF7C00"), O(l, "class", "svelte-43sxxs"), O(s, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), O(s, "fill", "#FF7C00"), O(s, "fill-opacity", "0.4"), O(s, "class", "svelte-43sxxs"), O(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), O(a, "fill", "#FF7C00"), O(a, "class", "svelte-43sxxs"), Je(i, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), O(o, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), O(o, "fill", "#FF7C00"), O(o, "fill-opacity", "0.4"), O(o, "class", "svelte-43sxxs"), O(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), O(f, "fill", "#FF7C00"), O(f, "class", "svelte-43sxxs"), O(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), O(_, "fill", "#FF7C00"), O(_, "fill-opacity", "0.4"), O(_, "class", "svelte-43sxxs"), O(h, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), O(h, "fill", "#FF7C00"), O(h, "class", "svelte-43sxxs"), Je(u, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), O(n, "viewBox", "-1200 -1200 3000 3000"), O(n, "fill", "none"), O(n, "xmlns", "http://www.w3.org/2000/svg"), O(n, "class", "svelte-43sxxs"), O(t, "class", "svelte-43sxxs"), mn(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(d, y) {
      es(d, t, y), re(t, n), re(n, i), re(i, r), re(i, l), re(i, s), re(i, a), re(n, u), re(u, o), re(u, f), re(u, _), re(u, h);
    },
    p(d, [y]) {
      y & /*$top*/
      2 && Je(i, "transform", "translate(" + /*$top*/
      d[1][0] + "px, " + /*$top*/
      d[1][1] + "px)"), y & /*$bottom*/
      4 && Je(u, "transform", "translate(" + /*$bottom*/
      d[2][0] + "px, " + /*$bottom*/
      d[2][1] + "px)"), y & /*margin*/
      1 && mn(
        t,
        "margin",
        /*margin*/
        d[0]
      );
    },
    i: _n,
    o: _n,
    d(d) {
      d && Jl(t);
    }
  };
}
function rs(e, t, n) {
  let i, r, { margin: l = !0 } = t;
  const s = Jt([0, 0]);
  cn(e, s, (h) => n(1, i = h));
  const a = Jt([0, 0]);
  cn(e, a, (h) => n(2, r = h));
  let u;
  async function o() {
    await Promise.all([s.set([125, 140]), a.set([-125, -140])]), await Promise.all([s.set([-125, 140]), a.set([125, -140])]), await Promise.all([s.set([-125, 0]), a.set([125, -0])]), await Promise.all([s.set([125, 0]), a.set([-125, 0])]);
  }
  async function f() {
    await o(), u || f();
  }
  async function _() {
    await Promise.all([s.set([125, 0]), a.set([-125, 0])]), f();
  }
  return ns(() => (_(), () => u = !0)), e.$$set = (h) => {
    "margin" in h && n(0, l = h.margin);
  }, [l, i, r, s, a];
}
class ls extends Ql {
  constructor(t) {
    super(), $l(this, t, rs, is, ts, { margin: 0 });
  }
}
const {
  SvelteComponent: ss,
  append: Ee,
  attr: ue,
  binding_callbacks: dn,
  check_outros: Ni,
  create_component: os,
  create_slot: as,
  destroy_component: us,
  destroy_each: Ii,
  detach: B,
  element: de,
  empty: Ge,
  ensure_array_like: st,
  get_all_dirty_from_scope: fs,
  get_slot_changes: hs,
  group_outros: Li,
  init: cs,
  insert: P,
  mount_component: _s,
  noop: Lt,
  safe_not_equal: ms,
  set_data: te,
  set_style: ve,
  space: fe,
  text: G,
  toggle_class: ee,
  transition_in: Ce,
  transition_out: De,
  update_slot_base: ds
} = window.__gradio__svelte__internal, { tick: gs } = window.__gradio__svelte__internal, { onDestroy: bs } = window.__gradio__svelte__internal, ps = (e) => ({}), gn = (e) => ({});
function bn(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i[40] = n, i;
}
function pn(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i;
}
function vs(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), i, r, l;
  const s = (
    /*#slots*/
    e[29].error
  ), a = as(
    s,
    e,
    /*$$scope*/
    e[28],
    gn
  );
  return {
    c() {
      t = de("span"), i = G(n), r = fe(), a && a.c(), ue(t, "class", "error svelte-14miwb5");
    },
    m(u, o) {
      P(u, t, o), Ee(t, i), P(u, r, o), a && a.m(u, o), l = !0;
    },
    p(u, o) {
      (!l || o[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      u[1]("common.error") + "") && te(i, n), a && a.p && (!l || o[0] & /*$$scope*/
      268435456) && ds(
        a,
        s,
        u,
        /*$$scope*/
        u[28],
        l ? hs(
          s,
          /*$$scope*/
          u[28],
          o,
          ps
        ) : fs(
          /*$$scope*/
          u[28]
        ),
        gn
      );
    },
    i(u) {
      l || (Ce(a, u), l = !0);
    },
    o(u) {
      De(a, u), l = !1;
    },
    d(u) {
      u && (B(t), B(r)), a && a.d(u);
    }
  };
}
function ys(e) {
  let t, n, i, r, l, s, a, u, o, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && vn(e)
  );
  function _(p, S) {
    if (
      /*progress*/
      p[7]
    )
      return Ts;
    if (
      /*queue_position*/
      p[2] !== null && /*queue_size*/
      p[3] !== void 0 && /*queue_position*/
      p[2] >= 0
    )
      return Es;
    if (
      /*queue_position*/
      p[2] === 0
    )
      return ws;
  }
  let h = _(e), d = h && h(e), y = (
    /*timer*/
    e[5] && En(e)
  );
  const m = [Bs, As], v = [];
  function E(p, S) {
    return (
      /*last_progress_level*/
      p[15] != null ? 0 : (
        /*show_progress*/
        p[6] === "full" ? 1 : -1
      )
    );
  }
  ~(l = E(e)) && (s = v[l] = m[l](e));
  let A = !/*timer*/
  e[5] && Mn(e);
  return {
    c() {
      f && f.c(), t = fe(), n = de("div"), d && d.c(), i = fe(), y && y.c(), r = fe(), s && s.c(), a = fe(), A && A.c(), u = Ge(), ue(n, "class", "progress-text svelte-14miwb5"), ee(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), ee(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(p, S) {
      f && f.m(p, S), P(p, t, S), P(p, n, S), d && d.m(n, null), Ee(n, i), y && y.m(n, null), P(p, r, S), ~l && v[l].m(p, S), P(p, a, S), A && A.m(p, S), P(p, u, S), o = !0;
    },
    p(p, S) {
      /*variant*/
      p[8] === "default" && /*show_eta_bar*/
      p[18] && /*show_progress*/
      p[6] === "full" ? f ? f.p(p, S) : (f = vn(p), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), h === (h = _(p)) && d ? d.p(p, S) : (d && d.d(1), d = h && h(p), d && (d.c(), d.m(n, i))), /*timer*/
      p[5] ? y ? y.p(p, S) : (y = En(p), y.c(), y.m(n, null)) : y && (y.d(1), y = null), (!o || S[0] & /*variant*/
      256) && ee(
        n,
        "meta-text-center",
        /*variant*/
        p[8] === "center"
      ), (!o || S[0] & /*variant*/
      256) && ee(
        n,
        "meta-text",
        /*variant*/
        p[8] === "default"
      );
      let H = l;
      l = E(p), l === H ? ~l && v[l].p(p, S) : (s && (Li(), De(v[H], 1, 1, () => {
        v[H] = null;
      }), Ni()), ~l ? (s = v[l], s ? s.p(p, S) : (s = v[l] = m[l](p), s.c()), Ce(s, 1), s.m(a.parentNode, a)) : s = null), /*timer*/
      p[5] ? A && (A.d(1), A = null) : A ? A.p(p, S) : (A = Mn(p), A.c(), A.m(u.parentNode, u));
    },
    i(p) {
      o || (Ce(s), o = !0);
    },
    o(p) {
      De(s), o = !1;
    },
    d(p) {
      p && (B(t), B(n), B(r), B(a), B(u)), f && f.d(p), d && d.d(), y && y.d(), ~l && v[l].d(p), A && A.d(p);
    }
  };
}
function vn(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = de("div"), ue(t, "class", "eta-bar svelte-14miwb5"), ve(t, "transform", n);
    },
    m(i, r) {
      P(i, t, r);
    },
    p(i, r) {
      r[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (i[17] || 0) * 100 - 100}%)`) && ve(t, "transform", n);
    },
    d(i) {
      i && B(t);
    }
  };
}
function ws(e) {
  let t;
  return {
    c() {
      t = G("processing |");
    },
    m(n, i) {
      P(n, t, i);
    },
    p: Lt,
    d(n) {
      n && B(t);
    }
  };
}
function Es(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), i, r, l, s;
  return {
    c() {
      t = G("queue: "), i = G(n), r = G("/"), l = G(
        /*queue_size*/
        e[3]
      ), s = G(" |");
    },
    m(a, u) {
      P(a, t, u), P(a, i, u), P(a, r, u), P(a, l, u), P(a, s, u);
    },
    p(a, u) {
      u[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      a[2] + 1 + "") && te(i, n), u[0] & /*queue_size*/
      8 && te(
        l,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (B(t), B(i), B(r), B(l), B(s));
    }
  };
}
function Ts(e) {
  let t, n = st(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = wn(pn(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Ge();
    },
    m(r, l) {
      for (let s = 0; s < i.length; s += 1)
        i[s] && i[s].m(r, l);
      P(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress*/
      128) {
        n = st(
          /*progress*/
          r[7]
        );
        let s;
        for (s = 0; s < n.length; s += 1) {
          const a = pn(r, n, s);
          i[s] ? i[s].p(a, l) : (i[s] = wn(a), i[s].c(), i[s].m(t.parentNode, t));
        }
        for (; s < i.length; s += 1)
          i[s].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && B(t), Ii(i, r);
    }
  };
}
function yn(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), i, r, l = " ", s;
  function a(f, _) {
    return (
      /*p*/
      f[38].length != null ? Hs : Ss
    );
  }
  let u = a(e), o = u(e);
  return {
    c() {
      o.c(), t = fe(), i = G(n), r = G(" | "), s = G(l);
    },
    m(f, _) {
      o.m(f, _), P(f, t, _), P(f, i, _), P(f, r, _), P(f, s, _);
    },
    p(f, _) {
      u === (u = a(f)) && o ? o.p(f, _) : (o.d(1), o = u(f), o && (o.c(), o.m(t.parentNode, t))), _[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && te(i, n);
    },
    d(f) {
      f && (B(t), B(i), B(r), B(s)), o.d(f);
    }
  };
}
function Ss(e) {
  let t = Pe(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = G(t);
    },
    m(i, r) {
      P(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = Pe(
        /*p*/
        i[38].index || 0
      ) + "") && te(n, t);
    },
    d(i) {
      i && B(n);
    }
  };
}
function Hs(e) {
  let t = Pe(
    /*p*/
    e[38].index || 0
  ) + "", n, i, r = Pe(
    /*p*/
    e[38].length
  ) + "", l;
  return {
    c() {
      n = G(t), i = G("/"), l = G(r);
    },
    m(s, a) {
      P(s, n, a), P(s, i, a), P(s, l, a);
    },
    p(s, a) {
      a[0] & /*progress*/
      128 && t !== (t = Pe(
        /*p*/
        s[38].index || 0
      ) + "") && te(n, t), a[0] & /*progress*/
      128 && r !== (r = Pe(
        /*p*/
        s[38].length
      ) + "") && te(l, r);
    },
    d(s) {
      s && (B(n), B(i), B(l));
    }
  };
}
function wn(e) {
  let t, n = (
    /*p*/
    e[38].index != null && yn(e)
  );
  return {
    c() {
      n && n.c(), t = Ge();
    },
    m(i, r) {
      n && n.m(i, r), P(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].index != null ? n ? n.p(i, r) : (n = yn(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && B(t), n && n.d(i);
    }
  };
}
function En(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), i, r;
  return {
    c() {
      t = G(
        /*formatted_timer*/
        e[20]
      ), i = G(n), r = G("s");
    },
    m(l, s) {
      P(l, t, s), P(l, i, s), P(l, r, s);
    },
    p(l, s) {
      s[0] & /*formatted_timer*/
      1048576 && te(
        t,
        /*formatted_timer*/
        l[20]
      ), s[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      l[0] ? `/${/*formatted_eta*/
      l[19]}` : "") && te(i, n);
    },
    d(l) {
      l && (B(t), B(i), B(r));
    }
  };
}
function As(e) {
  let t, n;
  return t = new ls({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      os(t.$$.fragment);
    },
    m(i, r) {
      _s(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*variant*/
      256 && (l.margin = /*variant*/
      i[8] === "default"), t.$set(l);
    },
    i(i) {
      n || (Ce(t.$$.fragment, i), n = !0);
    },
    o(i) {
      De(t.$$.fragment, i), n = !1;
    },
    d(i) {
      us(t, i);
    }
  };
}
function Bs(e) {
  let t, n, i, r, l, s = `${/*last_progress_level*/
  e[15] * 100}%`, a = (
    /*progress*/
    e[7] != null && Tn(e)
  );
  return {
    c() {
      t = de("div"), n = de("div"), a && a.c(), i = fe(), r = de("div"), l = de("div"), ue(n, "class", "progress-level-inner svelte-14miwb5"), ue(l, "class", "progress-bar svelte-14miwb5"), ve(l, "width", s), ue(r, "class", "progress-bar-wrap svelte-14miwb5"), ue(t, "class", "progress-level svelte-14miwb5");
    },
    m(u, o) {
      P(u, t, o), Ee(t, n), a && a.m(n, null), Ee(t, i), Ee(t, r), Ee(r, l), e[30](l);
    },
    p(u, o) {
      /*progress*/
      u[7] != null ? a ? a.p(u, o) : (a = Tn(u), a.c(), a.m(n, null)) : a && (a.d(1), a = null), o[0] & /*last_progress_level*/
      32768 && s !== (s = `${/*last_progress_level*/
      u[15] * 100}%`) && ve(l, "width", s);
    },
    i: Lt,
    o: Lt,
    d(u) {
      u && B(t), a && a.d(), e[30](null);
    }
  };
}
function Tn(e) {
  let t, n = st(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = Pn(bn(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Ge();
    },
    m(r, l) {
      for (let s = 0; s < i.length; s += 1)
        i[s] && i[s].m(r, l);
      P(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress_level, progress*/
      16512) {
        n = st(
          /*progress*/
          r[7]
        );
        let s;
        for (s = 0; s < n.length; s += 1) {
          const a = bn(r, n, s);
          i[s] ? i[s].p(a, l) : (i[s] = Pn(a), i[s].c(), i[s].m(t.parentNode, t));
        }
        for (; s < i.length; s += 1)
          i[s].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && B(t), Ii(i, r);
    }
  };
}
function Sn(e) {
  let t, n, i, r, l = (
    /*i*/
    e[40] !== 0 && Ps()
  ), s = (
    /*p*/
    e[38].desc != null && Hn(e)
  ), a = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && An()
  ), u = (
    /*progress_level*/
    e[14] != null && Bn(e)
  );
  return {
    c() {
      l && l.c(), t = fe(), s && s.c(), n = fe(), a && a.c(), i = fe(), u && u.c(), r = Ge();
    },
    m(o, f) {
      l && l.m(o, f), P(o, t, f), s && s.m(o, f), P(o, n, f), a && a.m(o, f), P(o, i, f), u && u.m(o, f), P(o, r, f);
    },
    p(o, f) {
      /*p*/
      o[38].desc != null ? s ? s.p(o, f) : (s = Hn(o), s.c(), s.m(n.parentNode, n)) : s && (s.d(1), s = null), /*p*/
      o[38].desc != null && /*progress_level*/
      o[14] && /*progress_level*/
      o[14][
        /*i*/
        o[40]
      ] != null ? a || (a = An(), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null), /*progress_level*/
      o[14] != null ? u ? u.p(o, f) : (u = Bn(o), u.c(), u.m(r.parentNode, r)) : u && (u.d(1), u = null);
    },
    d(o) {
      o && (B(t), B(n), B(i), B(r)), l && l.d(o), s && s.d(o), a && a.d(o), u && u.d(o);
    }
  };
}
function Ps(e) {
  let t;
  return {
    c() {
      t = G(" /");
    },
    m(n, i) {
      P(n, t, i);
    },
    d(n) {
      n && B(t);
    }
  };
}
function Hn(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = G(t);
    },
    m(i, r) {
      P(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = /*p*/
      i[38].desc + "") && te(n, t);
    },
    d(i) {
      i && B(n);
    }
  };
}
function An(e) {
  let t;
  return {
    c() {
      t = G("-");
    },
    m(n, i) {
      P(n, t, i);
    },
    d(n) {
      n && B(t);
    }
  };
}
function Bn(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, i;
  return {
    c() {
      n = G(t), i = G("%");
    },
    m(r, l) {
      P(r, n, l), P(r, i, l);
    },
    p(r, l) {
      l[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (r[14][
        /*i*/
        r[40]
      ] || 0)).toFixed(1) + "") && te(n, t);
    },
    d(r) {
      r && (B(n), B(i));
    }
  };
}
function Pn(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && Sn(e)
  );
  return {
    c() {
      n && n.c(), t = Ge();
    },
    m(i, r) {
      n && n.m(i, r), P(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].desc != null || /*progress_level*/
      i[14] && /*progress_level*/
      i[14][
        /*i*/
        i[40]
      ] != null ? n ? n.p(i, r) : (n = Sn(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && B(t), n && n.d(i);
    }
  };
}
function Mn(e) {
  let t, n;
  return {
    c() {
      t = de("p"), n = G(
        /*loading_text*/
        e[9]
      ), ue(t, "class", "loading svelte-14miwb5");
    },
    m(i, r) {
      P(i, t, r), Ee(t, n);
    },
    p(i, r) {
      r[0] & /*loading_text*/
      512 && te(
        n,
        /*loading_text*/
        i[9]
      );
    },
    d(i) {
      i && B(t);
    }
  };
}
function Ms(e) {
  let t, n, i, r, l;
  const s = [ys, vs], a = [];
  function u(o, f) {
    return (
      /*status*/
      o[4] === "pending" ? 0 : (
        /*status*/
        o[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = u(e)) && (i = a[n] = s[n](e)), {
    c() {
      t = de("div"), i && i.c(), ue(t, "class", r = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-14miwb5"), ee(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), ee(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), ee(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), ee(
        t,
        "border",
        /*border*/
        e[12]
      ), ve(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), ve(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(o, f) {
      P(o, t, f), ~n && a[n].m(t, null), e[31](t), l = !0;
    },
    p(o, f) {
      let _ = n;
      n = u(o), n === _ ? ~n && a[n].p(o, f) : (i && (Li(), De(a[_], 1, 1, () => {
        a[_] = null;
      }), Ni()), ~n ? (i = a[n], i ? i.p(o, f) : (i = a[n] = s[n](o), i.c()), Ce(i, 1), i.m(t, null)) : i = null), (!l || f[0] & /*variant, show_progress*/
      320 && r !== (r = "wrap " + /*variant*/
      o[8] + " " + /*show_progress*/
      o[6] + " svelte-14miwb5")) && ue(t, "class", r), (!l || f[0] & /*variant, show_progress, status, show_progress*/
      336) && ee(t, "hide", !/*status*/
      o[4] || /*status*/
      o[4] === "complete" || /*show_progress*/
      o[6] === "hidden"), (!l || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && ee(
        t,
        "translucent",
        /*variant*/
        o[8] === "center" && /*status*/
        (o[4] === "pending" || /*status*/
        o[4] === "error") || /*translucent*/
        o[11] || /*show_progress*/
        o[6] === "minimal"
      ), (!l || f[0] & /*variant, show_progress, status*/
      336) && ee(
        t,
        "generating",
        /*status*/
        o[4] === "generating"
      ), (!l || f[0] & /*variant, show_progress, border*/
      4416) && ee(
        t,
        "border",
        /*border*/
        o[12]
      ), f[0] & /*absolute*/
      1024 && ve(
        t,
        "position",
        /*absolute*/
        o[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && ve(
        t,
        "padding",
        /*absolute*/
        o[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(o) {
      l || (Ce(i), l = !0);
    },
    o(o) {
      De(i), l = !1;
    },
    d(o) {
      o && B(t), ~n && a[n].d(), e[31](null);
    }
  };
}
let Ke = [], bt = !1;
async function Ns(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (Ke.push(e), !bt)
      bt = !0;
    else
      return;
    await gs(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let i = 0; i < Ke.length; i++) {
        const l = Ke[i].getBoundingClientRect();
        (i === 0 || l.top + window.scrollY <= n[0]) && (n[0] = l.top + window.scrollY, n[1] = i);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), bt = !1, Ke = [];
    });
  }
}
function Is(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { i18n: s } = t, { eta: a = null } = t, { queue: u = !1 } = t, { queue_position: o } = t, { queue_size: f } = t, { status: _ } = t, { scroll_to_output: h = !1 } = t, { timer: d = !0 } = t, { show_progress: y = "full" } = t, { message: m = null } = t, { progress: v = null } = t, { variant: E = "default" } = t, { loading_text: A = "Loading..." } = t, { absolute: p = !0 } = t, { translucent: S = !1 } = t, { border: H = !1 } = t, { autoscroll: I } = t, Y, q = !1, ne = 0, Z = 0, se = null, Q = 0, D = null, U, C = null, b = !0;
  const R = () => {
    n(25, ne = performance.now()), n(26, Z = 0), q = !0, z();
  };
  function z() {
    requestAnimationFrame(() => {
      n(26, Z = (performance.now() - ne) / 1e3), q && z();
    });
  }
  function V() {
    n(26, Z = 0), q && (q = !1);
  }
  bs(() => {
    q && V();
  });
  let ie = null;
  function W(T) {
    dn[T ? "unshift" : "push"](() => {
      C = T, n(16, C), n(7, v), n(14, D), n(15, U);
    });
  }
  function oe(T) {
    dn[T ? "unshift" : "push"](() => {
      Y = T, n(13, Y);
    });
  }
  return e.$$set = (T) => {
    "i18n" in T && n(1, s = T.i18n), "eta" in T && n(0, a = T.eta), "queue" in T && n(21, u = T.queue), "queue_position" in T && n(2, o = T.queue_position), "queue_size" in T && n(3, f = T.queue_size), "status" in T && n(4, _ = T.status), "scroll_to_output" in T && n(22, h = T.scroll_to_output), "timer" in T && n(5, d = T.timer), "show_progress" in T && n(6, y = T.show_progress), "message" in T && n(23, m = T.message), "progress" in T && n(7, v = T.progress), "variant" in T && n(8, E = T.variant), "loading_text" in T && n(9, A = T.loading_text), "absolute" in T && n(10, p = T.absolute), "translucent" in T && n(11, S = T.translucent), "border" in T && n(12, H = T.border), "autoscroll" in T && n(24, I = T.autoscroll), "$$scope" in T && n(28, l = T.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (a === null ? n(0, a = se) : u && n(0, a = (performance.now() - ne) / 1e3 + a), a != null && (n(19, ie = a.toFixed(1)), n(27, se = a))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, Q = a === null || a <= 0 || !Z ? null : Math.min(Z / a, 1)), e.$$.dirty[0] & /*progress*/
    128 && v != null && n(18, b = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? n(14, D = v.map((T) => {
      if (T.index != null && T.length != null)
        return T.index / T.length;
      if (T.progress != null)
        return T.progress;
    })) : n(14, D = null), D ? (n(15, U = D[D.length - 1]), C && (U === 0 ? n(16, C.style.transition = "0", C) : n(16, C.style.transition = "150ms", C))) : n(15, U = void 0)), e.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? R() : V()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && Y && h && (_ === "pending" || _ === "complete") && Ns(Y, I), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, i = Z.toFixed(1));
  }, [
    a,
    s,
    o,
    f,
    _,
    d,
    y,
    v,
    E,
    A,
    p,
    S,
    H,
    Y,
    D,
    U,
    C,
    Q,
    b,
    ie,
    i,
    u,
    h,
    m,
    I,
    ne,
    Z,
    se,
    l,
    r,
    W,
    oe
  ];
}
class Ls extends ss {
  constructor(t) {
    super(), cs(
      this,
      t,
      Is,
      Ms,
      ms,
      {
        i18n: 1,
        eta: 0,
        queue: 21,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
function Os(e) {
  return e % 4 === 0 && e % 100 !== 0 || e % 400 === 0;
}
function qe(e, t) {
  return [31, Os(e) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][t];
}
function Nn(e, t) {
  let n = "";
  if (e)
    for (const i of t)
      typeof i == "string" ? n += i : n += i.toString(e);
  return n;
}
function pt(e, t) {
  const n = qe(e, t), i = [];
  for (let r = 0; r < n; r++)
    i.push({
      year: e,
      month: t,
      number: r + 1
    });
  return i;
}
function ks(e, t) {
  const n = e.getFullYear(), i = e.getMonth(), r = new Date(n, i, 1).getDay();
  let l = [];
  const s = (r - t + 7) % 7;
  if (s > 0) {
    let f = i - 1, _ = n;
    f === -1 && (f = 11, _ = n - 1), l = pt(_, f).slice(-s);
  }
  l = l.concat(pt(n, i));
  let a = i + 1, u = n;
  a === 12 && (a = 0, u = n + 1);
  const o = 42 - l.length;
  return l = l.concat(pt(u, a).slice(0, o)), l;
}
function Cs() {
  return {
    weekdays: ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"],
    months: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December"
    ],
    weekStartsOn: 1
  };
}
function Ds(e = {}) {
  const t = Cs();
  return typeof e.weekStartsOn == "number" && (t.weekStartsOn = e.weekStartsOn), e.months && (t.months = e.months), e.weekdays && (t.weekdays = e.weekdays), t;
}
const {
  SvelteComponent: xs,
  append: k,
  attr: M,
  bubble: Rs,
  destroy_each: ye,
  detach: he,
  element: X,
  empty: Fs,
  ensure_array_like: K,
  init: Us,
  insert: ce,
  listen: _e,
  noop: In,
  run_all: Gs,
  safe_not_equal: Vs,
  select_option: $e,
  set_data: He,
  set_input_value: xe,
  space: ae,
  svg_element: et,
  text: Ae,
  toggle_class: be
} = window.__gradio__svelte__internal, { createEventDispatcher: js } = window.__gradio__svelte__internal;
function Ln(e, t, n) {
  const i = e.slice();
  return i[29] = t[n], i[31] = n, i;
}
function On(e, t, n) {
  const i = e.slice();
  return i[32] = t[n], i;
}
function kn(e, t, n) {
  const i = e.slice();
  return i[29] = t[n], i[36] = n, i;
}
function Cn(e, t, n) {
  const i = e.slice();
  return i[37] = t[n], i;
}
function Dn(e, t, n) {
  const i = e.slice();
  return i[37] = t[n], i;
}
function xn(e, t, n) {
  const i = e.slice();
  return i[42] = t[n], i[36] = n, i;
}
function Rn(e, t, n) {
  const i = e.slice();
  return i[42] = t[n], i[36] = n, i;
}
function Fn(e) {
  let t, n = (
    /*monthName*/
    e[42] + ""
  ), i, r;
  return {
    c() {
      t = X("option"), i = Ae(n), t.disabled = r = new Date(
        /*browseYear*/
        e[8],
        /*i*/
        e[36],
        qe(
          /*browseYear*/
          e[8],
          /*i*/
          e[36]
        ),
        23,
        59,
        59,
        999
      ) < /*min*/
      e[1] || new Date(
        /*browseYear*/
        e[8],
        /*i*/
        e[36]
      ) > /*max*/
      e[2], t.__value = /*i*/
      e[36], xe(t, t.__value);
    },
    m(l, s) {
      ce(l, t, s), k(t, i);
    },
    p(l, s) {
      s[0] & /*iLocale*/
      16 && n !== (n = /*monthName*/
      l[42] + "") && He(i, n), s[0] & /*browseYear, min, max, years*/
      294 && r !== (r = new Date(
        /*browseYear*/
        l[8],
        /*i*/
        l[36],
        qe(
          /*browseYear*/
          l[8],
          /*i*/
          l[36]
        ),
        23,
        59,
        59,
        999
      ) < /*min*/
      l[1] || new Date(
        /*browseYear*/
        l[8],
        /*i*/
        l[36]
      ) > /*max*/
      l[2]) && (t.disabled = r);
    },
    d(l) {
      l && he(t);
    }
  };
}
function Un(e) {
  let t, n = (
    /*monthName*/
    e[42] + ""
  ), i, r;
  return {
    c() {
      t = X("option"), i = Ae(n), t.__value = /*i*/
      e[36], xe(t, t.__value), t.selected = r = /*i*/
      e[36] === /*browseMonth*/
      e[7];
    },
    m(l, s) {
      ce(l, t, s), k(t, i);
    },
    p(l, s) {
      s[0] & /*iLocale*/
      16 && n !== (n = /*monthName*/
      l[42] + "") && He(i, n), s[0] & /*browseMonth*/
      128 && r !== (r = /*i*/
      l[36] === /*browseMonth*/
      l[7]) && (t.selected = r);
    },
    d(l) {
      l && he(t);
    }
  };
}
function Gn(e) {
  let t, n = (
    /*v*/
    e[37] + ""
  ), i, r;
  return {
    c() {
      t = X("option"), i = Ae(n), t.__value = r = /*v*/
      e[37], xe(t, t.__value);
    },
    m(l, s) {
      ce(l, t, s), k(t, i);
    },
    p(l, s) {
      s[0] & /*years*/
      32 && n !== (n = /*v*/
      l[37] + "") && He(i, n), s[0] & /*years*/
      32 && r !== (r = /*v*/
      l[37]) && (t.__value = r, xe(t, t.__value));
    },
    d(l) {
      l && he(t);
    }
  };
}
function Vn(e) {
  let t, n = (
    /*v*/
    e[37] + ""
  ), i, r, l;
  return {
    c() {
      t = X("option"), i = Ae(n), t.__value = r = /*v*/
      e[37], xe(t, t.__value), t.selected = l = /*v*/
      e[37] === /*browseDate*/
      e[3].getFullYear();
    },
    m(s, a) {
      ce(s, t, a), k(t, i);
    },
    p(s, a) {
      a[0] & /*years*/
      32 && n !== (n = /*v*/
      s[37] + "") && He(i, n), a[0] & /*years*/
      32 && r !== (r = /*v*/
      s[37]) && (t.__value = r, xe(t, t.__value)), a[0] & /*years, browseDate*/
      40 && l !== (l = /*v*/
      s[37] === /*browseDate*/
      s[3].getFullYear()) && (t.selected = l);
    },
    d(s) {
      s && he(t);
    }
  };
}
function Xs(e) {
  let t, n = (
    /*iLocale*/
    e[4].weekdays[
      /*iLocale*/
      e[4].weekStartsOn + /*i*/
      e[36] - 7
    ] + ""
  ), i;
  return {
    c() {
      t = X("div"), i = Ae(n), M(t, "class", "header-cell svelte-w239uu");
    },
    m(r, l) {
      ce(r, t, l), k(t, i);
    },
    p(r, l) {
      l[0] & /*iLocale*/
      16 && n !== (n = /*iLocale*/
      r[4].weekdays[
        /*iLocale*/
        r[4].weekStartsOn + /*i*/
        r[36] - 7
      ] + "") && He(i, n);
    },
    d(r) {
      r && he(t);
    }
  };
}
function Ws(e) {
  let t, n = (
    /*iLocale*/
    e[4].weekdays[
      /*iLocale*/
      e[4].weekStartsOn + /*i*/
      e[36]
    ] + ""
  ), i;
  return {
    c() {
      t = X("div"), i = Ae(n), M(t, "class", "header-cell svelte-w239uu");
    },
    m(r, l) {
      ce(r, t, l), k(t, i);
    },
    p(r, l) {
      l[0] & /*iLocale*/
      16 && n !== (n = /*iLocale*/
      r[4].weekdays[
        /*iLocale*/
        r[4].weekStartsOn + /*i*/
        r[36]
      ] + "") && He(i, n);
    },
    d(r) {
      r && he(t);
    }
  };
}
function jn(e) {
  let t;
  function n(l, s) {
    return (
      /*i*/
      l[36] + /*iLocale*/
      l[4].weekStartsOn < 7 ? Ws : Xs
    );
  }
  let i = n(e), r = i(e);
  return {
    c() {
      r.c(), t = Fs();
    },
    m(l, s) {
      r.m(l, s), ce(l, t, s);
    },
    p(l, s) {
      i === (i = n(l)) && r ? r.p(l, s) : (r.d(1), r = i(l), r && (r.c(), r.m(t.parentNode, t)));
    },
    d(l) {
      l && he(t), r.d(l);
    }
  };
}
function Xn(e) {
  let t, n, i = (
    /*calendarDay*/
    e[32].number + ""
  ), r, l, s;
  function a() {
    return (
      /*click_handler_2*/
      e[23](
        /*calendarDay*/
        e[32]
      )
    );
  }
  return {
    c() {
      t = X("div"), n = X("span"), r = Ae(i), M(n, "class", "svelte-w239uu"), M(t, "class", "cell svelte-w239uu"), be(t, "disabled", !Ot(
        /*calendarDay*/
        e[32],
        /*min*/
        e[1],
        /*max*/
        e[2]
      )), be(
        t,
        "selected",
        /*value*/
        e[0] && /*calendarDay*/
        e[32].year === /*value*/
        e[0].getFullYear() && /*calendarDay*/
        e[32].month === /*value*/
        e[0].getMonth() && /*calendarDay*/
        e[32].number === /*value*/
        e[0].getDate()
      ), be(
        t,
        "today",
        /*calendarDay*/
        e[32].year === /*todayDate*/
        e[9].getFullYear() && /*calendarDay*/
        e[32].month === /*todayDate*/
        e[9].getMonth() && /*calendarDay*/
        e[32].number === /*todayDate*/
        e[9].getDate()
      ), be(
        t,
        "other-month",
        /*calendarDay*/
        e[32].month !== /*browseMonth*/
        e[7]
      );
    },
    m(u, o) {
      ce(u, t, o), k(t, n), k(n, r), l || (s = _e(t, "click", a), l = !0);
    },
    p(u, o) {
      e = u, o[0] & /*calendarDays*/
      64 && i !== (i = /*calendarDay*/
      e[32].number + "") && He(r, i), o[0] & /*calendarDays, min, max*/
      70 && be(t, "disabled", !Ot(
        /*calendarDay*/
        e[32],
        /*min*/
        e[1],
        /*max*/
        e[2]
      )), o[0] & /*value, calendarDays*/
      65 && be(
        t,
        "selected",
        /*value*/
        e[0] && /*calendarDay*/
        e[32].year === /*value*/
        e[0].getFullYear() && /*calendarDay*/
        e[32].month === /*value*/
        e[0].getMonth() && /*calendarDay*/
        e[32].number === /*value*/
        e[0].getDate()
      ), o[0] & /*calendarDays, todayDate*/
      576 && be(
        t,
        "today",
        /*calendarDay*/
        e[32].year === /*todayDate*/
        e[9].getFullYear() && /*calendarDay*/
        e[32].month === /*todayDate*/
        e[9].getMonth() && /*calendarDay*/
        e[32].number === /*todayDate*/
        e[9].getDate()
      ), o[0] & /*calendarDays, browseMonth*/
      192 && be(
        t,
        "other-month",
        /*calendarDay*/
        e[32].month !== /*browseMonth*/
        e[7]
      );
    },
    d(u) {
      u && he(t), l = !1, s();
    }
  };
}
function Wn(e) {
  let t, n, i = K(
    /*calendarDays*/
    e[6].slice(
      /*weekIndex*/
      e[31] * 7,
      /*weekIndex*/
      e[31] * 7 + 7
    )
  ), r = [];
  for (let l = 0; l < i.length; l += 1)
    r[l] = Xn(On(e, i, l));
  return {
    c() {
      t = X("div");
      for (let l = 0; l < r.length; l += 1)
        r[l].c();
      n = ae(), M(t, "class", "week svelte-w239uu");
    },
    m(l, s) {
      ce(l, t, s);
      for (let a = 0; a < r.length; a += 1)
        r[a] && r[a].m(t, null);
      k(t, n);
    },
    p(l, s) {
      if (s[0] & /*calendarDays, min, max, value, todayDate, browseMonth, selectDay*/
      4807) {
        i = K(
          /*calendarDays*/
          l[6].slice(
            /*weekIndex*/
            l[31] * 7,
            /*weekIndex*/
            l[31] * 7 + 7
          )
        );
        let a;
        for (a = 0; a < i.length; a += 1) {
          const u = On(l, i, a);
          r[a] ? r[a].p(u, s) : (r[a] = Xn(u), r[a].c(), r[a].m(t, n));
        }
        for (; a < r.length; a += 1)
          r[a].d(1);
        r.length = i.length;
      }
    },
    d(l) {
      l && he(t), ye(r, l);
    }
  };
}
function Ys(e) {
  let t, n, i, r, l, s, a, u, o, f, _, h, d, y, m, v, E, A, p, S, H, I, Y, q, ne, Z, se, Q = K(
    /*iLocale*/
    e[4].months
  ), D = [];
  for (let w = 0; w < Q.length; w += 1)
    D[w] = Fn(Rn(e, Q, w));
  let U = K(
    /*iLocale*/
    e[4].months
  ), C = [];
  for (let w = 0; w < U.length; w += 1)
    C[w] = Un(xn(e, U, w));
  let b = K(
    /*years*/
    e[5]
  ), R = [];
  for (let w = 0; w < b.length; w += 1)
    R[w] = Gn(Dn(e, b, w));
  let z = K(
    /*years*/
    e[5]
  ), V = [];
  for (let w = 0; w < z.length; w += 1)
    V[w] = Vn(Cn(e, z, w));
  let ie = K(Array(7)), W = [];
  for (let w = 0; w < ie.length; w += 1)
    W[w] = jn(kn(e, ie, w));
  let oe = K(Array(6)), T = [];
  for (let w = 0; w < oe.length; w += 1)
    T[w] = Wn(Ln(e, oe, w));
  return {
    c() {
      t = X("div"), n = X("div"), i = X("div"), r = X("button"), r.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="svelte-w239uu"><path d="M5 3l3.057-3 11.943 12-11.943 12-3.057-3 9-9z" transform="rotate(180, 12, 12)"></path></svg>', l = ae(), s = X("div"), a = X("select");
      for (let w = 0; w < D.length; w += 1)
        D[w].c();
      u = ae(), o = X("select");
      for (let w = 0; w < C.length; w += 1)
        C[w].c();
      f = ae(), _ = et("svg"), h = et("path"), d = ae(), y = X("div"), m = X("select");
      for (let w = 0; w < R.length; w += 1)
        R[w].c();
      v = ae(), E = X("select");
      for (let w = 0; w < V.length; w += 1)
        V[w].c();
      A = ae(), p = et("svg"), S = et("path"), H = ae(), I = X("button"), I.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="svelte-w239uu"><path d="M5 3l3.057-3 11.943 12-11.943 12-3.057-3 9-9z"></path></svg>', Y = ae(), q = X("div");
      for (let w = 0; w < W.length; w += 1)
        W[w].c();
      ne = ae();
      for (let w = 0; w < T.length; w += 1)
        T[w].c();
      M(r, "type", "button"), M(r, "class", "page-button svelte-w239uu"), M(r, "tabindex", "-1"), M(a, "class", "svelte-w239uu"), M(o, "class", "dummy-select svelte-w239uu"), M(o, "tabindex", "-1"), M(h, "d", "M6 0l12 12-12 12z"), M(h, "transform", "rotate(90, 12, 12)"), M(_, "xmlns", "http://www.w3.org/2000/svg"), M(_, "width", "24"), M(_, "height", "24"), M(_, "viewBox", "0 0 24 24"), M(_, "class", "svelte-w239uu"), M(s, "class", "dropdown month svelte-w239uu"), M(m, "class", "svelte-w239uu"), M(E, "class", "dummy-select svelte-w239uu"), M(E, "tabindex", "-1"), M(S, "d", "M6 0l12 12-12 12z"), M(S, "transform", "rotate(90, 12, 12)"), M(p, "xmlns", "http://www.w3.org/2000/svg"), M(p, "width", "24"), M(p, "height", "24"), M(p, "viewBox", "0 0 24 24"), M(p, "class", "svelte-w239uu"), M(y, "class", "dropdown year svelte-w239uu"), M(I, "type", "button"), M(I, "class", "page-button svelte-w239uu"), M(I, "tabindex", "-1"), M(i, "class", "top svelte-w239uu"), M(q, "class", "header svelte-w239uu"), M(n, "class", "tab-container svelte-w239uu"), M(n, "tabindex", "-1"), M(t, "class", "date-time-picker svelte-w239uu"), M(t, "tabindex", "0");
    },
    m(w, g) {
      ce(w, t, g), k(t, n), k(n, i), k(i, r), k(i, l), k(i, s), k(s, a);
      for (let c = 0; c < D.length; c += 1)
        D[c] && D[c].m(a, null);
      $e(
        a,
        /*browseMonth*/
        e[7]
      ), k(s, u), k(s, o);
      for (let c = 0; c < C.length; c += 1)
        C[c] && C[c].m(o, null);
      k(s, f), k(s, _), k(_, h), k(i, d), k(i, y), k(y, m);
      for (let c = 0; c < R.length; c += 1)
        R[c] && R[c].m(m, null);
      $e(
        m,
        /*browseYear*/
        e[8]
      ), k(y, v), k(y, E);
      for (let c = 0; c < V.length; c += 1)
        V[c] && V[c].m(E, null);
      k(y, A), k(y, p), k(p, S), k(i, H), k(i, I), k(n, Y), k(n, q);
      for (let c = 0; c < W.length; c += 1)
        W[c] && W[c].m(q, null);
      k(n, ne);
      for (let c = 0; c < T.length; c += 1)
        T[c] && T[c].m(n, null);
      Z || (se = [
        _e(
          r,
          "click",
          /*click_handler*/
          e[19]
        ),
        _e(
          a,
          "keydown",
          /*monthKeydown*/
          e[14]
        ),
        _e(
          a,
          "input",
          /*input_handler*/
          e[20]
        ),
        _e(
          m,
          "input",
          /*input_handler_1*/
          e[21]
        ),
        _e(
          m,
          "keydown",
          /*yearKeydown*/
          e[13]
        ),
        _e(
          I,
          "click",
          /*click_handler_1*/
          e[22]
        ),
        _e(
          t,
          "focusout",
          /*focusout_handler*/
          e[18]
        ),
        _e(
          t,
          "keydown",
          /*keydown*/
          e[15]
        )
      ], Z = !0);
    },
    p(w, g) {
      if (g[0] & /*browseYear, min, max, iLocale*/
      278) {
        Q = K(
          /*iLocale*/
          w[4].months
        );
        let c;
        for (c = 0; c < Q.length; c += 1) {
          const j = Rn(w, Q, c);
          D[c] ? D[c].p(j, g) : (D[c] = Fn(j), D[c].c(), D[c].m(a, null));
        }
        for (; c < D.length; c += 1)
          D[c].d(1);
        D.length = Q.length;
      }
      if (g[0] & /*browseMonth*/
      128 && $e(
        a,
        /*browseMonth*/
        w[7]
      ), g[0] & /*browseMonth, iLocale*/
      144) {
        U = K(
          /*iLocale*/
          w[4].months
        );
        let c;
        for (c = 0; c < U.length; c += 1) {
          const j = xn(w, U, c);
          C[c] ? C[c].p(j, g) : (C[c] = Un(j), C[c].c(), C[c].m(o, null));
        }
        for (; c < C.length; c += 1)
          C[c].d(1);
        C.length = U.length;
      }
      if (g[0] & /*years*/
      32) {
        b = K(
          /*years*/
          w[5]
        );
        let c;
        for (c = 0; c < b.length; c += 1) {
          const j = Dn(w, b, c);
          R[c] ? R[c].p(j, g) : (R[c] = Gn(j), R[c].c(), R[c].m(m, null));
        }
        for (; c < R.length; c += 1)
          R[c].d(1);
        R.length = b.length;
      }
      if (g[0] & /*browseYear, years*/
      288 && $e(
        m,
        /*browseYear*/
        w[8]
      ), g[0] & /*years, browseDate*/
      40) {
        z = K(
          /*years*/
          w[5]
        );
        let c;
        for (c = 0; c < z.length; c += 1) {
          const j = Cn(w, z, c);
          V[c] ? V[c].p(j, g) : (V[c] = Vn(j), V[c].c(), V[c].m(E, null));
        }
        for (; c < V.length; c += 1)
          V[c].d(1);
        V.length = z.length;
      }
      if (g[0] & /*iLocale*/
      16) {
        ie = K(Array(7));
        let c;
        for (c = 0; c < ie.length; c += 1) {
          const j = kn(w, ie, c);
          W[c] ? W[c].p(j, g) : (W[c] = jn(j), W[c].c(), W[c].m(q, null));
        }
        for (; c < W.length; c += 1)
          W[c].d(1);
        W.length = ie.length;
      }
      if (g[0] & /*calendarDays, min, max, value, todayDate, browseMonth, selectDay*/
      4807) {
        oe = K(Array(6));
        let c;
        for (c = 0; c < oe.length; c += 1) {
          const j = Ln(w, oe, c);
          T[c] ? T[c].p(j, g) : (T[c] = Wn(j), T[c].c(), T[c].m(n, null));
        }
        for (; c < T.length; c += 1)
          T[c].d(1);
        T.length = oe.length;
      }
    },
    i: In,
    o: In,
    d(w) {
      w && he(t), ye(D, w), ye(C, w), ye(R, w), ye(V, w), ye(W, w), ye(T, w), Z = !1, Gs(se);
    }
  };
}
function me(e) {
  return new Date(e.getTime());
}
function vt(e, t, n) {
  return e > n ? me(n) : e < t ? me(t) : me(e);
}
function Yn(e, t) {
  let n = [];
  for (let i = e.getFullYear(); i <= t.getFullYear(); i++)
    n.push(i);
  return n;
}
function Ot(e, t, n) {
  const i = new Date(e.year, e.month, e.number), r = new Date(t.getFullYear(), t.getMonth(), t.getDate()), l = new Date(n.getFullYear(), n.getMonth(), n.getDate());
  return i >= r && i <= l;
}
function qs(e, t, n) {
  let i, r, l, s;
  const a = js();
  let { value: u = null } = t;
  function o(b) {
    b.getTime() !== (u == null ? void 0 : u.getTime()) && (n(3, m = vt(b, d, y)), n(0, u = me(m)));
  }
  function f(b) {
    n(3, m = vt(b, d, y)), !A && u && o(m);
  }
  const _ = /* @__PURE__ */ new Date(), h = /* @__PURE__ */ new Date();
  let { min: d = new Date(h.getFullYear() - 20, 0, 1) } = t, { max: y = new Date(h.getFullYear(), 11, 31, 23, 59, 59, 999) } = t, m = me(u || vt(h, d, y)), v = Yn(d, y), { locale: E = {} } = t, { browseWithoutSelecting: A = !1 } = t;
  function p(b) {
    m.setFullYear(b), f(m);
  }
  function S(b) {
    let R = m.getFullYear();
    b === 12 ? (b = 0, R++) : b === -1 && (b = 11, R--);
    const z = qe(R, b), V = Math.min(m.getDate(), z);
    f(new Date(R, b, V, m.getHours(), m.getMinutes(), m.getSeconds(), m.getMilliseconds()));
  }
  function H(b) {
    Ot(b, d, y) && (m.setFullYear(0), m.setMonth(0), m.setDate(1), m.setFullYear(b.year), m.setMonth(b.month), m.setDate(b.number), o(m), a("select", me(m)));
  }
  function I(b) {
    if (b.shiftKey && b.key === "ArrowUp")
      p(m.getFullYear() - 1);
    else if (b.shiftKey && b.key === "ArrowDown")
      p(m.getFullYear() + 1);
    else if (b.shiftKey && b.key === "ArrowLeft")
      S(m.getMonth() - 1);
    else if (b.shiftKey && b.key === "ArrowRight")
      S(m.getMonth() + 1);
    else
      return !1;
    return b.preventDefault(), !0;
  }
  function Y(b) {
    if (b.shiftKey || b.altKey) {
      I(b);
      return;
    } else if (b.key === "ArrowUp")
      p(m.getFullYear() - 1);
    else if (b.key === "ArrowDown")
      p(m.getFullYear() + 1);
    else if (b.key === "ArrowLeft")
      S(m.getMonth() - 1);
    else if (b.key === "ArrowRight")
      S(m.getMonth() + 1);
    else {
      I(b);
      return;
    }
    b.preventDefault();
  }
  function q(b) {
    if (b.shiftKey || b.altKey) {
      I(b);
      return;
    } else if (b.key === "ArrowUp" || b.key === "ArrowLeft")
      S(m.getMonth() - 1);
    else if (b.key === "ArrowDown" || b.key === "ArrowRight")
      S(m.getMonth() + 1);
    else {
      I(b);
      return;
    }
    b.preventDefault();
  }
  function ne(b) {
    var z;
    let R = b.shiftKey || b.altKey;
    if (((z = b.target) == null ? void 0 : z.tagName) !== "SELECT") {
      if (R) {
        I(b);
        return;
      } else if (b.key === "ArrowUp")
        m.setDate(m.getDate() - 7), o(m);
      else if (b.key === "ArrowDown")
        m.setDate(m.getDate() + 7), o(m);
      else if (b.key === "ArrowLeft")
        m.setDate(m.getDate() - 1), o(m);
      else if (b.key === "ArrowRight")
        m.setDate(m.getDate() + 1), o(m);
      else if (b.key === "Enter")
        o(m), a("select", me(m));
      else
        return;
      b.preventDefault();
    }
  }
  function Z(b) {
    Rs.call(this, e, b);
  }
  const se = () => S(m.getMonth() - 1), Q = (b) => S(parseInt(b.currentTarget.value)), D = (b) => p(parseInt(b.currentTarget.value)), U = () => S(m.getMonth() + 1), C = (b) => H(b);
  return e.$$set = (b) => {
    "value" in b && n(0, u = b.value), "min" in b && n(1, d = b.min), "max" in b && n(2, y = b.max), "locale" in b && n(16, E = b.locale), "browseWithoutSelecting" in b && n(17, A = b.browseWithoutSelecting);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*value, max, min*/
    7 && (u && u > y ? o(y) : u && u < d && o(d)), e.$$.dirty[0] & /*browseDate, value, browseWithoutSelecting*/
    131081 && m.getTime() !== (u == null ? void 0 : u.getTime()) && !A && n(3, m = u ? me(u) : m), e.$$.dirty[0] & /*min, max*/
    6 && n(5, v = Yn(d, y)), e.$$.dirty[0] & /*locale*/
    65536 && n(4, i = Ds(E)), e.$$.dirty[0] & /*browseDate*/
    8 && n(8, r = m.getFullYear()), e.$$.dirty[0] & /*browseDate*/
    8 && n(7, l = m.getMonth()), e.$$.dirty[0] & /*browseDate, iLocale*/
    24 && n(6, s = ks(m, i.weekStartsOn));
  }, [
    u,
    d,
    y,
    m,
    i,
    v,
    s,
    l,
    r,
    _,
    p,
    S,
    H,
    Y,
    q,
    ne,
    E,
    A,
    Z,
    se,
    Q,
    D,
    U,
    C
  ];
}
class zs extends xs {
  constructor(t) {
    super(), Us(
      this,
      t,
      qs,
      Ys,
      Vs,
      {
        value: 0,
        min: 1,
        max: 2,
        locale: 16,
        browseWithoutSelecting: 17
      },
      null,
      [-1, -1]
    );
  }
}
function qn(e, t, n) {
  let i = "", r = !0;
  n = n || new Date(2020, 0, 1, 0, 0, 0, 0);
  let l = n.getFullYear(), s = n.getMonth(), a = n.getDate(), u = n.getHours(), o = n.getMinutes(), f = n.getSeconds();
  const _ = n.getMilliseconds();
  function h(v) {
    for (let E = 0; E < v.length; E++)
      if (e.startsWith(v[E]))
        e = e.slice(1);
      else {
        r = !1, e.length === 0 && (i = v.slice(E));
        return;
      }
  }
  function d(v, E, A) {
    const p = e.match(v);
    if (p != null && p[0]) {
      e = e.slice(p[0].length);
      const S = parseInt(p[0]);
      return S > A || S < E ? (r = !1, null) : S;
    } else
      return r = !1, null;
  }
  function y(v) {
    if (typeof v == "string")
      h(v);
    else if (v.id === "yy") {
      const E = d(/^[0-9]{2}/, 0, 99);
      E !== null && (l = 2e3 + E);
    } else if (v.id === "yyyy") {
      const E = d(/^[0-9]{4}/, 0, 9999);
      E !== null && (l = E);
    } else if (v.id === "MM") {
      const E = d(/^[0-9]{2}/, 1, 12);
      E !== null && (s = E - 1);
    } else if (v.id === "dd") {
      const E = d(/^[0-9]{2}/, 1, 31);
      E !== null && (a = E);
    } else if (v.id === "HH") {
      const E = d(/^[0-9]{2}/, 0, 23);
      E !== null && (u = E);
    } else if (v.id === "mm") {
      const E = d(/^[0-9]{2}/, 0, 59);
      E !== null && (o = E);
    } else if (v.id === "ss") {
      const E = d(/^[0-9]{2}/, 0, 59);
      E !== null && (f = E);
    }
  }
  for (const v of t)
    if (y(v), !r)
      break;
  const m = qe(l, s);
  return a > m && (r = !1), {
    date: r ? new Date(l, s, a, u, o, f, _) : null,
    missingPunctuation: i
  };
}
function je(e) {
  return ("0" + e.toString()).slice(-2);
}
const Zs = [
  {
    id: "yyyy",
    toString: (e) => e.getFullYear().toString()
  },
  {
    id: "yy",
    toString: (e) => e.getFullYear().toString().slice(-2)
  },
  {
    id: "MM",
    toString: (e) => je(e.getMonth() + 1)
  },
  {
    id: "dd",
    toString: (e) => je(e.getDate())
  },
  {
    id: "HH",
    toString: (e) => je(e.getHours())
  },
  {
    id: "mm",
    toString: (e) => je(e.getMinutes())
  },
  {
    id: "ss",
    toString: (e) => je(e.getSeconds())
  }
];
function Qs(e) {
  for (const t of Zs)
    if (e.startsWith(t.id))
      return t;
}
function zn(e) {
  const t = [];
  for (; e.length > 0; ) {
    const n = Qs(e);
    n ? (t.push(n), e = e.slice(n.id.length)) : typeof t[t.length - 1] == "string" ? (t[t.length - 1] += e[0], e = e.slice(1)) : (t.push(e[0]), e = e.slice(1));
  }
  return t;
}
const {
  SvelteComponent: Js,
  add_flush_callback: Ks,
  add_render_callback: $s,
  append: Zn,
  attr: we,
  bind: eo,
  binding_callbacks: kt,
  check_outros: to,
  component_subscribe: Qn,
  create_bidirectional_transition: Jn,
  create_component: no,
  destroy_component: io,
  detach: Oi,
  element: Ct,
  group_outros: ro,
  init: lo,
  insert: ki,
  listen: Xe,
  mount_component: so,
  run_all: oo,
  safe_not_equal: ao,
  set_style: Kn,
  space: uo,
  toggle_class: Me,
  transition_in: it,
  transition_out: Dt
} = window.__gradio__svelte__internal, { createEventDispatcher: fo } = window.__gradio__svelte__internal;
function $n(e) {
  let t, n, i, r, l = `${/*pickerLeftPosition*/
  e[15]}px`, s;
  function a(o) {
    e[30](o);
  }
  let u = {
    min: (
      /*min*/
      e[3]
    ),
    max: (
      /*max*/
      e[4]
    ),
    locale: (
      /*locale*/
      e[8]
    ),
    browseWithoutSelecting: (
      /*browseWithoutSelecting*/
      e[9]
    )
  };
  return (
    /*$store*/
    e[11] !== void 0 && (u.value = /*$store*/
    e[11]), n = new zs({ props: u }), kt.push(() => eo(n, "value", a)), n.$on(
      "focusout",
      /*onFocusOut*/
      e[18]
    ), n.$on(
      "select",
      /*onSelect*/
      e[20]
    ), {
      c() {
        t = Ct("div"), no(n.$$.fragment), we(t, "class", "picker svelte-1vabmef"), Me(
          t,
          "visible",
          /*visible*/
          e[2]
        ), Me(
          t,
          "above",
          /*showAbove*/
          e[14]
        ), Kn(t, "--picker-left-position", l);
      },
      m(o, f) {
        ki(o, t, f), so(n, t, null), e[31](t), s = !0;
      },
      p(o, f) {
        const _ = {};
        f[0] & /*min*/
        8 && (_.min = /*min*/
        o[3]), f[0] & /*max*/
        16 && (_.max = /*max*/
        o[4]), f[0] & /*locale*/
        256 && (_.locale = /*locale*/
        o[8]), f[0] & /*browseWithoutSelecting*/
        512 && (_.browseWithoutSelecting = /*browseWithoutSelecting*/
        o[9]), !i && f[0] & /*$store*/
        2048 && (i = !0, _.value = /*$store*/
        o[11], Ks(() => i = !1)), n.$set(_), (!s || f[0] & /*visible*/
        4) && Me(
          t,
          "visible",
          /*visible*/
          o[2]
        ), (!s || f[0] & /*showAbove*/
        16384) && Me(
          t,
          "above",
          /*showAbove*/
          o[14]
        ), f[0] & /*pickerLeftPosition*/
        32768 && l !== (l = `${/*pickerLeftPosition*/
        o[15]}px`) && Kn(t, "--picker-left-position", l);
      },
      i(o) {
        s || (it(n.$$.fragment, o), o && $s(() => {
          s && (r || (r = Jn(
            t,
            /*flyAutoPosition*/
            e[21],
            {},
            !0
          )), r.run(1));
        }), s = !0);
      },
      o(o) {
        Dt(n.$$.fragment, o), o && (r || (r = Jn(
          t,
          /*flyAutoPosition*/
          e[21],
          {},
          !1
        )), r.run(0)), s = !1;
      },
      d(o) {
        o && Oi(t), io(n), e[31](null), o && r && r.end();
      }
    }
  );
}
function ho(e) {
  let t, n, i, r, l, s, a, u = (
    /*visible*/
    e[2] && !/*disabled*/
    e[6] && $n(e)
  );
  return {
    c() {
      t = Ct("div"), n = Ct("input"), i = uo(), u && u.c(), we(n, "type", "text"), n.value = /*text*/
      e[0], we(
        n,
        "placeholder",
        /*placeholder*/
        e[5]
      ), n.disabled = /*disabled*/
      e[6], we(n, "class", "svelte-1vabmef"), Me(n, "invalid", !/*valid*/
      e[1]), we(t, "class", r = "date-time-field " + /*classes*/
      e[7] + " svelte-1vabmef");
    },
    m(o, f) {
      ki(o, t, f), Zn(t, n), e[26](n), Zn(t, i), u && u.m(t, null), l = !0, s || (a = [
        Xe(
          n,
          "focus",
          /*focus_handler*/
          e[27]
        ),
        Xe(
          n,
          "mousedown",
          /*mousedown_handler*/
          e[28]
        ),
        Xe(
          n,
          "input",
          /*input_handler*/
          e[29]
        ),
        Xe(
          t,
          "focusout",
          /*onFocusOut*/
          e[18]
        ),
        Xe(
          t,
          "keydown",
          /*keydown*/
          e[19]
        )
      ], s = !0);
    },
    p(o, f) {
      (!l || f[0] & /*text*/
      1 && n.value !== /*text*/
      o[0]) && (n.value = /*text*/
      o[0]), (!l || f[0] & /*placeholder*/
      32) && we(
        n,
        "placeholder",
        /*placeholder*/
        o[5]
      ), (!l || f[0] & /*disabled*/
      64) && (n.disabled = /*disabled*/
      o[6]), (!l || f[0] & /*valid*/
      2) && Me(n, "invalid", !/*valid*/
      o[1]), /*visible*/
      o[2] && !/*disabled*/
      o[6] ? u ? (u.p(o, f), f[0] & /*visible, disabled*/
      68 && it(u, 1)) : (u = $n(o), u.c(), it(u, 1), u.m(t, null)) : u && (ro(), Dt(u, 1, 1, () => {
        u = null;
      }), to()), (!l || f[0] & /*classes*/
      128 && r !== (r = "date-time-field " + /*classes*/
      o[7] + " svelte-1vabmef")) && we(t, "class", r);
    },
    i(o) {
      l || (it(u), l = !0);
    },
    o(o) {
      Dt(u), l = !1;
    },
    d(o) {
      o && Oi(t), e[26](null), u && u.d(), s = !1, oo(a);
    }
  };
}
function co(e, t, n) {
  let i, r;
  const l = fo(), s = /* @__PURE__ */ new Date(), a = Re(null);
  Qn(e, a, (g) => n(32, r = g));
  const u = (() => ({
    subscribe: a.subscribe,
    set: (g) => {
      g == null ? (a.set(null), n(22, o = g)) : g.getTime() !== (r == null ? void 0 : r.getTime()) && (a.set(g), n(22, o = g));
    }
  }))();
  Qn(e, u, (g) => n(11, i = g));
  let { value: o = null } = t, { min: f = new Date(s.getFullYear() - 20, 0, 1) } = t, { max: _ = new Date(s.getFullYear(), 11, 31, 23, 59, 59, 999) } = t, { placeholder: h = "2020-12-31 23:00:00" } = t, { valid: d = !0 } = t, { disabled: y = !1 } = t, { class: m = "" } = t, { format: v = "yyyy-MM-dd HH:mm:ss" } = t, E = zn(v), { locale: A = {} } = t;
  function p(g, c) {
    n(0, S = Nn(g, c));
  }
  let { text: S = Nn(i, E) } = t;
  function H(g, c) {
    if (g.length) {
      const j = qn(g, c, i);
      j.date !== null ? (n(1, d = !0), u.set(j.date)) : n(1, d = !1);
    } else
      n(1, d = !0), o && (n(22, o = null), u.set(null));
  }
  let { visible: I = !1 } = t, { closeOnSelection: Y = !1 } = t, { browseWithoutSelecting: q = !1 } = t;
  function ne(g) {
    (g == null ? void 0 : g.currentTarget) instanceof HTMLElement && g.relatedTarget && g.relatedTarget instanceof Node && g.currentTarget.contains(g.relatedTarget) || n(2, I = !1);
  }
  function Z(g) {
    g.key === "Escape" && I ? (n(2, I = !1), g.preventDefault(), g.stopPropagation()) : g.key === "Enter" && (n(2, I = !I), g.preventDefault());
  }
  function se(g) {
    l("select", g.detail), Y && n(2, I = !1);
  }
  let { dynamicPositioning: Q = !1 } = t, D, U, C = !1, b = null;
  function R() {
    if (n(14, C = !1), n(15, b = null), I && U && Q) {
      const g = D.getBoundingClientRect(), c = U.offsetWidth - g.width, j = g.bottom + U.offsetHeight + 5, Ci = g.left + U.offsetWidth + 5;
      if (j > window.innerHeight && n(14, C = !0), Ci > window.innerWidth && (n(15, b = -c), g.left < c + 5)) {
        const Di = window.innerWidth / 2 - U.offsetWidth / 2;
        n(15, b = Di - g.left);
      }
    }
  }
  function z(g) {
    return R(), ar(g, {
      duration: 200,
      easing: sr,
      y: C ? 5 : -5
    });
  }
  function V(g) {
    kt[g ? "unshift" : "push"](() => {
      D = g, n(12, D);
    });
  }
  const ie = () => n(2, I = !0), W = () => n(2, I = !0), oe = (g) => {
    if (g instanceof InputEvent && g.inputType === "insertText" && typeof g.data == "string" && g.currentTarget.value === S + g.data) {
      let c = qn(S, E, i);
      if (c.missingPunctuation !== "" && !c.missingPunctuation.startsWith(g.data)) {
        n(0, S = S + c.missingPunctuation + g.data);
        return;
      }
    }
    n(0, S = g.currentTarget.value);
  };
  function T(g) {
    i = g, u.set(i);
  }
  function w(g) {
    kt[g ? "unshift" : "push"](() => {
      U = g, n(13, U);
    });
  }
  return e.$$set = (g) => {
    "value" in g && n(22, o = g.value), "min" in g && n(3, f = g.min), "max" in g && n(4, _ = g.max), "placeholder" in g && n(5, h = g.placeholder), "valid" in g && n(1, d = g.valid), "disabled" in g && n(6, y = g.disabled), "class" in g && n(7, m = g.class), "format" in g && n(23, v = g.format), "locale" in g && n(8, A = g.locale), "text" in g && n(0, S = g.text), "visible" in g && n(2, I = g.visible), "closeOnSelection" in g && n(24, Y = g.closeOnSelection), "browseWithoutSelecting" in g && n(9, q = g.browseWithoutSelecting), "dynamicPositioning" in g && n(25, Q = g.dynamicPositioning);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*value*/
    4194304 && u.set(o), e.$$.dirty[0] & /*format*/
    8388608 && n(10, E = zn(v)), e.$$.dirty[0] & /*$store, formatTokens*/
    3072 && p(i, E), e.$$.dirty[0] & /*text, formatTokens*/
    1025 && H(S, E);
  }, [
    S,
    d,
    I,
    f,
    _,
    h,
    y,
    m,
    A,
    q,
    E,
    i,
    D,
    U,
    C,
    b,
    a,
    u,
    ne,
    Z,
    se,
    z,
    o,
    v,
    Y,
    Q,
    V,
    ie,
    W,
    oe,
    T,
    w
  ];
}
class _o extends Js {
  constructor(t) {
    super(), lo(
      this,
      t,
      co,
      ho,
      ao,
      {
        value: 22,
        min: 3,
        max: 4,
        placeholder: 5,
        valid: 1,
        disabled: 6,
        class: 7,
        format: 23,
        locale: 8,
        text: 0,
        visible: 2,
        closeOnSelection: 24,
        browseWithoutSelecting: 9,
        dynamicPositioning: 25
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: mo,
  add_flush_callback: go,
  assign: bo,
  bind: po,
  binding_callbacks: vo,
  create_component: xt,
  destroy_component: Rt,
  detach: yt,
  element: yo,
  get_spread_object: wo,
  get_spread_update: Eo,
  init: To,
  insert: wt,
  mount_component: Ft,
  safe_not_equal: So,
  space: ei,
  transition_in: Ut,
  transition_out: Gt
} = window.__gradio__svelte__internal;
function Ho(e) {
  let t, n, i, r, l, s, a;
  const u = [
    { autoscroll: (
      /*gradio*/
      e[8].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      e[8].i18n
    ) },
    /*loading_status*/
    e[7]
  ];
  let o = {};
  for (let h = 0; h < u.length; h += 1)
    o = bo(o, u[h]);
  t = new Ls({ props: o });
  function f(h) {
    e[11](h);
  }
  let _ = {};
  return (
    /*date_value*/
    e[0] !== void 0 && (_.value = /*date_value*/
    e[0]), l = new _o({ props: _ }), vo.push(() => po(l, "value", f)), {
      c() {
        xt(t.$$.fragment), n = ei(), i = yo("div"), i.textContent = '"Hello"', r = ei(), xt(l.$$.fragment);
      },
      m(h, d) {
        Ft(t, h, d), wt(h, n, d), wt(h, i, d), wt(h, r, d), Ft(l, h, d), a = !0;
      },
      p(h, d) {
        const y = d & /*gradio, loading_status*/
        384 ? Eo(u, [
          d & /*gradio*/
          256 && { autoscroll: (
            /*gradio*/
            h[8].autoscroll
          ) },
          d & /*gradio*/
          256 && { i18n: (
            /*gradio*/
            h[8].i18n
          ) },
          d & /*loading_status*/
          128 && wo(
            /*loading_status*/
            h[7]
          )
        ]) : {};
        t.$set(y);
        const m = {};
        !s && d & /*date_value*/
        1 && (s = !0, m.value = /*date_value*/
        h[0], go(() => s = !1)), l.$set(m);
      },
      i(h) {
        a || (Ut(t.$$.fragment, h), Ut(l.$$.fragment, h), a = !0);
      },
      o(h) {
        Gt(t.$$.fragment, h), Gt(l.$$.fragment, h), a = !1;
      },
      d(h) {
        h && (yt(n), yt(i), yt(r)), Rt(t, h), Rt(l, h);
      }
    }
  );
}
function Ao(e) {
  let t, n;
  return t = new Ki({
    props: {
      visible: (
        /*visible*/
        e[3]
      ),
      elem_id: (
        /*elem_id*/
        e[1]
      ),
      elem_classes: (
        /*elem_classes*/
        e[2]
      ),
      container: (
        /*container*/
        e[4]
      ),
      scale: (
        /*scale*/
        e[5]
      ),
      min_width: (
        /*min_width*/
        e[6]
      ),
      $$slots: { default: [Ho] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      xt(t.$$.fragment);
    },
    m(i, r) {
      Ft(t, i, r), n = !0;
    },
    p(i, [r]) {
      const l = {};
      r & /*visible*/
      8 && (l.visible = /*visible*/
      i[3]), r & /*elem_id*/
      2 && (l.elem_id = /*elem_id*/
      i[1]), r & /*elem_classes*/
      4 && (l.elem_classes = /*elem_classes*/
      i[2]), r & /*container*/
      16 && (l.container = /*container*/
      i[4]), r & /*scale*/
      32 && (l.scale = /*scale*/
      i[5]), r & /*min_width*/
      64 && (l.min_width = /*min_width*/
      i[6]), r & /*$$scope, date_value, gradio, loading_status*/
      8577 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (Ut(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Gt(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Rt(t, i);
    }
  };
}
function Bo(e, t, n) {
  let { elem_id: i = "" } = t, { elem_classes: r = [] } = t, { visible: l = !0 } = t, { value: s = null } = t, { date_value: a = /* @__PURE__ */ new Date() } = t, { value_is_output: u = !1 } = t, { container: o = !0 } = t, { scale: f = null } = t, { min_width: _ = void 0 } = t, { loading_status: h } = t, { gradio: d } = t;
  async function y() {
    n(9, s = a.toISOString().split("T")[0]), d.dispatch("change"), u || d.dispatch("input");
  }
  function m(v) {
    a = v, n(0, a), n(9, s);
  }
  return e.$$set = (v) => {
    "elem_id" in v && n(1, i = v.elem_id), "elem_classes" in v && n(2, r = v.elem_classes), "visible" in v && n(3, l = v.visible), "value" in v && n(9, s = v.value), "date_value" in v && n(0, a = v.date_value), "value_is_output" in v && n(10, u = v.value_is_output), "container" in v && n(4, o = v.container), "scale" in v && n(5, f = v.scale), "min_width" in v && n(6, _ = v.min_width), "loading_status" in v && n(7, h = v.loading_status), "gradio" in v && n(8, d = v.gradio);
  }, e.$$.update = () => {
    e.$$.dirty & /*value*/
    512 && s && n(0, a = new Date(s)), e.$$.dirty & /*date_value*/
    1 && y();
  }, [
    a,
    i,
    r,
    l,
    o,
    f,
    _,
    h,
    d,
    s,
    u,
    m
  ];
}
class Mo extends mo {
  constructor(t) {
    super(), To(this, t, Bo, Ao, So, {
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      value: 9,
      date_value: 0,
      value_is_output: 10,
      container: 4,
      scale: 5,
      min_width: 6,
      loading_status: 7,
      gradio: 8
    });
  }
}
export {
  Mo as default
};
