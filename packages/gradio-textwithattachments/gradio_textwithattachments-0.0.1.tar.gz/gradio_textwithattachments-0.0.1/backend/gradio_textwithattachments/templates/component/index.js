const {
  SvelteComponent: Vr,
  assign: qr,
  create_slot: zr,
  detach: Xr,
  element: Wr,
  get_all_dirty_from_scope: Zr,
  get_slot_changes: Jr,
  get_spread_update: Qr,
  init: Yr,
  insert: Kr,
  safe_not_equal: $r,
  set_dynamic_element_data: sn,
  set_style: Y,
  toggle_class: de,
  transition_in: er,
  transition_out: tr,
  update_slot_base: ei
} = window.__gradio__svelte__internal;
function ti(e) {
  let t, n, r;
  const i = (
    /*#slots*/
    e[17].default
  ), s = zr(
    i,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let a = [
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
  ], o = {};
  for (let l = 0; l < a.length; l += 1)
    o = qr(o, a[l]);
  return {
    c() {
      t = Wr(
        /*tag*/
        e[14]
      ), s && s.c(), sn(
        /*tag*/
        e[14]
      )(t, o), de(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        e[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), Y(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), Y(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), Y(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), Y(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), Y(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), Y(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), Y(t, "border-width", "var(--block-border-width)");
    },
    m(l, u) {
      Kr(l, t, u), s && s.m(t, null), r = !0;
    },
    p(l, u) {
      s && s.p && (!r || u & /*$$scope*/
      65536) && ei(
        s,
        i,
        l,
        /*$$scope*/
        l[16],
        r ? Jr(
          i,
          /*$$scope*/
          l[16],
          u,
          null
        ) : Zr(
          /*$$scope*/
          l[16]
        ),
        null
      ), sn(
        /*tag*/
        l[14]
      )(t, o = Qr(a, [
        (!r || u & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          l[7]
        ) },
        (!r || u & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          l[2]
        ) },
        (!r || u & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        l[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), de(
        t,
        "hidden",
        /*visible*/
        l[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        l[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), u & /*height*/
      1 && Y(t, "height", typeof /*height*/
      l[0] == "number" ? (
        /*height*/
        l[0] + "px"
      ) : void 0), u & /*width*/
      2 && Y(t, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : void 0), u & /*variant*/
      16 && Y(
        t,
        "border-style",
        /*variant*/
        l[4]
      ), u & /*allow_overflow*/
      2048 && Y(
        t,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), u & /*scale*/
      4096 && Y(
        t,
        "flex-grow",
        /*scale*/
        l[12]
      ), u & /*min_width*/
      8192 && Y(t, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`);
    },
    i(l) {
      r || (er(s, l), r = !0);
    },
    o(l) {
      tr(s, l), r = !1;
    },
    d(l) {
      l && Xr(t), s && s.d(l);
    }
  };
}
function ni(e) {
  let t, n = (
    /*tag*/
    e[14] && ti(e)
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
      t || (er(n, r), t = !0);
    },
    o(r) {
      tr(n, r), t = !1;
    },
    d(r) {
      n && n.d(r);
    }
  };
}
function ri(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { height: s = void 0 } = t, { width: a = void 0 } = t, { elem_id: o = "" } = t, { elem_classes: l = [] } = t, { variant: u = "solid" } = t, { border_mode: f = "base" } = t, { padding: h = !0 } = t, { type: _ = "normal" } = t, { test_id: b = void 0 } = t, { explicit_call: d = !1 } = t, { container: g = !0 } = t, { visible: v = !0 } = t, { allow_overflow: w = !0 } = t, { scale: E = null } = t, { min_width: m = 0 } = t, c = _ === "fieldset" ? "fieldset" : "div";
  return e.$$set = (p) => {
    "height" in p && n(0, s = p.height), "width" in p && n(1, a = p.width), "elem_id" in p && n(2, o = p.elem_id), "elem_classes" in p && n(3, l = p.elem_classes), "variant" in p && n(4, u = p.variant), "border_mode" in p && n(5, f = p.border_mode), "padding" in p && n(6, h = p.padding), "type" in p && n(15, _ = p.type), "test_id" in p && n(7, b = p.test_id), "explicit_call" in p && n(8, d = p.explicit_call), "container" in p && n(9, g = p.container), "visible" in p && n(10, v = p.visible), "allow_overflow" in p && n(11, w = p.allow_overflow), "scale" in p && n(12, E = p.scale), "min_width" in p && n(13, m = p.min_width), "$$scope" in p && n(16, i = p.$$scope);
  }, [
    s,
    a,
    o,
    l,
    u,
    f,
    h,
    b,
    d,
    g,
    v,
    w,
    E,
    m,
    c,
    _,
    i,
    r
  ];
}
class ii extends Vr {
  constructor(t) {
    super(), Yr(this, t, ri, ni, $r, {
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
  SvelteComponent: si,
  attr: oi,
  create_slot: ai,
  detach: li,
  element: ui,
  get_all_dirty_from_scope: fi,
  get_slot_changes: ci,
  init: hi,
  insert: _i,
  safe_not_equal: di,
  transition_in: mi,
  transition_out: bi,
  update_slot_base: pi
} = window.__gradio__svelte__internal;
function gi(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[1].default
  ), i = ai(
    r,
    e,
    /*$$scope*/
    e[0],
    null
  );
  return {
    c() {
      t = ui("div"), i && i.c(), oi(t, "class", "svelte-1hnfib2");
    },
    m(s, a) {
      _i(s, t, a), i && i.m(t, null), n = !0;
    },
    p(s, [a]) {
      i && i.p && (!n || a & /*$$scope*/
      1) && pi(
        i,
        r,
        s,
        /*$$scope*/
        s[0],
        n ? ci(
          r,
          /*$$scope*/
          s[0],
          a,
          null
        ) : fi(
          /*$$scope*/
          s[0]
        ),
        null
      );
    },
    i(s) {
      n || (mi(i, s), n = !0);
    },
    o(s) {
      bi(i, s), n = !1;
    },
    d(s) {
      s && li(t), i && i.d(s);
    }
  };
}
function vi(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t;
  return e.$$set = (s) => {
    "$$scope" in s && n(0, i = s.$$scope);
  }, [i, r];
}
class yi extends si {
  constructor(t) {
    super(), hi(this, t, vi, gi, di, {});
  }
}
const {
  SvelteComponent: wi,
  attr: on,
  check_outros: Ei,
  create_component: Si,
  create_slot: Ti,
  destroy_component: Bi,
  detach: nt,
  element: Ai,
  empty: Hi,
  get_all_dirty_from_scope: Ni,
  get_slot_changes: Pi,
  group_outros: Ii,
  init: xi,
  insert: rt,
  mount_component: Oi,
  safe_not_equal: Ci,
  set_data: Li,
  space: Mi,
  text: Ri,
  toggle_class: we,
  transition_in: Ge,
  transition_out: it,
  update_slot_base: ki
} = window.__gradio__svelte__internal;
function an(e) {
  let t, n;
  return t = new yi({
    props: {
      $$slots: { default: [Di] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Si(t.$$.fragment);
    },
    m(r, i) {
      Oi(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i & /*$$scope, info*/
      10 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (Ge(t.$$.fragment, r), n = !0);
    },
    o(r) {
      it(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Bi(t, r);
    }
  };
}
function Di(e) {
  let t;
  return {
    c() {
      t = Ri(
        /*info*/
        e[1]
      );
    },
    m(n, r) {
      rt(n, t, r);
    },
    p(n, r) {
      r & /*info*/
      2 && Li(
        t,
        /*info*/
        n[1]
      );
    },
    d(n) {
      n && nt(t);
    }
  };
}
function Ui(e) {
  let t, n, r, i;
  const s = (
    /*#slots*/
    e[2].default
  ), a = Ti(
    s,
    e,
    /*$$scope*/
    e[3],
    null
  );
  let o = (
    /*info*/
    e[1] && an(e)
  );
  return {
    c() {
      t = Ai("span"), a && a.c(), n = Mi(), o && o.c(), r = Hi(), on(t, "data-testid", "block-info"), on(t, "class", "svelte-22c38v"), we(t, "sr-only", !/*show_label*/
      e[0]), we(t, "hide", !/*show_label*/
      e[0]), we(
        t,
        "has-info",
        /*info*/
        e[1] != null
      );
    },
    m(l, u) {
      rt(l, t, u), a && a.m(t, null), rt(l, n, u), o && o.m(l, u), rt(l, r, u), i = !0;
    },
    p(l, [u]) {
      a && a.p && (!i || u & /*$$scope*/
      8) && ki(
        a,
        s,
        l,
        /*$$scope*/
        l[3],
        i ? Pi(
          s,
          /*$$scope*/
          l[3],
          u,
          null
        ) : Ni(
          /*$$scope*/
          l[3]
        ),
        null
      ), (!i || u & /*show_label*/
      1) && we(t, "sr-only", !/*show_label*/
      l[0]), (!i || u & /*show_label*/
      1) && we(t, "hide", !/*show_label*/
      l[0]), (!i || u & /*info*/
      2) && we(
        t,
        "has-info",
        /*info*/
        l[1] != null
      ), /*info*/
      l[1] ? o ? (o.p(l, u), u & /*info*/
      2 && Ge(o, 1)) : (o = an(l), o.c(), Ge(o, 1), o.m(r.parentNode, r)) : o && (Ii(), it(o, 1, 1, () => {
        o = null;
      }), Ei());
    },
    i(l) {
      i || (Ge(a, l), Ge(o), i = !0);
    },
    o(l) {
      it(a, l), it(o), i = !1;
    },
    d(l) {
      l && (nt(t), nt(n), nt(r)), a && a.d(l), o && o.d(l);
    }
  };
}
function Fi(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { show_label: s = !0 } = t, { info: a = void 0 } = t;
  return e.$$set = (o) => {
    "show_label" in o && n(0, s = o.show_label), "info" in o && n(1, a = o.info), "$$scope" in o && n(3, i = o.$$scope);
  }, [s, a, r, i];
}
class Gi extends wi {
  constructor(t) {
    super(), xi(this, t, Fi, Ui, Ci, { show_label: 0, info: 1 });
  }
}
const ji = [
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
], ln = {
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
ji.reduce(
  (e, { color: t, primary: n, secondary: r }) => ({
    ...e,
    [t]: {
      primary: ln[t][n],
      secondary: ln[t][r]
    }
  }),
  {}
);
function ve() {
}
function Vi(e) {
  return e();
}
function qi(e) {
  e.forEach(Vi);
}
function zi(e) {
  return typeof e == "function";
}
function Xi(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function nr(e, ...t) {
  if (e == null) {
    for (const r of t)
      r(void 0);
    return ve;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function Wi(e) {
  let t;
  return nr(e, (n) => t = n)(), t;
}
const rr = typeof window < "u";
let un = rr ? () => window.performance.now() : () => Date.now(), ir = rr ? (e) => requestAnimationFrame(e) : ve;
const He = /* @__PURE__ */ new Set();
function sr(e) {
  He.forEach((t) => {
    t.c(e) || (He.delete(t), t.f());
  }), He.size !== 0 && ir(sr);
}
function Zi(e) {
  let t;
  return He.size === 0 && ir(sr), {
    promise: new Promise((n) => {
      He.add(t = { c: e, f: n });
    }),
    abort() {
      He.delete(t);
    }
  };
}
const Ee = [];
function Ji(e, t) {
  return {
    subscribe: ze(e, t).subscribe
  };
}
function ze(e, t = ve) {
  let n;
  const r = /* @__PURE__ */ new Set();
  function i(o) {
    if (Xi(e, o) && (e = o, n)) {
      const l = !Ee.length;
      for (const u of r)
        u[1](), Ee.push(u, e);
      if (l) {
        for (let u = 0; u < Ee.length; u += 2)
          Ee[u][0](Ee[u + 1]);
        Ee.length = 0;
      }
    }
  }
  function s(o) {
    i(o(e));
  }
  function a(o, l = ve) {
    const u = [o, l];
    return r.add(u), r.size === 1 && (n = t(i, s) || ve), o(e), () => {
      r.delete(u), r.size === 0 && n && (n(), n = null);
    };
  }
  return { set: i, update: s, subscribe: a };
}
function Le(e, t, n) {
  const r = !Array.isArray(e), i = r ? [e] : e;
  if (!i.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const s = t.length < 2;
  return Ji(n, (a, o) => {
    let l = !1;
    const u = [];
    let f = 0, h = ve;
    const _ = () => {
      if (f)
        return;
      h();
      const d = t(r ? u[0] : u, a, o);
      s ? a(d) : h = zi(d) ? d : ve;
    }, b = i.map(
      (d, g) => nr(
        d,
        (v) => {
          u[g] = v, f &= ~(1 << g), l && _();
        },
        () => {
          f |= 1 << g;
        }
      )
    );
    return l = !0, _(), function() {
      qi(b), h(), l = !1;
    };
  });
}
function fn(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Dt(e, t, n, r) {
  if (typeof n == "number" || fn(n)) {
    const i = r - n, s = (n - t) / (e.dt || 1 / 60), a = e.opts.stiffness * i, o = e.opts.damping * s, l = (a - o) * e.inv_mass, u = (s + l) * e.dt;
    return Math.abs(u) < e.opts.precision && Math.abs(i) < e.opts.precision ? r : (e.settled = !1, fn(n) ? new Date(n.getTime() + u) : n + u);
  } else {
    if (Array.isArray(n))
      return n.map(
        (i, s) => Dt(e, t[s], n[s], r[s])
      );
    if (typeof n == "object") {
      const i = {};
      for (const s in n)
        i[s] = Dt(e, t[s], n[s], r[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function cn(e, t = {}) {
  const n = ze(e), { stiffness: r = 0.15, damping: i = 0.8, precision: s = 0.01 } = t;
  let a, o, l, u = e, f = e, h = 1, _ = 0, b = !1;
  function d(v, w = {}) {
    f = v;
    const E = l = {};
    return e == null || w.hard || g.stiffness >= 1 && g.damping >= 1 ? (b = !0, a = un(), u = v, n.set(e = f), Promise.resolve()) : (w.soft && (_ = 1 / ((w.soft === !0 ? 0.5 : +w.soft) * 60), h = 0), o || (a = un(), b = !1, o = Zi((m) => {
      if (b)
        return b = !1, o = null, !1;
      h = Math.min(h + _, 1);
      const c = {
        inv_mass: h,
        opts: g,
        settled: !0,
        dt: (m - a) * 60 / 1e3
      }, p = Dt(c, u, e, f);
      return a = m, u = e, n.set(e = p), c.settled && (o = null), !c.settled;
    })), new Promise((m) => {
      o.promise.then(() => {
        E === l && m();
      });
    }));
  }
  const g = {
    set: d,
    update: (v, w) => d(v(f, e), w),
    subscribe: n.subscribe,
    stiffness: r,
    damping: i,
    precision: s
  };
  return g;
}
function Qi(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var Yi = function(t) {
  return Ki(t) && !$i(t);
};
function Ki(e) {
  return !!e && typeof e == "object";
}
function $i(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || ns(e);
}
var es = typeof Symbol == "function" && Symbol.for, ts = es ? Symbol.for("react.element") : 60103;
function ns(e) {
  return e.$$typeof === ts;
}
function rs(e) {
  return Array.isArray(e) ? [] : {};
}
function Ve(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? Ne(rs(e), e, t) : e;
}
function is(e, t, n) {
  return e.concat(t).map(function(r) {
    return Ve(r, n);
  });
}
function ss(e, t) {
  if (!t.customMerge)
    return Ne;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : Ne;
}
function os(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function hn(e) {
  return Object.keys(e).concat(os(e));
}
function or(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function as(e, t) {
  return or(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function ls(e, t, n) {
  var r = {};
  return n.isMergeableObject(e) && hn(e).forEach(function(i) {
    r[i] = Ve(e[i], n);
  }), hn(t).forEach(function(i) {
    as(e, i) || (or(e, i) && n.isMergeableObject(t[i]) ? r[i] = ss(i, n)(e[i], t[i], n) : r[i] = Ve(t[i], n));
  }), r;
}
function Ne(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || is, n.isMergeableObject = n.isMergeableObject || Yi, n.cloneUnlessOtherwiseSpecified = Ve;
  var r = Array.isArray(t), i = Array.isArray(e), s = r === i;
  return s ? r ? n.arrayMerge(e, t, n) : ls(e, t, n) : Ve(t, n);
}
Ne.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(r, i) {
    return Ne(r, i, n);
  }, {});
};
var us = Ne, fs = us;
const cs = /* @__PURE__ */ Qi(fs);
var Ut = function(e, t) {
  return Ut = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, r) {
    n.__proto__ = r;
  } || function(n, r) {
    for (var i in r)
      Object.prototype.hasOwnProperty.call(r, i) && (n[i] = r[i]);
  }, Ut(e, t);
};
function gt(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  Ut(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var x = function() {
  return x = Object.assign || function(t) {
    for (var n, r = 1, i = arguments.length; r < i; r++) {
      n = arguments[r];
      for (var s in n)
        Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s]);
    }
    return t;
  }, x.apply(this, arguments);
};
function At(e, t, n) {
  if (n || arguments.length === 2)
    for (var r = 0, i = t.length, s; r < i; r++)
      (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)), s[r] = t[r]);
  return e.concat(s || Array.prototype.slice.call(t));
}
var N;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(N || (N = {}));
var M;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(M || (M = {}));
var Pe;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(Pe || (Pe = {}));
function _n(e) {
  return e.type === M.literal;
}
function hs(e) {
  return e.type === M.argument;
}
function ar(e) {
  return e.type === M.number;
}
function lr(e) {
  return e.type === M.date;
}
function ur(e) {
  return e.type === M.time;
}
function fr(e) {
  return e.type === M.select;
}
function cr(e) {
  return e.type === M.plural;
}
function _s(e) {
  return e.type === M.pound;
}
function hr(e) {
  return e.type === M.tag;
}
function _r(e) {
  return !!(e && typeof e == "object" && e.type === Pe.number);
}
function Ft(e) {
  return !!(e && typeof e == "object" && e.type === Pe.dateTime);
}
var dr = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, ds = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function ms(e) {
  var t = {};
  return e.replace(ds, function(n) {
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
var bs = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function ps(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(bs).filter(function(_) {
    return _.length > 0;
  }), n = [], r = 0, i = t; r < i.length; r++) {
    var s = i[r], a = s.split("/");
    if (a.length === 0)
      throw new Error("Invalid number skeleton");
    for (var o = a[0], l = a.slice(1), u = 0, f = l; u < f.length; u++) {
      var h = f[u];
      if (h.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: o, options: l });
  }
  return n;
}
function gs(e) {
  return e.replace(/^(.*?)-/, "");
}
var dn = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, mr = /^(@+)?(\+|#+)?[rs]?$/g, vs = /(\*)(0+)|(#+)(0+)|(0+)/g, br = /^(0+)$/;
function mn(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(mr, function(n, r, i) {
    return typeof i != "string" ? (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length) : i === "+" ? t.minimumSignificantDigits = r.length : r[0] === "#" ? t.maximumSignificantDigits = r.length : (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length + (typeof i == "string" ? i.length : 0)), "";
  }), t;
}
function pr(e) {
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
function ys(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !br.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function bn(e) {
  var t = {}, n = pr(e);
  return n || t;
}
function ws(e) {
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
        t.style = "unit", t.unit = gs(i.options[0]);
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
        t = x(x(x({}, t), { notation: "scientific" }), i.options.reduce(function(l, u) {
          return x(x({}, l), bn(u));
        }, {}));
        continue;
      case "engineering":
        t = x(x(x({}, t), { notation: "engineering" }), i.options.reduce(function(l, u) {
          return x(x({}, l), bn(u));
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
        i.options[0].replace(vs, function(l, u, f, h, _, b) {
          if (u)
            t.minimumIntegerDigits = f.length;
          else {
            if (h && _)
              throw new Error("We currently do not support maximum integer digits");
            if (b)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (br.test(i.stem)) {
      t.minimumIntegerDigits = i.stem.length;
      continue;
    }
    if (dn.test(i.stem)) {
      if (i.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      i.stem.replace(dn, function(l, u, f, h, _, b) {
        return f === "*" ? t.minimumFractionDigits = u.length : h && h[0] === "#" ? t.maximumFractionDigits = h.length : _ && b ? (t.minimumFractionDigits = _.length, t.maximumFractionDigits = _.length + b.length) : (t.minimumFractionDigits = u.length, t.maximumFractionDigits = u.length), "";
      });
      var s = i.options[0];
      s === "w" ? t = x(x({}, t), { trailingZeroDisplay: "stripIfInteger" }) : s && (t = x(x({}, t), mn(s)));
      continue;
    }
    if (mr.test(i.stem)) {
      t = x(x({}, t), mn(i.stem));
      continue;
    }
    var a = pr(i.stem);
    a && (t = x(x({}, t), a));
    var o = ys(i.stem);
    o && (t = x(x({}, t), o));
  }
  return t;
}
var Ke = {
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
function Es(e, t) {
  for (var n = "", r = 0; r < e.length; r++) {
    var i = e.charAt(r);
    if (i === "j") {
      for (var s = 0; r + 1 < e.length && e.charAt(r + 1) === i; )
        s++, r++;
      var a = 1 + (s & 1), o = s < 2 ? 1 : 3 + (s >> 1), l = "a", u = Ss(t);
      for ((u == "H" || u == "k") && (o = 0); o-- > 0; )
        n += l;
      for (; a-- > 0; )
        n = u + n;
    } else
      i === "J" ? n += "H" : n += i;
  }
  return n;
}
function Ss(e) {
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
  var i = Ke[r || ""] || Ke[n || ""] || Ke["".concat(n, "-001")] || Ke["001"];
  return i[0];
}
var Ht, Ts = new RegExp("^".concat(dr.source, "*")), Bs = new RegExp("".concat(dr.source, "*$"));
function P(e, t) {
  return { start: e, end: t };
}
var As = !!String.prototype.startsWith, Hs = !!String.fromCodePoint, Ns = !!Object.fromEntries, Ps = !!String.prototype.codePointAt, Is = !!String.prototype.trimStart, xs = !!String.prototype.trimEnd, Os = !!Number.isSafeInteger, Cs = Os ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, Gt = !0;
try {
  var Ls = vr("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Gt = ((Ht = Ls.exec("a")) === null || Ht === void 0 ? void 0 : Ht[0]) === "a";
} catch {
  Gt = !1;
}
var pn = As ? (
  // Native
  function(t, n, r) {
    return t.startsWith(n, r);
  }
) : (
  // For IE11
  function(t, n, r) {
    return t.slice(r, r + n.length) === n;
  }
), jt = Hs ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var r = "", i = t.length, s = 0, a; i > s; ) {
      if (a = t[s++], a > 1114111)
        throw RangeError(a + " is not a valid code point");
      r += a < 65536 ? String.fromCharCode(a) : String.fromCharCode(((a -= 65536) >> 10) + 55296, a % 1024 + 56320);
    }
    return r;
  }
), gn = (
  // native
  Ns ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, r = 0, i = t; r < i.length; r++) {
        var s = i[r], a = s[0], o = s[1];
        n[a] = o;
      }
      return n;
    }
  )
), gr = Ps ? (
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
), Ms = Is ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Ts, "");
  }
), Rs = xs ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Bs, "");
  }
);
function vr(e, t) {
  return new RegExp(e, t);
}
var Vt;
if (Gt) {
  var vn = vr("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Vt = function(t, n) {
    var r;
    vn.lastIndex = n;
    var i = vn.exec(t);
    return (r = i[1]) !== null && r !== void 0 ? r : "";
  };
} else
  Vt = function(t, n) {
    for (var r = []; ; ) {
      var i = gr(t, n);
      if (i === void 0 || yr(i) || Fs(i))
        break;
      r.push(i), n += i >= 65536 ? 2 : 1;
    }
    return jt.apply(void 0, r);
  };
var ks = (
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
          var a = this.parseArgument(t, r);
          if (a.err)
            return a;
          i.push(a.val);
        } else {
          if (s === 125 && t > 0)
            break;
          if (s === 35 && (n === "plural" || n === "selectordinal")) {
            var o = this.clonePosition();
            this.bump(), i.push({
              type: M.pound,
              location: P(o, this.clonePosition())
            });
          } else if (s === 60 && !this.ignoreTag && this.peek() === 47) {
            if (r)
              break;
            return this.error(N.UNMATCHED_CLOSING_TAG, P(this.clonePosition(), this.clonePosition()));
          } else if (s === 60 && !this.ignoreTag && qt(this.peek() || 0)) {
            var a = this.parseTag(t, n);
            if (a.err)
              return a;
            i.push(a.val);
          } else {
            var a = this.parseLiteral(t, n);
            if (a.err)
              return a;
            i.push(a.val);
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
            type: M.literal,
            value: "<".concat(i, "/>"),
            location: P(r, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var s = this.parseMessage(t + 1, n, !0);
        if (s.err)
          return s;
        var a = s.val, o = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !qt(this.char()))
            return this.error(N.INVALID_TAG, P(o, this.clonePosition()));
          var l = this.clonePosition(), u = this.parseTagName();
          return i !== u ? this.error(N.UNMATCHED_CLOSING_TAG, P(l, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: M.tag,
              value: i,
              children: a,
              location: P(r, this.clonePosition())
            },
            err: null
          } : this.error(N.INVALID_TAG, P(o, this.clonePosition())));
        } else
          return this.error(N.UNCLOSED_TAG, P(r, this.clonePosition()));
      } else
        return this.error(N.INVALID_TAG, P(r, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && Us(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var r = this.clonePosition(), i = ""; ; ) {
        var s = this.tryParseQuote(n);
        if (s) {
          i += s;
          continue;
        }
        var a = this.tryParseUnquoted(t, n);
        if (a) {
          i += a;
          continue;
        }
        var o = this.tryParseLeftAngleBracket();
        if (o) {
          i += o;
          continue;
        }
        break;
      }
      var l = P(r, this.clonePosition());
      return {
        val: { type: M.literal, value: i, location: l },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !Ds(this.peek() || 0)) ? (this.bump(), "<") : null;
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
      return jt.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var r = this.char();
      return r === 60 || r === 123 || r === 35 && (n === "plural" || n === "selectordinal") || r === 125 && t > 0 ? null : (this.bump(), jt(r));
    }, e.prototype.parseArgument = function(t, n) {
      var r = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, P(r, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(N.EMPTY_ARGUMENT, P(r, this.clonePosition()));
      var i = this.parseIdentifierIfPossible().value;
      if (!i)
        return this.error(N.MALFORMED_ARGUMENT, P(r, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, P(r, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: M.argument,
              // value does not include the opening and closing braces.
              value: i,
              location: P(r, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, P(r, this.clonePosition())) : this.parseArgumentOptions(t, n, i, r);
        default:
          return this.error(N.MALFORMED_ARGUMENT, P(r, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), r = Vt(this.message, n), i = n + r.length;
      this.bumpTo(i);
      var s = this.clonePosition(), a = P(t, s);
      return { value: r, location: a };
    }, e.prototype.parseArgumentOptions = function(t, n, r, i) {
      var s, a = this.clonePosition(), o = this.parseIdentifierIfPossible().value, l = this.clonePosition();
      switch (o) {
        case "":
          return this.error(N.EXPECT_ARGUMENT_TYPE, P(a, l));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var u = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), h = this.parseSimpleArgStyleIfPossible();
            if (h.err)
              return h;
            var _ = Rs(h.val);
            if (_.length === 0)
              return this.error(N.EXPECT_ARGUMENT_STYLE, P(this.clonePosition(), this.clonePosition()));
            var b = P(f, this.clonePosition());
            u = { style: _, styleLocation: b };
          }
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var g = P(i, this.clonePosition());
          if (u && pn(u == null ? void 0 : u.style, "::", 0)) {
            var v = Ms(u.style.slice(2));
            if (o === "number") {
              var h = this.parseNumberSkeletonFromString(v, u.styleLocation);
              return h.err ? h : {
                val: { type: M.number, value: r, location: g, style: h.val },
                err: null
              };
            } else {
              if (v.length === 0)
                return this.error(N.EXPECT_DATE_TIME_SKELETON, g);
              var w = v;
              this.locale && (w = Es(v, this.locale));
              var _ = {
                type: Pe.dateTime,
                pattern: w,
                location: u.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? ms(w) : {}
              }, E = o === "date" ? M.date : M.time;
              return {
                val: { type: E, value: r, location: g, style: _ },
                err: null
              };
            }
          }
          return {
            val: {
              type: o === "number" ? M.number : o === "date" ? M.date : M.time,
              value: r,
              location: g,
              style: (s = u == null ? void 0 : u.style) !== null && s !== void 0 ? s : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var m = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(N.EXPECT_SELECT_ARGUMENT_OPTIONS, P(m, x({}, m)));
          this.bumpSpace();
          var c = this.parseIdentifierIfPossible(), p = 0;
          if (o !== "select" && c.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(N.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, P(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var h = this.tryParseDecimalInteger(N.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, N.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (h.err)
              return h;
            this.bumpSpace(), c = this.parseIdentifierIfPossible(), p = h.val;
          }
          var U = this.tryParsePluralOrSelectOptions(t, o, n, c);
          if (U.err)
            return U;
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var D = P(i, this.clonePosition());
          return o === "select" ? {
            val: {
              type: M.select,
              value: r,
              options: gn(U.val),
              location: D
            },
            err: null
          } : {
            val: {
              type: M.plural,
              value: r,
              options: gn(U.val),
              offset: p,
              pluralType: o === "plural" ? "cardinal" : "ordinal",
              location: D
            },
            err: null
          };
        }
        default:
          return this.error(N.INVALID_ARGUMENT_TYPE, P(a, l));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(N.EXPECT_ARGUMENT_CLOSING_BRACE, P(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var r = this.char();
        switch (r) {
          case 39: {
            this.bump();
            var i = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(N.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, P(i, this.clonePosition()));
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
        r = ps(t);
      } catch {
        return this.error(N.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: Pe.number,
          tokens: r,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? ws(r) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, r, i) {
      for (var s, a = !1, o = [], l = /* @__PURE__ */ new Set(), u = i.value, f = i.location; ; ) {
        if (u.length === 0) {
          var h = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var _ = this.tryParseDecimalInteger(N.EXPECT_PLURAL_ARGUMENT_SELECTOR, N.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (_.err)
              return _;
            f = P(h, this.clonePosition()), u = this.message.slice(h.offset, this.offset());
          } else
            break;
        }
        if (l.has(u))
          return this.error(n === "select" ? N.DUPLICATE_SELECT_ARGUMENT_SELECTOR : N.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        u === "other" && (a = !0), this.bumpSpace();
        var b = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? N.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : N.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, P(this.clonePosition(), this.clonePosition()));
        var d = this.parseMessage(t + 1, n, r);
        if (d.err)
          return d;
        var g = this.tryParseArgumentClose(b);
        if (g.err)
          return g;
        o.push([
          u,
          {
            value: d.val,
            location: P(b, this.clonePosition())
          }
        ]), l.add(u), this.bumpSpace(), s = this.parseIdentifierIfPossible(), u = s.value, f = s.location;
      }
      return o.length === 0 ? this.error(n === "select" ? N.EXPECT_SELECT_ARGUMENT_SELECTOR : N.EXPECT_PLURAL_ARGUMENT_SELECTOR, P(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !a ? this.error(N.MISSING_OTHER_CLAUSE, P(this.clonePosition(), this.clonePosition())) : { val: o, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var r = 1, i = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (r = -1);
      for (var s = !1, a = 0; !this.isEOF(); ) {
        var o = this.char();
        if (o >= 48 && o <= 57)
          s = !0, a = a * 10 + (o - 48), this.bump();
        else
          break;
      }
      var l = P(i, this.clonePosition());
      return s ? (a *= r, Cs(a) ? { val: a, err: null } : this.error(n, l)) : this.error(t, l);
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
      var n = gr(this.message, t);
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
      if (pn(this.message, t, this.offset())) {
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
      for (; !this.isEOF() && yr(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), r = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return r ?? null;
    }, e;
  }()
);
function qt(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Ds(e) {
  return qt(e) || e === 47;
}
function Us(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function yr(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function Fs(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function zt(e) {
  e.forEach(function(t) {
    if (delete t.location, fr(t) || cr(t))
      for (var n in t.options)
        delete t.options[n].location, zt(t.options[n].value);
    else
      ar(t) && _r(t.style) || (lr(t) || ur(t)) && Ft(t.style) ? delete t.style.location : hr(t) && zt(t.children);
  });
}
function Gs(e, t) {
  t === void 0 && (t = {}), t = x({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new ks(e, t).parse();
  if (n.err) {
    var r = SyntaxError(N[n.err.kind]);
    throw r.location = n.err.location, r.originalMessage = n.err.message, r;
  }
  return t != null && t.captureLocation || zt(n.val), n.val;
}
function Nt(e, t) {
  var n = t && t.cache ? t.cache : Ws, r = t && t.serializer ? t.serializer : Xs, i = t && t.strategy ? t.strategy : Vs;
  return i(e, {
    cache: n,
    serializer: r
  });
}
function js(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function wr(e, t, n, r) {
  var i = js(r) ? r : n(r), s = t.get(i);
  return typeof s > "u" && (s = e.call(this, r), t.set(i, s)), s;
}
function Er(e, t, n) {
  var r = Array.prototype.slice.call(arguments, 3), i = n(r), s = t.get(i);
  return typeof s > "u" && (s = e.apply(this, r), t.set(i, s)), s;
}
function en(e, t, n, r, i) {
  return n.bind(t, e, r, i);
}
function Vs(e, t) {
  var n = e.length === 1 ? wr : Er;
  return en(e, this, n, t.cache.create(), t.serializer);
}
function qs(e, t) {
  return en(e, this, Er, t.cache.create(), t.serializer);
}
function zs(e, t) {
  return en(e, this, wr, t.cache.create(), t.serializer);
}
var Xs = function() {
  return JSON.stringify(arguments);
};
function tn() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
tn.prototype.get = function(e) {
  return this.cache[e];
};
tn.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var Ws = {
  create: function() {
    return new tn();
  }
}, Pt = {
  variadic: qs,
  monadic: zs
}, Ie;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(Ie || (Ie = {}));
var vt = (
  /** @class */
  function(e) {
    gt(t, e);
    function t(n, r, i) {
      var s = e.call(this, n) || this;
      return s.code = r, s.originalMessage = i, s;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), yn = (
  /** @class */
  function(e) {
    gt(t, e);
    function t(n, r, i, s) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(r, '". Options are "').concat(Object.keys(i).join('", "'), '"'), Ie.INVALID_VALUE, s) || this;
    }
    return t;
  }(vt)
), Zs = (
  /** @class */
  function(e) {
    gt(t, e);
    function t(n, r, i) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(r), Ie.INVALID_VALUE, i) || this;
    }
    return t;
  }(vt)
), Js = (
  /** @class */
  function(e) {
    gt(t, e);
    function t(n, r) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(r, '"'), Ie.MISSING_VALUE, r) || this;
    }
    return t;
  }(vt)
), q;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(q || (q = {}));
function Qs(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var r = t[t.length - 1];
    return !r || r.type !== q.literal || n.type !== q.literal ? t.push(n) : r.value += n.value, t;
  }, []);
}
function Ys(e) {
  return typeof e == "function";
}
function st(e, t, n, r, i, s, a) {
  if (e.length === 1 && _n(e[0]))
    return [
      {
        type: q.literal,
        value: e[0].value
      }
    ];
  for (var o = [], l = 0, u = e; l < u.length; l++) {
    var f = u[l];
    if (_n(f)) {
      o.push({
        type: q.literal,
        value: f.value
      });
      continue;
    }
    if (_s(f)) {
      typeof s == "number" && o.push({
        type: q.literal,
        value: n.getNumberFormat(t).format(s)
      });
      continue;
    }
    var h = f.value;
    if (!(i && h in i))
      throw new Js(h, a);
    var _ = i[h];
    if (hs(f)) {
      (!_ || typeof _ == "string" || typeof _ == "number") && (_ = typeof _ == "string" || typeof _ == "number" ? String(_) : ""), o.push({
        type: typeof _ == "string" ? q.literal : q.object,
        value: _
      });
      continue;
    }
    if (lr(f)) {
      var b = typeof f.style == "string" ? r.date[f.style] : Ft(f.style) ? f.style.parsedOptions : void 0;
      o.push({
        type: q.literal,
        value: n.getDateTimeFormat(t, b).format(_)
      });
      continue;
    }
    if (ur(f)) {
      var b = typeof f.style == "string" ? r.time[f.style] : Ft(f.style) ? f.style.parsedOptions : r.time.medium;
      o.push({
        type: q.literal,
        value: n.getDateTimeFormat(t, b).format(_)
      });
      continue;
    }
    if (ar(f)) {
      var b = typeof f.style == "string" ? r.number[f.style] : _r(f.style) ? f.style.parsedOptions : void 0;
      b && b.scale && (_ = _ * (b.scale || 1)), o.push({
        type: q.literal,
        value: n.getNumberFormat(t, b).format(_)
      });
      continue;
    }
    if (hr(f)) {
      var d = f.children, g = f.value, v = i[g];
      if (!Ys(v))
        throw new Zs(g, "function", a);
      var w = st(d, t, n, r, i, s), E = v(w.map(function(p) {
        return p.value;
      }));
      Array.isArray(E) || (E = [E]), o.push.apply(o, E.map(function(p) {
        return {
          type: typeof p == "string" ? q.literal : q.object,
          value: p
        };
      }));
    }
    if (fr(f)) {
      var m = f.options[_] || f.options.other;
      if (!m)
        throw new yn(f.value, _, Object.keys(f.options), a);
      o.push.apply(o, st(m.value, t, n, r, i));
      continue;
    }
    if (cr(f)) {
      var m = f.options["=".concat(_)];
      if (!m) {
        if (!Intl.PluralRules)
          throw new vt(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, Ie.MISSING_INTL_API, a);
        var c = n.getPluralRules(t, { type: f.pluralType }).select(_ - (f.offset || 0));
        m = f.options[c] || f.options.other;
      }
      if (!m)
        throw new yn(f.value, _, Object.keys(f.options), a);
      o.push.apply(o, st(m.value, t, n, r, i, _ - (f.offset || 0)));
      continue;
    }
  }
  return Qs(o);
}
function Ks(e, t) {
  return t ? x(x(x({}, e || {}), t || {}), Object.keys(e).reduce(function(n, r) {
    return n[r] = x(x({}, e[r]), t[r] || {}), n;
  }, {})) : e;
}
function $s(e, t) {
  return t ? Object.keys(e).reduce(function(n, r) {
    return n[r] = Ks(e[r], t[r]), n;
  }, x({}, e)) : e;
}
function It(e) {
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
function eo(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Nt(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.NumberFormat).bind.apply(t, At([void 0], n, !1)))();
    }, {
      cache: It(e.number),
      strategy: Pt.variadic
    }),
    getDateTimeFormat: Nt(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, At([void 0], n, !1)))();
    }, {
      cache: It(e.dateTime),
      strategy: Pt.variadic
    }),
    getPluralRules: Nt(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.PluralRules).bind.apply(t, At([void 0], n, !1)))();
    }, {
      cache: It(e.pluralRules),
      strategy: Pt.variadic
    })
  };
}
var to = (
  /** @class */
  function() {
    function e(t, n, r, i) {
      var s = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(a) {
        var o = s.formatToParts(a);
        if (o.length === 1)
          return o[0].value;
        var l = o.reduce(function(u, f) {
          return !u.length || f.type !== q.literal || typeof u[u.length - 1] != "string" ? u.push(f.value) : u[u.length - 1] += f.value, u;
        }, []);
        return l.length <= 1 ? l[0] || "" : l;
      }, this.formatToParts = function(a) {
        return st(s.ast, s.locales, s.formatters, s.formats, a, void 0, s.message);
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
      this.formats = $s(e.formats, r), this.formatters = i && i.formatters || eo(this.formatterCache);
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
    }, e.__parse = Gs, e.formats = {
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
function no(e, t) {
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
const me = {}, ro = (e, t, n) => n && (t in me || (me[t] = {}), e in me[t] || (me[t][e] = n), n), Sr = (e, t) => {
  if (t == null)
    return;
  if (t in me && e in me[t])
    return me[t][e];
  const n = yt(t);
  for (let r = 0; r < n.length; r++) {
    const i = n[r], s = so(i, e);
    if (s)
      return ro(e, t, s);
  }
};
let nn;
const Xe = ze({});
function io(e) {
  return nn[e] || null;
}
function Tr(e) {
  return e in nn;
}
function so(e, t) {
  if (!Tr(e))
    return null;
  const n = io(e);
  return no(n, t);
}
function oo(e) {
  if (e == null)
    return;
  const t = yt(e);
  for (let n = 0; n < t.length; n++) {
    const r = t[n];
    if (Tr(r))
      return r;
  }
}
function ao(e, ...t) {
  delete me[e], Xe.update((n) => (n[e] = cs.all([n[e] || {}, ...t]), n));
}
Le(
  [Xe],
  ([e]) => Object.keys(e)
);
Xe.subscribe((e) => nn = e);
const ot = {};
function lo(e, t) {
  ot[e].delete(t), ot[e].size === 0 && delete ot[e];
}
function Br(e) {
  return ot[e];
}
function uo(e) {
  return yt(e).map((t) => {
    const n = Br(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function Xt(e) {
  return e == null ? !1 : yt(e).some(
    (t) => {
      var n;
      return (n = Br(t)) == null ? void 0 : n.size;
    }
  );
}
function fo(e, t) {
  return Promise.all(
    t.map((r) => (lo(e, r), r().then((i) => i.default || i)))
  ).then((r) => ao(e, ...r));
}
const De = {};
function Ar(e) {
  if (!Xt(e))
    return e in De ? De[e] : Promise.resolve();
  const t = uo(e);
  return De[e] = Promise.all(
    t.map(
      ([n, r]) => fo(n, r)
    )
  ).then(() => {
    if (Xt(e))
      return Ar(e);
    delete De[e];
  }), De[e];
}
const co = {
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
}, ho = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: co,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, _o = ho;
function xe() {
  return _o;
}
const xt = ze(!1);
var mo = Object.defineProperty, bo = Object.defineProperties, po = Object.getOwnPropertyDescriptors, wn = Object.getOwnPropertySymbols, go = Object.prototype.hasOwnProperty, vo = Object.prototype.propertyIsEnumerable, En = (e, t, n) => t in e ? mo(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, yo = (e, t) => {
  for (var n in t || (t = {}))
    go.call(t, n) && En(e, n, t[n]);
  if (wn)
    for (var n of wn(t))
      vo.call(t, n) && En(e, n, t[n]);
  return e;
}, wo = (e, t) => bo(e, po(t));
let Wt;
const ut = ze(null);
function Sn(e) {
  return e.split("-").map((t, n, r) => r.slice(0, n + 1).join("-")).reverse();
}
function yt(e, t = xe().fallbackLocale) {
  const n = Sn(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Sn(t)])] : n;
}
function ye() {
  return Wt ?? void 0;
}
ut.subscribe((e) => {
  Wt = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const Eo = (e) => {
  if (e && oo(e) && Xt(e)) {
    const { loadingDelay: t } = xe();
    let n;
    return typeof window < "u" && ye() != null && t ? n = window.setTimeout(
      () => xt.set(!0),
      t
    ) : xt.set(!0), Ar(e).then(() => {
      ut.set(e);
    }).finally(() => {
      clearTimeout(n), xt.set(!1);
    });
  }
  return ut.set(e);
}, We = wo(yo({}, ut), {
  set: Eo
}), wt = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (r) => {
    const i = JSON.stringify(r);
    return i in t ? t[i] : t[i] = e(r);
  };
};
var So = Object.defineProperty, ft = Object.getOwnPropertySymbols, Hr = Object.prototype.hasOwnProperty, Nr = Object.prototype.propertyIsEnumerable, Tn = (e, t, n) => t in e ? So(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, rn = (e, t) => {
  for (var n in t || (t = {}))
    Hr.call(t, n) && Tn(e, n, t[n]);
  if (ft)
    for (var n of ft(t))
      Nr.call(t, n) && Tn(e, n, t[n]);
  return e;
}, Me = (e, t) => {
  var n = {};
  for (var r in e)
    Hr.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
  if (e != null && ft)
    for (var r of ft(e))
      t.indexOf(r) < 0 && Nr.call(e, r) && (n[r] = e[r]);
  return n;
};
const qe = (e, t) => {
  const { formats: n } = xe();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, To = wt(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = Me(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return r && (i = qe("number", r)), new Intl.NumberFormat(n, i);
  }
), Bo = wt(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = Me(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return r ? i = qe("date", r) : Object.keys(i).length === 0 && (i = qe("date", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ao = wt(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = Me(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return r ? i = qe("time", r) : Object.keys(i).length === 0 && (i = qe("time", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ho = (e = {}) => {
  var t = e, {
    locale: n = ye()
  } = t, r = Me(t, [
    "locale"
  ]);
  return To(rn({ locale: n }, r));
}, No = (e = {}) => {
  var t = e, {
    locale: n = ye()
  } = t, r = Me(t, [
    "locale"
  ]);
  return Bo(rn({ locale: n }, r));
}, Po = (e = {}) => {
  var t = e, {
    locale: n = ye()
  } = t, r = Me(t, [
    "locale"
  ]);
  return Ao(rn({ locale: n }, r));
}, Io = wt(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = ye()) => new to(e, t, xe().formats, {
    ignoreTag: xe().ignoreTag
  })
), xo = (e, t = {}) => {
  var n, r, i, s;
  let a = t;
  typeof e == "object" && (a = e, e = a.id);
  const {
    values: o,
    locale: l = ye(),
    default: u
  } = a;
  if (l == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = Sr(e, l);
  if (!f)
    f = (s = (i = (r = (n = xe()).handleMissingMessage) == null ? void 0 : r.call(n, { locale: l, id: e, defaultValue: u })) != null ? i : u) != null ? s : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!o)
    return f;
  let h = f;
  try {
    h = Io(f, l).format(o);
  } catch (_) {
    _ instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      _.message
    );
  }
  return h;
}, Oo = (e, t) => Po(t).format(e), Co = (e, t) => No(t).format(e), Lo = (e, t) => Ho(t).format(e), Mo = (e, t = ye()) => Sr(e, t), Ro = Le([We, Xe], () => xo);
Le([We], () => Oo);
Le([We], () => Co);
Le([We], () => Lo);
Le([We, Xe], () => Mo);
Wi(Ro);
function Te(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let r = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + r;
}
const {
  SvelteComponent: ko,
  append: ie,
  attr: I,
  component_subscribe: Bn,
  detach: Do,
  element: Uo,
  init: Fo,
  insert: Go,
  noop: An,
  safe_not_equal: jo,
  set_style: $e,
  svg_element: se,
  toggle_class: Hn
} = window.__gradio__svelte__internal, { onMount: Vo } = window.__gradio__svelte__internal;
function qo(e) {
  let t, n, r, i, s, a, o, l, u, f, h, _;
  return {
    c() {
      t = Uo("div"), n = se("svg"), r = se("g"), i = se("path"), s = se("path"), a = se("path"), o = se("path"), l = se("g"), u = se("path"), f = se("path"), h = se("path"), _ = se("path"), I(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), I(i, "fill", "#FF7C00"), I(i, "fill-opacity", "0.4"), I(i, "class", "svelte-43sxxs"), I(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), I(s, "fill", "#FF7C00"), I(s, "class", "svelte-43sxxs"), I(a, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), I(a, "fill", "#FF7C00"), I(a, "fill-opacity", "0.4"), I(a, "class", "svelte-43sxxs"), I(o, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), I(o, "fill", "#FF7C00"), I(o, "class", "svelte-43sxxs"), $e(r, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), I(u, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), I(u, "fill", "#FF7C00"), I(u, "fill-opacity", "0.4"), I(u, "class", "svelte-43sxxs"), I(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), I(f, "fill", "#FF7C00"), I(f, "class", "svelte-43sxxs"), I(h, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), I(h, "fill", "#FF7C00"), I(h, "fill-opacity", "0.4"), I(h, "class", "svelte-43sxxs"), I(_, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), I(_, "fill", "#FF7C00"), I(_, "class", "svelte-43sxxs"), $e(l, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), I(n, "viewBox", "-1200 -1200 3000 3000"), I(n, "fill", "none"), I(n, "xmlns", "http://www.w3.org/2000/svg"), I(n, "class", "svelte-43sxxs"), I(t, "class", "svelte-43sxxs"), Hn(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(b, d) {
      Go(b, t, d), ie(t, n), ie(n, r), ie(r, i), ie(r, s), ie(r, a), ie(r, o), ie(n, l), ie(l, u), ie(l, f), ie(l, h), ie(l, _);
    },
    p(b, [d]) {
      d & /*$top*/
      2 && $e(r, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), d & /*$bottom*/
      4 && $e(l, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), d & /*margin*/
      1 && Hn(
        t,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: An,
    o: An,
    d(b) {
      b && Do(t);
    }
  };
}
function zo(e, t, n) {
  let r, i, { margin: s = !0 } = t;
  const a = cn([0, 0]);
  Bn(e, a, (_) => n(1, r = _));
  const o = cn([0, 0]);
  Bn(e, o, (_) => n(2, i = _));
  let l;
  async function u() {
    await Promise.all([a.set([125, 140]), o.set([-125, -140])]), await Promise.all([a.set([-125, 140]), o.set([125, -140])]), await Promise.all([a.set([-125, 0]), o.set([125, -0])]), await Promise.all([a.set([125, 0]), o.set([-125, 0])]);
  }
  async function f() {
    await u(), l || f();
  }
  async function h() {
    await Promise.all([a.set([125, 0]), o.set([-125, 0])]), f();
  }
  return Vo(() => (h(), () => l = !0)), e.$$set = (_) => {
    "margin" in _ && n(0, s = _.margin);
  }, [s, r, i, a, o];
}
class Xo extends ko {
  constructor(t) {
    super(), Fo(this, t, zo, qo, jo, { margin: 0 });
  }
}
const {
  SvelteComponent: Wo,
  append: ge,
  attr: le,
  binding_callbacks: Nn,
  check_outros: Pr,
  create_component: Zo,
  create_slot: Jo,
  destroy_component: Qo,
  destroy_each: Ir,
  detach: T,
  element: ce,
  empty: Re,
  ensure_array_like: ct,
  get_all_dirty_from_scope: Yo,
  get_slot_changes: Ko,
  group_outros: xr,
  init: $o,
  insert: B,
  mount_component: ea,
  noop: Zt,
  safe_not_equal: ta,
  set_data: te,
  set_style: be,
  space: ue,
  text: k,
  toggle_class: ee,
  transition_in: Oe,
  transition_out: Ce,
  update_slot_base: na
} = window.__gradio__svelte__internal, { tick: ra } = window.__gradio__svelte__internal, { onDestroy: ia } = window.__gradio__svelte__internal, sa = (e) => ({}), Pn = (e) => ({});
function In(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r[40] = n, r;
}
function xn(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r;
}
function oa(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), r, i, s;
  const a = (
    /*#slots*/
    e[29].error
  ), o = Jo(
    a,
    e,
    /*$$scope*/
    e[28],
    Pn
  );
  return {
    c() {
      t = ce("span"), r = k(n), i = ue(), o && o.c(), le(t, "class", "error svelte-14miwb5");
    },
    m(l, u) {
      B(l, t, u), ge(t, r), B(l, i, u), o && o.m(l, u), s = !0;
    },
    p(l, u) {
      (!s || u[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      l[1]("common.error") + "") && te(r, n), o && o.p && (!s || u[0] & /*$$scope*/
      268435456) && na(
        o,
        a,
        l,
        /*$$scope*/
        l[28],
        s ? Ko(
          a,
          /*$$scope*/
          l[28],
          u,
          sa
        ) : Yo(
          /*$$scope*/
          l[28]
        ),
        Pn
      );
    },
    i(l) {
      s || (Oe(o, l), s = !0);
    },
    o(l) {
      Ce(o, l), s = !1;
    },
    d(l) {
      l && (T(t), T(i)), o && o.d(l);
    }
  };
}
function aa(e) {
  let t, n, r, i, s, a, o, l, u, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && On(e)
  );
  function h(m, c) {
    if (
      /*progress*/
      m[7]
    )
      return fa;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return ua;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return la;
  }
  let _ = h(e), b = _ && _(e), d = (
    /*timer*/
    e[5] && Mn(e)
  );
  const g = [da, _a], v = [];
  function w(m, c) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = w(e)) && (a = v[s] = g[s](e));
  let E = !/*timer*/
  e[5] && jn(e);
  return {
    c() {
      f && f.c(), t = ue(), n = ce("div"), b && b.c(), r = ue(), d && d.c(), i = ue(), a && a.c(), o = ue(), E && E.c(), l = Re(), le(n, "class", "progress-text svelte-14miwb5"), ee(
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
    m(m, c) {
      f && f.m(m, c), B(m, t, c), B(m, n, c), b && b.m(n, null), ge(n, r), d && d.m(n, null), B(m, i, c), ~s && v[s].m(m, c), B(m, o, c), E && E.m(m, c), B(m, l, c), u = !0;
    },
    p(m, c) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? f ? f.p(m, c) : (f = On(m), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), _ === (_ = h(m)) && b ? b.p(m, c) : (b && b.d(1), b = _ && _(m), b && (b.c(), b.m(n, r))), /*timer*/
      m[5] ? d ? d.p(m, c) : (d = Mn(m), d.c(), d.m(n, null)) : d && (d.d(1), d = null), (!u || c[0] & /*variant*/
      256) && ee(
        n,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!u || c[0] & /*variant*/
      256) && ee(
        n,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let p = s;
      s = w(m), s === p ? ~s && v[s].p(m, c) : (a && (xr(), Ce(v[p], 1, 1, () => {
        v[p] = null;
      }), Pr()), ~s ? (a = v[s], a ? a.p(m, c) : (a = v[s] = g[s](m), a.c()), Oe(a, 1), a.m(o.parentNode, o)) : a = null), /*timer*/
      m[5] ? E && (E.d(1), E = null) : E ? E.p(m, c) : (E = jn(m), E.c(), E.m(l.parentNode, l));
    },
    i(m) {
      u || (Oe(a), u = !0);
    },
    o(m) {
      Ce(a), u = !1;
    },
    d(m) {
      m && (T(t), T(n), T(i), T(o), T(l)), f && f.d(m), b && b.d(), d && d.d(), ~s && v[s].d(m), E && E.d(m);
    }
  };
}
function On(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = ce("div"), le(t, "class", "eta-bar svelte-14miwb5"), be(t, "transform", n);
    },
    m(r, i) {
      B(r, t, i);
    },
    p(r, i) {
      i[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (r[17] || 0) * 100 - 100}%)`) && be(t, "transform", n);
    },
    d(r) {
      r && T(t);
    }
  };
}
function la(e) {
  let t;
  return {
    c() {
      t = k("processing |");
    },
    m(n, r) {
      B(n, t, r);
    },
    p: Zt,
    d(n) {
      n && T(t);
    }
  };
}
function ua(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), r, i, s, a;
  return {
    c() {
      t = k("queue: "), r = k(n), i = k("/"), s = k(
        /*queue_size*/
        e[3]
      ), a = k(" |");
    },
    m(o, l) {
      B(o, t, l), B(o, r, l), B(o, i, l), B(o, s, l), B(o, a, l);
    },
    p(o, l) {
      l[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      o[2] + 1 + "") && te(r, n), l[0] & /*queue_size*/
      8 && te(
        s,
        /*queue_size*/
        o[3]
      );
    },
    d(o) {
      o && (T(t), T(r), T(i), T(s), T(a));
    }
  };
}
function fa(e) {
  let t, n = ct(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = Ln(xn(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = Re();
    },
    m(i, s) {
      for (let a = 0; a < r.length; a += 1)
        r[a] && r[a].m(i, s);
      B(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        n = ct(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < n.length; a += 1) {
          const o = xn(i, n, a);
          r[a] ? r[a].p(o, s) : (r[a] = Ln(o), r[a].c(), r[a].m(t.parentNode, t));
        }
        for (; a < r.length; a += 1)
          r[a].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && T(t), Ir(r, i);
    }
  };
}
function Cn(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), r, i, s = " ", a;
  function o(f, h) {
    return (
      /*p*/
      f[38].length != null ? ha : ca
    );
  }
  let l = o(e), u = l(e);
  return {
    c() {
      u.c(), t = ue(), r = k(n), i = k(" | "), a = k(s);
    },
    m(f, h) {
      u.m(f, h), B(f, t, h), B(f, r, h), B(f, i, h), B(f, a, h);
    },
    p(f, h) {
      l === (l = o(f)) && u ? u.p(f, h) : (u.d(1), u = l(f), u && (u.c(), u.m(t.parentNode, t))), h[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && te(r, n);
    },
    d(f) {
      f && (T(t), T(r), T(i), T(a)), u.d(f);
    }
  };
}
function ca(e) {
  let t = Te(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = k(t);
    },
    m(r, i) {
      B(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = Te(
        /*p*/
        r[38].index || 0
      ) + "") && te(n, t);
    },
    d(r) {
      r && T(n);
    }
  };
}
function ha(e) {
  let t = Te(
    /*p*/
    e[38].index || 0
  ) + "", n, r, i = Te(
    /*p*/
    e[38].length
  ) + "", s;
  return {
    c() {
      n = k(t), r = k("/"), s = k(i);
    },
    m(a, o) {
      B(a, n, o), B(a, r, o), B(a, s, o);
    },
    p(a, o) {
      o[0] & /*progress*/
      128 && t !== (t = Te(
        /*p*/
        a[38].index || 0
      ) + "") && te(n, t), o[0] & /*progress*/
      128 && i !== (i = Te(
        /*p*/
        a[38].length
      ) + "") && te(s, i);
    },
    d(a) {
      a && (T(n), T(r), T(s));
    }
  };
}
function Ln(e) {
  let t, n = (
    /*p*/
    e[38].index != null && Cn(e)
  );
  return {
    c() {
      n && n.c(), t = Re();
    },
    m(r, i) {
      n && n.m(r, i), B(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].index != null ? n ? n.p(r, i) : (n = Cn(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && T(t), n && n.d(r);
    }
  };
}
function Mn(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), r, i;
  return {
    c() {
      t = k(
        /*formatted_timer*/
        e[20]
      ), r = k(n), i = k("s");
    },
    m(s, a) {
      B(s, t, a), B(s, r, a), B(s, i, a);
    },
    p(s, a) {
      a[0] & /*formatted_timer*/
      1048576 && te(
        t,
        /*formatted_timer*/
        s[20]
      ), a[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && te(r, n);
    },
    d(s) {
      s && (T(t), T(r), T(i));
    }
  };
}
function _a(e) {
  let t, n;
  return t = new Xo({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      Zo(t.$$.fragment);
    },
    m(r, i) {
      ea(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      r[8] === "default"), t.$set(s);
    },
    i(r) {
      n || (Oe(t.$$.fragment, r), n = !0);
    },
    o(r) {
      Ce(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Qo(t, r);
    }
  };
}
function da(e) {
  let t, n, r, i, s, a = `${/*last_progress_level*/
  e[15] * 100}%`, o = (
    /*progress*/
    e[7] != null && Rn(e)
  );
  return {
    c() {
      t = ce("div"), n = ce("div"), o && o.c(), r = ue(), i = ce("div"), s = ce("div"), le(n, "class", "progress-level-inner svelte-14miwb5"), le(s, "class", "progress-bar svelte-14miwb5"), be(s, "width", a), le(i, "class", "progress-bar-wrap svelte-14miwb5"), le(t, "class", "progress-level svelte-14miwb5");
    },
    m(l, u) {
      B(l, t, u), ge(t, n), o && o.m(n, null), ge(t, r), ge(t, i), ge(i, s), e[30](s);
    },
    p(l, u) {
      /*progress*/
      l[7] != null ? o ? o.p(l, u) : (o = Rn(l), o.c(), o.m(n, null)) : o && (o.d(1), o = null), u[0] & /*last_progress_level*/
      32768 && a !== (a = `${/*last_progress_level*/
      l[15] * 100}%`) && be(s, "width", a);
    },
    i: Zt,
    o: Zt,
    d(l) {
      l && T(t), o && o.d(), e[30](null);
    }
  };
}
function Rn(e) {
  let t, n = ct(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = Gn(In(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = Re();
    },
    m(i, s) {
      for (let a = 0; a < r.length; a += 1)
        r[a] && r[a].m(i, s);
      B(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        n = ct(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < n.length; a += 1) {
          const o = In(i, n, a);
          r[a] ? r[a].p(o, s) : (r[a] = Gn(o), r[a].c(), r[a].m(t.parentNode, t));
        }
        for (; a < r.length; a += 1)
          r[a].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && T(t), Ir(r, i);
    }
  };
}
function kn(e) {
  let t, n, r, i, s = (
    /*i*/
    e[40] !== 0 && ma()
  ), a = (
    /*p*/
    e[38].desc != null && Dn(e)
  ), o = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && Un()
  ), l = (
    /*progress_level*/
    e[14] != null && Fn(e)
  );
  return {
    c() {
      s && s.c(), t = ue(), a && a.c(), n = ue(), o && o.c(), r = ue(), l && l.c(), i = Re();
    },
    m(u, f) {
      s && s.m(u, f), B(u, t, f), a && a.m(u, f), B(u, n, f), o && o.m(u, f), B(u, r, f), l && l.m(u, f), B(u, i, f);
    },
    p(u, f) {
      /*p*/
      u[38].desc != null ? a ? a.p(u, f) : (a = Dn(u), a.c(), a.m(n.parentNode, n)) : a && (a.d(1), a = null), /*p*/
      u[38].desc != null && /*progress_level*/
      u[14] && /*progress_level*/
      u[14][
        /*i*/
        u[40]
      ] != null ? o || (o = Un(), o.c(), o.m(r.parentNode, r)) : o && (o.d(1), o = null), /*progress_level*/
      u[14] != null ? l ? l.p(u, f) : (l = Fn(u), l.c(), l.m(i.parentNode, i)) : l && (l.d(1), l = null);
    },
    d(u) {
      u && (T(t), T(n), T(r), T(i)), s && s.d(u), a && a.d(u), o && o.d(u), l && l.d(u);
    }
  };
}
function ma(e) {
  let t;
  return {
    c() {
      t = k(" /");
    },
    m(n, r) {
      B(n, t, r);
    },
    d(n) {
      n && T(t);
    }
  };
}
function Dn(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = k(t);
    },
    m(r, i) {
      B(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[38].desc + "") && te(n, t);
    },
    d(r) {
      r && T(n);
    }
  };
}
function Un(e) {
  let t;
  return {
    c() {
      t = k("-");
    },
    m(n, r) {
      B(n, t, r);
    },
    d(n) {
      n && T(t);
    }
  };
}
function Fn(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, r;
  return {
    c() {
      n = k(t), r = k("%");
    },
    m(i, s) {
      B(i, n, s), B(i, r, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && te(n, t);
    },
    d(i) {
      i && (T(n), T(r));
    }
  };
}
function Gn(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && kn(e)
  );
  return {
    c() {
      n && n.c(), t = Re();
    },
    m(r, i) {
      n && n.m(r, i), B(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].desc != null || /*progress_level*/
      r[14] && /*progress_level*/
      r[14][
        /*i*/
        r[40]
      ] != null ? n ? n.p(r, i) : (n = kn(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && T(t), n && n.d(r);
    }
  };
}
function jn(e) {
  let t, n;
  return {
    c() {
      t = ce("p"), n = k(
        /*loading_text*/
        e[9]
      ), le(t, "class", "loading svelte-14miwb5");
    },
    m(r, i) {
      B(r, t, i), ge(t, n);
    },
    p(r, i) {
      i[0] & /*loading_text*/
      512 && te(
        n,
        /*loading_text*/
        r[9]
      );
    },
    d(r) {
      r && T(t);
    }
  };
}
function ba(e) {
  let t, n, r, i, s;
  const a = [aa, oa], o = [];
  function l(u, f) {
    return (
      /*status*/
      u[4] === "pending" ? 0 : (
        /*status*/
        u[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = l(e)) && (r = o[n] = a[n](e)), {
    c() {
      t = ce("div"), r && r.c(), le(t, "class", i = "wrap " + /*variant*/
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
      ), be(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), be(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(u, f) {
      B(u, t, f), ~n && o[n].m(t, null), e[31](t), s = !0;
    },
    p(u, f) {
      let h = n;
      n = l(u), n === h ? ~n && o[n].p(u, f) : (r && (xr(), Ce(o[h], 1, 1, () => {
        o[h] = null;
      }), Pr()), ~n ? (r = o[n], r ? r.p(u, f) : (r = o[n] = a[n](u), r.c()), Oe(r, 1), r.m(t, null)) : r = null), (!s || f[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      u[8] + " " + /*show_progress*/
      u[6] + " svelte-14miwb5")) && le(t, "class", i), (!s || f[0] & /*variant, show_progress, status, show_progress*/
      336) && ee(t, "hide", !/*status*/
      u[4] || /*status*/
      u[4] === "complete" || /*show_progress*/
      u[6] === "hidden"), (!s || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && ee(
        t,
        "translucent",
        /*variant*/
        u[8] === "center" && /*status*/
        (u[4] === "pending" || /*status*/
        u[4] === "error") || /*translucent*/
        u[11] || /*show_progress*/
        u[6] === "minimal"
      ), (!s || f[0] & /*variant, show_progress, status*/
      336) && ee(
        t,
        "generating",
        /*status*/
        u[4] === "generating"
      ), (!s || f[0] & /*variant, show_progress, border*/
      4416) && ee(
        t,
        "border",
        /*border*/
        u[12]
      ), f[0] & /*absolute*/
      1024 && be(
        t,
        "position",
        /*absolute*/
        u[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && be(
        t,
        "padding",
        /*absolute*/
        u[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(u) {
      s || (Oe(r), s = !0);
    },
    o(u) {
      Ce(r), s = !1;
    },
    d(u) {
      u && T(t), ~n && o[n].d(), e[31](null);
    }
  };
}
let et = [], Ot = !1;
async function pa(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (et.push(e), !Ot)
      Ot = !0;
    else
      return;
    await ra(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let r = 0; r < et.length; r++) {
        const s = et[r].getBoundingClientRect();
        (r === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = r);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Ot = !1, et = [];
    });
  }
}
function ga(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { i18n: a } = t, { eta: o = null } = t, { queue: l = !1 } = t, { queue_position: u } = t, { queue_size: f } = t, { status: h } = t, { scroll_to_output: _ = !1 } = t, { timer: b = !0 } = t, { show_progress: d = "full" } = t, { message: g = null } = t, { progress: v = null } = t, { variant: w = "default" } = t, { loading_text: E = "Loading..." } = t, { absolute: m = !0 } = t, { translucent: c = !1 } = t, { border: p = !1 } = t, { autoscroll: U } = t, D, Z = !1, he = 0, ne = 0, S = null, Qe = 0, ae = null, H, C = null, J = !0;
  const A = () => {
    n(25, he = performance.now()), n(26, ne = 0), Z = !0, V();
  };
  function V() {
    requestAnimationFrame(() => {
      n(26, ne = (performance.now() - he) / 1e3), Z && V();
    });
  }
  function L() {
    n(26, ne = 0), Z && (Z = !1);
  }
  ia(() => {
    Z && L();
  });
  let O = null;
  function re(y) {
    Nn[y ? "unshift" : "push"](() => {
      C = y, n(16, C), n(7, v), n(14, ae), n(15, H);
    });
  }
  function K(y) {
    Nn[y ? "unshift" : "push"](() => {
      D = y, n(13, D);
    });
  }
  return e.$$set = (y) => {
    "i18n" in y && n(1, a = y.i18n), "eta" in y && n(0, o = y.eta), "queue" in y && n(21, l = y.queue), "queue_position" in y && n(2, u = y.queue_position), "queue_size" in y && n(3, f = y.queue_size), "status" in y && n(4, h = y.status), "scroll_to_output" in y && n(22, _ = y.scroll_to_output), "timer" in y && n(5, b = y.timer), "show_progress" in y && n(6, d = y.show_progress), "message" in y && n(23, g = y.message), "progress" in y && n(7, v = y.progress), "variant" in y && n(8, w = y.variant), "loading_text" in y && n(9, E = y.loading_text), "absolute" in y && n(10, m = y.absolute), "translucent" in y && n(11, c = y.translucent), "border" in y && n(12, p = y.border), "autoscroll" in y && n(24, U = y.autoscroll), "$$scope" in y && n(28, s = y.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (o === null ? n(0, o = S) : l && n(0, o = (performance.now() - he) / 1e3 + o), o != null && (n(19, O = o.toFixed(1)), n(27, S = o))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, Qe = o === null || o <= 0 || !ne ? null : Math.min(ne / o, 1)), e.$$.dirty[0] & /*progress*/
    128 && v != null && n(18, J = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? n(14, ae = v.map((y) => {
      if (y.index != null && y.length != null)
        return y.index / y.length;
      if (y.progress != null)
        return y.progress;
    })) : n(14, ae = null), ae ? (n(15, H = ae[ae.length - 1]), C && (H === 0 ? n(16, C.style.transition = "0", C) : n(16, C.style.transition = "150ms", C))) : n(15, H = void 0)), e.$$.dirty[0] & /*status*/
    16 && (h === "pending" ? A() : L()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && D && _ && (h === "pending" || h === "complete") && pa(D, U), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, r = ne.toFixed(1));
  }, [
    o,
    a,
    u,
    f,
    h,
    b,
    d,
    v,
    w,
    E,
    m,
    c,
    p,
    D,
    ae,
    H,
    C,
    Qe,
    J,
    O,
    r,
    l,
    _,
    g,
    U,
    he,
    ne,
    S,
    s,
    i,
    re,
    K
  ];
}
class va extends Wo {
  constructor(t) {
    super(), $o(
      this,
      t,
      ga,
      ba,
      ta,
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
function Or(e, t, n) {
  if (e == null)
    return null;
  if (typeof e == "string")
    return {
      name: "file_data",
      data: e
    };
  if (Array.isArray(e)) {
    const r = [];
    for (const i of e)
      i === null ? r.push(null) : r.push(Or(i, t, n));
    return r;
  } else
    e.is_file ? e.data = Cr(e.name, t, n) : e.is_stream && (n == null ? e.data = t + "/stream/" + e.name : e.data = "/proxy=" + n + "stream/" + e.name);
  return e;
}
function ya(e) {
  try {
    const t = new URL(e);
    return t.protocol === "http:" || t.protocol === "https:";
  } catch {
    return !1;
  }
}
function Cr(e, t, n) {
  return e == null ? n ? `/proxy=${n}file=` : `${t}/file=` : ya(e) ? e : n ? `/proxy=${n}file=${e}` : `${t}/file=${e}`;
}
const wa = (e) => {
  const t = new FileReader();
  return t.readAsDataURL(e), new Promise((n) => {
    t.onloadend = () => {
      n(t.result);
    };
  });
};
var Ct = new Intl.Collator(0, { numeric: 1 }).compare;
function Vn(e, t, n) {
  return e = e.split("."), t = t.split("."), Ct(e[0], t[0]) || Ct(e[1], t[1]) || (t[2] = t.slice(2).join("."), n = /[.-]/.test(e[2] = e.slice(2).join(".")), n == /[.-]/.test(t[2]) ? Ct(e[2], t[2]) : n ? -1 : 1);
}
function Se(e, t, n) {
  return t.startsWith("http://") || t.startsWith("https://") ? n ? e : t : e + t;
}
function Lt(e) {
  if (e.startsWith("http")) {
    const { protocol: t, host: n } = new URL(e);
    return n.endsWith("hf.space") ? {
      ws_protocol: "wss",
      host: n,
      http_protocol: t
    } : {
      ws_protocol: t === "https:" ? "wss" : "ws",
      http_protocol: t,
      host: n
    };
  }
  return {
    ws_protocol: "wss",
    http_protocol: "https:",
    host: e
  };
}
const Lr = /^[^\/]*\/[^\/]*$/, Ea = /.*hf\.space\/{0,1}$/;
async function Sa(e, t) {
  const n = {};
  t && (n.Authorization = `Bearer ${t}`);
  const r = e.trim();
  if (Lr.test(r))
    try {
      const i = await fetch(
        `https://huggingface.co/api/spaces/${r}/host`,
        { headers: n }
      );
      if (i.status !== 200)
        throw new Error("Space metadata could not be loaded.");
      const s = (await i.json()).host;
      return {
        space_id: e,
        ...Lt(s)
      };
    } catch (i) {
      throw new Error("Space metadata could not be loaded." + i.message);
    }
  if (Ea.test(r)) {
    const { ws_protocol: i, http_protocol: s, host: a } = Lt(r);
    return {
      space_id: a.replace(".hf.space", ""),
      ws_protocol: i,
      http_protocol: s,
      host: a
    };
  }
  return {
    space_id: !1,
    ...Lt(r)
  };
}
function Ta(e) {
  let t = {};
  return e.forEach(({ api_name: n }, r) => {
    n && (t[n] = r);
  }), t;
}
const Ba = /^(?=[^]*\b[dD]iscussions{0,1}\b)(?=[^]*\b[dD]isabled\b)[^]*$/;
async function qn(e) {
  try {
    const n = (await fetch(
      `https://huggingface.co/api/spaces/${e}/discussions`,
      {
        method: "HEAD"
      }
    )).headers.get("x-error-message");
    return !(n && Ba.test(n));
  } catch {
    return !1;
  }
}
const Aa = "This application is too busy. Keep trying!", tt = "Connection errored out.";
let Mr;
function Ha(e, t) {
  return { post_data: n, upload_files: r, client: i, handle_blob: s };
  async function n(a, o, l) {
    const u = { "Content-Type": "application/json" };
    l && (u.Authorization = `Bearer ${l}`);
    try {
      var f = await e(a, {
        method: "POST",
        body: JSON.stringify(o),
        headers: u
      });
    } catch {
      return [{ error: tt }, 500];
    }
    return [await f.json(), f.status];
  }
  async function r(a, o, l) {
    const u = {};
    l && (u.Authorization = `Bearer ${l}`);
    const f = 1e3, h = [];
    for (let b = 0; b < o.length; b += f) {
      const d = o.slice(b, b + f), g = new FormData();
      d.forEach((w) => {
        g.append("files", w);
      });
      try {
        var _ = await e(`${a}/upload`, {
          method: "POST",
          body: g,
          headers: u
        });
      } catch {
        return { error: tt };
      }
      const v = await _.json();
      h.push(...v);
    }
    return { files: h };
  }
  async function i(a, o = { normalise_files: !0 }) {
    return new Promise(async (l) => {
      const { status_callback: u, hf_token: f, normalise_files: h } = o, _ = {
        predict: ne,
        submit: S,
        view_api: ae,
        component_server: Qe
        // duplicate
      }, b = h ?? !0;
      if ((typeof window > "u" || !("WebSocket" in window)) && !global.Websocket) {
        const H = await import("./wrapper-6f348d45-492a1cb9.mjs");
        Mr = (await import("./__vite-browser-external-2447137e.mjs")).Blob, global.WebSocket = H.WebSocket;
      }
      const { ws_protocol: d, http_protocol: g, host: v, space_id: w } = await Sa(a, f), E = Math.random().toString(36).substring(2), m = {};
      let c, p = {}, U = !1;
      f && w && (U = await Ia(w, f));
      async function D(H) {
        if (c = H, p = Ta((H == null ? void 0 : H.dependencies) || []), c.auth_required)
          return {
            config: c,
            ..._
          };
        try {
          Z = await ae(c);
        } catch (C) {
          console.error(`Could not get api details: ${C.message}`);
        }
        return {
          config: c,
          ..._
        };
      }
      let Z;
      async function he(H) {
        if (u && u(H), H.status === "running")
          try {
            c = await Zn(
              e,
              `${g}//${v}`,
              f
            );
            const C = await D(c);
            l(C);
          } catch (C) {
            console.error(C), u && u({
              status: "error",
              message: "Could not load this space.",
              load_status: "error",
              detail: "NOT_FOUND"
            });
          }
      }
      try {
        c = await Zn(
          e,
          `${g}//${v}`,
          f
        );
        const H = await D(c);
        l(H);
      } catch (H) {
        console.error(H), w ? Qt(
          w,
          Lr.test(w) ? "space_name" : "subdomain",
          he
        ) : u && u({
          status: "error",
          message: "Could not load this space.",
          load_status: "error",
          detail: "NOT_FOUND"
        });
      }
      function ne(H, C, J) {
        let A = !1, V = !1, L;
        if (typeof H == "number")
          L = c.dependencies[H];
        else {
          const O = H.replace(/^\//, "");
          L = c.dependencies[p[O]];
        }
        if (L.types.continuous)
          throw new Error(
            "Cannot call predict on this function as it may run forever. Use submit instead"
          );
        return new Promise((O, re) => {
          const K = S(H, C, J);
          let y;
          K.on("data", ($) => {
            V && (K.destroy(), O($)), A = !0, y = $;
          }).on("status", ($) => {
            $.stage === "error" && re($), $.stage === "complete" && (V = !0, A && (K.destroy(), O(y)));
          });
        });
      }
      function S(H, C, J) {
        let A, V;
        if (typeof H == "number")
          A = H, V = Z.unnamed_endpoints[A];
        else {
          const F = H.replace(/^\//, "");
          A = p[F], V = Z.named_endpoints[H.trim()];
        }
        if (typeof A != "number")
          throw new Error(
            "There is no endpoint matching that name of fn_index matching that number."
          );
        let L;
        const O = typeof H == "number" ? "/predict" : H;
        let re, K = !1;
        const y = {};
        let $ = "";
        typeof window < "u" && ($ = new URLSearchParams(
          window.location.search
        ).toString()), s(
          `${g}//${Se(v, c.path, !0)}`,
          C,
          V,
          f
        ).then((F) => {
          if (re = { data: F || [], event_data: J, fn_index: A }, Oa(A, c))
            Q({
              type: "status",
              endpoint: O,
              stage: "pending",
              queue: !1,
              fn_index: A,
              time: /* @__PURE__ */ new Date()
            }), n(
              `${g}//${Se(v, c.path, !0)}/run${O.startsWith("/") ? O : `/${O}`}${$ ? "?" + $ : ""}`,
              {
                ...re,
                session_hash: E
              },
              f
            ).then(([G, z]) => {
              const X = b ? zn(
                G.data,
                V,
                c.root,
                c.root_url
              ) : G.data;
              z == 200 ? (Q({
                type: "data",
                endpoint: O,
                fn_index: A,
                data: X,
                time: /* @__PURE__ */ new Date()
              }), Q({
                type: "status",
                endpoint: O,
                fn_index: A,
                stage: "complete",
                eta: G.average_duration,
                queue: !1,
                time: /* @__PURE__ */ new Date()
              })) : Q({
                type: "status",
                stage: "error",
                endpoint: O,
                fn_index: A,
                message: G.error,
                queue: !1,
                time: /* @__PURE__ */ new Date()
              });
            }).catch((G) => {
              Q({
                type: "status",
                stage: "error",
                message: G.message,
                endpoint: O,
                fn_index: A,
                queue: !1,
                time: /* @__PURE__ */ new Date()
              });
            });
          else {
            Q({
              type: "status",
              stage: "pending",
              queue: !0,
              endpoint: O,
              fn_index: A,
              time: /* @__PURE__ */ new Date()
            });
            let G = new URL(`${d}://${Se(
              v,
              c.path,
              !0
            )}
							/queue/join${$ ? "?" + $ : ""}`);
            U && G.searchParams.set("__sign", U), L = t(G), L.onclose = (z) => {
              z.wasClean || Q({
                type: "status",
                stage: "error",
                broken: !0,
                message: tt,
                queue: !0,
                endpoint: O,
                fn_index: A,
                time: /* @__PURE__ */ new Date()
              });
            }, L.onmessage = function(z) {
              const X = JSON.parse(z.data), { type: _e, status: fe, data: ke } = Ca(
                X,
                m[A]
              );
              if (_e === "update" && fe && !K)
                Q({
                  type: "status",
                  endpoint: O,
                  fn_index: A,
                  time: /* @__PURE__ */ new Date(),
                  ...fe
                }), fe.stage === "error" && L.close();
              else if (_e === "hash") {
                L.send(JSON.stringify({ fn_index: A, session_hash: E }));
                return;
              } else
                _e === "data" ? L.send(JSON.stringify({ ...re, session_hash: E })) : _e === "complete" ? K = fe : _e === "log" ? Q({
                  type: "log",
                  log: ke.log,
                  level: ke.level,
                  endpoint: O,
                  fn_index: A
                }) : _e === "generating" && Q({
                  type: "status",
                  time: /* @__PURE__ */ new Date(),
                  ...fe,
                  stage: fe == null ? void 0 : fe.stage,
                  queue: !0,
                  endpoint: O,
                  fn_index: A
                });
              ke && (Q({
                type: "data",
                time: /* @__PURE__ */ new Date(),
                data: b ? zn(
                  ke.data,
                  V,
                  c.root,
                  c.root_url
                ) : ke.data,
                endpoint: O,
                fn_index: A
              }), K && (Q({
                type: "status",
                time: /* @__PURE__ */ new Date(),
                ...K,
                stage: fe == null ? void 0 : fe.stage,
                queue: !0,
                endpoint: O,
                fn_index: A
              }), L.close()));
            }, Vn(c.version || "2.0.0", "3.6") < 0 && addEventListener(
              "open",
              () => L.send(JSON.stringify({ hash: E }))
            );
          }
        });
        function Q(F) {
          const z = y[F.type] || [];
          z == null || z.forEach((X) => X(F));
        }
        function St(F, G) {
          const z = y, X = z[F] || [];
          return z[F] = X, X == null || X.push(G), { on: St, off: Ye, cancel: Tt, destroy: Bt };
        }
        function Ye(F, G) {
          const z = y;
          let X = z[F] || [];
          return X = X == null ? void 0 : X.filter((_e) => _e !== G), z[F] = X, { on: St, off: Ye, cancel: Tt, destroy: Bt };
        }
        async function Tt() {
          const F = {
            stage: "complete",
            queue: !1,
            time: /* @__PURE__ */ new Date()
          };
          K = F, Q({
            ...F,
            type: "status",
            endpoint: O,
            fn_index: A
          }), L && L.readyState === 0 ? L.addEventListener("open", () => {
            L.close();
          }) : L.close();
          try {
            await e(
              `${g}//${Se(
                v,
                c.path,
                !0
              )}/reset`,
              {
                headers: { "Content-Type": "application/json" },
                method: "POST",
                body: JSON.stringify({ fn_index: A, session_hash: E })
              }
            );
          } catch {
            console.warn(
              "The `/reset` endpoint could not be called. Subsequent endpoint results may be unreliable."
            );
          }
        }
        function Bt() {
          for (const F in y)
            y[F].forEach((G) => {
              Ye(F, G);
            });
        }
        return {
          on: St,
          off: Ye,
          cancel: Tt,
          destroy: Bt
        };
      }
      async function Qe(H, C, J) {
        var A;
        const V = { "Content-Type": "application/json" };
        f && (V.Authorization = `Bearer ${f}`);
        let L, O = c.components.find(
          (y) => y.id === H
        );
        (A = O == null ? void 0 : O.props) != null && A.root_url ? L = O.props.root_url : L = `${g}//${Se(
          v,
          c.path,
          !0
        )}/`;
        const re = await e(
          `${L}component_server/`,
          {
            method: "POST",
            body: JSON.stringify({
              data: J,
              component_id: H,
              fn_name: C,
              session_hash: E
            }),
            headers: V
          }
        );
        if (!re.ok)
          throw new Error(
            "Could not connect to component server: " + re.statusText
          );
        return await re.json();
      }
      async function ae(H) {
        if (Z)
          return Z;
        const C = { "Content-Type": "application/json" };
        f && (C.Authorization = `Bearer ${f}`);
        let J;
        if (Vn(H.version || "2.0.0", "3.30") < 0 ? J = await e(
          "https://gradio-space-api-fetcher-v2.hf.space/api",
          {
            method: "POST",
            body: JSON.stringify({
              serialize: !1,
              config: JSON.stringify(H)
            }),
            headers: C
          }
        ) : J = await e(`${H.root}/info`, {
          headers: C
        }), !J.ok)
          throw new Error(tt);
        let A = await J.json();
        return "api" in A && (A = A.api), A.named_endpoints["/predict"] && !A.unnamed_endpoints[0] && (A.unnamed_endpoints[0] = A.named_endpoints["/predict"]), Pa(A, H, p);
      }
    });
  }
  async function s(a, o, l, u) {
    const f = await Jt(
      o,
      void 0,
      [],
      !0,
      l
    );
    return Promise.all(
      f.map(async ({ path: h, blob: _, data: b, type: d }) => {
        if (_) {
          const g = (await r(a, [_], u)).files[0];
          return { path: h, file_url: g, type: d };
        }
        return { path: h, base64: b, type: d };
      })
    ).then((h) => (h.forEach(({ path: _, file_url: b, base64: d, type: g }) => {
      if (d)
        Mt(o, d, _);
      else if (g === "Gallery")
        Mt(o, b, _);
      else if (b) {
        const v = {
          is_file: !0,
          name: `${b}`,
          data: null
          // orig_name: "file.csv"
        };
        Mt(o, v, _);
      }
    }), o));
  }
}
const { post_data: Ll, upload_files: Na, client: Ml, handle_blob: Rl } = Ha(
  fetch,
  (...e) => new WebSocket(...e)
);
function zn(e, t, n, r) {
  return e.map((i, s) => {
    var a, o, l, u;
    return ((o = (a = t == null ? void 0 : t.returns) == null ? void 0 : a[s]) == null ? void 0 : o.component) === "File" ? je(i, n, r) : ((u = (l = t == null ? void 0 : t.returns) == null ? void 0 : l[s]) == null ? void 0 : u.component) === "Gallery" ? i.map((f) => Array.isArray(f) ? [je(f[0], n, r), f[1]] : [je(f, n, r), null]) : typeof i == "object" && (i != null && i.is_file) ? je(i, n, r) : i;
  });
}
function je(e, t, n) {
  if (e == null)
    return null;
  if (typeof e == "string")
    return {
      name: "file_data",
      data: e
    };
  if (Array.isArray(e)) {
    const r = [];
    for (const i of e)
      i === null ? r.push(null) : r.push(je(i, t, n));
    return r;
  } else
    e.is_file && (n ? e.data = "/proxy=" + n + "file=" + e.name : e.data = t + "/file=" + e.name);
  return e;
}
function Xn(e, t, n, r) {
  switch (e.type) {
    case "string":
      return "string";
    case "boolean":
      return "boolean";
    case "number":
      return "number";
  }
  if (n === "JSONSerializable" || n === "StringSerializable")
    return "any";
  if (n === "ListStringSerializable")
    return "string[]";
  if (t === "Image")
    return r === "parameter" ? "Blob | File | Buffer" : "string";
  if (n === "FileSerializable")
    return (e == null ? void 0 : e.type) === "array" ? r === "parameter" ? "(Blob | File | Buffer)[]" : "{ name: string; data: string; size?: number; is_file?: boolean; orig_name?: string}[]" : r === "parameter" ? "Blob | File | Buffer" : "{ name: string; data: string; size?: number; is_file?: boolean; orig_name?: string}";
  if (n === "GallerySerializable")
    return r === "parameter" ? "[(Blob | File | Buffer), (string | null)][]" : "[{ name: string; data: string; size?: number; is_file?: boolean; orig_name?: string}, (string | null))][]";
}
function Wn(e, t) {
  return t === "GallerySerializable" ? "array of [file, label] tuples" : t === "ListStringSerializable" ? "array of strings" : t === "FileSerializable" ? "array of files or single file" : e.description;
}
function Pa(e, t, n) {
  const r = {
    named_endpoints: {},
    unnamed_endpoints: {}
  };
  for (const i in e) {
    const s = e[i];
    for (const a in s) {
      const o = t.dependencies[a] ? a : n[a.replace("/", "")], l = s[a];
      r[i][a] = {}, r[i][a].parameters = {}, r[i][a].returns = {}, r[i][a].type = t.dependencies[o].types, r[i][a].parameters = l.parameters.map(
        ({ label: u, component: f, type: h, serializer: _ }) => ({
          label: u,
          component: f,
          type: Xn(h, f, _, "parameter"),
          description: Wn(h, _)
        })
      ), r[i][a].returns = l.returns.map(
        ({ label: u, component: f, type: h, serializer: _ }) => ({
          label: u,
          component: f,
          type: Xn(h, f, _, "return"),
          description: Wn(h, _)
        })
      );
    }
  }
  return r;
}
async function Ia(e, t) {
  try {
    return (await (await fetch(`https://huggingface.co/api/spaces/${e}/jwt`, {
      headers: {
        Authorization: `Bearer ${t}`
      }
    })).json()).token || !1;
  } catch (n) {
    return console.error(n), !1;
  }
}
function Mt(e, t, n) {
  for (; n.length > 1; )
    e = e[n.shift()];
  e[n.shift()] = t;
}
async function Jt(e, t = void 0, n = [], r = !1, i = void 0) {
  if (Array.isArray(e)) {
    let s = [];
    return await Promise.all(
      e.map(async (a, o) => {
        var l;
        let u = n.slice();
        u.push(o);
        const f = await Jt(
          e[o],
          r ? ((l = i == null ? void 0 : i.parameters[o]) == null ? void 0 : l.component) || void 0 : t,
          u,
          !1,
          i
        );
        s = s.concat(f);
      })
    ), s;
  } else if (globalThis.Buffer && e instanceof globalThis.Buffer) {
    const s = t === "Image";
    return [
      {
        path: n,
        blob: s ? !1 : new Mr([e]),
        data: s ? `${e.toString("base64")}` : !1,
        type: t
      }
    ];
  } else if (e instanceof Blob || typeof window < "u" && e instanceof File) {
    if (t === "Image") {
      let s;
      if (typeof window < "u")
        s = await xa(e);
      else {
        const a = await e.arrayBuffer();
        s = Buffer.from(a).toString("base64");
      }
      return [{ path: n, data: s, type: t, blob: !1 }];
    }
    return [{ path: n, blob: e, type: t, data: !1 }];
  } else if (typeof e == "object") {
    let s = [];
    for (let a in e)
      if (e.hasOwnProperty(a)) {
        let o = n.slice();
        o.push(a), s = s.concat(
          await Jt(
            e[a],
            void 0,
            o,
            !1,
            i
          )
        );
      }
    return s;
  }
  return [];
}
function xa(e) {
  return new Promise((t, n) => {
    const r = new FileReader();
    r.onloadend = () => t(r.result), r.readAsDataURL(e);
  });
}
function Oa(e, t) {
  var n, r, i, s;
  return !(((r = (n = t == null ? void 0 : t.dependencies) == null ? void 0 : n[e]) == null ? void 0 : r.queue) === null ? t.enable_queue : (s = (i = t == null ? void 0 : t.dependencies) == null ? void 0 : i[e]) != null && s.queue) || !1;
}
async function Zn(e, t, n) {
  const r = {};
  if (n && (r.Authorization = `Bearer ${n}`), typeof window < "u" && window.gradio_config && location.origin !== "http://localhost:9876" && !window.gradio_config.dev_mode) {
    const i = window.gradio_config.root, s = window.gradio_config;
    return s.root = Se(t, s.root, !1), { ...s, path: i };
  } else if (t) {
    let i = await e(`${t}/config`, {
      headers: r
    });
    if (i.status === 200) {
      const s = await i.json();
      return s.path = s.path ?? "", s.root = t, s;
    }
    throw new Error("Could not get config.");
  }
  throw new Error("No config or app endpoint found");
}
async function Qt(e, t, n) {
  let r = t === "subdomain" ? `https://huggingface.co/api/spaces/by-subdomain/${e}` : `https://huggingface.co/api/spaces/${e}`, i, s;
  try {
    if (i = await fetch(r), s = i.status, s !== 200)
      throw new Error();
    i = await i.json();
  } catch {
    n({
      status: "error",
      load_status: "error",
      message: "Could not get space status",
      detail: "NOT_FOUND"
    });
    return;
  }
  if (!i || s !== 200)
    return;
  const {
    runtime: { stage: a },
    id: o
  } = i;
  switch (a) {
    case "STOPPED":
    case "SLEEPING":
      n({
        status: "sleeping",
        load_status: "pending",
        message: "Space is asleep. Waking it up...",
        detail: a
      }), setTimeout(() => {
        Qt(e, t, n);
      }, 1e3);
      break;
    case "PAUSED":
      n({
        status: "paused",
        load_status: "error",
        message: "This space has been paused by the author. If you would like to try this demo, consider duplicating the space.",
        detail: a,
        discussions_enabled: await qn(o)
      });
      break;
    case "RUNNING":
    case "RUNNING_BUILDING":
      n({
        status: "running",
        load_status: "complete",
        message: "",
        detail: a
      });
      break;
    case "BUILDING":
      n({
        status: "building",
        load_status: "pending",
        message: "Space is building...",
        detail: a
      }), setTimeout(() => {
        Qt(e, t, n);
      }, 1e3);
      break;
    default:
      n({
        status: "space_error",
        load_status: "error",
        message: "This space is experiencing an issue.",
        detail: a,
        discussions_enabled: await qn(o)
      });
      break;
  }
}
function Ca(e, t) {
  switch (e.msg) {
    case "send_data":
      return { type: "data" };
    case "send_hash":
      return { type: "hash" };
    case "queue_full":
      return {
        type: "update",
        status: {
          queue: !0,
          message: Aa,
          stage: "error",
          code: e.code,
          success: e.success
        }
      };
    case "estimation":
      return {
        type: "update",
        status: {
          queue: !0,
          stage: t || "pending",
          code: e.code,
          size: e.queue_size,
          position: e.rank,
          eta: e.rank_eta,
          success: e.success
        }
      };
    case "progress":
      return {
        type: "update",
        status: {
          queue: !0,
          stage: "pending",
          code: e.code,
          progress_data: e.progress_data,
          success: e.success
        }
      };
    case "log":
      return { type: "log", data: e };
    case "process_generating":
      return {
        type: "generating",
        status: {
          queue: !0,
          message: e.success ? null : e.output.error,
          stage: e.success ? "generating" : "error",
          code: e.code,
          progress_data: e.progress_data,
          eta: e.average_duration
        },
        data: e.success ? e.output : null
      };
    case "process_completed":
      return "error" in e.output ? {
        type: "update",
        status: {
          queue: !0,
          message: e.output.error,
          stage: "error",
          code: e.code,
          success: e.success
        }
      } : {
        type: "complete",
        status: {
          queue: !0,
          message: e.success ? void 0 : e.output.error,
          stage: e.success ? "complete" : "error",
          code: e.code,
          progress_data: e.progress_data,
          eta: e.output.average_duration
        },
        data: e.success ? e.output : null
      };
    case "process_starts":
      return {
        type: "update",
        status: {
          queue: !0,
          stage: "pending",
          code: e.code,
          size: e.rank,
          position: 0,
          success: e.success
        }
      };
  }
  return { type: "none", status: { stage: "error", queue: !0 } };
}
const {
  SvelteComponent: La,
  append: Rr,
  attr: R,
  bubble: Ma,
  check_outros: Ra,
  create_slot: kr,
  detach: Ze,
  element: Et,
  empty: ka,
  get_all_dirty_from_scope: Dr,
  get_slot_changes: Ur,
  group_outros: Da,
  init: Ua,
  insert: Je,
  listen: Fa,
  safe_not_equal: Ga,
  set_style: W,
  space: Fr,
  src_url_equal: ht,
  toggle_class: Be,
  transition_in: _t,
  transition_out: dt,
  update_slot_base: Gr
} = window.__gradio__svelte__internal;
function ja(e) {
  let t, n, r, i, s, a, o = (
    /*icon*/
    e[7] && Jn(e)
  );
  const l = (
    /*#slots*/
    e[15].default
  ), u = kr(
    l,
    e,
    /*$$scope*/
    e[14],
    null
  );
  return {
    c() {
      t = Et("button"), o && o.c(), n = Fr(), u && u.c(), R(t, "class", r = /*size*/
      e[4] + " " + /*variant*/
      e[3] + " " + /*elem_classes*/
      e[1].join(" ") + " svelte-8huxfn"), R(
        t,
        "id",
        /*elem_id*/
        e[0]
      ), t.disabled = /*disabled*/
      e[8], Be(t, "hidden", !/*visible*/
      e[2]), W(
        t,
        "flex-grow",
        /*scale*/
        e[9]
      ), W(
        t,
        "width",
        /*scale*/
        e[9] === 0 ? "fit-content" : null
      ), W(t, "min-width", typeof /*min_width*/
      e[10] == "number" ? `calc(min(${/*min_width*/
      e[10]}px, 100%))` : null);
    },
    m(f, h) {
      Je(f, t, h), o && o.m(t, null), Rr(t, n), u && u.m(t, null), i = !0, s || (a = Fa(
        t,
        "click",
        /*click_handler*/
        e[16]
      ), s = !0);
    },
    p(f, h) {
      /*icon*/
      f[7] ? o ? o.p(f, h) : (o = Jn(f), o.c(), o.m(t, n)) : o && (o.d(1), o = null), u && u.p && (!i || h & /*$$scope*/
      16384) && Gr(
        u,
        l,
        f,
        /*$$scope*/
        f[14],
        i ? Ur(
          l,
          /*$$scope*/
          f[14],
          h,
          null
        ) : Dr(
          /*$$scope*/
          f[14]
        ),
        null
      ), (!i || h & /*size, variant, elem_classes*/
      26 && r !== (r = /*size*/
      f[4] + " " + /*variant*/
      f[3] + " " + /*elem_classes*/
      f[1].join(" ") + " svelte-8huxfn")) && R(t, "class", r), (!i || h & /*elem_id*/
      1) && R(
        t,
        "id",
        /*elem_id*/
        f[0]
      ), (!i || h & /*disabled*/
      256) && (t.disabled = /*disabled*/
      f[8]), (!i || h & /*size, variant, elem_classes, visible*/
      30) && Be(t, "hidden", !/*visible*/
      f[2]), h & /*scale*/
      512 && W(
        t,
        "flex-grow",
        /*scale*/
        f[9]
      ), h & /*scale*/
      512 && W(
        t,
        "width",
        /*scale*/
        f[9] === 0 ? "fit-content" : null
      ), h & /*min_width*/
      1024 && W(t, "min-width", typeof /*min_width*/
      f[10] == "number" ? `calc(min(${/*min_width*/
      f[10]}px, 100%))` : null);
    },
    i(f) {
      i || (_t(u, f), i = !0);
    },
    o(f) {
      dt(u, f), i = !1;
    },
    d(f) {
      f && Ze(t), o && o.d(), u && u.d(f), s = !1, a();
    }
  };
}
function Va(e) {
  let t, n, r, i, s = (
    /*icon*/
    e[7] && Qn(e)
  );
  const a = (
    /*#slots*/
    e[15].default
  ), o = kr(
    a,
    e,
    /*$$scope*/
    e[14],
    null
  );
  return {
    c() {
      t = Et("a"), s && s.c(), n = Fr(), o && o.c(), R(
        t,
        "href",
        /*link*/
        e[6]
      ), R(t, "rel", "noopener noreferrer"), R(
        t,
        "aria-disabled",
        /*disabled*/
        e[8]
      ), R(t, "class", r = /*size*/
      e[4] + " " + /*variant*/
      e[3] + " " + /*elem_classes*/
      e[1].join(" ") + " svelte-8huxfn"), R(
        t,
        "id",
        /*elem_id*/
        e[0]
      ), Be(t, "hidden", !/*visible*/
      e[2]), Be(
        t,
        "disabled",
        /*disabled*/
        e[8]
      ), W(
        t,
        "flex-grow",
        /*scale*/
        e[9]
      ), W(
        t,
        "pointer-events",
        /*disabled*/
        e[8] ? "none" : null
      ), W(
        t,
        "width",
        /*scale*/
        e[9] === 0 ? "fit-content" : null
      ), W(t, "min-width", typeof /*min_width*/
      e[10] == "number" ? `calc(min(${/*min_width*/
      e[10]}px, 100%))` : null);
    },
    m(l, u) {
      Je(l, t, u), s && s.m(t, null), Rr(t, n), o && o.m(t, null), i = !0;
    },
    p(l, u) {
      /*icon*/
      l[7] ? s ? s.p(l, u) : (s = Qn(l), s.c(), s.m(t, n)) : s && (s.d(1), s = null), o && o.p && (!i || u & /*$$scope*/
      16384) && Gr(
        o,
        a,
        l,
        /*$$scope*/
        l[14],
        i ? Ur(
          a,
          /*$$scope*/
          l[14],
          u,
          null
        ) : Dr(
          /*$$scope*/
          l[14]
        ),
        null
      ), (!i || u & /*link*/
      64) && R(
        t,
        "href",
        /*link*/
        l[6]
      ), (!i || u & /*disabled*/
      256) && R(
        t,
        "aria-disabled",
        /*disabled*/
        l[8]
      ), (!i || u & /*size, variant, elem_classes*/
      26 && r !== (r = /*size*/
      l[4] + " " + /*variant*/
      l[3] + " " + /*elem_classes*/
      l[1].join(" ") + " svelte-8huxfn")) && R(t, "class", r), (!i || u & /*elem_id*/
      1) && R(
        t,
        "id",
        /*elem_id*/
        l[0]
      ), (!i || u & /*size, variant, elem_classes, visible*/
      30) && Be(t, "hidden", !/*visible*/
      l[2]), (!i || u & /*size, variant, elem_classes, disabled*/
      282) && Be(
        t,
        "disabled",
        /*disabled*/
        l[8]
      ), u & /*scale*/
      512 && W(
        t,
        "flex-grow",
        /*scale*/
        l[9]
      ), u & /*disabled*/
      256 && W(
        t,
        "pointer-events",
        /*disabled*/
        l[8] ? "none" : null
      ), u & /*scale*/
      512 && W(
        t,
        "width",
        /*scale*/
        l[9] === 0 ? "fit-content" : null
      ), u & /*min_width*/
      1024 && W(t, "min-width", typeof /*min_width*/
      l[10] == "number" ? `calc(min(${/*min_width*/
      l[10]}px, 100%))` : null);
    },
    i(l) {
      i || (_t(o, l), i = !0);
    },
    o(l) {
      dt(o, l), i = !1;
    },
    d(l) {
      l && Ze(t), s && s.d(), o && o.d(l);
    }
  };
}
function Jn(e) {
  let t, n, r;
  return {
    c() {
      t = Et("img"), R(t, "class", "button-icon svelte-8huxfn"), ht(t.src, n = /*icon_path*/
      e[11]) || R(t, "src", n), R(t, "alt", r = `${/*value*/
      e[5]} icon`);
    },
    m(i, s) {
      Je(i, t, s);
    },
    p(i, s) {
      s & /*icon_path*/
      2048 && !ht(t.src, n = /*icon_path*/
      i[11]) && R(t, "src", n), s & /*value*/
      32 && r !== (r = `${/*value*/
      i[5]} icon`) && R(t, "alt", r);
    },
    d(i) {
      i && Ze(t);
    }
  };
}
function Qn(e) {
  let t, n, r;
  return {
    c() {
      t = Et("img"), R(t, "class", "button-icon svelte-8huxfn"), ht(t.src, n = /*icon_path*/
      e[11]) || R(t, "src", n), R(t, "alt", r = `${/*value*/
      e[5]} icon`);
    },
    m(i, s) {
      Je(i, t, s);
    },
    p(i, s) {
      s & /*icon_path*/
      2048 && !ht(t.src, n = /*icon_path*/
      i[11]) && R(t, "src", n), s & /*value*/
      32 && r !== (r = `${/*value*/
      i[5]} icon`) && R(t, "alt", r);
    },
    d(i) {
      i && Ze(t);
    }
  };
}
function qa(e) {
  let t, n, r, i;
  const s = [Va, ja], a = [];
  function o(l, u) {
    return (
      /*link*/
      l[6] && /*link*/
      l[6].length > 0 ? 0 : 1
    );
  }
  return t = o(e), n = a[t] = s[t](e), {
    c() {
      n.c(), r = ka();
    },
    m(l, u) {
      a[t].m(l, u), Je(l, r, u), i = !0;
    },
    p(l, [u]) {
      let f = t;
      t = o(l), t === f ? a[t].p(l, u) : (Da(), dt(a[f], 1, 1, () => {
        a[f] = null;
      }), Ra(), n = a[t], n ? n.p(l, u) : (n = a[t] = s[t](l), n.c()), _t(n, 1), n.m(r.parentNode, r));
    },
    i(l) {
      i || (_t(n), i = !0);
    },
    o(l) {
      dt(n), i = !1;
    },
    d(l) {
      l && Ze(r), a[t].d(l);
    }
  };
}
function za(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { elem_id: a = "" } = t, { elem_classes: o = [] } = t, { visible: l = !0 } = t, { variant: u = "secondary" } = t, { size: f = "lg" } = t, { value: h = null } = t, { link: _ = null } = t, { icon: b = null } = t, { disabled: d = !1 } = t, { scale: g = null } = t, { min_width: v = void 0 } = t, { root: w = "" } = t, { root_url: E = null } = t;
  function m(c) {
    Ma.call(this, e, c);
  }
  return e.$$set = (c) => {
    "elem_id" in c && n(0, a = c.elem_id), "elem_classes" in c && n(1, o = c.elem_classes), "visible" in c && n(2, l = c.visible), "variant" in c && n(3, u = c.variant), "size" in c && n(4, f = c.size), "value" in c && n(5, h = c.value), "link" in c && n(6, _ = c.link), "icon" in c && n(7, b = c.icon), "disabled" in c && n(8, d = c.disabled), "scale" in c && n(9, g = c.scale), "min_width" in c && n(10, v = c.min_width), "root" in c && n(12, w = c.root), "root_url" in c && n(13, E = c.root_url), "$$scope" in c && n(14, s = c.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty & /*icon, root, root_url*/
    12416 && n(11, r = Cr(b, w, E));
  }, [
    a,
    o,
    l,
    u,
    f,
    h,
    _,
    b,
    d,
    g,
    v,
    r,
    w,
    E,
    s,
    i,
    m
  ];
}
let Xa = class extends La {
  constructor(t) {
    super(), Ua(this, t, za, qa, Ga, {
      elem_id: 0,
      elem_classes: 1,
      visible: 2,
      variant: 3,
      size: 4,
      value: 5,
      link: 6,
      icon: 7,
      disabled: 8,
      scale: 9,
      min_width: 10,
      root: 12,
      root_url: 13
    });
  }
};
const {
  SvelteComponent: Wa,
  attr: Yn,
  binding_callbacks: Za,
  create_component: Ja,
  destroy_component: Qa,
  detach: Yt,
  element: Ya,
  init: Ka,
  insert: Kt,
  listen: $a,
  mount_component: el,
  safe_not_equal: tl,
  set_data: nl,
  set_style: rl,
  space: il,
  text: sl,
  transition_in: ol,
  transition_out: al
} = window.__gradio__svelte__internal, { tick: ll, createEventDispatcher: ul } = window.__gradio__svelte__internal;
function fl(e) {
  let t;
  return {
    c() {
      t = sl(
        /*button_label*/
        e[0]
      );
    },
    m(n, r) {
      Kt(n, t, r);
    },
    p(n, r) {
      r & /*button_label*/
      1 && nl(
        t,
        /*button_label*/
        n[0]
      );
    },
    d(n) {
      n && Yt(t);
    }
  };
}
function cl(e) {
  let t, n, r, i, s, a;
  return r = new Xa({
    props: {
      size: "lg",
      variant: "secondary",
      elem_id: "",
      elem_classes: [],
      visible: !0,
      scale: null,
      "min-width": void 0,
      disabled: (
        /*disabled*/
        e[1]
      ),
      $$slots: { default: [fl] },
      $$scope: { ctx: e }
    }
  }), r.$on(
    "click",
    /*openFileUpload*/
    e[4]
  ), {
    c() {
      t = Ya("input"), n = il(), Ja(r.$$.fragment), rl(t, "display", "none"), Yn(t, "accept", null), Yn(t, "type", "file"), t.multiple = !0;
    },
    m(o, l) {
      Kt(o, t, l), e[9](t), Kt(o, n, l), el(r, o, l), i = !0, s || (a = $a(
        t,
        "change",
        /*loadFilesFromUpload*/
        e[3]
      ), s = !0);
    },
    p(o, [l]) {
      const u = {};
      l & /*disabled*/
      2 && (u.disabled = /*disabled*/
      o[1]), l & /*$$scope, button_label*/
      4097 && (u.$$scope = { dirty: l, ctx: o }), r.$set(u);
    },
    i(o) {
      i || (ol(r.$$.fragment, o), i = !0);
    },
    o(o) {
      al(r.$$.fragment, o), i = !1;
    },
    d(o) {
      o && (Yt(t), Yt(n)), e[9](null), Qa(r, o), s = !1, a();
    }
  };
}
async function $t(e) {
  var t = [];
  return e.forEach((n, r) => {
    t[r] = {
      name: n.name,
      size: n.size,
      data: "",
      blob: n
    };
  }), t;
}
function hl(e, t, n) {
  let { button_label: r = "Upload" } = t, { disabled: i = !1 } = t, { root: s } = t, { value: a = [] } = t, o;
  const l = ul();
  async function u(d, g, v = Na) {
    let w = (Array.isArray(d) ? d : [d]).map((E) => E.blob);
    return await v(g, w).then(async (E) => {
      E.error ? (Array.isArray(d) ? d : [d]).forEach(async (m, c) => {
        m.data = await wa(m.blob), m.blob = void 0;
      }) : (Array.isArray(d) ? d : [d]).forEach((m, c) => {
        E.files && (m.orig_name = m.name, m.name = E.files[c], m.is_file = !0, m.blob = void 0, Or(m, g, null));
      });
    }), d;
  }
  async function f(d) {
    let g = Array.from(d);
    if (!d.length)
      return;
    let v = await $t(g);
    await ll(), v = await u(v, s), l("upload"), n(5, a = v);
  }
  async function h(d) {
    const g = d.target;
    g.files && await f(g.files);
  }
  function _() {
    o.click();
  }
  function b(d) {
    Za[d ? "unshift" : "push"](() => {
      o = d, n(2, o);
    });
  }
  return e.$$set = (d) => {
    "button_label" in d && n(0, r = d.button_label), "disabled" in d && n(1, i = d.disabled), "root" in d && n(6, s = d.root), "value" in d && n(5, a = d.value);
  }, [
    r,
    i,
    o,
    h,
    _,
    a,
    s,
    u,
    $t,
    b
  ];
}
class _l extends Wa {
  constructor(t) {
    super(), Ka(this, t, hl, cl, tl, {
      button_label: 0,
      disabled: 1,
      root: 6,
      value: 5,
      upload: 7,
      prepare_files: 8
    });
  }
  get upload() {
    return this.$$.ctx[7];
  }
  get prepare_files() {
    return $t;
  }
}
const {
  SvelteComponent: dl,
  add_flush_callback: ml,
  append: Ue,
  assign: bl,
  attr: oe,
  bind: pl,
  binding_callbacks: jr,
  check_outros: gl,
  create_component: mt,
  destroy_component: bt,
  detach: at,
  element: Fe,
  flush: j,
  get_spread_object: vl,
  get_spread_update: yl,
  group_outros: wl,
  init: El,
  insert: lt,
  listen: Rt,
  mount_component: pt,
  run_all: Sl,
  safe_not_equal: Tl,
  set_data: Bl,
  set_input_value: Kn,
  space: kt,
  text: Al,
  toggle_class: Hl,
  transition_in: pe,
  transition_out: Ae
} = window.__gradio__svelte__internal, { tick: Nl } = window.__gradio__svelte__internal;
function $n(e) {
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
    e[11]
  ];
  let i = {};
  for (let s = 0; s < r.length; s += 1)
    i = bl(i, r[s]);
  return t = new va({ props: i }), {
    c() {
      mt(t.$$.fragment);
    },
    m(s, a) {
      pt(t, s, a), n = !0;
    },
    p(s, a) {
      const o = a & /*gradio, loading_status*/
      2050 ? yl(r, [
        a & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          s[1].autoscroll
        ) },
        a & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          s[1].i18n
        ) },
        a & /*loading_status*/
        2048 && vl(
          /*loading_status*/
          s[11]
        )
      ]) : {};
      t.$set(o);
    },
    i(s) {
      n || (pe(t.$$.fragment, s), n = !0);
    },
    o(s) {
      Ae(t.$$.fragment, s), n = !1;
    },
    d(s) {
      bt(t, s);
    }
  };
}
function Pl(e) {
  let t;
  return {
    c() {
      t = Al(
        /*label*/
        e[2]
      );
    },
    m(n, r) {
      lt(n, t, r);
    },
    p(n, r) {
      r & /*label*/
      4 && Bl(
        t,
        /*label*/
        n[2]
      );
    },
    d(n) {
      n && at(t);
    }
  };
}
function Il(e) {
  let t, n, r, i, s, a, o, l, u, f, h, _, b, d, g, v, w = (
    /*loading_status*/
    e[11] && $n(e)
  );
  n = new Gi({
    props: {
      show_label: (
        /*show_label*/
        e[8]
      ),
      info: void 0,
      $$slots: { default: [Pl] },
      $$scope: { ctx: e }
    }
  });
  function E(c) {
    e[22](c);
  }
  let m = {
    root: (
      /*root*/
      e[12]
    ),
    disabled: (
      /*mode*/
      e[13] === "static"
    ),
    button_label: (
      /*button_label*/
      e[3]
    )
  };
  return (
    /*value*/
    e[0].attachments !== void 0 && (m.value = /*value*/
    e[0].attachments), _ = new _l({ props: m }), jr.push(() => pl(_, "value", E)), _.$on(
      "upload",
      /*upload_handler*/
      e[23]
    ), {
      c() {
        w && w.c(), t = kt(), mt(n.$$.fragment), r = kt(), i = Fe("div"), s = Fe("div"), a = Fe("label"), o = Fe("input"), f = kt(), h = Fe("div"), mt(_.$$.fragment), oe(o, "data-testid", "textbox"), oe(o, "type", "text"), oe(o, "class", "scroll-hide svelte-ipvka1"), oe(
          o,
          "placeholder",
          /*placeholder*/
          e[7]
        ), o.disabled = l = /*mode*/
        e[13] === "static", oe(o, "dir", u = /*rtl*/
        e[14] ? "rtl" : "ltr"), oe(a, "class", "svelte-ipvka1"), Hl(a, "container", Ol), oe(s, "class", "parent-input svelte-ipvka1"), oe(h, "class", "upload-btn svelte-ipvka1"), oe(i, "class", "flex-row svelte-ipvka1");
      },
      m(c, p) {
        w && w.m(c, p), lt(c, t, p), pt(n, c, p), lt(c, r, p), lt(c, i, p), Ue(i, s), Ue(s, a), Ue(a, o), Kn(
          o,
          /*value*/
          e[0].text
        ), e[20](o), Ue(i, f), Ue(i, h), pt(_, h, null), d = !0, g || (v = [
          Rt(
            o,
            "input",
            /*input_input_handler*/
            e[19]
          ),
          Rt(
            o,
            "keypress",
            /*handle_keypress*/
            e[16]
          ),
          Rt(
            o,
            "change",
            /*change_handler*/
            e[21]
          )
        ], g = !0);
      },
      p(c, p) {
        /*loading_status*/
        c[11] ? w ? (w.p(c, p), p & /*loading_status*/
        2048 && pe(w, 1)) : (w = $n(c), w.c(), pe(w, 1), w.m(t.parentNode, t)) : w && (wl(), Ae(w, 1, 1, () => {
          w = null;
        }), gl());
        const U = {};
        p & /*show_label*/
        256 && (U.show_label = /*show_label*/
        c[8]), p & /*$$scope, label*/
        16777220 && (U.$$scope = { dirty: p, ctx: c }), n.$set(U), (!d || p & /*placeholder*/
        128) && oe(
          o,
          "placeholder",
          /*placeholder*/
          c[7]
        ), (!d || p & /*mode*/
        8192 && l !== (l = /*mode*/
        c[13] === "static")) && (o.disabled = l), (!d || p & /*rtl*/
        16384 && u !== (u = /*rtl*/
        c[14] ? "rtl" : "ltr")) && oe(o, "dir", u), p & /*value*/
        1 && o.value !== /*value*/
        c[0].text && Kn(
          o,
          /*value*/
          c[0].text
        );
        const D = {};
        p & /*root*/
        4096 && (D.root = /*root*/
        c[12]), p & /*mode*/
        8192 && (D.disabled = /*mode*/
        c[13] === "static"), p & /*button_label*/
        8 && (D.button_label = /*button_label*/
        c[3]), !b && p & /*value*/
        1 && (b = !0, D.value = /*value*/
        c[0].attachments, ml(() => b = !1)), _.$set(D);
      },
      i(c) {
        d || (pe(w), pe(n.$$.fragment, c), pe(_.$$.fragment, c), d = !0);
      },
      o(c) {
        Ae(w), Ae(n.$$.fragment, c), Ae(_.$$.fragment, c), d = !1;
      },
      d(c) {
        c && (at(t), at(r), at(i)), w && w.d(c), bt(n, c), e[20](null), bt(_), g = !1, Sl(v);
      }
    }
  );
}
function xl(e) {
  let t, n;
  return t = new ii({
    props: {
      visible: (
        /*visible*/
        e[6]
      ),
      elem_id: (
        /*elem_id*/
        e[4]
      ),
      elem_classes: (
        /*elem_classes*/
        e[5]
      ),
      scale: (
        /*scale*/
        e[9]
      ),
      min_width: (
        /*min_width*/
        e[10]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [Il] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      mt(t.$$.fragment);
    },
    m(r, i) {
      pt(t, r, i), n = !0;
    },
    p(r, [i]) {
      const s = {};
      i & /*visible*/
      64 && (s.visible = /*visible*/
      r[6]), i & /*elem_id*/
      16 && (s.elem_id = /*elem_id*/
      r[4]), i & /*elem_classes*/
      32 && (s.elem_classes = /*elem_classes*/
      r[5]), i & /*scale*/
      512 && (s.scale = /*scale*/
      r[9]), i & /*min_width*/
      1024 && (s.min_width = /*min_width*/
      r[10]), i & /*$$scope, root, mode, button_label, value, gradio, placeholder, rtl, el, show_label, label, loading_status*/
      16841103 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (pe(t.$$.fragment, r), n = !0);
    },
    o(r) {
      Ae(t.$$.fragment, r), n = !1;
    },
    d(r) {
      bt(t, r);
    }
  };
}
const Ol = !0;
function Cl(e, t, n) {
  let r, { gradio: i } = t, { label: s = "Textbox With Attachments" } = t, { button_label: a } = t, { elem_id: o = "" } = t, { elem_classes: l = [] } = t, { visible: u = !0 } = t, { value: f = { text: "", attachments: [] } } = t, { placeholder: h = "" } = t, { show_label: _ } = t, { scale: b = null } = t, { min_width: d = void 0 } = t, { loading_status: g = void 0 } = t, { value_is_output: v = !1 } = t, { root: w } = t, { mode: E } = t, { rtl: m = !1 } = t, c;
  async function p(S) {
    await Nl(), S.key === "Enter" && (S.preventDefault(), i.dispatch("text_submit"));
  }
  function U() {
    f.text = this.value, n(0, f);
  }
  function D(S) {
    jr[S ? "unshift" : "push"](() => {
      c = S, n(15, c);
    });
  }
  const Z = () => i.dispatch("text_change");
  function he(S) {
    e.$$.not_equal(f.attachments, S) && (f.attachments = S, n(0, f));
  }
  const ne = () => i.dispatch("file_upload");
  return e.$$set = (S) => {
    "gradio" in S && n(1, i = S.gradio), "label" in S && n(2, s = S.label), "button_label" in S && n(3, a = S.button_label), "elem_id" in S && n(4, o = S.elem_id), "elem_classes" in S && n(5, l = S.elem_classes), "visible" in S && n(6, u = S.visible), "value" in S && n(0, f = S.value), "placeholder" in S && n(7, h = S.placeholder), "show_label" in S && n(8, _ = S.show_label), "scale" in S && n(9, b = S.scale), "min_width" in S && n(10, d = S.min_width), "loading_status" in S && n(11, g = S.loading_status), "value_is_output" in S && n(17, v = S.value_is_output), "root" in S && n(12, w = S.root), "mode" in S && n(13, E = S.mode), "rtl" in S && n(14, m = S.rtl);
  }, e.$$.update = () => {
    e.$$.dirty & /*value*/
    1 && f === null && n(0, f = { text: "", attachments: [] }), e.$$.dirty & /*value*/
    1 && n(18, r = f.text), e.$$.dirty & /*text_change, gradio*/
    262146 && i.dispatch("text_change");
  }, [
    f,
    i,
    s,
    a,
    o,
    l,
    u,
    h,
    _,
    b,
    d,
    g,
    w,
    E,
    m,
    c,
    p,
    v,
    r,
    U,
    D,
    Z,
    he,
    ne
  ];
}
class Dl extends dl {
  constructor(t) {
    super(), El(this, t, Cl, xl, Tl, {
      gradio: 1,
      label: 2,
      button_label: 3,
      elem_id: 4,
      elem_classes: 5,
      visible: 6,
      value: 0,
      placeholder: 7,
      show_label: 8,
      scale: 9,
      min_width: 10,
      loading_status: 11,
      value_is_output: 17,
      root: 12,
      mode: 13,
      rtl: 14
    });
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(t) {
    this.$$set({ gradio: t }), j();
  }
  get label() {
    return this.$$.ctx[2];
  }
  set label(t) {
    this.$$set({ label: t }), j();
  }
  get button_label() {
    return this.$$.ctx[3];
  }
  set button_label(t) {
    this.$$set({ button_label: t }), j();
  }
  get elem_id() {
    return this.$$.ctx[4];
  }
  set elem_id(t) {
    this.$$set({ elem_id: t }), j();
  }
  get elem_classes() {
    return this.$$.ctx[5];
  }
  set elem_classes(t) {
    this.$$set({ elem_classes: t }), j();
  }
  get visible() {
    return this.$$.ctx[6];
  }
  set visible(t) {
    this.$$set({ visible: t }), j();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(t) {
    this.$$set({ value: t }), j();
  }
  get placeholder() {
    return this.$$.ctx[7];
  }
  set placeholder(t) {
    this.$$set({ placeholder: t }), j();
  }
  get show_label() {
    return this.$$.ctx[8];
  }
  set show_label(t) {
    this.$$set({ show_label: t }), j();
  }
  get scale() {
    return this.$$.ctx[9];
  }
  set scale(t) {
    this.$$set({ scale: t }), j();
  }
  get min_width() {
    return this.$$.ctx[10];
  }
  set min_width(t) {
    this.$$set({ min_width: t }), j();
  }
  get loading_status() {
    return this.$$.ctx[11];
  }
  set loading_status(t) {
    this.$$set({ loading_status: t }), j();
  }
  get value_is_output() {
    return this.$$.ctx[17];
  }
  set value_is_output(t) {
    this.$$set({ value_is_output: t }), j();
  }
  get root() {
    return this.$$.ctx[12];
  }
  set root(t) {
    this.$$set({ root: t }), j();
  }
  get mode() {
    return this.$$.ctx[13];
  }
  set mode(t) {
    this.$$set({ mode: t }), j();
  }
  get rtl() {
    return this.$$.ctx[14];
  }
  set rtl(t) {
    this.$$set({ rtl: t }), j();
  }
}
export {
  Dl as default
};
