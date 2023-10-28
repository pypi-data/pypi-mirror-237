const {
  SvelteComponent: Xn,
  assign: qn,
  create_slot: zn,
  detach: Zn,
  element: Wn,
  get_all_dirty_from_scope: Qn,
  get_slot_changes: Jn,
  get_spread_update: Yn,
  init: Kn,
  insert: $n,
  safe_not_equal: er,
  set_dynamic_element_data: gt,
  set_style: O,
  toggle_class: X,
  transition_in: un,
  transition_out: fn,
  update_slot_base: tr
} = window.__gradio__svelte__internal;
function nr(e) {
  let t, n, r;
  const i = (
    /*#slots*/
    e[17].default
  ), s = zn(
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
  ], l = {};
  for (let u = 0; u < o.length; u += 1)
    l = qn(l, o[u]);
  return {
    c() {
      t = Wn(
        /*tag*/
        e[14]
      ), s && s.c(), gt(
        /*tag*/
        e[14]
      )(t, l), X(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), X(
        t,
        "padded",
        /*padding*/
        e[6]
      ), X(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), X(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), O(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), O(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), O(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), O(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), O(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), O(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), O(t, "border-width", "var(--block-border-width)");
    },
    m(u, a) {
      $n(u, t, a), s && s.m(t, null), r = !0;
    },
    p(u, a) {
      s && s.p && (!r || a & /*$$scope*/
      65536) && tr(
        s,
        i,
        u,
        /*$$scope*/
        u[16],
        r ? Jn(
          i,
          /*$$scope*/
          u[16],
          a,
          null
        ) : Qn(
          /*$$scope*/
          u[16]
        ),
        null
      ), gt(
        /*tag*/
        u[14]
      )(t, l = Yn(o, [
        (!r || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          u[7]
        ) },
        (!r || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          u[2]
        ) },
        (!r || a & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        u[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), X(
        t,
        "hidden",
        /*visible*/
        u[10] === !1
      ), X(
        t,
        "padded",
        /*padding*/
        u[6]
      ), X(
        t,
        "border_focus",
        /*border_mode*/
        u[5] === "focus"
      ), X(t, "hide-container", !/*explicit_call*/
      u[8] && !/*container*/
      u[9]), a & /*height*/
      1 && O(t, "height", typeof /*height*/
      u[0] == "number" ? (
        /*height*/
        u[0] + "px"
      ) : void 0), a & /*width*/
      2 && O(t, "width", typeof /*width*/
      u[1] == "number" ? `calc(min(${/*width*/
      u[1]}px, 100%))` : void 0), a & /*variant*/
      16 && O(
        t,
        "border-style",
        /*variant*/
        u[4]
      ), a & /*allow_overflow*/
      2048 && O(
        t,
        "overflow",
        /*allow_overflow*/
        u[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && O(
        t,
        "flex-grow",
        /*scale*/
        u[12]
      ), a & /*min_width*/
      8192 && O(t, "min-width", `calc(min(${/*min_width*/
      u[13]}px, 100%))`);
    },
    i(u) {
      r || (un(s, u), r = !0);
    },
    o(u) {
      fn(s, u), r = !1;
    },
    d(u) {
      u && Zn(t), s && s.d(u);
    }
  };
}
function rr(e) {
  let t, n = (
    /*tag*/
    e[14] && nr(e)
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
      t || (un(n, r), t = !0);
    },
    o(r) {
      fn(n, r), t = !1;
    },
    d(r) {
      n && n.d(r);
    }
  };
}
function ir(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { height: s = void 0 } = t, { width: o = void 0 } = t, { elem_id: l = "" } = t, { elem_classes: u = [] } = t, { variant: a = "solid" } = t, { border_mode: f = "base" } = t, { padding: c = !0 } = t, { type: h = "normal" } = t, { test_id: _ = void 0 } = t, { explicit_call: d = !1 } = t, { container: B = !0 } = t, { visible: E = !0 } = t, { allow_overflow: P = !0 } = t, { scale: S = null } = t, { min_width: m = 0 } = t, w = h === "fieldset" ? "fieldset" : "div";
  return e.$$set = (b) => {
    "height" in b && n(0, s = b.height), "width" in b && n(1, o = b.width), "elem_id" in b && n(2, l = b.elem_id), "elem_classes" in b && n(3, u = b.elem_classes), "variant" in b && n(4, a = b.variant), "border_mode" in b && n(5, f = b.border_mode), "padding" in b && n(6, c = b.padding), "type" in b && n(15, h = b.type), "test_id" in b && n(7, _ = b.test_id), "explicit_call" in b && n(8, d = b.explicit_call), "container" in b && n(9, B = b.container), "visible" in b && n(10, E = b.visible), "allow_overflow" in b && n(11, P = b.allow_overflow), "scale" in b && n(12, S = b.scale), "min_width" in b && n(13, m = b.min_width), "$$scope" in b && n(16, i = b.$$scope);
  }, [
    s,
    o,
    l,
    u,
    a,
    f,
    c,
    _,
    d,
    B,
    E,
    P,
    S,
    m,
    w,
    h,
    i,
    r
  ];
}
class sr extends Xn {
  constructor(t) {
    super(), Kn(this, t, ir, rr, er, {
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
  SvelteComponent: or,
  attr: lr,
  create_slot: ar,
  detach: ur,
  element: fr,
  get_all_dirty_from_scope: hr,
  get_slot_changes: cr,
  init: _r,
  insert: mr,
  safe_not_equal: dr,
  transition_in: br,
  transition_out: pr,
  update_slot_base: gr
} = window.__gradio__svelte__internal;
function vr(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[1].default
  ), i = ar(
    r,
    e,
    /*$$scope*/
    e[0],
    null
  );
  return {
    c() {
      t = fr("div"), i && i.c(), lr(t, "class", "svelte-1hnfib2");
    },
    m(s, o) {
      mr(s, t, o), i && i.m(t, null), n = !0;
    },
    p(s, [o]) {
      i && i.p && (!n || o & /*$$scope*/
      1) && gr(
        i,
        r,
        s,
        /*$$scope*/
        s[0],
        n ? cr(
          r,
          /*$$scope*/
          s[0],
          o,
          null
        ) : hr(
          /*$$scope*/
          s[0]
        ),
        null
      );
    },
    i(s) {
      n || (br(i, s), n = !0);
    },
    o(s) {
      pr(i, s), n = !1;
    },
    d(s) {
      s && ur(t), i && i.d(s);
    }
  };
}
function yr(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t;
  return e.$$set = (s) => {
    "$$scope" in s && n(0, i = s.$$scope);
  }, [i, r];
}
class Er extends or {
  constructor(t) {
    super(), _r(this, t, yr, vr, dr, {});
  }
}
const {
  SvelteComponent: wr,
  attr: vt,
  check_outros: Tr,
  create_component: Hr,
  create_slot: xr,
  destroy_component: Br,
  detach: Se,
  element: Sr,
  empty: Ar,
  get_all_dirty_from_scope: Pr,
  get_slot_changes: Nr,
  group_outros: Ir,
  init: Lr,
  insert: Ae,
  mount_component: Cr,
  safe_not_equal: Or,
  set_data: Mr,
  space: Rr,
  text: Dr,
  toggle_class: $,
  transition_in: be,
  transition_out: Pe,
  update_slot_base: Ur
} = window.__gradio__svelte__internal;
function yt(e) {
  let t, n;
  return t = new Er({
    props: {
      $$slots: { default: [Gr] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Hr(t.$$.fragment);
    },
    m(r, i) {
      Cr(t, r, i), n = !0;
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
      Pe(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Br(t, r);
    }
  };
}
function Gr(e) {
  let t;
  return {
    c() {
      t = Dr(
        /*info*/
        e[1]
      );
    },
    m(n, r) {
      Ae(n, t, r);
    },
    p(n, r) {
      r & /*info*/
      2 && Mr(
        t,
        /*info*/
        n[1]
      );
    },
    d(n) {
      n && Se(t);
    }
  };
}
function kr(e) {
  let t, n, r, i;
  const s = (
    /*#slots*/
    e[2].default
  ), o = xr(
    s,
    e,
    /*$$scope*/
    e[3],
    null
  );
  let l = (
    /*info*/
    e[1] && yt(e)
  );
  return {
    c() {
      t = Sr("span"), o && o.c(), n = Rr(), l && l.c(), r = Ar(), vt(t, "data-testid", "block-info"), vt(t, "class", "svelte-22c38v"), $(t, "sr-only", !/*show_label*/
      e[0]), $(t, "hide", !/*show_label*/
      e[0]), $(
        t,
        "has-info",
        /*info*/
        e[1] != null
      );
    },
    m(u, a) {
      Ae(u, t, a), o && o.m(t, null), Ae(u, n, a), l && l.m(u, a), Ae(u, r, a), i = !0;
    },
    p(u, [a]) {
      o && o.p && (!i || a & /*$$scope*/
      8) && Ur(
        o,
        s,
        u,
        /*$$scope*/
        u[3],
        i ? Nr(
          s,
          /*$$scope*/
          u[3],
          a,
          null
        ) : Pr(
          /*$$scope*/
          u[3]
        ),
        null
      ), (!i || a & /*show_label*/
      1) && $(t, "sr-only", !/*show_label*/
      u[0]), (!i || a & /*show_label*/
      1) && $(t, "hide", !/*show_label*/
      u[0]), (!i || a & /*info*/
      2) && $(
        t,
        "has-info",
        /*info*/
        u[1] != null
      ), /*info*/
      u[1] ? l ? (l.p(u, a), a & /*info*/
      2 && be(l, 1)) : (l = yt(u), l.c(), be(l, 1), l.m(r.parentNode, r)) : l && (Ir(), Pe(l, 1, 1, () => {
        l = null;
      }), Tr());
    },
    i(u) {
      i || (be(o, u), be(l), i = !0);
    },
    o(u) {
      Pe(o, u), Pe(l), i = !1;
    },
    d(u) {
      u && (Se(t), Se(n), Se(r)), o && o.d(u), l && l.d(u);
    }
  };
}
function Fr(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { show_label: s = !0 } = t, { info: o = void 0 } = t;
  return e.$$set = (l) => {
    "show_label" in l && n(0, s = l.show_label), "info" in l && n(1, o = l.info), "$$scope" in l && n(3, i = l.$$scope);
  }, [s, o, r, i];
}
class Vr extends wr {
  constructor(t) {
    super(), Lr(this, t, Fr, kr, Or, { show_label: 0, info: 1 });
  }
}
const jr = [
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
], Et = {
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
jr.reduce(
  (e, { color: t, primary: n, secondary: r }) => ({
    ...e,
    [t]: {
      primary: Et[t][n],
      secondary: Et[t][r]
    }
  }),
  {}
);
function Y() {
}
function Xr(e) {
  return e();
}
function qr(e) {
  e.forEach(Xr);
}
function zr(e) {
  return typeof e == "function";
}
function Zr(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function hn(e, ...t) {
  if (e == null) {
    for (const r of t)
      r(void 0);
    return Y;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function Wr(e) {
  let t;
  return hn(e, (n) => t = n)(), t;
}
const cn = typeof window < "u";
let wt = cn ? () => window.performance.now() : () => Date.now(), _n = cn ? (e) => requestAnimationFrame(e) : Y;
const re = /* @__PURE__ */ new Set();
function mn(e) {
  re.forEach((t) => {
    t.c(e) || (re.delete(t), t.f());
  }), re.size !== 0 && _n(mn);
}
function Qr(e) {
  let t;
  return re.size === 0 && _n(mn), {
    promise: new Promise((n) => {
      re.add(t = { c: e, f: n });
    }),
    abort() {
      re.delete(t);
    }
  };
}
const ee = [];
function Jr(e, t) {
  return {
    subscribe: ye(e, t).subscribe
  };
}
function ye(e, t = Y) {
  let n;
  const r = /* @__PURE__ */ new Set();
  function i(l) {
    if (Zr(e, l) && (e = l, n)) {
      const u = !ee.length;
      for (const a of r)
        a[1](), ee.push(a, e);
      if (u) {
        for (let a = 0; a < ee.length; a += 2)
          ee[a][0](ee[a + 1]);
        ee.length = 0;
      }
    }
  }
  function s(l) {
    i(l(e));
  }
  function o(l, u = Y) {
    const a = [l, u];
    return r.add(a), r.size === 1 && (n = t(i, s) || Y), l(e), () => {
      r.delete(a), r.size === 0 && n && (n(), n = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function fe(e, t, n) {
  const r = !Array.isArray(e), i = r ? [e] : e;
  if (!i.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const s = t.length < 2;
  return Jr(n, (o, l) => {
    let u = !1;
    const a = [];
    let f = 0, c = Y;
    const h = () => {
      if (f)
        return;
      c();
      const d = t(r ? a[0] : a, o, l);
      s ? o(d) : c = zr(d) ? d : Y;
    }, _ = i.map(
      (d, B) => hn(
        d,
        (E) => {
          a[B] = E, f &= ~(1 << B), u && h();
        },
        () => {
          f |= 1 << B;
        }
      )
    );
    return u = !0, h(), function() {
      qr(_), c(), u = !1;
    };
  });
}
function Tt(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Ze(e, t, n, r) {
  if (typeof n == "number" || Tt(n)) {
    const i = r - n, s = (n - t) / (e.dt || 1 / 60), o = e.opts.stiffness * i, l = e.opts.damping * s, u = (o - l) * e.inv_mass, a = (s + u) * e.dt;
    return Math.abs(a) < e.opts.precision && Math.abs(i) < e.opts.precision ? r : (e.settled = !1, Tt(n) ? new Date(n.getTime() + a) : n + a);
  } else {
    if (Array.isArray(n))
      return n.map(
        (i, s) => Ze(e, t[s], n[s], r[s])
      );
    if (typeof n == "object") {
      const i = {};
      for (const s in n)
        i[s] = Ze(e, t[s], n[s], r[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function Ht(e, t = {}) {
  const n = ye(e), { stiffness: r = 0.15, damping: i = 0.8, precision: s = 0.01 } = t;
  let o, l, u, a = e, f = e, c = 1, h = 0, _ = !1;
  function d(E, P = {}) {
    f = E;
    const S = u = {};
    return e == null || P.hard || B.stiffness >= 1 && B.damping >= 1 ? (_ = !0, o = wt(), a = E, n.set(e = f), Promise.resolve()) : (P.soft && (h = 1 / ((P.soft === !0 ? 0.5 : +P.soft) * 60), c = 0), l || (o = wt(), _ = !1, l = Qr((m) => {
      if (_)
        return _ = !1, l = null, !1;
      c = Math.min(c + h, 1);
      const w = {
        inv_mass: c,
        opts: B,
        settled: !0,
        dt: (m - o) * 60 / 1e3
      }, b = Ze(w, a, e, f);
      return o = m, a = e, n.set(e = b), w.settled && (l = null), !w.settled;
    })), new Promise((m) => {
      l.promise.then(() => {
        S === u && m();
      });
    }));
  }
  const B = {
    set: d,
    update: (E, P) => d(E(f, e), P),
    subscribe: n.subscribe,
    stiffness: r,
    damping: i,
    precision: s
  };
  return B;
}
function Yr(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var Kr = function(t) {
  return $r(t) && !ei(t);
};
function $r(e) {
  return !!e && typeof e == "object";
}
function ei(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || ri(e);
}
var ti = typeof Symbol == "function" && Symbol.for, ni = ti ? Symbol.for("react.element") : 60103;
function ri(e) {
  return e.$$typeof === ni;
}
function ii(e) {
  return Array.isArray(e) ? [] : {};
}
function ge(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? ie(ii(e), e, t) : e;
}
function si(e, t, n) {
  return e.concat(t).map(function(r) {
    return ge(r, n);
  });
}
function oi(e, t) {
  if (!t.customMerge)
    return ie;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : ie;
}
function li(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function xt(e) {
  return Object.keys(e).concat(li(e));
}
function dn(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function ai(e, t) {
  return dn(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function ui(e, t, n) {
  var r = {};
  return n.isMergeableObject(e) && xt(e).forEach(function(i) {
    r[i] = ge(e[i], n);
  }), xt(t).forEach(function(i) {
    ai(e, i) || (dn(e, i) && n.isMergeableObject(t[i]) ? r[i] = oi(i, n)(e[i], t[i], n) : r[i] = ge(t[i], n));
  }), r;
}
function ie(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || si, n.isMergeableObject = n.isMergeableObject || Kr, n.cloneUnlessOtherwiseSpecified = ge;
  var r = Array.isArray(t), i = Array.isArray(e), s = r === i;
  return s ? r ? n.arrayMerge(e, t, n) : ui(e, t, n) : ge(t, n);
}
ie.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(r, i) {
    return ie(r, i, n);
  }, {});
};
var fi = ie, hi = fi;
const ci = /* @__PURE__ */ Yr(hi);
var We = function(e, t) {
  return We = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, r) {
    n.__proto__ = r;
  } || function(n, r) {
    for (var i in r)
      Object.prototype.hasOwnProperty.call(r, i) && (n[i] = r[i]);
  }, We(e, t);
};
function Me(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  We(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var A = function() {
  return A = Object.assign || function(t) {
    for (var n, r = 1, i = arguments.length; r < i; r++) {
      n = arguments[r];
      for (var s in n)
        Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s]);
    }
    return t;
  }, A.apply(this, arguments);
};
function ke(e, t, n) {
  if (n || arguments.length === 2)
    for (var r = 0, i = t.length, s; r < i; r++)
      (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)), s[r] = t[r]);
  return e.concat(s || Array.prototype.slice.call(t));
}
var T;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(T || (T = {}));
var N;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(N || (N = {}));
var se;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(se || (se = {}));
function Bt(e) {
  return e.type === N.literal;
}
function _i(e) {
  return e.type === N.argument;
}
function bn(e) {
  return e.type === N.number;
}
function pn(e) {
  return e.type === N.date;
}
function gn(e) {
  return e.type === N.time;
}
function vn(e) {
  return e.type === N.select;
}
function yn(e) {
  return e.type === N.plural;
}
function mi(e) {
  return e.type === N.pound;
}
function En(e) {
  return e.type === N.tag;
}
function wn(e) {
  return !!(e && typeof e == "object" && e.type === se.number);
}
function Qe(e) {
  return !!(e && typeof e == "object" && e.type === se.dateTime);
}
var Tn = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, di = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function bi(e) {
  var t = {};
  return e.replace(di, function(n) {
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
var pi = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function gi(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(pi).filter(function(h) {
    return h.length > 0;
  }), n = [], r = 0, i = t; r < i.length; r++) {
    var s = i[r], o = s.split("/");
    if (o.length === 0)
      throw new Error("Invalid number skeleton");
    for (var l = o[0], u = o.slice(1), a = 0, f = u; a < f.length; a++) {
      var c = f[a];
      if (c.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: l, options: u });
  }
  return n;
}
function vi(e) {
  return e.replace(/^(.*?)-/, "");
}
var St = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, Hn = /^(@+)?(\+|#+)?[rs]?$/g, yi = /(\*)(0+)|(#+)(0+)|(0+)/g, xn = /^(0+)$/;
function At(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(Hn, function(n, r, i) {
    return typeof i != "string" ? (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length) : i === "+" ? t.minimumSignificantDigits = r.length : r[0] === "#" ? t.maximumSignificantDigits = r.length : (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length + (typeof i == "string" ? i.length : 0)), "";
  }), t;
}
function Bn(e) {
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
function Ei(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !xn.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Pt(e) {
  var t = {}, n = Bn(e);
  return n || t;
}
function wi(e) {
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
        t.style = "unit", t.unit = vi(i.options[0]);
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
        t = A(A(A({}, t), { notation: "scientific" }), i.options.reduce(function(u, a) {
          return A(A({}, u), Pt(a));
        }, {}));
        continue;
      case "engineering":
        t = A(A(A({}, t), { notation: "engineering" }), i.options.reduce(function(u, a) {
          return A(A({}, u), Pt(a));
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
        i.options[0].replace(yi, function(u, a, f, c, h, _) {
          if (a)
            t.minimumIntegerDigits = f.length;
          else {
            if (c && h)
              throw new Error("We currently do not support maximum integer digits");
            if (_)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (xn.test(i.stem)) {
      t.minimumIntegerDigits = i.stem.length;
      continue;
    }
    if (St.test(i.stem)) {
      if (i.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      i.stem.replace(St, function(u, a, f, c, h, _) {
        return f === "*" ? t.minimumFractionDigits = a.length : c && c[0] === "#" ? t.maximumFractionDigits = c.length : h && _ ? (t.minimumFractionDigits = h.length, t.maximumFractionDigits = h.length + _.length) : (t.minimumFractionDigits = a.length, t.maximumFractionDigits = a.length), "";
      });
      var s = i.options[0];
      s === "w" ? t = A(A({}, t), { trailingZeroDisplay: "stripIfInteger" }) : s && (t = A(A({}, t), At(s)));
      continue;
    }
    if (Hn.test(i.stem)) {
      t = A(A({}, t), At(i.stem));
      continue;
    }
    var o = Bn(i.stem);
    o && (t = A(A({}, t), o));
    var l = Ei(i.stem);
    l && (t = A(A({}, t), l));
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
function Ti(e, t) {
  for (var n = "", r = 0; r < e.length; r++) {
    var i = e.charAt(r);
    if (i === "j") {
      for (var s = 0; r + 1 < e.length && e.charAt(r + 1) === i; )
        s++, r++;
      var o = 1 + (s & 1), l = s < 2 ? 1 : 3 + (s >> 1), u = "a", a = Hi(t);
      for ((a == "H" || a == "k") && (l = 0); l-- > 0; )
        n += u;
      for (; o-- > 0; )
        n = a + n;
    } else
      i === "J" ? n += "H" : n += i;
  }
  return n;
}
function Hi(e) {
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
var Fe, xi = new RegExp("^".concat(Tn.source, "*")), Bi = new RegExp("".concat(Tn.source, "*$"));
function H(e, t) {
  return { start: e, end: t };
}
var Si = !!String.prototype.startsWith, Ai = !!String.fromCodePoint, Pi = !!Object.fromEntries, Ni = !!String.prototype.codePointAt, Ii = !!String.prototype.trimStart, Li = !!String.prototype.trimEnd, Ci = !!Number.isSafeInteger, Oi = Ci ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, Je = !0;
try {
  var Mi = An("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Je = ((Fe = Mi.exec("a")) === null || Fe === void 0 ? void 0 : Fe[0]) === "a";
} catch {
  Je = !1;
}
var Nt = Si ? (
  // Native
  function(t, n, r) {
    return t.startsWith(n, r);
  }
) : (
  // For IE11
  function(t, n, r) {
    return t.slice(r, r + n.length) === n;
  }
), Ye = Ai ? String.fromCodePoint : (
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
), It = (
  // native
  Pi ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, r = 0, i = t; r < i.length; r++) {
        var s = i[r], o = s[0], l = s[1];
        n[o] = l;
      }
      return n;
    }
  )
), Sn = Ni ? (
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
), Ri = Ii ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(xi, "");
  }
), Di = Li ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Bi, "");
  }
);
function An(e, t) {
  return new RegExp(e, t);
}
var Ke;
if (Je) {
  var Lt = An("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Ke = function(t, n) {
    var r;
    Lt.lastIndex = n;
    var i = Lt.exec(t);
    return (r = i[1]) !== null && r !== void 0 ? r : "";
  };
} else
  Ke = function(t, n) {
    for (var r = []; ; ) {
      var i = Sn(t, n);
      if (i === void 0 || Pn(i) || Fi(i))
        break;
      r.push(i), n += i >= 65536 ? 2 : 1;
    }
    return Ye.apply(void 0, r);
  };
var Ui = (
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
            var l = this.clonePosition();
            this.bump(), i.push({
              type: N.pound,
              location: H(l, this.clonePosition())
            });
          } else if (s === 60 && !this.ignoreTag && this.peek() === 47) {
            if (r)
              break;
            return this.error(T.UNMATCHED_CLOSING_TAG, H(this.clonePosition(), this.clonePosition()));
          } else if (s === 60 && !this.ignoreTag && $e(this.peek() || 0)) {
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
        var o = s.val, l = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !$e(this.char()))
            return this.error(T.INVALID_TAG, H(l, this.clonePosition()));
          var u = this.clonePosition(), a = this.parseTagName();
          return i !== a ? this.error(T.UNMATCHED_CLOSING_TAG, H(u, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: N.tag,
              value: i,
              children: o,
              location: H(r, this.clonePosition())
            },
            err: null
          } : this.error(T.INVALID_TAG, H(l, this.clonePosition())));
        } else
          return this.error(T.UNCLOSED_TAG, H(r, this.clonePosition()));
      } else
        return this.error(T.INVALID_TAG, H(r, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && ki(this.char()); )
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
        var l = this.tryParseLeftAngleBracket();
        if (l) {
          i += l;
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
      !Gi(this.peek() || 0)) ? (this.bump(), "<") : null;
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
      return Ye.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var r = this.char();
      return r === 60 || r === 123 || r === 35 && (n === "plural" || n === "selectordinal") || r === 125 && t > 0 ? null : (this.bump(), Ye(r));
    }, e.prototype.parseArgument = function(t, n) {
      var r = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(T.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(T.EMPTY_ARGUMENT, H(r, this.clonePosition()));
      var i = this.parseIdentifierIfPossible().value;
      if (!i)
        return this.error(T.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(T.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
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
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(T.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition())) : this.parseArgumentOptions(t, n, i, r);
        default:
          return this.error(T.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), r = Ke(this.message, n), i = n + r.length;
      this.bumpTo(i);
      var s = this.clonePosition(), o = H(t, s);
      return { value: r, location: o };
    }, e.prototype.parseArgumentOptions = function(t, n, r, i) {
      var s, o = this.clonePosition(), l = this.parseIdentifierIfPossible().value, u = this.clonePosition();
      switch (l) {
        case "":
          return this.error(T.EXPECT_ARGUMENT_TYPE, H(o, u));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var a = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), c = this.parseSimpleArgStyleIfPossible();
            if (c.err)
              return c;
            var h = Di(c.val);
            if (h.length === 0)
              return this.error(T.EXPECT_ARGUMENT_STYLE, H(this.clonePosition(), this.clonePosition()));
            var _ = H(f, this.clonePosition());
            a = { style: h, styleLocation: _ };
          }
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var B = H(i, this.clonePosition());
          if (a && Nt(a == null ? void 0 : a.style, "::", 0)) {
            var E = Ri(a.style.slice(2));
            if (l === "number") {
              var c = this.parseNumberSkeletonFromString(E, a.styleLocation);
              return c.err ? c : {
                val: { type: N.number, value: r, location: B, style: c.val },
                err: null
              };
            } else {
              if (E.length === 0)
                return this.error(T.EXPECT_DATE_TIME_SKELETON, B);
              var P = E;
              this.locale && (P = Ti(E, this.locale));
              var h = {
                type: se.dateTime,
                pattern: P,
                location: a.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? bi(P) : {}
              }, S = l === "date" ? N.date : N.time;
              return {
                val: { type: S, value: r, location: B, style: h },
                err: null
              };
            }
          }
          return {
            val: {
              type: l === "number" ? N.number : l === "date" ? N.date : N.time,
              value: r,
              location: B,
              style: (s = a == null ? void 0 : a.style) !== null && s !== void 0 ? s : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var m = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(T.EXPECT_SELECT_ARGUMENT_OPTIONS, H(m, A({}, m)));
          this.bumpSpace();
          var w = this.parseIdentifierIfPossible(), b = 0;
          if (l !== "select" && w.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(T.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, H(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var c = this.tryParseDecimalInteger(T.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, T.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (c.err)
              return c;
            this.bumpSpace(), w = this.parseIdentifierIfPossible(), b = c.val;
          }
          var g = this.tryParsePluralOrSelectOptions(t, l, n, w);
          if (g.err)
            return g;
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var V = H(i, this.clonePosition());
          return l === "select" ? {
            val: {
              type: N.select,
              value: r,
              options: It(g.val),
              location: V
            },
            err: null
          } : {
            val: {
              type: N.plural,
              value: r,
              options: It(g.val),
              offset: b,
              pluralType: l === "plural" ? "cardinal" : "ordinal",
              location: V
            },
            err: null
          };
        }
        default:
          return this.error(T.INVALID_ARGUMENT_TYPE, H(o, u));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(T.EXPECT_ARGUMENT_CLOSING_BRACE, H(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var r = this.char();
        switch (r) {
          case 39: {
            this.bump();
            var i = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(T.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, H(i, this.clonePosition()));
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
        r = gi(t);
      } catch {
        return this.error(T.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: se.number,
          tokens: r,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? wi(r) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, r, i) {
      for (var s, o = !1, l = [], u = /* @__PURE__ */ new Set(), a = i.value, f = i.location; ; ) {
        if (a.length === 0) {
          var c = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var h = this.tryParseDecimalInteger(T.EXPECT_PLURAL_ARGUMENT_SELECTOR, T.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (h.err)
              return h;
            f = H(c, this.clonePosition()), a = this.message.slice(c.offset, this.offset());
          } else
            break;
        }
        if (u.has(a))
          return this.error(n === "select" ? T.DUPLICATE_SELECT_ARGUMENT_SELECTOR : T.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        a === "other" && (o = !0), this.bumpSpace();
        var _ = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? T.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : T.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, H(this.clonePosition(), this.clonePosition()));
        var d = this.parseMessage(t + 1, n, r);
        if (d.err)
          return d;
        var B = this.tryParseArgumentClose(_);
        if (B.err)
          return B;
        l.push([
          a,
          {
            value: d.val,
            location: H(_, this.clonePosition())
          }
        ]), u.add(a), this.bumpSpace(), s = this.parseIdentifierIfPossible(), a = s.value, f = s.location;
      }
      return l.length === 0 ? this.error(n === "select" ? T.EXPECT_SELECT_ARGUMENT_SELECTOR : T.EXPECT_PLURAL_ARGUMENT_SELECTOR, H(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !o ? this.error(T.MISSING_OTHER_CLAUSE, H(this.clonePosition(), this.clonePosition())) : { val: l, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var r = 1, i = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (r = -1);
      for (var s = !1, o = 0; !this.isEOF(); ) {
        var l = this.char();
        if (l >= 48 && l <= 57)
          s = !0, o = o * 10 + (l - 48), this.bump();
        else
          break;
      }
      var u = H(i, this.clonePosition());
      return s ? (o *= r, Oi(o) ? { val: o, err: null } : this.error(n, u)) : this.error(t, u);
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
      if (Nt(this.message, t, this.offset())) {
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
      for (; !this.isEOF() && Pn(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), r = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return r ?? null;
    }, e;
  }()
);
function $e(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Gi(e) {
  return $e(e) || e === 47;
}
function ki(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function Pn(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function Fi(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function et(e) {
  e.forEach(function(t) {
    if (delete t.location, vn(t) || yn(t))
      for (var n in t.options)
        delete t.options[n].location, et(t.options[n].value);
    else
      bn(t) && wn(t.style) || (pn(t) || gn(t)) && Qe(t.style) ? delete t.style.location : En(t) && et(t.children);
  });
}
function Vi(e, t) {
  t === void 0 && (t = {}), t = A({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new Ui(e, t).parse();
  if (n.err) {
    var r = SyntaxError(T[n.err.kind]);
    throw r.location = n.err.location, r.originalMessage = n.err.message, r;
  }
  return t != null && t.captureLocation || et(n.val), n.val;
}
function Ve(e, t) {
  var n = t && t.cache ? t.cache : Wi, r = t && t.serializer ? t.serializer : Zi, i = t && t.strategy ? t.strategy : Xi;
  return i(e, {
    cache: n,
    serializer: r
  });
}
function ji(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function Nn(e, t, n, r) {
  var i = ji(r) ? r : n(r), s = t.get(i);
  return typeof s > "u" && (s = e.call(this, r), t.set(i, s)), s;
}
function In(e, t, n) {
  var r = Array.prototype.slice.call(arguments, 3), i = n(r), s = t.get(i);
  return typeof s > "u" && (s = e.apply(this, r), t.set(i, s)), s;
}
function ot(e, t, n, r, i) {
  return n.bind(t, e, r, i);
}
function Xi(e, t) {
  var n = e.length === 1 ? Nn : In;
  return ot(e, this, n, t.cache.create(), t.serializer);
}
function qi(e, t) {
  return ot(e, this, In, t.cache.create(), t.serializer);
}
function zi(e, t) {
  return ot(e, this, Nn, t.cache.create(), t.serializer);
}
var Zi = function() {
  return JSON.stringify(arguments);
};
function lt() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
lt.prototype.get = function(e) {
  return this.cache[e];
};
lt.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var Wi = {
  create: function() {
    return new lt();
  }
}, je = {
  variadic: qi,
  monadic: zi
}, oe;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(oe || (oe = {}));
var Re = (
  /** @class */
  function(e) {
    Me(t, e);
    function t(n, r, i) {
      var s = e.call(this, n) || this;
      return s.code = r, s.originalMessage = i, s;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), Ct = (
  /** @class */
  function(e) {
    Me(t, e);
    function t(n, r, i, s) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(r, '". Options are "').concat(Object.keys(i).join('", "'), '"'), oe.INVALID_VALUE, s) || this;
    }
    return t;
  }(Re)
), Qi = (
  /** @class */
  function(e) {
    Me(t, e);
    function t(n, r, i) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(r), oe.INVALID_VALUE, i) || this;
    }
    return t;
  }(Re)
), Ji = (
  /** @class */
  function(e) {
    Me(t, e);
    function t(n, r) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(r, '"'), oe.MISSING_VALUE, r) || this;
    }
    return t;
  }(Re)
), L;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(L || (L = {}));
function Yi(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var r = t[t.length - 1];
    return !r || r.type !== L.literal || n.type !== L.literal ? t.push(n) : r.value += n.value, t;
  }, []);
}
function Ki(e) {
  return typeof e == "function";
}
function Ne(e, t, n, r, i, s, o) {
  if (e.length === 1 && Bt(e[0]))
    return [
      {
        type: L.literal,
        value: e[0].value
      }
    ];
  for (var l = [], u = 0, a = e; u < a.length; u++) {
    var f = a[u];
    if (Bt(f)) {
      l.push({
        type: L.literal,
        value: f.value
      });
      continue;
    }
    if (mi(f)) {
      typeof s == "number" && l.push({
        type: L.literal,
        value: n.getNumberFormat(t).format(s)
      });
      continue;
    }
    var c = f.value;
    if (!(i && c in i))
      throw new Ji(c, o);
    var h = i[c];
    if (_i(f)) {
      (!h || typeof h == "string" || typeof h == "number") && (h = typeof h == "string" || typeof h == "number" ? String(h) : ""), l.push({
        type: typeof h == "string" ? L.literal : L.object,
        value: h
      });
      continue;
    }
    if (pn(f)) {
      var _ = typeof f.style == "string" ? r.date[f.style] : Qe(f.style) ? f.style.parsedOptions : void 0;
      l.push({
        type: L.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (gn(f)) {
      var _ = typeof f.style == "string" ? r.time[f.style] : Qe(f.style) ? f.style.parsedOptions : r.time.medium;
      l.push({
        type: L.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (bn(f)) {
      var _ = typeof f.style == "string" ? r.number[f.style] : wn(f.style) ? f.style.parsedOptions : void 0;
      _ && _.scale && (h = h * (_.scale || 1)), l.push({
        type: L.literal,
        value: n.getNumberFormat(t, _).format(h)
      });
      continue;
    }
    if (En(f)) {
      var d = f.children, B = f.value, E = i[B];
      if (!Ki(E))
        throw new Qi(B, "function", o);
      var P = Ne(d, t, n, r, i, s), S = E(P.map(function(b) {
        return b.value;
      }));
      Array.isArray(S) || (S = [S]), l.push.apply(l, S.map(function(b) {
        return {
          type: typeof b == "string" ? L.literal : L.object,
          value: b
        };
      }));
    }
    if (vn(f)) {
      var m = f.options[h] || f.options.other;
      if (!m)
        throw new Ct(f.value, h, Object.keys(f.options), o);
      l.push.apply(l, Ne(m.value, t, n, r, i));
      continue;
    }
    if (yn(f)) {
      var m = f.options["=".concat(h)];
      if (!m) {
        if (!Intl.PluralRules)
          throw new Re(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, oe.MISSING_INTL_API, o);
        var w = n.getPluralRules(t, { type: f.pluralType }).select(h - (f.offset || 0));
        m = f.options[w] || f.options.other;
      }
      if (!m)
        throw new Ct(f.value, h, Object.keys(f.options), o);
      l.push.apply(l, Ne(m.value, t, n, r, i, h - (f.offset || 0)));
      continue;
    }
  }
  return Yi(l);
}
function $i(e, t) {
  return t ? A(A(A({}, e || {}), t || {}), Object.keys(e).reduce(function(n, r) {
    return n[r] = A(A({}, e[r]), t[r] || {}), n;
  }, {})) : e;
}
function es(e, t) {
  return t ? Object.keys(e).reduce(function(n, r) {
    return n[r] = $i(e[r], t[r]), n;
  }, A({}, e)) : e;
}
function Xe(e) {
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
function ts(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Ve(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.NumberFormat).bind.apply(t, ke([void 0], n, !1)))();
    }, {
      cache: Xe(e.number),
      strategy: je.variadic
    }),
    getDateTimeFormat: Ve(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, ke([void 0], n, !1)))();
    }, {
      cache: Xe(e.dateTime),
      strategy: je.variadic
    }),
    getPluralRules: Ve(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.PluralRules).bind.apply(t, ke([void 0], n, !1)))();
    }, {
      cache: Xe(e.pluralRules),
      strategy: je.variadic
    })
  };
}
var ns = (
  /** @class */
  function() {
    function e(t, n, r, i) {
      var s = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(o) {
        var l = s.formatToParts(o);
        if (l.length === 1)
          return l[0].value;
        var u = l.reduce(function(a, f) {
          return !a.length || f.type !== L.literal || typeof a[a.length - 1] != "string" ? a.push(f.value) : a[a.length - 1] += f.value, a;
        }, []);
        return u.length <= 1 ? u[0] || "" : u;
      }, this.formatToParts = function(o) {
        return Ne(s.ast, s.locales, s.formatters, s.formats, o, void 0, s.message);
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
      this.formats = es(e.formats, r), this.formatters = i && i.formatters || ts(this.formatterCache);
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
    }, e.__parse = Vi, e.formats = {
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
function rs(e, t) {
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
const z = {}, is = (e, t, n) => n && (t in z || (z[t] = {}), e in z[t] || (z[t][e] = n), n), Ln = (e, t) => {
  if (t == null)
    return;
  if (t in z && e in z[t])
    return z[t][e];
  const n = De(t);
  for (let r = 0; r < n.length; r++) {
    const i = n[r], s = os(i, e);
    if (s)
      return is(e, t, s);
  }
};
let at;
const Ee = ye({});
function ss(e) {
  return at[e] || null;
}
function Cn(e) {
  return e in at;
}
function os(e, t) {
  if (!Cn(e))
    return null;
  const n = ss(e);
  return rs(n, t);
}
function ls(e) {
  if (e == null)
    return;
  const t = De(e);
  for (let n = 0; n < t.length; n++) {
    const r = t[n];
    if (Cn(r))
      return r;
  }
}
function as(e, ...t) {
  delete z[e], Ee.update((n) => (n[e] = ci.all([n[e] || {}, ...t]), n));
}
fe(
  [Ee],
  ([e]) => Object.keys(e)
);
Ee.subscribe((e) => at = e);
const Ie = {};
function us(e, t) {
  Ie[e].delete(t), Ie[e].size === 0 && delete Ie[e];
}
function On(e) {
  return Ie[e];
}
function fs(e) {
  return De(e).map((t) => {
    const n = On(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function tt(e) {
  return e == null ? !1 : De(e).some(
    (t) => {
      var n;
      return (n = On(t)) == null ? void 0 : n.size;
    }
  );
}
function hs(e, t) {
  return Promise.all(
    t.map((r) => (us(e, r), r().then((i) => i.default || i)))
  ).then((r) => as(e, ...r));
}
const de = {};
function Mn(e) {
  if (!tt(e))
    return e in de ? de[e] : Promise.resolve();
  const t = fs(e);
  return de[e] = Promise.all(
    t.map(
      ([n, r]) => hs(n, r)
    )
  ).then(() => {
    if (tt(e))
      return Mn(e);
    delete de[e];
  }), de[e];
}
const cs = {
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
}, _s = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: cs,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, ms = _s;
function le() {
  return ms;
}
const qe = ye(!1);
var ds = Object.defineProperty, bs = Object.defineProperties, ps = Object.getOwnPropertyDescriptors, Ot = Object.getOwnPropertySymbols, gs = Object.prototype.hasOwnProperty, vs = Object.prototype.propertyIsEnumerable, Mt = (e, t, n) => t in e ? ds(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, ys = (e, t) => {
  for (var n in t || (t = {}))
    gs.call(t, n) && Mt(e, n, t[n]);
  if (Ot)
    for (var n of Ot(t))
      vs.call(t, n) && Mt(e, n, t[n]);
  return e;
}, Es = (e, t) => bs(e, ps(t));
let nt;
const Le = ye(null);
function Rt(e) {
  return e.split("-").map((t, n, r) => r.slice(0, n + 1).join("-")).reverse();
}
function De(e, t = le().fallbackLocale) {
  const n = Rt(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Rt(t)])] : n;
}
function K() {
  return nt ?? void 0;
}
Le.subscribe((e) => {
  nt = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const ws = (e) => {
  if (e && ls(e) && tt(e)) {
    const { loadingDelay: t } = le();
    let n;
    return typeof window < "u" && K() != null && t ? n = window.setTimeout(
      () => qe.set(!0),
      t
    ) : qe.set(!0), Mn(e).then(() => {
      Le.set(e);
    }).finally(() => {
      clearTimeout(n), qe.set(!1);
    });
  }
  return Le.set(e);
}, we = Es(ys({}, Le), {
  set: ws
}), Ue = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (r) => {
    const i = JSON.stringify(r);
    return i in t ? t[i] : t[i] = e(r);
  };
};
var Ts = Object.defineProperty, Ce = Object.getOwnPropertySymbols, Rn = Object.prototype.hasOwnProperty, Dn = Object.prototype.propertyIsEnumerable, Dt = (e, t, n) => t in e ? Ts(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, ut = (e, t) => {
  for (var n in t || (t = {}))
    Rn.call(t, n) && Dt(e, n, t[n]);
  if (Ce)
    for (var n of Ce(t))
      Dn.call(t, n) && Dt(e, n, t[n]);
  return e;
}, he = (e, t) => {
  var n = {};
  for (var r in e)
    Rn.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
  if (e != null && Ce)
    for (var r of Ce(e))
      t.indexOf(r) < 0 && Dn.call(e, r) && (n[r] = e[r]);
  return n;
};
const ve = (e, t) => {
  const { formats: n } = le();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, Hs = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = he(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return r && (i = ve("number", r)), new Intl.NumberFormat(n, i);
  }
), xs = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = he(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return r ? i = ve("date", r) : Object.keys(i).length === 0 && (i = ve("date", "short")), new Intl.DateTimeFormat(n, i);
  }
), Bs = Ue(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = he(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return r ? i = ve("time", r) : Object.keys(i).length === 0 && (i = ve("time", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ss = (e = {}) => {
  var t = e, {
    locale: n = K()
  } = t, r = he(t, [
    "locale"
  ]);
  return Hs(ut({ locale: n }, r));
}, As = (e = {}) => {
  var t = e, {
    locale: n = K()
  } = t, r = he(t, [
    "locale"
  ]);
  return xs(ut({ locale: n }, r));
}, Ps = (e = {}) => {
  var t = e, {
    locale: n = K()
  } = t, r = he(t, [
    "locale"
  ]);
  return Bs(ut({ locale: n }, r));
}, Ns = Ue(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = K()) => new ns(e, t, le().formats, {
    ignoreTag: le().ignoreTag
  })
), Is = (e, t = {}) => {
  var n, r, i, s;
  let o = t;
  typeof e == "object" && (o = e, e = o.id);
  const {
    values: l,
    locale: u = K(),
    default: a
  } = o;
  if (u == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = Ln(e, u);
  if (!f)
    f = (s = (i = (r = (n = le()).handleMissingMessage) == null ? void 0 : r.call(n, { locale: u, id: e, defaultValue: a })) != null ? i : a) != null ? s : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!l)
    return f;
  let c = f;
  try {
    c = Ns(f, u).format(l);
  } catch (h) {
    h instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      h.message
    );
  }
  return c;
}, Ls = (e, t) => Ps(t).format(e), Cs = (e, t) => As(t).format(e), Os = (e, t) => Ss(t).format(e), Ms = (e, t = K()) => Ln(e, t), Rs = fe([we, Ee], () => Is);
fe([we], () => Ls);
fe([we], () => Cs);
fe([we], () => Os);
fe([we, Ee], () => Ms);
Wr(Rs);
function te(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let r = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + r;
}
const {
  SvelteComponent: Ds,
  append: D,
  attr: x,
  component_subscribe: Ut,
  detach: Us,
  element: Gs,
  init: ks,
  insert: Fs,
  noop: Gt,
  safe_not_equal: Vs,
  set_style: xe,
  svg_element: U,
  toggle_class: kt
} = window.__gradio__svelte__internal, { onMount: js } = window.__gradio__svelte__internal;
function Xs(e) {
  let t, n, r, i, s, o, l, u, a, f, c, h;
  return {
    c() {
      t = Gs("div"), n = U("svg"), r = U("g"), i = U("path"), s = U("path"), o = U("path"), l = U("path"), u = U("g"), a = U("path"), f = U("path"), c = U("path"), h = U("path"), x(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), x(i, "fill", "#FF7C00"), x(i, "fill-opacity", "0.4"), x(i, "class", "svelte-43sxxs"), x(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), x(s, "fill", "#FF7C00"), x(s, "class", "svelte-43sxxs"), x(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), x(o, "fill", "#FF7C00"), x(o, "fill-opacity", "0.4"), x(o, "class", "svelte-43sxxs"), x(l, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), x(l, "fill", "#FF7C00"), x(l, "class", "svelte-43sxxs"), xe(r, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), x(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), x(a, "fill", "#FF7C00"), x(a, "fill-opacity", "0.4"), x(a, "class", "svelte-43sxxs"), x(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), x(f, "fill", "#FF7C00"), x(f, "class", "svelte-43sxxs"), x(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), x(c, "fill", "#FF7C00"), x(c, "fill-opacity", "0.4"), x(c, "class", "svelte-43sxxs"), x(h, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), x(h, "fill", "#FF7C00"), x(h, "class", "svelte-43sxxs"), xe(u, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), x(n, "viewBox", "-1200 -1200 3000 3000"), x(n, "fill", "none"), x(n, "xmlns", "http://www.w3.org/2000/svg"), x(n, "class", "svelte-43sxxs"), x(t, "class", "svelte-43sxxs"), kt(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(_, d) {
      Fs(_, t, d), D(t, n), D(n, r), D(r, i), D(r, s), D(r, o), D(r, l), D(n, u), D(u, a), D(u, f), D(u, c), D(u, h);
    },
    p(_, [d]) {
      d & /*$top*/
      2 && xe(r, "transform", "translate(" + /*$top*/
      _[1][0] + "px, " + /*$top*/
      _[1][1] + "px)"), d & /*$bottom*/
      4 && xe(u, "transform", "translate(" + /*$bottom*/
      _[2][0] + "px, " + /*$bottom*/
      _[2][1] + "px)"), d & /*margin*/
      1 && kt(
        t,
        "margin",
        /*margin*/
        _[0]
      );
    },
    i: Gt,
    o: Gt,
    d(_) {
      _ && Us(t);
    }
  };
}
function qs(e, t, n) {
  let r, i, { margin: s = !0 } = t;
  const o = Ht([0, 0]);
  Ut(e, o, (h) => n(1, r = h));
  const l = Ht([0, 0]);
  Ut(e, l, (h) => n(2, i = h));
  let u;
  async function a() {
    await Promise.all([o.set([125, 140]), l.set([-125, -140])]), await Promise.all([o.set([-125, 140]), l.set([125, -140])]), await Promise.all([o.set([-125, 0]), l.set([125, -0])]), await Promise.all([o.set([125, 0]), l.set([-125, 0])]);
  }
  async function f() {
    await a(), u || f();
  }
  async function c() {
    await Promise.all([o.set([125, 0]), l.set([-125, 0])]), f();
  }
  return js(() => (c(), () => u = !0)), e.$$set = (h) => {
    "margin" in h && n(0, s = h.margin);
  }, [s, r, i, o, l];
}
class zs extends Ds {
  constructor(t) {
    super(), ks(this, t, qs, Xs, Vs, { margin: 0 });
  }
}
const {
  SvelteComponent: Zs,
  append: J,
  attr: G,
  binding_callbacks: Ft,
  check_outros: Un,
  create_component: Ws,
  create_slot: Qs,
  destroy_component: Js,
  destroy_each: Gn,
  detach: v,
  element: F,
  empty: ce,
  ensure_array_like: Oe,
  get_all_dirty_from_scope: Ys,
  get_slot_changes: Ks,
  group_outros: kn,
  init: $s,
  insert: y,
  mount_component: eo,
  noop: rt,
  safe_not_equal: to,
  set_data: R,
  set_style: Z,
  space: k,
  text: I,
  toggle_class: M,
  transition_in: ae,
  transition_out: ue,
  update_slot_base: no
} = window.__gradio__svelte__internal, { tick: ro } = window.__gradio__svelte__internal, { onDestroy: io } = window.__gradio__svelte__internal, so = (e) => ({}), Vt = (e) => ({});
function jt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r[40] = n, r;
}
function Xt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r;
}
function oo(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), r, i, s;
  const o = (
    /*#slots*/
    e[29].error
  ), l = Qs(
    o,
    e,
    /*$$scope*/
    e[28],
    Vt
  );
  return {
    c() {
      t = F("span"), r = I(n), i = k(), l && l.c(), G(t, "class", "error svelte-14miwb5");
    },
    m(u, a) {
      y(u, t, a), J(t, r), y(u, i, a), l && l.m(u, a), s = !0;
    },
    p(u, a) {
      (!s || a[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      u[1]("common.error") + "") && R(r, n), l && l.p && (!s || a[0] & /*$$scope*/
      268435456) && no(
        l,
        o,
        u,
        /*$$scope*/
        u[28],
        s ? Ks(
          o,
          /*$$scope*/
          u[28],
          a,
          so
        ) : Ys(
          /*$$scope*/
          u[28]
        ),
        Vt
      );
    },
    i(u) {
      s || (ae(l, u), s = !0);
    },
    o(u) {
      ue(l, u), s = !1;
    },
    d(u) {
      u && (v(t), v(i)), l && l.d(u);
    }
  };
}
function lo(e) {
  let t, n, r, i, s, o, l, u, a, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && qt(e)
  );
  function c(m, w) {
    if (
      /*progress*/
      m[7]
    )
      return fo;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return uo;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return ao;
  }
  let h = c(e), _ = h && h(e), d = (
    /*timer*/
    e[5] && Wt(e)
  );
  const B = [mo, _o], E = [];
  function P(m, w) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = P(e)) && (o = E[s] = B[s](e));
  let S = !/*timer*/
  e[5] && tn(e);
  return {
    c() {
      f && f.c(), t = k(), n = F("div"), _ && _.c(), r = k(), d && d.c(), i = k(), o && o.c(), l = k(), S && S.c(), u = ce(), G(n, "class", "progress-text svelte-14miwb5"), M(
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
    m(m, w) {
      f && f.m(m, w), y(m, t, w), y(m, n, w), _ && _.m(n, null), J(n, r), d && d.m(n, null), y(m, i, w), ~s && E[s].m(m, w), y(m, l, w), S && S.m(m, w), y(m, u, w), a = !0;
    },
    p(m, w) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? f ? f.p(m, w) : (f = qt(m), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), h === (h = c(m)) && _ ? _.p(m, w) : (_ && _.d(1), _ = h && h(m), _ && (_.c(), _.m(n, r))), /*timer*/
      m[5] ? d ? d.p(m, w) : (d = Wt(m), d.c(), d.m(n, null)) : d && (d.d(1), d = null), (!a || w[0] & /*variant*/
      256) && M(
        n,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!a || w[0] & /*variant*/
      256) && M(
        n,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let b = s;
      s = P(m), s === b ? ~s && E[s].p(m, w) : (o && (kn(), ue(E[b], 1, 1, () => {
        E[b] = null;
      }), Un()), ~s ? (o = E[s], o ? o.p(m, w) : (o = E[s] = B[s](m), o.c()), ae(o, 1), o.m(l.parentNode, l)) : o = null), /*timer*/
      m[5] ? S && (S.d(1), S = null) : S ? S.p(m, w) : (S = tn(m), S.c(), S.m(u.parentNode, u));
    },
    i(m) {
      a || (ae(o), a = !0);
    },
    o(m) {
      ue(o), a = !1;
    },
    d(m) {
      m && (v(t), v(n), v(i), v(l), v(u)), f && f.d(m), _ && _.d(), d && d.d(), ~s && E[s].d(m), S && S.d(m);
    }
  };
}
function qt(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = F("div"), G(t, "class", "eta-bar svelte-14miwb5"), Z(t, "transform", n);
    },
    m(r, i) {
      y(r, t, i);
    },
    p(r, i) {
      i[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (r[17] || 0) * 100 - 100}%)`) && Z(t, "transform", n);
    },
    d(r) {
      r && v(t);
    }
  };
}
function ao(e) {
  let t;
  return {
    c() {
      t = I("processing |");
    },
    m(n, r) {
      y(n, t, r);
    },
    p: rt,
    d(n) {
      n && v(t);
    }
  };
}
function uo(e) {
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
    m(l, u) {
      y(l, t, u), y(l, r, u), y(l, i, u), y(l, s, u), y(l, o, u);
    },
    p(l, u) {
      u[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      l[2] + 1 + "") && R(r, n), u[0] & /*queue_size*/
      8 && R(
        s,
        /*queue_size*/
        l[3]
      );
    },
    d(l) {
      l && (v(t), v(r), v(i), v(s), v(o));
    }
  };
}
function fo(e) {
  let t, n = Oe(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = Zt(Xt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = ce();
    },
    m(i, s) {
      for (let o = 0; o < r.length; o += 1)
        r[o] && r[o].m(i, s);
      y(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        n = Oe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const l = Xt(i, n, o);
          r[o] ? r[o].p(l, s) : (r[o] = Zt(l), r[o].c(), r[o].m(t.parentNode, t));
        }
        for (; o < r.length; o += 1)
          r[o].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && v(t), Gn(r, i);
    }
  };
}
function zt(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), r, i, s = " ", o;
  function l(f, c) {
    return (
      /*p*/
      f[38].length != null ? co : ho
    );
  }
  let u = l(e), a = u(e);
  return {
    c() {
      a.c(), t = k(), r = I(n), i = I(" | "), o = I(s);
    },
    m(f, c) {
      a.m(f, c), y(f, t, c), y(f, r, c), y(f, i, c), y(f, o, c);
    },
    p(f, c) {
      u === (u = l(f)) && a ? a.p(f, c) : (a.d(1), a = u(f), a && (a.c(), a.m(t.parentNode, t))), c[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && R(r, n);
    },
    d(f) {
      f && (v(t), v(r), v(i), v(o)), a.d(f);
    }
  };
}
function ho(e) {
  let t = te(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = I(t);
    },
    m(r, i) {
      y(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = te(
        /*p*/
        r[38].index || 0
      ) + "") && R(n, t);
    },
    d(r) {
      r && v(n);
    }
  };
}
function co(e) {
  let t = te(
    /*p*/
    e[38].index || 0
  ) + "", n, r, i = te(
    /*p*/
    e[38].length
  ) + "", s;
  return {
    c() {
      n = I(t), r = I("/"), s = I(i);
    },
    m(o, l) {
      y(o, n, l), y(o, r, l), y(o, s, l);
    },
    p(o, l) {
      l[0] & /*progress*/
      128 && t !== (t = te(
        /*p*/
        o[38].index || 0
      ) + "") && R(n, t), l[0] & /*progress*/
      128 && i !== (i = te(
        /*p*/
        o[38].length
      ) + "") && R(s, i);
    },
    d(o) {
      o && (v(n), v(r), v(s));
    }
  };
}
function Zt(e) {
  let t, n = (
    /*p*/
    e[38].index != null && zt(e)
  );
  return {
    c() {
      n && n.c(), t = ce();
    },
    m(r, i) {
      n && n.m(r, i), y(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].index != null ? n ? n.p(r, i) : (n = zt(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && v(t), n && n.d(r);
    }
  };
}
function Wt(e) {
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
      y(s, t, o), y(s, r, o), y(s, i, o);
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
      s && (v(t), v(r), v(i));
    }
  };
}
function _o(e) {
  let t, n;
  return t = new zs({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      Ws(t.$$.fragment);
    },
    m(r, i) {
      eo(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      r[8] === "default"), t.$set(s);
    },
    i(r) {
      n || (ae(t.$$.fragment, r), n = !0);
    },
    o(r) {
      ue(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Js(t, r);
    }
  };
}
function mo(e) {
  let t, n, r, i, s, o = `${/*last_progress_level*/
  e[15] * 100}%`, l = (
    /*progress*/
    e[7] != null && Qt(e)
  );
  return {
    c() {
      t = F("div"), n = F("div"), l && l.c(), r = k(), i = F("div"), s = F("div"), G(n, "class", "progress-level-inner svelte-14miwb5"), G(s, "class", "progress-bar svelte-14miwb5"), Z(s, "width", o), G(i, "class", "progress-bar-wrap svelte-14miwb5"), G(t, "class", "progress-level svelte-14miwb5");
    },
    m(u, a) {
      y(u, t, a), J(t, n), l && l.m(n, null), J(t, r), J(t, i), J(i, s), e[30](s);
    },
    p(u, a) {
      /*progress*/
      u[7] != null ? l ? l.p(u, a) : (l = Qt(u), l.c(), l.m(n, null)) : l && (l.d(1), l = null), a[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      u[15] * 100}%`) && Z(s, "width", o);
    },
    i: rt,
    o: rt,
    d(u) {
      u && v(t), l && l.d(), e[30](null);
    }
  };
}
function Qt(e) {
  let t, n = Oe(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = en(jt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = ce();
    },
    m(i, s) {
      for (let o = 0; o < r.length; o += 1)
        r[o] && r[o].m(i, s);
      y(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        n = Oe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const l = jt(i, n, o);
          r[o] ? r[o].p(l, s) : (r[o] = en(l), r[o].c(), r[o].m(t.parentNode, t));
        }
        for (; o < r.length; o += 1)
          r[o].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && v(t), Gn(r, i);
    }
  };
}
function Jt(e) {
  let t, n, r, i, s = (
    /*i*/
    e[40] !== 0 && bo()
  ), o = (
    /*p*/
    e[38].desc != null && Yt(e)
  ), l = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && Kt()
  ), u = (
    /*progress_level*/
    e[14] != null && $t(e)
  );
  return {
    c() {
      s && s.c(), t = k(), o && o.c(), n = k(), l && l.c(), r = k(), u && u.c(), i = ce();
    },
    m(a, f) {
      s && s.m(a, f), y(a, t, f), o && o.m(a, f), y(a, n, f), l && l.m(a, f), y(a, r, f), u && u.m(a, f), y(a, i, f);
    },
    p(a, f) {
      /*p*/
      a[38].desc != null ? o ? o.p(a, f) : (o = Yt(a), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null), /*p*/
      a[38].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[40]
      ] != null ? l || (l = Kt(), l.c(), l.m(r.parentNode, r)) : l && (l.d(1), l = null), /*progress_level*/
      a[14] != null ? u ? u.p(a, f) : (u = $t(a), u.c(), u.m(i.parentNode, i)) : u && (u.d(1), u = null);
    },
    d(a) {
      a && (v(t), v(n), v(r), v(i)), s && s.d(a), o && o.d(a), l && l.d(a), u && u.d(a);
    }
  };
}
function bo(e) {
  let t;
  return {
    c() {
      t = I(" /");
    },
    m(n, r) {
      y(n, t, r);
    },
    d(n) {
      n && v(t);
    }
  };
}
function Yt(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = I(t);
    },
    m(r, i) {
      y(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[38].desc + "") && R(n, t);
    },
    d(r) {
      r && v(n);
    }
  };
}
function Kt(e) {
  let t;
  return {
    c() {
      t = I("-");
    },
    m(n, r) {
      y(n, t, r);
    },
    d(n) {
      n && v(t);
    }
  };
}
function $t(e) {
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
      y(i, n, s), y(i, r, s);
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
      i && (v(n), v(r));
    }
  };
}
function en(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && Jt(e)
  );
  return {
    c() {
      n && n.c(), t = ce();
    },
    m(r, i) {
      n && n.m(r, i), y(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].desc != null || /*progress_level*/
      r[14] && /*progress_level*/
      r[14][
        /*i*/
        r[40]
      ] != null ? n ? n.p(r, i) : (n = Jt(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && v(t), n && n.d(r);
    }
  };
}
function tn(e) {
  let t, n;
  return {
    c() {
      t = F("p"), n = I(
        /*loading_text*/
        e[9]
      ), G(t, "class", "loading svelte-14miwb5");
    },
    m(r, i) {
      y(r, t, i), J(t, n);
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
      r && v(t);
    }
  };
}
function po(e) {
  let t, n, r, i, s;
  const o = [lo, oo], l = [];
  function u(a, f) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = u(e)) && (r = l[n] = o[n](e)), {
    c() {
      t = F("div"), r && r.c(), G(t, "class", i = "wrap " + /*variant*/
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
      ), Z(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), Z(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, f) {
      y(a, t, f), ~n && l[n].m(t, null), e[31](t), s = !0;
    },
    p(a, f) {
      let c = n;
      n = u(a), n === c ? ~n && l[n].p(a, f) : (r && (kn(), ue(l[c], 1, 1, () => {
        l[c] = null;
      }), Un()), ~n ? (r = l[n], r ? r.p(a, f) : (r = l[n] = o[n](a), r.c()), ae(r, 1), r.m(t, null)) : r = null), (!s || f[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-14miwb5")) && G(t, "class", i), (!s || f[0] & /*variant, show_progress, status, show_progress*/
      336) && M(t, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!s || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && M(
        t,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!s || f[0] & /*variant, show_progress, status*/
      336) && M(
        t,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!s || f[0] & /*variant, show_progress, border*/
      4416) && M(
        t,
        "border",
        /*border*/
        a[12]
      ), f[0] & /*absolute*/
      1024 && Z(
        t,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && Z(
        t,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      s || (ae(r), s = !0);
    },
    o(a) {
      ue(r), s = !1;
    },
    d(a) {
      a && v(t), ~n && l[n].d(), e[31](null);
    }
  };
}
let Be = [], ze = !1;
async function go(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (Be.push(e), !ze)
      ze = !0;
    else
      return;
    await ro(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let r = 0; r < Be.length; r++) {
        const s = Be[r].getBoundingClientRect();
        (r === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = r);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), ze = !1, Be = [];
    });
  }
}
function vo(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { i18n: o } = t, { eta: l = null } = t, { queue: u = !1 } = t, { queue_position: a } = t, { queue_size: f } = t, { status: c } = t, { scroll_to_output: h = !1 } = t, { timer: _ = !0 } = t, { show_progress: d = "full" } = t, { message: B = null } = t, { progress: E = null } = t, { variant: P = "default" } = t, { loading_text: S = "Loading..." } = t, { absolute: m = !0 } = t, { translucent: w = !1 } = t, { border: b = !1 } = t, { autoscroll: g } = t, V, _e = !1, Te = 0, W = 0, Ge = null, _t = 0, Q = null, me, j = null, mt = !0;
  const Fn = () => {
    n(25, Te = performance.now()), n(26, W = 0), _e = !0, dt();
  };
  function dt() {
    requestAnimationFrame(() => {
      n(26, W = (performance.now() - Te) / 1e3), _e && dt();
    });
  }
  function bt() {
    n(26, W = 0), _e && (_e = !1);
  }
  io(() => {
    _e && bt();
  });
  let pt = null;
  function Vn(p) {
    Ft[p ? "unshift" : "push"](() => {
      j = p, n(16, j), n(7, E), n(14, Q), n(15, me);
    });
  }
  function jn(p) {
    Ft[p ? "unshift" : "push"](() => {
      V = p, n(13, V);
    });
  }
  return e.$$set = (p) => {
    "i18n" in p && n(1, o = p.i18n), "eta" in p && n(0, l = p.eta), "queue" in p && n(21, u = p.queue), "queue_position" in p && n(2, a = p.queue_position), "queue_size" in p && n(3, f = p.queue_size), "status" in p && n(4, c = p.status), "scroll_to_output" in p && n(22, h = p.scroll_to_output), "timer" in p && n(5, _ = p.timer), "show_progress" in p && n(6, d = p.show_progress), "message" in p && n(23, B = p.message), "progress" in p && n(7, E = p.progress), "variant" in p && n(8, P = p.variant), "loading_text" in p && n(9, S = p.loading_text), "absolute" in p && n(10, m = p.absolute), "translucent" in p && n(11, w = p.translucent), "border" in p && n(12, b = p.border), "autoscroll" in p && n(24, g = p.autoscroll), "$$scope" in p && n(28, s = p.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (l === null ? n(0, l = Ge) : u && n(0, l = (performance.now() - Te) / 1e3 + l), l != null && (n(19, pt = l.toFixed(1)), n(27, Ge = l))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, _t = l === null || l <= 0 || !W ? null : Math.min(W / l, 1)), e.$$.dirty[0] & /*progress*/
    128 && E != null && n(18, mt = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (E != null ? n(14, Q = E.map((p) => {
      if (p.index != null && p.length != null)
        return p.index / p.length;
      if (p.progress != null)
        return p.progress;
    })) : n(14, Q = null), Q ? (n(15, me = Q[Q.length - 1]), j && (me === 0 ? n(16, j.style.transition = "0", j) : n(16, j.style.transition = "150ms", j))) : n(15, me = void 0)), e.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Fn() : bt()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && V && h && (c === "pending" || c === "complete") && go(V, g), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, r = W.toFixed(1));
  }, [
    l,
    o,
    a,
    f,
    c,
    _,
    d,
    E,
    P,
    S,
    m,
    w,
    b,
    V,
    Q,
    me,
    j,
    _t,
    mt,
    pt,
    r,
    u,
    h,
    B,
    g,
    Te,
    W,
    Ge,
    s,
    i,
    Vn,
    jn
  ];
}
class yo extends Zs {
  constructor(t) {
    super(), $s(
      this,
      t,
      vo,
      po,
      to,
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
const {
  SvelteComponent: Eo,
  append: nn,
  assign: wo,
  attr: q,
  binding_callbacks: To,
  check_outros: Ho,
  create_component: ft,
  destroy_component: ht,
  detach: it,
  element: rn,
  flush: C,
  get_spread_object: xo,
  get_spread_update: Bo,
  group_outros: So,
  init: Ao,
  insert: st,
  listen: sn,
  mount_component: ct,
  run_all: Po,
  safe_not_equal: No,
  set_data: Io,
  set_input_value: on,
  space: ln,
  text: Lo,
  toggle_class: Co,
  transition_in: ne,
  transition_out: pe
} = window.__gradio__svelte__internal, { tick: Oo } = window.__gradio__svelte__internal;
function an(e) {
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
    e[10]
  ];
  let i = {};
  for (let s = 0; s < r.length; s += 1)
    i = wo(i, r[s]);
  return t = new yo({ props: i }), {
    c() {
      ft(t.$$.fragment);
    },
    m(s, o) {
      ct(t, s, o), n = !0;
    },
    p(s, o) {
      const l = o & /*gradio, loading_status*/
      1026 ? Bo(r, [
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
        1024 && xo(
          /*loading_status*/
          s[10]
        )
      ]) : {};
      t.$set(l);
    },
    i(s) {
      n || (ne(t.$$.fragment, s), n = !0);
    },
    o(s) {
      pe(t.$$.fragment, s), n = !1;
    },
    d(s) {
      ht(t, s);
    }
  };
}
function Mo(e) {
  let t;
  return {
    c() {
      t = Lo(
        /*label*/
        e[2]
      );
    },
    m(n, r) {
      st(n, t, r);
    },
    p(n, r) {
      r & /*label*/
      4 && Io(
        t,
        /*label*/
        n[2]
      );
    },
    d(n) {
      n && it(t);
    }
  };
}
function Ro(e) {
  let t, n, r, i, s, o, l, u, a, f, c = (
    /*loading_status*/
    e[10] && an(e)
  );
  return r = new Vr({
    props: {
      show_label: (
        /*show_label*/
        e[7]
      ),
      info: void 0,
      $$slots: { default: [Mo] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      c && c.c(), t = ln(), n = rn("label"), ft(r.$$.fragment), i = ln(), s = rn("input"), q(s, "data-testid", "textbox"), q(s, "type", "text"), q(s, "class", "scroll-hide svelte-2jrh70"), q(
        s,
        "placeholder",
        /*placeholder*/
        e[6]
      ), s.disabled = o = /*mode*/
      e[11] === "static", q(s, "dir", l = /*rtl*/
      e[12] ? "rtl" : "ltr"), q(n, "class", "svelte-2jrh70"), Co(n, "container", Uo);
    },
    m(h, _) {
      c && c.m(h, _), st(h, t, _), st(h, n, _), ct(r, n, null), nn(n, i), nn(n, s), on(
        s,
        /*value*/
        e[0]
      ), e[17](s), u = !0, a || (f = [
        sn(
          s,
          "input",
          /*input_input_handler*/
          e[16]
        ),
        sn(
          s,
          "keypress",
          /*handle_keypress*/
          e[14]
        )
      ], a = !0);
    },
    p(h, _) {
      /*loading_status*/
      h[10] ? c ? (c.p(h, _), _ & /*loading_status*/
      1024 && ne(c, 1)) : (c = an(h), c.c(), ne(c, 1), c.m(t.parentNode, t)) : c && (So(), pe(c, 1, 1, () => {
        c = null;
      }), Ho());
      const d = {};
      _ & /*show_label*/
      128 && (d.show_label = /*show_label*/
      h[7]), _ & /*$$scope, label*/
      524292 && (d.$$scope = { dirty: _, ctx: h }), r.$set(d), (!u || _ & /*placeholder*/
      64) && q(
        s,
        "placeholder",
        /*placeholder*/
        h[6]
      ), (!u || _ & /*mode*/
      2048 && o !== (o = /*mode*/
      h[11] === "static")) && (s.disabled = o), (!u || _ & /*rtl*/
      4096 && l !== (l = /*rtl*/
      h[12] ? "rtl" : "ltr")) && q(s, "dir", l), _ & /*value*/
      1 && s.value !== /*value*/
      h[0] && on(
        s,
        /*value*/
        h[0]
      );
    },
    i(h) {
      u || (ne(c), ne(r.$$.fragment, h), u = !0);
    },
    o(h) {
      pe(c), pe(r.$$.fragment, h), u = !1;
    },
    d(h) {
      h && (it(t), it(n)), c && c.d(h), ht(r), e[17](null), a = !1, Po(f);
    }
  };
}
function Do(e) {
  let t, n;
  return t = new sr({
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
        e[8]
      ),
      min_width: (
        /*min_width*/
        e[9]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [Ro] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      ft(t.$$.fragment);
    },
    m(r, i) {
      ct(t, r, i), n = !0;
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
      256 && (s.scale = /*scale*/
      r[8]), i & /*min_width*/
      512 && (s.min_width = /*min_width*/
      r[9]), i & /*$$scope, placeholder, mode, rtl, value, el, show_label, label, gradio, loading_status*/
      539847 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (ne(t.$$.fragment, r), n = !0);
    },
    o(r) {
      pe(t.$$.fragment, r), n = !1;
    },
    d(r) {
      ht(t, r);
    }
  };
}
const Uo = !0;
function Go(e, t, n) {
  let { gradio: r } = t, { label: i = "Textbox" } = t, { elem_id: s = "" } = t, { elem_classes: o = [] } = t, { visible: l = !0 } = t, { value: u = "" } = t, { placeholder: a = "" } = t, { show_label: f } = t, { scale: c = null } = t, { min_width: h = void 0 } = t, { loading_status: _ = void 0 } = t, { value_is_output: d = !1 } = t, { mode: B } = t, { rtl: E = !1 } = t, P;
  function S() {
    r.dispatch("change"), d || r.dispatch("input");
  }
  async function m(g) {
    await Oo(), g.key === "Enter" && (g.preventDefault(), r.dispatch("submit"));
  }
  function w() {
    u = this.value, n(0, u);
  }
  function b(g) {
    To[g ? "unshift" : "push"](() => {
      P = g, n(13, P);
    });
  }
  return e.$$set = (g) => {
    "gradio" in g && n(1, r = g.gradio), "label" in g && n(2, i = g.label), "elem_id" in g && n(3, s = g.elem_id), "elem_classes" in g && n(4, o = g.elem_classes), "visible" in g && n(5, l = g.visible), "value" in g && n(0, u = g.value), "placeholder" in g && n(6, a = g.placeholder), "show_label" in g && n(7, f = g.show_label), "scale" in g && n(8, c = g.scale), "min_width" in g && n(9, h = g.min_width), "loading_status" in g && n(10, _ = g.loading_status), "value_is_output" in g && n(15, d = g.value_is_output), "mode" in g && n(11, B = g.mode), "rtl" in g && n(12, E = g.rtl);
  }, e.$$.update = () => {
    e.$$.dirty & /*value*/
    1 && u === null && n(0, u = ""), e.$$.dirty & /*value*/
    1 && S();
  }, [
    u,
    r,
    i,
    s,
    o,
    l,
    a,
    f,
    c,
    h,
    _,
    B,
    E,
    P,
    m,
    d,
    w,
    b
  ];
}
class ko extends Eo {
  constructor(t) {
    super(), Ao(this, t, Go, Do, No, {
      gradio: 1,
      label: 2,
      elem_id: 3,
      elem_classes: 4,
      visible: 5,
      value: 0,
      placeholder: 6,
      show_label: 7,
      scale: 8,
      min_width: 9,
      loading_status: 10,
      value_is_output: 15,
      mode: 11,
      rtl: 12
    });
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(t) {
    this.$$set({ gradio: t }), C();
  }
  get label() {
    return this.$$.ctx[2];
  }
  set label(t) {
    this.$$set({ label: t }), C();
  }
  get elem_id() {
    return this.$$.ctx[3];
  }
  set elem_id(t) {
    this.$$set({ elem_id: t }), C();
  }
  get elem_classes() {
    return this.$$.ctx[4];
  }
  set elem_classes(t) {
    this.$$set({ elem_classes: t }), C();
  }
  get visible() {
    return this.$$.ctx[5];
  }
  set visible(t) {
    this.$$set({ visible: t }), C();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(t) {
    this.$$set({ value: t }), C();
  }
  get placeholder() {
    return this.$$.ctx[6];
  }
  set placeholder(t) {
    this.$$set({ placeholder: t }), C();
  }
  get show_label() {
    return this.$$.ctx[7];
  }
  set show_label(t) {
    this.$$set({ show_label: t }), C();
  }
  get scale() {
    return this.$$.ctx[8];
  }
  set scale(t) {
    this.$$set({ scale: t }), C();
  }
  get min_width() {
    return this.$$.ctx[9];
  }
  set min_width(t) {
    this.$$set({ min_width: t }), C();
  }
  get loading_status() {
    return this.$$.ctx[10];
  }
  set loading_status(t) {
    this.$$set({ loading_status: t }), C();
  }
  get value_is_output() {
    return this.$$.ctx[15];
  }
  set value_is_output(t) {
    this.$$set({ value_is_output: t }), C();
  }
  get mode() {
    return this.$$.ctx[11];
  }
  set mode(t) {
    this.$$set({ mode: t }), C();
  }
  get rtl() {
    return this.$$.ctx[12];
  }
  set rtl(t) {
    this.$$set({ rtl: t }), C();
  }
}
export {
  ko as default
};
