const {
  SvelteComponent: Zn,
  assign: Wn,
  create_slot: Qn,
  detach: Jn,
  element: Yn,
  get_all_dirty_from_scope: Kn,
  get_slot_changes: $n,
  get_spread_update: er,
  init: tr,
  insert: nr,
  safe_not_equal: rr,
  set_dynamic_element_data: yt,
  set_style: L,
  toggle_class: z,
  transition_in: fn,
  transition_out: hn,
  update_slot_base: ir
} = window.__gradio__svelte__internal;
function sr(e) {
  let t, n, r;
  const i = (
    /*#slots*/
    e[17].default
  ), s = Qn(
    i,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let o = [
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
  for (let u = 0; u < o.length; u += 1)
    a = Wn(a, o[u]);
  return {
    c() {
      t = Yn(
        /*tag*/
        e[14]
      ), s && s.c(), yt(
        /*tag*/
        e[14]
      )(t, a), z(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), z(
        t,
        "padded",
        /*padding*/
        e[6]
      ), z(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), z(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), L(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), L(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), L(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), L(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), L(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), L(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), L(t, "border-width", "var(--block-border-width)");
    },
    m(u, l) {
      nr(u, t, l), s && s.m(t, null), r = !0;
    },
    p(u, l) {
      s && s.p && (!r || l & /*$$scope*/
      65536) && ir(
        s,
        i,
        u,
        /*$$scope*/
        u[16],
        r ? $n(
          i,
          /*$$scope*/
          u[16],
          l,
          null
        ) : Kn(
          /*$$scope*/
          u[16]
        ),
        null
      ), yt(
        /*tag*/
        u[14]
      )(t, a = er(o, [
        (!r || l & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          u[7]
        ) },
        (!r || l & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          u[2]
        ) },
        (!r || l & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        u[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), z(
        t,
        "hidden",
        /*visible*/
        u[10] === !1
      ), z(
        t,
        "padded",
        /*padding*/
        u[6]
      ), z(
        t,
        "border_focus",
        /*border_mode*/
        u[5] === "focus"
      ), z(t, "hide-container", !/*explicit_call*/
      u[8] && !/*container*/
      u[9]), l & /*height*/
      1 && L(t, "height", typeof /*height*/
      u[0] == "number" ? (
        /*height*/
        u[0] + "px"
      ) : void 0), l & /*width*/
      2 && L(t, "width", typeof /*width*/
      u[1] == "number" ? `calc(min(${/*width*/
      u[1]}px, 100%))` : void 0), l & /*variant*/
      16 && L(
        t,
        "border-style",
        /*variant*/
        u[4]
      ), l & /*allow_overflow*/
      2048 && L(
        t,
        "overflow",
        /*allow_overflow*/
        u[11] ? "visible" : "hidden"
      ), l & /*scale*/
      4096 && L(
        t,
        "flex-grow",
        /*scale*/
        u[12]
      ), l & /*min_width*/
      8192 && L(t, "min-width", `calc(min(${/*min_width*/
      u[13]}px, 100%))`);
    },
    i(u) {
      r || (fn(s, u), r = !0);
    },
    o(u) {
      hn(s, u), r = !1;
    },
    d(u) {
      u && Jn(t), s && s.d(u);
    }
  };
}
function or(e) {
  let t, n = (
    /*tag*/
    e[14] && sr(e)
  );
  return {
    c() {
      n && n.c();
    },
    m(r, i) {
      n && n.m(r, i), t = !0;
    },
    p(r, [i]) {
      /*tag*/
      r[14] && n.p(r, i);
    },
    i(r) {
      t || (fn(n, r), t = !0);
    },
    o(r) {
      hn(n, r), t = !1;
    },
    d(r) {
      n && n.d(r);
    }
  };
}
function ar(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { height: s = void 0 } = t, { width: o = void 0 } = t, { elem_id: a = "" } = t, { elem_classes: u = [] } = t, { variant: l = "solid" } = t, { border_mode: f = "base" } = t, { padding: h = !0 } = t, { type: c = "normal" } = t, { test_id: _ = void 0 } = t, { explicit_call: m = !1 } = t, { container: b = !0 } = t, { visible: v = !0 } = t, { allow_overflow: P = !0 } = t, { scale: x = null } = t, { min_width: d = 0 } = t, E = c === "fieldset" ? "fieldset" : "div";
  return e.$$set = (p) => {
    "height" in p && n(0, s = p.height), "width" in p && n(1, o = p.width), "elem_id" in p && n(2, a = p.elem_id), "elem_classes" in p && n(3, u = p.elem_classes), "variant" in p && n(4, l = p.variant), "border_mode" in p && n(5, f = p.border_mode), "padding" in p && n(6, h = p.padding), "type" in p && n(15, c = p.type), "test_id" in p && n(7, _ = p.test_id), "explicit_call" in p && n(8, m = p.explicit_call), "container" in p && n(9, b = p.container), "visible" in p && n(10, v = p.visible), "allow_overflow" in p && n(11, P = p.allow_overflow), "scale" in p && n(12, x = p.scale), "min_width" in p && n(13, d = p.min_width), "$$scope" in p && n(16, i = p.$$scope);
  }, [
    s,
    o,
    a,
    u,
    l,
    f,
    h,
    _,
    m,
    b,
    v,
    P,
    x,
    d,
    E,
    c,
    i,
    r
  ];
}
class lr extends Zn {
  constructor(t) {
    super(), tr(this, t, ar, or, rr, {
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
const {
  SvelteComponent: ur,
  attr: fr,
  create_slot: hr,
  detach: cr,
  element: _r,
  get_all_dirty_from_scope: mr,
  get_slot_changes: dr,
  init: br,
  insert: pr,
  safe_not_equal: gr,
  transition_in: vr,
  transition_out: Er,
  update_slot_base: yr
} = window.__gradio__svelte__internal;
function wr(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[1].default
  ), i = hr(
    r,
    e,
    /*$$scope*/
    e[0],
    null
  );
  return {
    c() {
      t = _r("div"), i && i.c(), fr(t, "class", "svelte-1hnfib2");
    },
    m(s, o) {
      pr(s, t, o), i && i.m(t, null), n = !0;
    },
    p(s, [o]) {
      i && i.p && (!n || o & /*$$scope*/
      1) && yr(
        i,
        r,
        s,
        /*$$scope*/
        s[0],
        n ? dr(
          r,
          /*$$scope*/
          s[0],
          o,
          null
        ) : mr(
          /*$$scope*/
          s[0]
        ),
        null
      );
    },
    i(s) {
      n || (vr(i, s), n = !0);
    },
    o(s) {
      Er(i, s), n = !1;
    },
    d(s) {
      s && cr(t), i && i.d(s);
    }
  };
}
function Tr(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t;
  return e.$$set = (s) => {
    "$$scope" in s && n(0, i = s.$$scope);
  }, [i, r];
}
class xr extends ur {
  constructor(t) {
    super(), br(this, t, Tr, wr, gr, {});
  }
}
const {
  SvelteComponent: Br,
  attr: wt,
  check_outros: Hr,
  create_component: Ar,
  create_slot: Sr,
  destroy_component: Pr,
  detach: Pe,
  element: Nr,
  empty: Ir,
  get_all_dirty_from_scope: Cr,
  get_slot_changes: Lr,
  group_outros: Or,
  init: Mr,
  insert: Ne,
  mount_component: Rr,
  safe_not_equal: Dr,
  set_data: kr,
  space: Fr,
  text: Ur,
  toggle_class: ee,
  transition_in: be,
  transition_out: Ie,
  update_slot_base: Gr
} = window.__gradio__svelte__internal;
function Tt(e) {
  let t, n;
  return t = new xr({
    props: {
      $$slots: { default: [Vr] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Ar(t.$$.fragment);
    },
    m(r, i) {
      Rr(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i & /*$$scope, info*/
      10 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (be(t.$$.fragment, r), n = !0);
    },
    o(r) {
      Ie(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Pr(t, r);
    }
  };
}
function Vr(e) {
  let t;
  return {
    c() {
      t = Ur(
        /*info*/
        e[1]
      );
    },
    m(n, r) {
      Ne(n, t, r);
    },
    p(n, r) {
      r & /*info*/
      2 && kr(
        t,
        /*info*/
        n[1]
      );
    },
    d(n) {
      n && Pe(t);
    }
  };
}
function jr(e) {
  let t, n, r, i;
  const s = (
    /*#slots*/
    e[2].default
  ), o = Sr(
    s,
    e,
    /*$$scope*/
    e[3],
    null
  );
  let a = (
    /*info*/
    e[1] && Tt(e)
  );
  return {
    c() {
      t = Nr("span"), o && o.c(), n = Fr(), a && a.c(), r = Ir(), wt(t, "data-testid", "block-info"), wt(t, "class", "svelte-22c38v"), ee(t, "sr-only", !/*show_label*/
      e[0]), ee(t, "hide", !/*show_label*/
      e[0]), ee(
        t,
        "has-info",
        /*info*/
        e[1] != null
      );
    },
    m(u, l) {
      Ne(u, t, l), o && o.m(t, null), Ne(u, n, l), a && a.m(u, l), Ne(u, r, l), i = !0;
    },
    p(u, [l]) {
      o && o.p && (!i || l & /*$$scope*/
      8) && Gr(
        o,
        s,
        u,
        /*$$scope*/
        u[3],
        i ? Lr(
          s,
          /*$$scope*/
          u[3],
          l,
          null
        ) : Cr(
          /*$$scope*/
          u[3]
        ),
        null
      ), (!i || l & /*show_label*/
      1) && ee(t, "sr-only", !/*show_label*/
      u[0]), (!i || l & /*show_label*/
      1) && ee(t, "hide", !/*show_label*/
      u[0]), (!i || l & /*info*/
      2) && ee(
        t,
        "has-info",
        /*info*/
        u[1] != null
      ), /*info*/
      u[1] ? a ? (a.p(u, l), l & /*info*/
      2 && be(a, 1)) : (a = Tt(u), a.c(), be(a, 1), a.m(r.parentNode, r)) : a && (Or(), Ie(a, 1, 1, () => {
        a = null;
      }), Hr());
    },
    i(u) {
      i || (be(o, u), be(a), i = !0);
    },
    o(u) {
      Ie(o, u), Ie(a), i = !1;
    },
    d(u) {
      u && (Pe(t), Pe(n), Pe(r)), o && o.d(u), a && a.d(u);
    }
  };
}
function Xr(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { show_label: s = !0 } = t, { info: o = void 0 } = t;
  return e.$$set = (a) => {
    "show_label" in a && n(0, s = a.show_label), "info" in a && n(1, o = a.info), "$$scope" in a && n(3, i = a.$$scope);
  }, [s, o, r, i];
}
class zr extends Br {
  constructor(t) {
    super(), Mr(this, t, Xr, jr, Dr, { show_label: 0, info: 1 });
  }
}
const qr = [
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
], xt = {
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
qr.reduce(
  (e, { color: t, primary: n, secondary: r }) => ({
    ...e,
    [t]: {
      primary: xt[t][n],
      secondary: xt[t][r]
    }
  }),
  {}
);
function K() {
}
function Zr(e) {
  return e();
}
function Wr(e) {
  e.forEach(Zr);
}
function Qr(e) {
  return typeof e == "function";
}
function Jr(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function cn(e, ...t) {
  if (e == null) {
    for (const r of t)
      r(void 0);
    return K;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function Yr(e) {
  let t;
  return cn(e, (n) => t = n)(), t;
}
const _n = typeof window < "u";
let Bt = _n ? () => window.performance.now() : () => Date.now(), mn = _n ? (e) => requestAnimationFrame(e) : K;
const ie = /* @__PURE__ */ new Set();
function dn(e) {
  ie.forEach((t) => {
    t.c(e) || (ie.delete(t), t.f());
  }), ie.size !== 0 && mn(dn);
}
function Kr(e) {
  let t;
  return ie.size === 0 && mn(dn), {
    promise: new Promise((n) => {
      ie.add(t = { c: e, f: n });
    }),
    abort() {
      ie.delete(t);
    }
  };
}
const te = [];
function $r(e, t) {
  return {
    subscribe: we(e, t).subscribe
  };
}
function we(e, t = K) {
  let n;
  const r = /* @__PURE__ */ new Set();
  function i(a) {
    if (Jr(e, a) && (e = a, n)) {
      const u = !te.length;
      for (const l of r)
        l[1](), te.push(l, e);
      if (u) {
        for (let l = 0; l < te.length; l += 2)
          te[l][0](te[l + 1]);
        te.length = 0;
      }
    }
  }
  function s(a) {
    i(a(e));
  }
  function o(a, u = K) {
    const l = [a, u];
    return r.add(l), r.size === 1 && (n = t(i, s) || K), a(e), () => {
      r.delete(l), r.size === 0 && n && (n(), n = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function he(e, t, n) {
  const r = !Array.isArray(e), i = r ? [e] : e;
  if (!i.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const s = t.length < 2;
  return $r(n, (o, a) => {
    let u = !1;
    const l = [];
    let f = 0, h = K;
    const c = () => {
      if (f)
        return;
      h();
      const m = t(r ? l[0] : l, o, a);
      s ? o(m) : h = Qr(m) ? m : K;
    }, _ = i.map(
      (m, b) => cn(
        m,
        (v) => {
          l[b] = v, f &= ~(1 << b), u && c();
        },
        () => {
          f |= 1 << b;
        }
      )
    );
    return u = !0, c(), function() {
      Wr(_), h(), u = !1;
    };
  });
}
function Ht(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Ke(e, t, n, r) {
  if (typeof n == "number" || Ht(n)) {
    const i = r - n, s = (n - t) / (e.dt || 1 / 60), o = e.opts.stiffness * i, a = e.opts.damping * s, u = (o - a) * e.inv_mass, l = (s + u) * e.dt;
    return Math.abs(l) < e.opts.precision && Math.abs(i) < e.opts.precision ? r : (e.settled = !1, Ht(n) ? new Date(n.getTime() + l) : n + l);
  } else {
    if (Array.isArray(n))
      return n.map(
        (i, s) => Ke(e, t[s], n[s], r[s])
      );
    if (typeof n == "object") {
      const i = {};
      for (const s in n)
        i[s] = Ke(e, t[s], n[s], r[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function At(e, t = {}) {
  const n = we(e), { stiffness: r = 0.15, damping: i = 0.8, precision: s = 0.01 } = t;
  let o, a, u, l = e, f = e, h = 1, c = 0, _ = !1;
  function m(v, P = {}) {
    f = v;
    const x = u = {};
    return e == null || P.hard || b.stiffness >= 1 && b.damping >= 1 ? (_ = !0, o = Bt(), l = v, n.set(e = f), Promise.resolve()) : (P.soft && (c = 1 / ((P.soft === !0 ? 0.5 : +P.soft) * 60), h = 0), a || (o = Bt(), _ = !1, a = Kr((d) => {
      if (_)
        return _ = !1, a = null, !1;
      h = Math.min(h + c, 1);
      const E = {
        inv_mass: h,
        opts: b,
        settled: !0,
        dt: (d - o) * 60 / 1e3
      }, p = Ke(E, l, e, f);
      return o = d, l = e, n.set(e = p), E.settled && (a = null), !E.settled;
    })), new Promise((d) => {
      a.promise.then(() => {
        x === u && d();
      });
    }));
  }
  const b = {
    set: m,
    update: (v, P) => m(v(f, e), P),
    subscribe: n.subscribe,
    stiffness: r,
    damping: i,
    precision: s
  };
  return b;
}
function ei(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var ti = function(t) {
  return ni(t) && !ri(t);
};
function ni(e) {
  return !!e && typeof e == "object";
}
function ri(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || oi(e);
}
var ii = typeof Symbol == "function" && Symbol.for, si = ii ? Symbol.for("react.element") : 60103;
function oi(e) {
  return e.$$typeof === si;
}
function ai(e) {
  return Array.isArray(e) ? [] : {};
}
function ge(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? se(ai(e), e, t) : e;
}
function li(e, t, n) {
  return e.concat(t).map(function(r) {
    return ge(r, n);
  });
}
function ui(e, t) {
  if (!t.customMerge)
    return se;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : se;
}
function fi(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function St(e) {
  return Object.keys(e).concat(fi(e));
}
function bn(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function hi(e, t) {
  return bn(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function ci(e, t, n) {
  var r = {};
  return n.isMergeableObject(e) && St(e).forEach(function(i) {
    r[i] = ge(e[i], n);
  }), St(t).forEach(function(i) {
    hi(e, i) || (bn(e, i) && n.isMergeableObject(t[i]) ? r[i] = ui(i, n)(e[i], t[i], n) : r[i] = ge(t[i], n));
  }), r;
}
function se(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || li, n.isMergeableObject = n.isMergeableObject || ti, n.cloneUnlessOtherwiseSpecified = ge;
  var r = Array.isArray(t), i = Array.isArray(e), s = r === i;
  return s ? r ? n.arrayMerge(e, t, n) : ci(e, t, n) : ge(t, n);
}
se.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(r, i) {
    return se(r, i, n);
  }, {});
};
var _i = se, mi = _i;
const di = /* @__PURE__ */ ei(mi);
var $e = function(e, t) {
  return $e = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, r) {
    n.__proto__ = r;
  } || function(n, r) {
    for (var i in r)
      Object.prototype.hasOwnProperty.call(r, i) && (n[i] = r[i]);
  }, $e(e, t);
};
function De(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  $e(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var S = function() {
  return S = Object.assign || function(t) {
    for (var n, r = 1, i = arguments.length; r < i; r++) {
      n = arguments[r];
      for (var s in n)
        Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s]);
    }
    return t;
  }, S.apply(this, arguments);
};
function Ve(e, t, n) {
  if (n || arguments.length === 2)
    for (var r = 0, i = t.length, s; r < i; r++)
      (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)), s[r] = t[r]);
  return e.concat(s || Array.prototype.slice.call(t));
}
var B;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(B || (B = {}));
var N;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(N || (N = {}));
var oe;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(oe || (oe = {}));
function Pt(e) {
  return e.type === N.literal;
}
function bi(e) {
  return e.type === N.argument;
}
function pn(e) {
  return e.type === N.number;
}
function gn(e) {
  return e.type === N.date;
}
function vn(e) {
  return e.type === N.time;
}
function En(e) {
  return e.type === N.select;
}
function yn(e) {
  return e.type === N.plural;
}
function pi(e) {
  return e.type === N.pound;
}
function wn(e) {
  return e.type === N.tag;
}
function Tn(e) {
  return !!(e && typeof e == "object" && e.type === oe.number);
}
function et(e) {
  return !!(e && typeof e == "object" && e.type === oe.dateTime);
}
var xn = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, gi = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function vi(e) {
  var t = {};
  return e.replace(gi, function(n) {
    var r = n.length;
    switch (n[0]) {
      case "G":
        t.era = r === 4 ? "long" : r === 5 ? "narrow" : "short";
        break;
      case "y":
        t.year = r === 2 ? "2-digit" : "numeric";
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
        t.month = ["numeric", "2-digit", "short", "long", "narrow"][r - 1];
        break;
      case "w":
      case "W":
        throw new RangeError("`w/W` (week) patterns are not supported");
      case "d":
        t.day = ["numeric", "2-digit"][r - 1];
        break;
      case "D":
      case "F":
      case "g":
        throw new RangeError("`D/F/g` (day) patterns are not supported, use `d` instead");
      case "E":
        t.weekday = r === 4 ? "short" : r === 5 ? "narrow" : "short";
        break;
      case "e":
        if (r < 4)
          throw new RangeError("`e..eee` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][r - 4];
        break;
      case "c":
        if (r < 4)
          throw new RangeError("`c..ccc` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][r - 4];
        break;
      case "a":
        t.hour12 = !0;
        break;
      case "b":
      case "B":
        throw new RangeError("`b/B` (period) patterns are not supported, use `a` instead");
      case "h":
        t.hourCycle = "h12", t.hour = ["numeric", "2-digit"][r - 1];
        break;
      case "H":
        t.hourCycle = "h23", t.hour = ["numeric", "2-digit"][r - 1];
        break;
      case "K":
        t.hourCycle = "h11", t.hour = ["numeric", "2-digit"][r - 1];
        break;
      case "k":
        t.hourCycle = "h24", t.hour = ["numeric", "2-digit"][r - 1];
        break;
      case "j":
      case "J":
      case "C":
        throw new RangeError("`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead");
      case "m":
        t.minute = ["numeric", "2-digit"][r - 1];
        break;
      case "s":
        t.second = ["numeric", "2-digit"][r - 1];
        break;
      case "S":
      case "A":
        throw new RangeError("`S/A` (second) patterns are not supported, use `s` instead");
      case "z":
        t.timeZoneName = r < 4 ? "short" : "long";
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
var Ei = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function yi(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(Ei).filter(function(c) {
    return c.length > 0;
  }), n = [], r = 0, i = t; r < i.length; r++) {
    var s = i[r], o = s.split("/");
    if (o.length === 0)
      throw new Error("Invalid number skeleton");
    for (var a = o[0], u = o.slice(1), l = 0, f = u; l < f.length; l++) {
      var h = f[l];
      if (h.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: a, options: u });
  }
  return n;
}
function wi(e) {
  return e.replace(/^(.*?)-/, "");
}
var Nt = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, Bn = /^(@+)?(\+|#+)?[rs]?$/g, Ti = /(\*)(0+)|(#+)(0+)|(0+)/g, Hn = /^(0+)$/;
function It(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(Bn, function(n, r, i) {
    return typeof i != "string" ? (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length) : i === "+" ? t.minimumSignificantDigits = r.length : r[0] === "#" ? t.maximumSignificantDigits = r.length : (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length + (typeof i == "string" ? i.length : 0)), "";
  }), t;
}
function An(e) {
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
function xi(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !Hn.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Ct(e) {
  var t = {}, n = An(e);
  return n || t;
}
function Bi(e) {
  for (var t = {}, n = 0, r = e; n < r.length; n++) {
    var i = r[n];
    switch (i.stem) {
      case "percent":
      case "%":
        t.style = "percent";
        continue;
      case "%x100":
        t.style = "percent", t.scale = 100;
        continue;
      case "currency":
        t.style = "currency", t.currency = i.options[0];
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
        t.style = "unit", t.unit = wi(i.options[0]);
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
        t = S(S(S({}, t), { notation: "scientific" }), i.options.reduce(function(u, l) {
          return S(S({}, u), Ct(l));
        }, {}));
        continue;
      case "engineering":
        t = S(S(S({}, t), { notation: "engineering" }), i.options.reduce(function(u, l) {
          return S(S({}, u), Ct(l));
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
        t.scale = parseFloat(i.options[0]);
        continue;
      case "integer-width":
        if (i.options.length > 1)
          throw new RangeError("integer-width stems only accept a single optional option");
        i.options[0].replace(Ti, function(u, l, f, h, c, _) {
          if (l)
            t.minimumIntegerDigits = f.length;
          else {
            if (h && c)
              throw new Error("We currently do not support maximum integer digits");
            if (_)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (Hn.test(i.stem)) {
      t.minimumIntegerDigits = i.stem.length;
      continue;
    }
    if (Nt.test(i.stem)) {
      if (i.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      i.stem.replace(Nt, function(u, l, f, h, c, _) {
        return f === "*" ? t.minimumFractionDigits = l.length : h && h[0] === "#" ? t.maximumFractionDigits = h.length : c && _ ? (t.minimumFractionDigits = c.length, t.maximumFractionDigits = c.length + _.length) : (t.minimumFractionDigits = l.length, t.maximumFractionDigits = l.length), "";
      });
      var s = i.options[0];
      s === "w" ? t = S(S({}, t), { trailingZeroDisplay: "stripIfInteger" }) : s && (t = S(S({}, t), It(s)));
      continue;
    }
    if (Bn.test(i.stem)) {
      t = S(S({}, t), It(i.stem));
      continue;
    }
    var o = An(i.stem);
    o && (t = S(S({}, t), o));
    var a = xi(i.stem);
    a && (t = S(S({}, t), a));
  }
  return t;
}
var He = {
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
function Hi(e, t) {
  for (var n = "", r = 0; r < e.length; r++) {
    var i = e.charAt(r);
    if (i === "j") {
      for (var s = 0; r + 1 < e.length && e.charAt(r + 1) === i; )
        s++, r++;
      var o = 1 + (s & 1), a = s < 2 ? 1 : 3 + (s >> 1), u = "a", l = Ai(t);
      for ((l == "H" || l == "k") && (a = 0); a-- > 0; )
        n += u;
      for (; o-- > 0; )
        n = l + n;
    } else
      i === "J" ? n += "H" : n += i;
  }
  return n;
}
function Ai(e) {
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
  var n = e.language, r;
  n !== "root" && (r = e.maximize().region);
  var i = He[r || ""] || He[n || ""] || He["".concat(n, "-001")] || He["001"];
  return i[0];
}
var je, Si = new RegExp("^".concat(xn.source, "*")), Pi = new RegExp("".concat(xn.source, "*$"));
function H(e, t) {
  return { start: e, end: t };
}
var Ni = !!String.prototype.startsWith, Ii = !!String.fromCodePoint, Ci = !!Object.fromEntries, Li = !!String.prototype.codePointAt, Oi = !!String.prototype.trimStart, Mi = !!String.prototype.trimEnd, Ri = !!Number.isSafeInteger, Di = Ri ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, tt = !0;
try {
  var ki = Pn("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  tt = ((je = ki.exec("a")) === null || je === void 0 ? void 0 : je[0]) === "a";
} catch {
  tt = !1;
}
var Lt = Ni ? (
  // Native
  function(t, n, r) {
    return t.startsWith(n, r);
  }
) : (
  // For IE11
  function(t, n, r) {
    return t.slice(r, r + n.length) === n;
  }
), nt = Ii ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var r = "", i = t.length, s = 0, o; i > s; ) {
      if (o = t[s++], o > 1114111)
        throw RangeError(o + " is not a valid code point");
      r += o < 65536 ? String.fromCharCode(o) : String.fromCharCode(((o -= 65536) >> 10) + 55296, o % 1024 + 56320);
    }
    return r;
  }
), Ot = (
  // native
  Ci ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, r = 0, i = t; r < i.length; r++) {
        var s = i[r], o = s[0], a = s[1];
        n[o] = a;
      }
      return n;
    }
  )
), Sn = Li ? (
  // Native
  function(t, n) {
    return t.codePointAt(n);
  }
) : (
  // IE 11
  function(t, n) {
    var r = t.length;
    if (!(n < 0 || n >= r)) {
      var i = t.charCodeAt(n), s;
      return i < 55296 || i > 56319 || n + 1 === r || (s = t.charCodeAt(n + 1)) < 56320 || s > 57343 ? i : (i - 55296 << 10) + (s - 56320) + 65536;
    }
  }
), Fi = Oi ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Si, "");
  }
), Ui = Mi ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Pi, "");
  }
);
function Pn(e, t) {
  return new RegExp(e, t);
}
var rt;
if (tt) {
  var Mt = Pn("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  rt = function(t, n) {
    var r;
    Mt.lastIndex = n;
    var i = Mt.exec(t);
    return (r = i[1]) !== null && r !== void 0 ? r : "";
  };
} else
  rt = function(t, n) {
    for (var r = []; ; ) {
      var i = Sn(t, n);
      if (i === void 0 || Nn(i) || Xi(i))
        break;
      r.push(i), n += i >= 65536 ? 2 : 1;
    }
    return nt.apply(void 0, r);
  };
var Gi = (
  /** @class */
  function() {
    function e(t, n) {
      n === void 0 && (n = {}), this.message = t, this.position = { offset: 0, line: 1, column: 1 }, this.ignoreTag = !!n.ignoreTag, this.locale = n.locale, this.requiresOtherClause = !!n.requiresOtherClause, this.shouldParseSkeletons = !!n.shouldParseSkeletons;
    }
    return e.prototype.parse = function() {
      if (this.offset() !== 0)
        throw Error("parser can only be used once");
      return this.parseMessage(0, "", !1);
    }, e.prototype.parseMessage = function(t, n, r) {
      for (var i = []; !this.isEOF(); ) {
        var s = this.char();
        if (s === 123) {
          var o = this.parseArgument(t, r);
          if (o.err)
            return o;
          i.push(o.val);
        } else {
          if (s === 125 && t > 0)
            break;
          if (s === 35 && (n === "plural" || n === "selectordinal")) {
            var a = this.clonePosition();
            this.bump(), i.push({
              type: N.pound,
              location: H(a, this.clonePosition())
            });
          } else if (s === 60 && !this.ignoreTag && this.peek() === 47) {
            if (r)
              break;
            return this.error(B.UNMATCHED_CLOSING_TAG, H(this.clonePosition(), this.clonePosition()));
          } else if (s === 60 && !this.ignoreTag && it(this.peek() || 0)) {
            var o = this.parseTag(t, n);
            if (o.err)
              return o;
            i.push(o.val);
          } else {
            var o = this.parseLiteral(t, n);
            if (o.err)
              return o;
            i.push(o.val);
          }
        }
      }
      return { val: i, err: null };
    }, e.prototype.parseTag = function(t, n) {
      var r = this.clonePosition();
      this.bump();
      var i = this.parseTagName();
      if (this.bumpSpace(), this.bumpIf("/>"))
        return {
          val: {
            type: N.literal,
            value: "<".concat(i, "/>"),
            location: H(r, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var s = this.parseMessage(t + 1, n, !0);
        if (s.err)
          return s;
        var o = s.val, a = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !it(this.char()))
            return this.error(B.INVALID_TAG, H(a, this.clonePosition()));
          var u = this.clonePosition(), l = this.parseTagName();
          return i !== l ? this.error(B.UNMATCHED_CLOSING_TAG, H(u, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: N.tag,
              value: i,
              children: o,
              location: H(r, this.clonePosition())
            },
            err: null
          } : this.error(B.INVALID_TAG, H(a, this.clonePosition())));
        } else
          return this.error(B.UNCLOSED_TAG, H(r, this.clonePosition()));
      } else
        return this.error(B.INVALID_TAG, H(r, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && ji(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var r = this.clonePosition(), i = ""; ; ) {
        var s = this.tryParseQuote(n);
        if (s) {
          i += s;
          continue;
        }
        var o = this.tryParseUnquoted(t, n);
        if (o) {
          i += o;
          continue;
        }
        var a = this.tryParseLeftAngleBracket();
        if (a) {
          i += a;
          continue;
        }
        break;
      }
      var u = H(r, this.clonePosition());
      return {
        val: { type: N.literal, value: i, location: u },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !Vi(this.peek() || 0)) ? (this.bump(), "<") : null;
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
        var r = this.char();
        if (r === 39)
          if (this.peek() === 39)
            n.push(39), this.bump();
          else {
            this.bump();
            break;
          }
        else
          n.push(r);
        this.bump();
      }
      return nt.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var r = this.char();
      return r === 60 || r === 123 || r === 35 && (n === "plural" || n === "selectordinal") || r === 125 && t > 0 ? null : (this.bump(), nt(r));
    }, e.prototype.parseArgument = function(t, n) {
      var r = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(B.EMPTY_ARGUMENT, H(r, this.clonePosition()));
      var i = this.parseIdentifierIfPossible().value;
      if (!i)
        return this.error(B.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: N.argument,
              // value does not include the opening and closing braces.
              value: i,
              location: H(r, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition())) : this.parseArgumentOptions(t, n, i, r);
        default:
          return this.error(B.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), r = rt(this.message, n), i = n + r.length;
      this.bumpTo(i);
      var s = this.clonePosition(), o = H(t, s);
      return { value: r, location: o };
    }, e.prototype.parseArgumentOptions = function(t, n, r, i) {
      var s, o = this.clonePosition(), a = this.parseIdentifierIfPossible().value, u = this.clonePosition();
      switch (a) {
        case "":
          return this.error(B.EXPECT_ARGUMENT_TYPE, H(o, u));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var l = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), h = this.parseSimpleArgStyleIfPossible();
            if (h.err)
              return h;
            var c = Ui(h.val);
            if (c.length === 0)
              return this.error(B.EXPECT_ARGUMENT_STYLE, H(this.clonePosition(), this.clonePosition()));
            var _ = H(f, this.clonePosition());
            l = { style: c, styleLocation: _ };
          }
          var m = this.tryParseArgumentClose(i);
          if (m.err)
            return m;
          var b = H(i, this.clonePosition());
          if (l && Lt(l == null ? void 0 : l.style, "::", 0)) {
            var v = Fi(l.style.slice(2));
            if (a === "number") {
              var h = this.parseNumberSkeletonFromString(v, l.styleLocation);
              return h.err ? h : {
                val: { type: N.number, value: r, location: b, style: h.val },
                err: null
              };
            } else {
              if (v.length === 0)
                return this.error(B.EXPECT_DATE_TIME_SKELETON, b);
              var P = v;
              this.locale && (P = Hi(v, this.locale));
              var c = {
                type: oe.dateTime,
                pattern: P,
                location: l.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? vi(P) : {}
              }, x = a === "date" ? N.date : N.time;
              return {
                val: { type: x, value: r, location: b, style: c },
                err: null
              };
            }
          }
          return {
            val: {
              type: a === "number" ? N.number : a === "date" ? N.date : N.time,
              value: r,
              location: b,
              style: (s = l == null ? void 0 : l.style) !== null && s !== void 0 ? s : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var d = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(B.EXPECT_SELECT_ARGUMENT_OPTIONS, H(d, S({}, d)));
          this.bumpSpace();
          var E = this.parseIdentifierIfPossible(), p = 0;
          if (a !== "select" && E.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(B.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, H(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var h = this.tryParseDecimalInteger(B.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, B.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (h.err)
              return h;
            this.bumpSpace(), E = this.parseIdentifierIfPossible(), p = h.val;
          }
          var F = this.tryParsePluralOrSelectOptions(t, a, n, E);
          if (F.err)
            return F;
          var m = this.tryParseArgumentClose(i);
          if (m.err)
            return m;
          var U = H(i, this.clonePosition());
          return a === "select" ? {
            val: {
              type: N.select,
              value: r,
              options: Ot(F.val),
              location: U
            },
            err: null
          } : {
            val: {
              type: N.plural,
              value: r,
              options: Ot(F.val),
              offset: p,
              pluralType: a === "plural" ? "cardinal" : "ordinal",
              location: U
            },
            err: null
          };
        }
        default:
          return this.error(B.INVALID_ARGUMENT_TYPE, H(o, u));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, H(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var r = this.char();
        switch (r) {
          case 39: {
            this.bump();
            var i = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(B.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, H(i, this.clonePosition()));
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
      var r = [];
      try {
        r = yi(t);
      } catch {
        return this.error(B.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: oe.number,
          tokens: r,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? Bi(r) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, r, i) {
      for (var s, o = !1, a = [], u = /* @__PURE__ */ new Set(), l = i.value, f = i.location; ; ) {
        if (l.length === 0) {
          var h = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var c = this.tryParseDecimalInteger(B.EXPECT_PLURAL_ARGUMENT_SELECTOR, B.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (c.err)
              return c;
            f = H(h, this.clonePosition()), l = this.message.slice(h.offset, this.offset());
          } else
            break;
        }
        if (u.has(l))
          return this.error(n === "select" ? B.DUPLICATE_SELECT_ARGUMENT_SELECTOR : B.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        l === "other" && (o = !0), this.bumpSpace();
        var _ = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? B.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : B.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, H(this.clonePosition(), this.clonePosition()));
        var m = this.parseMessage(t + 1, n, r);
        if (m.err)
          return m;
        var b = this.tryParseArgumentClose(_);
        if (b.err)
          return b;
        a.push([
          l,
          {
            value: m.val,
            location: H(_, this.clonePosition())
          }
        ]), u.add(l), this.bumpSpace(), s = this.parseIdentifierIfPossible(), l = s.value, f = s.location;
      }
      return a.length === 0 ? this.error(n === "select" ? B.EXPECT_SELECT_ARGUMENT_SELECTOR : B.EXPECT_PLURAL_ARGUMENT_SELECTOR, H(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !o ? this.error(B.MISSING_OTHER_CLAUSE, H(this.clonePosition(), this.clonePosition())) : { val: a, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var r = 1, i = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (r = -1);
      for (var s = !1, o = 0; !this.isEOF(); ) {
        var a = this.char();
        if (a >= 48 && a <= 57)
          s = !0, o = o * 10 + (a - 48), this.bump();
        else
          break;
      }
      var u = H(i, this.clonePosition());
      return s ? (o *= r, Di(o) ? { val: o, err: null } : this.error(n, u)) : this.error(t, u);
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
      var n = Sn(this.message, t);
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
      if (Lt(this.message, t, this.offset())) {
        for (var n = 0; n < t.length; n++)
          this.bump();
        return !0;
      }
      return !1;
    }, e.prototype.bumpUntil = function(t) {
      var n = this.offset(), r = this.message.indexOf(t, n);
      return r >= 0 ? (this.bumpTo(r), !0) : (this.bumpTo(this.message.length), !1);
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
      for (; !this.isEOF() && Nn(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), r = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return r ?? null;
    }, e;
  }()
);
function it(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Vi(e) {
  return it(e) || e === 47;
}
function ji(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function Nn(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function Xi(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function st(e) {
  e.forEach(function(t) {
    if (delete t.location, En(t) || yn(t))
      for (var n in t.options)
        delete t.options[n].location, st(t.options[n].value);
    else
      pn(t) && Tn(t.style) || (gn(t) || vn(t)) && et(t.style) ? delete t.style.location : wn(t) && st(t.children);
  });
}
function zi(e, t) {
  t === void 0 && (t = {}), t = S({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new Gi(e, t).parse();
  if (n.err) {
    var r = SyntaxError(B[n.err.kind]);
    throw r.location = n.err.location, r.originalMessage = n.err.message, r;
  }
  return t != null && t.captureLocation || st(n.val), n.val;
}
function Xe(e, t) {
  var n = t && t.cache ? t.cache : Yi, r = t && t.serializer ? t.serializer : Ji, i = t && t.strategy ? t.strategy : Zi;
  return i(e, {
    cache: n,
    serializer: r
  });
}
function qi(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function In(e, t, n, r) {
  var i = qi(r) ? r : n(r), s = t.get(i);
  return typeof s > "u" && (s = e.call(this, r), t.set(i, s)), s;
}
function Cn(e, t, n) {
  var r = Array.prototype.slice.call(arguments, 3), i = n(r), s = t.get(i);
  return typeof s > "u" && (s = e.apply(this, r), t.set(i, s)), s;
}
function ut(e, t, n, r, i) {
  return n.bind(t, e, r, i);
}
function Zi(e, t) {
  var n = e.length === 1 ? In : Cn;
  return ut(e, this, n, t.cache.create(), t.serializer);
}
function Wi(e, t) {
  return ut(e, this, Cn, t.cache.create(), t.serializer);
}
function Qi(e, t) {
  return ut(e, this, In, t.cache.create(), t.serializer);
}
var Ji = function() {
  return JSON.stringify(arguments);
};
function ft() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
ft.prototype.get = function(e) {
  return this.cache[e];
};
ft.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var Yi = {
  create: function() {
    return new ft();
  }
}, ze = {
  variadic: Wi,
  monadic: Qi
}, ae;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(ae || (ae = {}));
var ke = (
  /** @class */
  function(e) {
    De(t, e);
    function t(n, r, i) {
      var s = e.call(this, n) || this;
      return s.code = r, s.originalMessage = i, s;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), Rt = (
  /** @class */
  function(e) {
    De(t, e);
    function t(n, r, i, s) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(r, '". Options are "').concat(Object.keys(i).join('", "'), '"'), ae.INVALID_VALUE, s) || this;
    }
    return t;
  }(ke)
), Ki = (
  /** @class */
  function(e) {
    De(t, e);
    function t(n, r, i) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(r), ae.INVALID_VALUE, i) || this;
    }
    return t;
  }(ke)
), $i = (
  /** @class */
  function(e) {
    De(t, e);
    function t(n, r) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(r, '"'), ae.MISSING_VALUE, r) || this;
    }
    return t;
  }(ke)
), C;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(C || (C = {}));
function es(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var r = t[t.length - 1];
    return !r || r.type !== C.literal || n.type !== C.literal ? t.push(n) : r.value += n.value, t;
  }, []);
}
function ts(e) {
  return typeof e == "function";
}
function Ce(e, t, n, r, i, s, o) {
  if (e.length === 1 && Pt(e[0]))
    return [
      {
        type: C.literal,
        value: e[0].value
      }
    ];
  for (var a = [], u = 0, l = e; u < l.length; u++) {
    var f = l[u];
    if (Pt(f)) {
      a.push({
        type: C.literal,
        value: f.value
      });
      continue;
    }
    if (pi(f)) {
      typeof s == "number" && a.push({
        type: C.literal,
        value: n.getNumberFormat(t).format(s)
      });
      continue;
    }
    var h = f.value;
    if (!(i && h in i))
      throw new $i(h, o);
    var c = i[h];
    if (bi(f)) {
      (!c || typeof c == "string" || typeof c == "number") && (c = typeof c == "string" || typeof c == "number" ? String(c) : ""), a.push({
        type: typeof c == "string" ? C.literal : C.object,
        value: c
      });
      continue;
    }
    if (gn(f)) {
      var _ = typeof f.style == "string" ? r.date[f.style] : et(f.style) ? f.style.parsedOptions : void 0;
      a.push({
        type: C.literal,
        value: n.getDateTimeFormat(t, _).format(c)
      });
      continue;
    }
    if (vn(f)) {
      var _ = typeof f.style == "string" ? r.time[f.style] : et(f.style) ? f.style.parsedOptions : r.time.medium;
      a.push({
        type: C.literal,
        value: n.getDateTimeFormat(t, _).format(c)
      });
      continue;
    }
    if (pn(f)) {
      var _ = typeof f.style == "string" ? r.number[f.style] : Tn(f.style) ? f.style.parsedOptions : void 0;
      _ && _.scale && (c = c * (_.scale || 1)), a.push({
        type: C.literal,
        value: n.getNumberFormat(t, _).format(c)
      });
      continue;
    }
    if (wn(f)) {
      var m = f.children, b = f.value, v = i[b];
      if (!ts(v))
        throw new Ki(b, "function", o);
      var P = Ce(m, t, n, r, i, s), x = v(P.map(function(p) {
        return p.value;
      }));
      Array.isArray(x) || (x = [x]), a.push.apply(a, x.map(function(p) {
        return {
          type: typeof p == "string" ? C.literal : C.object,
          value: p
        };
      }));
    }
    if (En(f)) {
      var d = f.options[c] || f.options.other;
      if (!d)
        throw new Rt(f.value, c, Object.keys(f.options), o);
      a.push.apply(a, Ce(d.value, t, n, r, i));
      continue;
    }
    if (yn(f)) {
      var d = f.options["=".concat(c)];
      if (!d) {
        if (!Intl.PluralRules)
          throw new ke(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, ae.MISSING_INTL_API, o);
        var E = n.getPluralRules(t, { type: f.pluralType }).select(c - (f.offset || 0));
        d = f.options[E] || f.options.other;
      }
      if (!d)
        throw new Rt(f.value, c, Object.keys(f.options), o);
      a.push.apply(a, Ce(d.value, t, n, r, i, c - (f.offset || 0)));
      continue;
    }
  }
  return es(a);
}
function ns(e, t) {
  return t ? S(S(S({}, e || {}), t || {}), Object.keys(e).reduce(function(n, r) {
    return n[r] = S(S({}, e[r]), t[r] || {}), n;
  }, {})) : e;
}
function rs(e, t) {
  return t ? Object.keys(e).reduce(function(n, r) {
    return n[r] = ns(e[r], t[r]), n;
  }, S({}, e)) : e;
}
function qe(e) {
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
function is(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Xe(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.NumberFormat).bind.apply(t, Ve([void 0], n, !1)))();
    }, {
      cache: qe(e.number),
      strategy: ze.variadic
    }),
    getDateTimeFormat: Xe(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, Ve([void 0], n, !1)))();
    }, {
      cache: qe(e.dateTime),
      strategy: ze.variadic
    }),
    getPluralRules: Xe(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.PluralRules).bind.apply(t, Ve([void 0], n, !1)))();
    }, {
      cache: qe(e.pluralRules),
      strategy: ze.variadic
    })
  };
}
var ss = (
  /** @class */
  function() {
    function e(t, n, r, i) {
      var s = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(o) {
        var a = s.formatToParts(o);
        if (a.length === 1)
          return a[0].value;
        var u = a.reduce(function(l, f) {
          return !l.length || f.type !== C.literal || typeof l[l.length - 1] != "string" ? l.push(f.value) : l[l.length - 1] += f.value, l;
        }, []);
        return u.length <= 1 ? u[0] || "" : u;
      }, this.formatToParts = function(o) {
        return Ce(s.ast, s.locales, s.formatters, s.formats, o, void 0, s.message);
      }, this.resolvedOptions = function() {
        return {
          locale: s.resolvedLocale.toString()
        };
      }, this.getAst = function() {
        return s.ast;
      }, this.locales = n, this.resolvedLocale = e.resolveLocale(n), typeof t == "string") {
        if (this.message = t, !e.__parse)
          throw new TypeError("IntlMessageFormat.__parse must be set to process `message` of type `string`");
        this.ast = e.__parse(t, {
          ignoreTag: i == null ? void 0 : i.ignoreTag,
          locale: this.resolvedLocale
        });
      } else
        this.ast = t;
      if (!Array.isArray(this.ast))
        throw new TypeError("A message must be provided as a String or AST.");
      this.formats = rs(e.formats, r), this.formatters = i && i.formatters || is(this.formatterCache);
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
    }, e.__parse = zi, e.formats = {
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
function os(e, t) {
  if (t == null)
    return;
  if (t in e)
    return e[t];
  const n = t.split(".");
  let r = e;
  for (let i = 0; i < n.length; i++)
    if (typeof r == "object") {
      if (i > 0) {
        const s = n.slice(i, n.length).join(".");
        if (s in r) {
          r = r[s];
          break;
        }
      }
      r = r[n[i]];
    } else
      r = void 0;
  return r;
}
const Z = {}, as = (e, t, n) => n && (t in Z || (Z[t] = {}), e in Z[t] || (Z[t][e] = n), n), Ln = (e, t) => {
  if (t == null)
    return;
  if (t in Z && e in Z[t])
    return Z[t][e];
  const n = Fe(t);
  for (let r = 0; r < n.length; r++) {
    const i = n[r], s = us(i, e);
    if (s)
      return as(e, t, s);
  }
};
let ht;
const Te = we({});
function ls(e) {
  return ht[e] || null;
}
function On(e) {
  return e in ht;
}
function us(e, t) {
  if (!On(e))
    return null;
  const n = ls(e);
  return os(n, t);
}
function fs(e) {
  if (e == null)
    return;
  const t = Fe(e);
  for (let n = 0; n < t.length; n++) {
    const r = t[n];
    if (On(r))
      return r;
  }
}
function hs(e, ...t) {
  delete Z[e], Te.update((n) => (n[e] = di.all([n[e] || {}, ...t]), n));
}
he(
  [Te],
  ([e]) => Object.keys(e)
);
Te.subscribe((e) => ht = e);
const Le = {};
function cs(e, t) {
  Le[e].delete(t), Le[e].size === 0 && delete Le[e];
}
function Mn(e) {
  return Le[e];
}
function _s(e) {
  return Fe(e).map((t) => {
    const n = Mn(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function ot(e) {
  return e == null ? !1 : Fe(e).some(
    (t) => {
      var n;
      return (n = Mn(t)) == null ? void 0 : n.size;
    }
  );
}
function ms(e, t) {
  return Promise.all(
    t.map((r) => (cs(e, r), r().then((i) => i.default || i)))
  ).then((r) => hs(e, ...r));
}
const de = {};
function Rn(e) {
  if (!ot(e))
    return e in de ? de[e] : Promise.resolve();
  const t = _s(e);
  return de[e] = Promise.all(
    t.map(
      ([n, r]) => ms(n, r)
    )
  ).then(() => {
    if (ot(e))
      return Rn(e);
    delete de[e];
  }), de[e];
}
const ds = {
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
}, bs = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: ds,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, ps = bs;
function le() {
  return ps;
}
const Ze = we(!1);
var gs = Object.defineProperty, vs = Object.defineProperties, Es = Object.getOwnPropertyDescriptors, Dt = Object.getOwnPropertySymbols, ys = Object.prototype.hasOwnProperty, ws = Object.prototype.propertyIsEnumerable, kt = (e, t, n) => t in e ? gs(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, Ts = (e, t) => {
  for (var n in t || (t = {}))
    ys.call(t, n) && kt(e, n, t[n]);
  if (Dt)
    for (var n of Dt(t))
      ws.call(t, n) && kt(e, n, t[n]);
  return e;
}, xs = (e, t) => vs(e, Es(t));
let at;
const Oe = we(null);
function Ft(e) {
  return e.split("-").map((t, n, r) => r.slice(0, n + 1).join("-")).reverse();
}
function Fe(e, t = le().fallbackLocale) {
  const n = Ft(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Ft(t)])] : n;
}
function $() {
  return at ?? void 0;
}
Oe.subscribe((e) => {
  at = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const Bs = (e) => {
  if (e && fs(e) && ot(e)) {
    const { loadingDelay: t } = le();
    let n;
    return typeof window < "u" && $() != null && t ? n = window.setTimeout(
      () => Ze.set(!0),
      t
    ) : Ze.set(!0), Rn(e).then(() => {
      Oe.set(e);
    }).finally(() => {
      clearTimeout(n), Ze.set(!1);
    });
  }
  return Oe.set(e);
}, xe = xs(Ts({}, Oe), {
  set: Bs
}), Ue = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (r) => {
    const i = JSON.stringify(r);
    return i in t ? t[i] : t[i] = e(r);
  };
};
var Hs = Object.defineProperty, Me = Object.getOwnPropertySymbols, Dn = Object.prototype.hasOwnProperty, kn = Object.prototype.propertyIsEnumerable, Ut = (e, t, n) => t in e ? Hs(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, ct = (e, t) => {
  for (var n in t || (t = {}))
    Dn.call(t, n) && Ut(e, n, t[n]);
  if (Me)
    for (var n of Me(t))
      kn.call(t, n) && Ut(e, n, t[n]);
  return e;
}, ce = (e, t) => {
  var n = {};
  for (var r in e)
    Dn.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
  if (e != null && Me)
    for (var r of Me(e))
      t.indexOf(r) < 0 && kn.call(e, r) && (n[r] = e[r]);
  return n;
};
const ve = (e, t) => {
  const { formats: n } = le();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, As = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = ce(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return r && (i = ve("number", r)), new Intl.NumberFormat(n, i);
  }
), Ss = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = ce(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return r ? i = ve("date", r) : Object.keys(i).length === 0 && (i = ve("date", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ps = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = ce(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return r ? i = ve("time", r) : Object.keys(i).length === 0 && (i = ve("time", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ns = (e = {}) => {
  var t = e, {
    locale: n = $()
  } = t, r = ce(t, [
    "locale"
  ]);
  return As(ct({ locale: n }, r));
}, Is = (e = {}) => {
  var t = e, {
    locale: n = $()
  } = t, r = ce(t, [
    "locale"
  ]);
  return Ss(ct({ locale: n }, r));
}, Cs = (e = {}) => {
  var t = e, {
    locale: n = $()
  } = t, r = ce(t, [
    "locale"
  ]);
  return Ps(ct({ locale: n }, r));
}, Ls = Ue(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = $()) => new ss(e, t, le().formats, {
    ignoreTag: le().ignoreTag
  })
), Os = (e, t = {}) => {
  var n, r, i, s;
  let o = t;
  typeof e == "object" && (o = e, e = o.id);
  const {
    values: a,
    locale: u = $(),
    default: l
  } = o;
  if (u == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = Ln(e, u);
  if (!f)
    f = (s = (i = (r = (n = le()).handleMissingMessage) == null ? void 0 : r.call(n, { locale: u, id: e, defaultValue: l })) != null ? i : l) != null ? s : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!a)
    return f;
  let h = f;
  try {
    h = Ls(f, u).format(a);
  } catch (c) {
    c instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      c.message
    );
  }
  return h;
}, Ms = (e, t) => Cs(t).format(e), Rs = (e, t) => Is(t).format(e), Ds = (e, t) => Ns(t).format(e), ks = (e, t = $()) => Ln(e, t), Fs = he([xe, Te], () => Os);
he([xe], () => Ms);
he([xe], () => Rs);
he([xe], () => Ds);
he([xe, Te], () => ks);
Yr(Fs);
function ne(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let r = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + r;
}
const {
  SvelteComponent: Us,
  append: D,
  attr: A,
  component_subscribe: Gt,
  detach: Gs,
  element: Vs,
  init: js,
  insert: Xs,
  noop: Vt,
  safe_not_equal: zs,
  set_style: Ae,
  svg_element: k,
  toggle_class: jt
} = window.__gradio__svelte__internal, { onMount: qs } = window.__gradio__svelte__internal;
function Zs(e) {
  let t, n, r, i, s, o, a, u, l, f, h, c;
  return {
    c() {
      t = Vs("div"), n = k("svg"), r = k("g"), i = k("path"), s = k("path"), o = k("path"), a = k("path"), u = k("g"), l = k("path"), f = k("path"), h = k("path"), c = k("path"), A(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), A(i, "fill", "#FF7C00"), A(i, "fill-opacity", "0.4"), A(i, "class", "svelte-43sxxs"), A(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), A(s, "fill", "#FF7C00"), A(s, "class", "svelte-43sxxs"), A(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), A(o, "fill", "#FF7C00"), A(o, "fill-opacity", "0.4"), A(o, "class", "svelte-43sxxs"), A(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), A(a, "fill", "#FF7C00"), A(a, "class", "svelte-43sxxs"), Ae(r, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), A(l, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), A(l, "fill", "#FF7C00"), A(l, "fill-opacity", "0.4"), A(l, "class", "svelte-43sxxs"), A(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), A(f, "fill", "#FF7C00"), A(f, "class", "svelte-43sxxs"), A(h, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), A(h, "fill", "#FF7C00"), A(h, "fill-opacity", "0.4"), A(h, "class", "svelte-43sxxs"), A(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), A(c, "fill", "#FF7C00"), A(c, "class", "svelte-43sxxs"), Ae(u, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), A(n, "viewBox", "-1200 -1200 3000 3000"), A(n, "fill", "none"), A(n, "xmlns", "http://www.w3.org/2000/svg"), A(n, "class", "svelte-43sxxs"), A(t, "class", "svelte-43sxxs"), jt(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(_, m) {
      Xs(_, t, m), D(t, n), D(n, r), D(r, i), D(r, s), D(r, o), D(r, a), D(n, u), D(u, l), D(u, f), D(u, h), D(u, c);
    },
    p(_, [m]) {
      m & /*$top*/
      2 && Ae(r, "transform", "translate(" + /*$top*/
      _[1][0] + "px, " + /*$top*/
      _[1][1] + "px)"), m & /*$bottom*/
      4 && Ae(u, "transform", "translate(" + /*$bottom*/
      _[2][0] + "px, " + /*$bottom*/
      _[2][1] + "px)"), m & /*margin*/
      1 && jt(
        t,
        "margin",
        /*margin*/
        _[0]
      );
    },
    i: Vt,
    o: Vt,
    d(_) {
      _ && Gs(t);
    }
  };
}
function Ws(e, t, n) {
  let r, i, { margin: s = !0 } = t;
  const o = At([0, 0]);
  Gt(e, o, (c) => n(1, r = c));
  const a = At([0, 0]);
  Gt(e, a, (c) => n(2, i = c));
  let u;
  async function l() {
    await Promise.all([o.set([125, 140]), a.set([-125, -140])]), await Promise.all([o.set([-125, 140]), a.set([125, -140])]), await Promise.all([o.set([-125, 0]), a.set([125, -0])]), await Promise.all([o.set([125, 0]), a.set([-125, 0])]);
  }
  async function f() {
    await l(), u || f();
  }
  async function h() {
    await Promise.all([o.set([125, 0]), a.set([-125, 0])]), f();
  }
  return qs(() => (h(), () => u = !0)), e.$$set = (c) => {
    "margin" in c && n(0, s = c.margin);
  }, [s, r, i, o, a];
}
class Qs extends Us {
  constructor(t) {
    super(), js(this, t, Ws, Zs, zs, { margin: 0 });
  }
}
const {
  SvelteComponent: Js,
  append: Y,
  attr: G,
  binding_callbacks: Xt,
  check_outros: Fn,
  create_component: Ys,
  create_slot: Ks,
  destroy_component: $s,
  destroy_each: Un,
  detach: y,
  element: j,
  empty: _e,
  ensure_array_like: Re,
  get_all_dirty_from_scope: eo,
  get_slot_changes: to,
  group_outros: Gn,
  init: no,
  insert: w,
  mount_component: ro,
  noop: lt,
  safe_not_equal: io,
  set_data: R,
  set_style: W,
  space: V,
  text: I,
  toggle_class: M,
  transition_in: ue,
  transition_out: fe,
  update_slot_base: so
} = window.__gradio__svelte__internal, { tick: oo } = window.__gradio__svelte__internal, { onDestroy: ao } = window.__gradio__svelte__internal, lo = (e) => ({}), zt = (e) => ({});
function qt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r[40] = n, r;
}
function Zt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r;
}
function uo(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), r, i, s;
  const o = (
    /*#slots*/
    e[29].error
  ), a = Ks(
    o,
    e,
    /*$$scope*/
    e[28],
    zt
  );
  return {
    c() {
      t = j("span"), r = I(n), i = V(), a && a.c(), G(t, "class", "error svelte-14miwb5");
    },
    m(u, l) {
      w(u, t, l), Y(t, r), w(u, i, l), a && a.m(u, l), s = !0;
    },
    p(u, l) {
      (!s || l[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      u[1]("common.error") + "") && R(r, n), a && a.p && (!s || l[0] & /*$$scope*/
      268435456) && so(
        a,
        o,
        u,
        /*$$scope*/
        u[28],
        s ? to(
          o,
          /*$$scope*/
          u[28],
          l,
          lo
        ) : eo(
          /*$$scope*/
          u[28]
        ),
        zt
      );
    },
    i(u) {
      s || (ue(a, u), s = !0);
    },
    o(u) {
      fe(a, u), s = !1;
    },
    d(u) {
      u && (y(t), y(i)), a && a.d(u);
    }
  };
}
function fo(e) {
  let t, n, r, i, s, o, a, u, l, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && Wt(e)
  );
  function h(d, E) {
    if (
      /*progress*/
      d[7]
    )
      return _o;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return co;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return ho;
  }
  let c = h(e), _ = c && c(e), m = (
    /*timer*/
    e[5] && Yt(e)
  );
  const b = [go, po], v = [];
  function P(d, E) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = P(e)) && (o = v[s] = b[s](e));
  let x = !/*timer*/
  e[5] && sn(e);
  return {
    c() {
      f && f.c(), t = V(), n = j("div"), _ && _.c(), r = V(), m && m.c(), i = V(), o && o.c(), a = V(), x && x.c(), u = _e(), G(n, "class", "progress-text svelte-14miwb5"), M(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), M(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(d, E) {
      f && f.m(d, E), w(d, t, E), w(d, n, E), _ && _.m(n, null), Y(n, r), m && m.m(n, null), w(d, i, E), ~s && v[s].m(d, E), w(d, a, E), x && x.m(d, E), w(d, u, E), l = !0;
    },
    p(d, E) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? f ? f.p(d, E) : (f = Wt(d), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), c === (c = h(d)) && _ ? _.p(d, E) : (_ && _.d(1), _ = c && c(d), _ && (_.c(), _.m(n, r))), /*timer*/
      d[5] ? m ? m.p(d, E) : (m = Yt(d), m.c(), m.m(n, null)) : m && (m.d(1), m = null), (!l || E[0] & /*variant*/
      256) && M(
        n,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!l || E[0] & /*variant*/
      256) && M(
        n,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let p = s;
      s = P(d), s === p ? ~s && v[s].p(d, E) : (o && (Gn(), fe(v[p], 1, 1, () => {
        v[p] = null;
      }), Fn()), ~s ? (o = v[s], o ? o.p(d, E) : (o = v[s] = b[s](d), o.c()), ue(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      d[5] ? x && (x.d(1), x = null) : x ? x.p(d, E) : (x = sn(d), x.c(), x.m(u.parentNode, u));
    },
    i(d) {
      l || (ue(o), l = !0);
    },
    o(d) {
      fe(o), l = !1;
    },
    d(d) {
      d && (y(t), y(n), y(i), y(a), y(u)), f && f.d(d), _ && _.d(), m && m.d(), ~s && v[s].d(d), x && x.d(d);
    }
  };
}
function Wt(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = j("div"), G(t, "class", "eta-bar svelte-14miwb5"), W(t, "transform", n);
    },
    m(r, i) {
      w(r, t, i);
    },
    p(r, i) {
      i[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (r[17] || 0) * 100 - 100}%)`) && W(t, "transform", n);
    },
    d(r) {
      r && y(t);
    }
  };
}
function ho(e) {
  let t;
  return {
    c() {
      t = I("processing |");
    },
    m(n, r) {
      w(n, t, r);
    },
    p: lt,
    d(n) {
      n && y(t);
    }
  };
}
function co(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), r, i, s, o;
  return {
    c() {
      t = I("queue: "), r = I(n), i = I("/"), s = I(
        /*queue_size*/
        e[3]
      ), o = I(" |");
    },
    m(a, u) {
      w(a, t, u), w(a, r, u), w(a, i, u), w(a, s, u), w(a, o, u);
    },
    p(a, u) {
      u[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      a[2] + 1 + "") && R(r, n), u[0] & /*queue_size*/
      8 && R(
        s,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (y(t), y(r), y(i), y(s), y(o));
    }
  };
}
function _o(e) {
  let t, n = Re(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = Jt(Zt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = _e();
    },
    m(i, s) {
      for (let o = 0; o < r.length; o += 1)
        r[o] && r[o].m(i, s);
      w(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        n = Re(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = Zt(i, n, o);
          r[o] ? r[o].p(a, s) : (r[o] = Jt(a), r[o].c(), r[o].m(t.parentNode, t));
        }
        for (; o < r.length; o += 1)
          r[o].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && y(t), Un(r, i);
    }
  };
}
function Qt(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), r, i, s = " ", o;
  function a(f, h) {
    return (
      /*p*/
      f[38].length != null ? bo : mo
    );
  }
  let u = a(e), l = u(e);
  return {
    c() {
      l.c(), t = V(), r = I(n), i = I(" | "), o = I(s);
    },
    m(f, h) {
      l.m(f, h), w(f, t, h), w(f, r, h), w(f, i, h), w(f, o, h);
    },
    p(f, h) {
      u === (u = a(f)) && l ? l.p(f, h) : (l.d(1), l = u(f), l && (l.c(), l.m(t.parentNode, t))), h[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && R(r, n);
    },
    d(f) {
      f && (y(t), y(r), y(i), y(o)), l.d(f);
    }
  };
}
function mo(e) {
  let t = ne(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = I(t);
    },
    m(r, i) {
      w(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = ne(
        /*p*/
        r[38].index || 0
      ) + "") && R(n, t);
    },
    d(r) {
      r && y(n);
    }
  };
}
function bo(e) {
  let t = ne(
    /*p*/
    e[38].index || 0
  ) + "", n, r, i = ne(
    /*p*/
    e[38].length
  ) + "", s;
  return {
    c() {
      n = I(t), r = I("/"), s = I(i);
    },
    m(o, a) {
      w(o, n, a), w(o, r, a), w(o, s, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && t !== (t = ne(
        /*p*/
        o[38].index || 0
      ) + "") && R(n, t), a[0] & /*progress*/
      128 && i !== (i = ne(
        /*p*/
        o[38].length
      ) + "") && R(s, i);
    },
    d(o) {
      o && (y(n), y(r), y(s));
    }
  };
}
function Jt(e) {
  let t, n = (
    /*p*/
    e[38].index != null && Qt(e)
  );
  return {
    c() {
      n && n.c(), t = _e();
    },
    m(r, i) {
      n && n.m(r, i), w(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].index != null ? n ? n.p(r, i) : (n = Qt(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && y(t), n && n.d(r);
    }
  };
}
function Yt(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), r, i;
  return {
    c() {
      t = I(
        /*formatted_timer*/
        e[20]
      ), r = I(n), i = I("s");
    },
    m(s, o) {
      w(s, t, o), w(s, r, o), w(s, i, o);
    },
    p(s, o) {
      o[0] & /*formatted_timer*/
      1048576 && R(
        t,
        /*formatted_timer*/
        s[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && R(r, n);
    },
    d(s) {
      s && (y(t), y(r), y(i));
    }
  };
}
function po(e) {
  let t, n;
  return t = new Qs({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      Ys(t.$$.fragment);
    },
    m(r, i) {
      ro(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      r[8] === "default"), t.$set(s);
    },
    i(r) {
      n || (ue(t.$$.fragment, r), n = !0);
    },
    o(r) {
      fe(t.$$.fragment, r), n = !1;
    },
    d(r) {
      $s(t, r);
    }
  };
}
function go(e) {
  let t, n, r, i, s, o = `${/*last_progress_level*/
  e[15] * 100}%`, a = (
    /*progress*/
    e[7] != null && Kt(e)
  );
  return {
    c() {
      t = j("div"), n = j("div"), a && a.c(), r = V(), i = j("div"), s = j("div"), G(n, "class", "progress-level-inner svelte-14miwb5"), G(s, "class", "progress-bar svelte-14miwb5"), W(s, "width", o), G(i, "class", "progress-bar-wrap svelte-14miwb5"), G(t, "class", "progress-level svelte-14miwb5");
    },
    m(u, l) {
      w(u, t, l), Y(t, n), a && a.m(n, null), Y(t, r), Y(t, i), Y(i, s), e[30](s);
    },
    p(u, l) {
      /*progress*/
      u[7] != null ? a ? a.p(u, l) : (a = Kt(u), a.c(), a.m(n, null)) : a && (a.d(1), a = null), l[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      u[15] * 100}%`) && W(s, "width", o);
    },
    i: lt,
    o: lt,
    d(u) {
      u && y(t), a && a.d(), e[30](null);
    }
  };
}
function Kt(e) {
  let t, n = Re(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = rn(qt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = _e();
    },
    m(i, s) {
      for (let o = 0; o < r.length; o += 1)
        r[o] && r[o].m(i, s);
      w(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        n = Re(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = qt(i, n, o);
          r[o] ? r[o].p(a, s) : (r[o] = rn(a), r[o].c(), r[o].m(t.parentNode, t));
        }
        for (; o < r.length; o += 1)
          r[o].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && y(t), Un(r, i);
    }
  };
}
function $t(e) {
  let t, n, r, i, s = (
    /*i*/
    e[40] !== 0 && vo()
  ), o = (
    /*p*/
    e[38].desc != null && en(e)
  ), a = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && tn()
  ), u = (
    /*progress_level*/
    e[14] != null && nn(e)
  );
  return {
    c() {
      s && s.c(), t = V(), o && o.c(), n = V(), a && a.c(), r = V(), u && u.c(), i = _e();
    },
    m(l, f) {
      s && s.m(l, f), w(l, t, f), o && o.m(l, f), w(l, n, f), a && a.m(l, f), w(l, r, f), u && u.m(l, f), w(l, i, f);
    },
    p(l, f) {
      /*p*/
      l[38].desc != null ? o ? o.p(l, f) : (o = en(l), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null), /*p*/
      l[38].desc != null && /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[40]
      ] != null ? a || (a = tn(), a.c(), a.m(r.parentNode, r)) : a && (a.d(1), a = null), /*progress_level*/
      l[14] != null ? u ? u.p(l, f) : (u = nn(l), u.c(), u.m(i.parentNode, i)) : u && (u.d(1), u = null);
    },
    d(l) {
      l && (y(t), y(n), y(r), y(i)), s && s.d(l), o && o.d(l), a && a.d(l), u && u.d(l);
    }
  };
}
function vo(e) {
  let t;
  return {
    c() {
      t = I(" /");
    },
    m(n, r) {
      w(n, t, r);
    },
    d(n) {
      n && y(t);
    }
  };
}
function en(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = I(t);
    },
    m(r, i) {
      w(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[38].desc + "") && R(n, t);
    },
    d(r) {
      r && y(n);
    }
  };
}
function tn(e) {
  let t;
  return {
    c() {
      t = I("-");
    },
    m(n, r) {
      w(n, t, r);
    },
    d(n) {
      n && y(t);
    }
  };
}
function nn(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, r;
  return {
    c() {
      n = I(t), r = I("%");
    },
    m(i, s) {
      w(i, n, s), w(i, r, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && R(n, t);
    },
    d(i) {
      i && (y(n), y(r));
    }
  };
}
function rn(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && $t(e)
  );
  return {
    c() {
      n && n.c(), t = _e();
    },
    m(r, i) {
      n && n.m(r, i), w(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].desc != null || /*progress_level*/
      r[14] && /*progress_level*/
      r[14][
        /*i*/
        r[40]
      ] != null ? n ? n.p(r, i) : (n = $t(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && y(t), n && n.d(r);
    }
  };
}
function sn(e) {
  let t, n;
  return {
    c() {
      t = j("p"), n = I(
        /*loading_text*/
        e[9]
      ), G(t, "class", "loading svelte-14miwb5");
    },
    m(r, i) {
      w(r, t, i), Y(t, n);
    },
    p(r, i) {
      i[0] & /*loading_text*/
      512 && R(
        n,
        /*loading_text*/
        r[9]
      );
    },
    d(r) {
      r && y(t);
    }
  };
}
function Eo(e) {
  let t, n, r, i, s;
  const o = [fo, uo], a = [];
  function u(l, f) {
    return (
      /*status*/
      l[4] === "pending" ? 0 : (
        /*status*/
        l[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = u(e)) && (r = a[n] = o[n](e)), {
    c() {
      t = j("div"), r && r.c(), G(t, "class", i = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-14miwb5"), M(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), M(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), M(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), M(
        t,
        "border",
        /*border*/
        e[12]
      ), W(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), W(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(l, f) {
      w(l, t, f), ~n && a[n].m(t, null), e[31](t), s = !0;
    },
    p(l, f) {
      let h = n;
      n = u(l), n === h ? ~n && a[n].p(l, f) : (r && (Gn(), fe(a[h], 1, 1, () => {
        a[h] = null;
      }), Fn()), ~n ? (r = a[n], r ? r.p(l, f) : (r = a[n] = o[n](l), r.c()), ue(r, 1), r.m(t, null)) : r = null), (!s || f[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-14miwb5")) && G(t, "class", i), (!s || f[0] & /*variant, show_progress, status, show_progress*/
      336) && M(t, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), (!s || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && M(
        t,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), (!s || f[0] & /*variant, show_progress, status*/
      336) && M(
        t,
        "generating",
        /*status*/
        l[4] === "generating"
      ), (!s || f[0] & /*variant, show_progress, border*/
      4416) && M(
        t,
        "border",
        /*border*/
        l[12]
      ), f[0] & /*absolute*/
      1024 && W(
        t,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && W(
        t,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(l) {
      s || (ue(r), s = !0);
    },
    o(l) {
      fe(r), s = !1;
    },
    d(l) {
      l && y(t), ~n && a[n].d(), e[31](null);
    }
  };
}
let Se = [], We = !1;
async function yo(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (Se.push(e), !We)
      We = !0;
    else
      return;
    await oo(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let r = 0; r < Se.length; r++) {
        const s = Se[r].getBoundingClientRect();
        (r === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = r);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), We = !1, Se = [];
    });
  }
}
function wo(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { i18n: o } = t, { eta: a = null } = t, { queue: u = !1 } = t, { queue_position: l } = t, { queue_size: f } = t, { status: h } = t, { scroll_to_output: c = !1 } = t, { timer: _ = !0 } = t, { show_progress: m = "full" } = t, { message: b = null } = t, { progress: v = null } = t, { variant: P = "default" } = t, { loading_text: x = "Loading..." } = t, { absolute: d = !0 } = t, { translucent: E = !1 } = t, { border: p = !1 } = t, { autoscroll: F } = t, U, T = !1, Be = 0, Q = 0, Ge = null, bt = 0, J = null, me, X = null, pt = !0;
  const Xn = () => {
    n(25, Be = performance.now()), n(26, Q = 0), T = !0, gt();
  };
  function gt() {
    requestAnimationFrame(() => {
      n(26, Q = (performance.now() - Be) / 1e3), T && gt();
    });
  }
  function vt() {
    n(26, Q = 0), T && (T = !1);
  }
  ao(() => {
    T && vt();
  });
  let Et = null;
  function zn(g) {
    Xt[g ? "unshift" : "push"](() => {
      X = g, n(16, X), n(7, v), n(14, J), n(15, me);
    });
  }
  function qn(g) {
    Xt[g ? "unshift" : "push"](() => {
      U = g, n(13, U);
    });
  }
  return e.$$set = (g) => {
    "i18n" in g && n(1, o = g.i18n), "eta" in g && n(0, a = g.eta), "queue" in g && n(21, u = g.queue), "queue_position" in g && n(2, l = g.queue_position), "queue_size" in g && n(3, f = g.queue_size), "status" in g && n(4, h = g.status), "scroll_to_output" in g && n(22, c = g.scroll_to_output), "timer" in g && n(5, _ = g.timer), "show_progress" in g && n(6, m = g.show_progress), "message" in g && n(23, b = g.message), "progress" in g && n(7, v = g.progress), "variant" in g && n(8, P = g.variant), "loading_text" in g && n(9, x = g.loading_text), "absolute" in g && n(10, d = g.absolute), "translucent" in g && n(11, E = g.translucent), "border" in g && n(12, p = g.border), "autoscroll" in g && n(24, F = g.autoscroll), "$$scope" in g && n(28, s = g.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (a === null ? n(0, a = Ge) : u && n(0, a = (performance.now() - Be) / 1e3 + a), a != null && (n(19, Et = a.toFixed(1)), n(27, Ge = a))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, bt = a === null || a <= 0 || !Q ? null : Math.min(Q / a, 1)), e.$$.dirty[0] & /*progress*/
    128 && v != null && n(18, pt = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? n(14, J = v.map((g) => {
      if (g.index != null && g.length != null)
        return g.index / g.length;
      if (g.progress != null)
        return g.progress;
    })) : n(14, J = null), J ? (n(15, me = J[J.length - 1]), X && (me === 0 ? n(16, X.style.transition = "0", X) : n(16, X.style.transition = "150ms", X))) : n(15, me = void 0)), e.$$.dirty[0] & /*status*/
    16 && (h === "pending" ? Xn() : vt()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && U && c && (h === "pending" || h === "complete") && yo(U, F), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, r = Q.toFixed(1));
  }, [
    a,
    o,
    l,
    f,
    h,
    _,
    m,
    v,
    P,
    x,
    d,
    E,
    p,
    U,
    J,
    me,
    X,
    bt,
    pt,
    Et,
    r,
    u,
    c,
    b,
    F,
    Be,
    Q,
    Ge,
    s,
    i,
    zn,
    qn
  ];
}
class To extends Js {
  constructor(t) {
    super(), no(
      this,
      t,
      wo,
      Eo,
      io,
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
var xo = function() {
  var e = this, t = /{[A-Z_]+[0-9]*}/ig, n = {
    URL: "((?:(?:[a-z][a-z\\d+\\-.]*:\\/{2}(?:(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})+|[0-9.]+|\\[[a-z0-9.]+:[a-z0-9.]+:[a-z0-9.:]+\\])(?::\\d*)?(?:\\/(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})*)*(?:\\?(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?(?:#(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?)|(?:www\\.(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})+(?::\\d*)?(?:\\/(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})*)*(?:\\?(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?(?:#(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?)))",
    LINK: `([a-z0-9-./]+[^"' ]*)`,
    EMAIL: "((?:[\\w!#$%&'*+-/=?^`{|}~]+.)*(?:[\\w!#$%'*+-/=?^`{|}~]|&)+@(?:(?:(?:(?:(?:[a-z0-9]{1}[a-z0-9-]{0,62}[a-z0-9]{1})|[a-z]).)+[a-z]{2,6})|(?:\\d{1,3}.){3}\\d{1,3}(?::\\d{1,5})?))",
    TEXT: "(.*?)",
    SIMPLETEXT: "([a-zA-Z0-9-+.,_ ]+)",
    INTTEXT: "([a-zA-Z0-9-+,_. ]+)",
    IDENTIFIER: "([a-zA-Z0-9-_]+)",
    COLOR: "([a-z]+|#[0-9abcdef]+)",
    NUMBER: "([0-9]+)"
  }, r = [], i = [], s = [], o = [], a = function(f) {
    var h = f.match(t), c = h.length, _ = 0, m = "";
    if (c <= 0)
      return new RegExp(l(f), "g");
    for (; _ < c; _ += 1) {
      var b = h[_].replace(/[{}0-9]/g, "");
      n[b] && (m += l(f.substr(0, f.indexOf(h[_]))) + n[b], f = f.substr(f.indexOf(h[_]) + h[_].length));
    }
    return m += l(f), new RegExp(m, "gi");
  }, u = function(f) {
    var h = f.match(t), c = h.length, _ = 0, m = "", b = {}, v = 0;
    if (c <= 0)
      return f;
    for (; _ < c; _ += 1) {
      var P = h[_].replace(/[{}0-9]/g, ""), x;
      b[h[_]] ? x = b[h[_]] : (v += 1, x = v, b[h[_]] = x), n[P] && (m += f.substr(0, f.indexOf(h[_])) + "$" + x, f = f.substr(f.indexOf(h[_]) + h[_].length));
    }
    return m += f, m;
  };
  e.addBBCode = function(f, h) {
    r.push(a(f)), i.push(u(h)), s.push(a(h)), o.push(u(f));
  }, e.bbcodeToHtml = function(f) {
    for (var h = r.length, c = 0; c < h; c += 1)
      f = f.replace(r[c], i[c]);
    return f;
  }, e.htmlToBBCode = function(f) {
    for (var h = s.length, c = 0; c < h; c += 1)
      f = f.replace(s[c], o[c]);
    return f;
  };
  function l(f, h) {
    return (f + "").replace(new RegExp("[.\\\\+*?\\[\\^\\]$(){}=!<>|:\\" + (h || "") + "-]", "g"), "\\$&");
  }
  e.addBBCode("[b]{TEXT}[/b]", "<strong>{TEXT}</strong>"), e.addBBCode("[i]{TEXT}[/i]", "<em>{TEXT}</em>"), e.addBBCode("[u]{TEXT}[/u]", '<span style="text-decoration:underline;">{TEXT}</span>'), e.addBBCode("[s]{TEXT}[/s]", '<span style="text-decoration:line-through;">{TEXT}</span>'), e.addBBCode("[color={COLOR}]{TEXT}[/color]", '<span style="color:{COLOR}">{TEXT}</span>');
}, Bo = new xo();
const {
  HtmlTag: Ho,
  SvelteComponent: Ao,
  append: on,
  assign: So,
  attr: q,
  binding_callbacks: Po,
  check_outros: No,
  create_component: _t,
  destroy_component: mt,
  detach: Ee,
  element: an,
  empty: Io,
  flush: O,
  get_spread_object: Co,
  get_spread_update: Lo,
  group_outros: Oo,
  init: Mo,
  insert: ye,
  listen: Qe,
  mount_component: dt,
  run_all: Ro,
  safe_not_equal: Do,
  set_data: Vn,
  space: ln,
  text: jn,
  toggle_class: Je,
  transition_in: re,
  transition_out: pe
} = window.__gradio__svelte__internal, { tick: Ye } = window.__gradio__svelte__internal;
function un(e) {
  let t, n;
  const r = [
    { autoscroll: (
      /*gradio*/
      e[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      e[1].i18n
    ) },
    /*loading_status*/
    e[9]
  ];
  let i = {};
  for (let s = 0; s < r.length; s += 1)
    i = So(i, r[s]);
  return t = new To({ props: i }), {
    c() {
      _t(t.$$.fragment);
    },
    m(s, o) {
      dt(t, s, o), n = !0;
    },
    p(s, o) {
      const a = o & /*gradio, loading_status*/
      514 ? Lo(r, [
        o & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          s[1].autoscroll
        ) },
        o & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          s[1].i18n
        ) },
        o & /*loading_status*/
        512 && Co(
          /*loading_status*/
          s[9]
        )
      ]) : {};
      t.$set(a);
    },
    i(s) {
      n || (re(t.$$.fragment, s), n = !0);
    },
    o(s) {
      pe(t.$$.fragment, s), n = !1;
    },
    d(s) {
      mt(t, s);
    }
  };
}
function ko(e) {
  let t;
  return {
    c() {
      t = jn(
        /*label*/
        e[2]
      );
    },
    m(n, r) {
      ye(n, t, r);
    },
    p(n, r) {
      r & /*label*/
      4 && Vn(
        t,
        /*label*/
        n[2]
      );
    },
    d(n) {
      n && Ee(t);
    }
  };
}
function Fo(e) {
  let t, n;
  return {
    c() {
      t = new Ho(!1), n = Io(), t.a = n;
    },
    m(r, i) {
      t.m(
        /*_value*/
        e[13],
        r,
        i
      ), ye(r, n, i);
    },
    p(r, i) {
      i & /*_value*/
      8192 && t.p(
        /*_value*/
        r[13]
      );
    },
    d(r) {
      r && (Ee(n), t.d());
    }
  };
}
function Uo(e) {
  let t;
  return {
    c() {
      t = jn(
        /*value*/
        e[0]
      );
    },
    m(n, r) {
      ye(n, t, r);
    },
    p(n, r) {
      r & /*value*/
      1 && Vn(
        t,
        /*value*/
        n[0]
      );
    },
    d(n) {
      n && Ee(t);
    }
  };
}
function Go(e) {
  let t, n, r, i, s, o, a, u, l, f = (
    /*loading_status*/
    e[9] && un(e)
  );
  r = new zr({
    props: {
      show_label: (
        /*show_label*/
        e[6]
      ),
      info: void 0,
      $$slots: { default: [ko] },
      $$scope: { ctx: e }
    }
  });
  function h(m, b) {
    return (
      /*is_being_edited*/
      m[12] ? Uo : Fo
    );
  }
  let c = h(e), _ = c(e);
  return {
    c() {
      f && f.c(), t = ln(), n = an("label"), _t(r.$$.fragment), i = ln(), s = an("div"), _.c(), q(s, "data-testid", "textbox"), q(s, "contenteditable", "true"), q(s, "class", "text-container svelte-elvujf"), q(s, "role", "textbox"), q(s, "tabindex", "0"), q(s, "dir", o = /*rtl*/
      e[11] ? "rtl" : "ltr"), Je(
        s,
        "disabled",
        /*mode*/
        e[10] === "static"
      ), q(n, "class", "svelte-elvujf"), Je(n, "container", jo);
    },
    m(m, b) {
      f && f.m(m, b), ye(m, t, b), ye(m, n, b), dt(r, n, null), on(n, i), on(n, s), _.m(s, null), e[19](s), a = !0, u || (l = [
        Qe(
          s,
          "keypress",
          /*handle_keypress*/
          e[17]
        ),
        Qe(
          s,
          "blur",
          /*handle_blur*/
          e[15]
        ),
        Qe(
          s,
          "focus",
          /*handle_focus*/
          e[16]
        )
      ], u = !0);
    },
    p(m, b) {
      /*loading_status*/
      m[9] ? f ? (f.p(m, b), b & /*loading_status*/
      512 && re(f, 1)) : (f = un(m), f.c(), re(f, 1), f.m(t.parentNode, t)) : f && (Oo(), pe(f, 1, 1, () => {
        f = null;
      }), No());
      const v = {};
      b & /*show_label*/
      64 && (v.show_label = /*show_label*/
      m[6]), b & /*$$scope, label*/
      2097156 && (v.$$scope = { dirty: b, ctx: m }), r.$set(v), c === (c = h(m)) && _ ? _.p(m, b) : (_.d(1), _ = c(m), _ && (_.c(), _.m(s, null))), (!a || b & /*rtl*/
      2048 && o !== (o = /*rtl*/
      m[11] ? "rtl" : "ltr")) && q(s, "dir", o), (!a || b & /*mode*/
      1024) && Je(
        s,
        "disabled",
        /*mode*/
        m[10] === "static"
      );
    },
    i(m) {
      a || (re(f), re(r.$$.fragment, m), a = !0);
    },
    o(m) {
      pe(f), pe(r.$$.fragment, m), a = !1;
    },
    d(m) {
      m && (Ee(t), Ee(n)), f && f.d(m), mt(r), _.d(), e[19](null), u = !1, Ro(l);
    }
  };
}
function Vo(e) {
  let t, n;
  return t = new lr({
    props: {
      visible: (
        /*visible*/
        e[5]
      ),
      elem_id: (
        /*elem_id*/
        e[3]
      ),
      elem_classes: (
        /*elem_classes*/
        e[4]
      ),
      scale: (
        /*scale*/
        e[7]
      ),
      min_width: (
        /*min_width*/
        e[8]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [Go] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      _t(t.$$.fragment);
    },
    m(r, i) {
      dt(t, r, i), n = !0;
    },
    p(r, [i]) {
      const s = {};
      i & /*visible*/
      32 && (s.visible = /*visible*/
      r[5]), i & /*elem_id*/
      8 && (s.elem_id = /*elem_id*/
      r[3]), i & /*elem_classes*/
      16 && (s.elem_classes = /*elem_classes*/
      r[4]), i & /*scale*/
      128 && (s.scale = /*scale*/
      r[7]), i & /*min_width*/
      256 && (s.min_width = /*min_width*/
      r[8]), i & /*$$scope, rtl, el, mode, value, is_being_edited, _value, show_label, label, gradio, loading_status*/
      2129479 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (re(t.$$.fragment, r), n = !0);
    },
    o(r) {
      pe(t.$$.fragment, r), n = !1;
    },
    d(r) {
      mt(t, r);
    }
  };
}
const jo = !0;
function Xo(e, t, n) {
  let { gradio: r } = t, { label: i = "Textbox" } = t, { elem_id: s = "" } = t, { elem_classes: o = [] } = t, { visible: a = !0 } = t, { value: u = "" } = t, { show_label: l } = t, { scale: f = null } = t, { min_width: h = void 0 } = t, { loading_status: c = void 0 } = t, { value_is_output: _ = !1 } = t, { mode: m } = t, { rtl: b = !1 } = t, v = !1, P = "";
  async function x() {
    await Ye(), m !== "static" && (n(0, u = E.innerText), n(12, v = !1), n(14, E.innerText = "", E));
  }
  async function d() {
    if (await Ye(), m === "static") {
      E.blur();
      return;
    }
    n(12, v = !0);
  }
  let E;
  function p() {
    r.dispatch("change"), _ || r.dispatch("input");
  }
  async function F(T) {
    await Ye(), T.key === "Enter" && (T.preventDefault(), r.dispatch("submit"));
  }
  function U(T) {
    Po[T ? "unshift" : "push"](() => {
      E = T, n(14, E);
    });
  }
  return e.$$set = (T) => {
    "gradio" in T && n(1, r = T.gradio), "label" in T && n(2, i = T.label), "elem_id" in T && n(3, s = T.elem_id), "elem_classes" in T && n(4, o = T.elem_classes), "visible" in T && n(5, a = T.visible), "value" in T && n(0, u = T.value), "show_label" in T && n(6, l = T.show_label), "scale" in T && n(7, f = T.scale), "min_width" in T && n(8, h = T.min_width), "loading_status" in T && n(9, c = T.loading_status), "value_is_output" in T && n(18, _ = T.value_is_output), "mode" in T && n(10, m = T.mode), "rtl" in T && n(11, b = T.rtl);
  }, e.$$.update = () => {
    e.$$.dirty & /*value*/
    1 && u === null && n(0, u = ""), e.$$.dirty & /*value*/
    1 && n(13, P = Bo.bbcodeToHtml(u || "")), e.$$.dirty & /*value*/
    1 && p();
  }, [
    u,
    r,
    i,
    s,
    o,
    a,
    l,
    f,
    h,
    c,
    m,
    b,
    v,
    P,
    E,
    x,
    d,
    F,
    _,
    U
  ];
}
class zo extends Ao {
  constructor(t) {
    super(), Mo(this, t, Xo, Vo, Do, {
      gradio: 1,
      label: 2,
      elem_id: 3,
      elem_classes: 4,
      visible: 5,
      value: 0,
      show_label: 6,
      scale: 7,
      min_width: 8,
      loading_status: 9,
      value_is_output: 18,
      mode: 10,
      rtl: 11
    });
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(t) {
    this.$$set({ gradio: t }), O();
  }
  get label() {
    return this.$$.ctx[2];
  }
  set label(t) {
    this.$$set({ label: t }), O();
  }
  get elem_id() {
    return this.$$.ctx[3];
  }
  set elem_id(t) {
    this.$$set({ elem_id: t }), O();
  }
  get elem_classes() {
    return this.$$.ctx[4];
  }
  set elem_classes(t) {
    this.$$set({ elem_classes: t }), O();
  }
  get visible() {
    return this.$$.ctx[5];
  }
  set visible(t) {
    this.$$set({ visible: t }), O();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(t) {
    this.$$set({ value: t }), O();
  }
  get show_label() {
    return this.$$.ctx[6];
  }
  set show_label(t) {
    this.$$set({ show_label: t }), O();
  }
  get scale() {
    return this.$$.ctx[7];
  }
  set scale(t) {
    this.$$set({ scale: t }), O();
  }
  get min_width() {
    return this.$$.ctx[8];
  }
  set min_width(t) {
    this.$$set({ min_width: t }), O();
  }
  get loading_status() {
    return this.$$.ctx[9];
  }
  set loading_status(t) {
    this.$$set({ loading_status: t }), O();
  }
  get value_is_output() {
    return this.$$.ctx[18];
  }
  set value_is_output(t) {
    this.$$set({ value_is_output: t }), O();
  }
  get mode() {
    return this.$$.ctx[10];
  }
  set mode(t) {
    this.$$set({ mode: t }), O();
  }
  get rtl() {
    return this.$$.ctx[11];
  }
  set rtl(t) {
    this.$$set({ rtl: t }), O();
  }
}
export {
  zo as default
};
