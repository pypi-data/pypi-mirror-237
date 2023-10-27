const {
  SvelteComponent: Jn,
  assign: Yn,
  create_slot: Kn,
  detach: $n,
  element: er,
  get_all_dirty_from_scope: tr,
  get_slot_changes: nr,
  get_spread_update: rr,
  init: ir,
  insert: sr,
  safe_not_equal: lr,
  set_dynamic_element_data: Et,
  set_style: L,
  toggle_class: z,
  transition_in: _n,
  transition_out: mn,
  update_slot_base: or
} = window.__gradio__svelte__internal;
function ar(e) {
  let t, n, r;
  const i = (
    /*#slots*/
    e[17].default
  ), s = Kn(
    i,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let l = [
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
  for (let a = 0; a < l.length; a += 1)
    o = Yn(o, l[a]);
  return {
    c() {
      t = er(
        /*tag*/
        e[14]
      ), s && s.c(), Et(
        /*tag*/
        e[14]
      )(t, o), z(
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
    m(a, u) {
      sr(a, t, u), s && s.m(t, null), r = !0;
    },
    p(a, u) {
      s && s.p && (!r || u & /*$$scope*/
      65536) && or(
        s,
        i,
        a,
        /*$$scope*/
        a[16],
        r ? nr(
          i,
          /*$$scope*/
          a[16],
          u,
          null
        ) : tr(
          /*$$scope*/
          a[16]
        ),
        null
      ), Et(
        /*tag*/
        a[14]
      )(t, o = rr(l, [
        (!r || u & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          a[7]
        ) },
        (!r || u & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          a[2]
        ) },
        (!r || u & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        a[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), z(
        t,
        "hidden",
        /*visible*/
        a[10] === !1
      ), z(
        t,
        "padded",
        /*padding*/
        a[6]
      ), z(
        t,
        "border_focus",
        /*border_mode*/
        a[5] === "focus"
      ), z(t, "hide-container", !/*explicit_call*/
      a[8] && !/*container*/
      a[9]), u & /*height*/
      1 && L(t, "height", typeof /*height*/
      a[0] == "number" ? (
        /*height*/
        a[0] + "px"
      ) : void 0), u & /*width*/
      2 && L(t, "width", typeof /*width*/
      a[1] == "number" ? `calc(min(${/*width*/
      a[1]}px, 100%))` : void 0), u & /*variant*/
      16 && L(
        t,
        "border-style",
        /*variant*/
        a[4]
      ), u & /*allow_overflow*/
      2048 && L(
        t,
        "overflow",
        /*allow_overflow*/
        a[11] ? "visible" : "hidden"
      ), u & /*scale*/
      4096 && L(
        t,
        "flex-grow",
        /*scale*/
        a[12]
      ), u & /*min_width*/
      8192 && L(t, "min-width", `calc(min(${/*min_width*/
      a[13]}px, 100%))`);
    },
    i(a) {
      r || (_n(s, a), r = !0);
    },
    o(a) {
      mn(s, a), r = !1;
    },
    d(a) {
      a && $n(t), s && s.d(a);
    }
  };
}
function ur(e) {
  let t, n = (
    /*tag*/
    e[14] && ar(e)
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
      t || (_n(n, r), t = !0);
    },
    o(r) {
      mn(n, r), t = !1;
    },
    d(r) {
      n && n.d(r);
    }
  };
}
function fr(e, t, n) {
  let { $$slots: r = {}, $$scope: i } = t, { height: s = void 0 } = t, { width: l = void 0 } = t, { elem_id: o = "" } = t, { elem_classes: a = [] } = t, { variant: u = "solid" } = t, { border_mode: f = "base" } = t, { padding: c = !0 } = t, { type: h = "normal" } = t, { test_id: _ = void 0 } = t, { explicit_call: d = !1 } = t, { container: E = !0 } = t, { visible: w = !0 } = t, { allow_overflow: N = !0 } = t, { scale: b = null } = t, { min_width: m = 0 } = t, T = h === "fieldset" ? "fieldset" : "div";
  return e.$$set = (g) => {
    "height" in g && n(0, s = g.height), "width" in g && n(1, l = g.width), "elem_id" in g && n(2, o = g.elem_id), "elem_classes" in g && n(3, a = g.elem_classes), "variant" in g && n(4, u = g.variant), "border_mode" in g && n(5, f = g.border_mode), "padding" in g && n(6, c = g.padding), "type" in g && n(15, h = g.type), "test_id" in g && n(7, _ = g.test_id), "explicit_call" in g && n(8, d = g.explicit_call), "container" in g && n(9, E = g.container), "visible" in g && n(10, w = g.visible), "allow_overflow" in g && n(11, N = g.allow_overflow), "scale" in g && n(12, b = g.scale), "min_width" in g && n(13, m = g.min_width), "$$scope" in g && n(16, i = g.$$scope);
  }, [
    s,
    l,
    o,
    a,
    u,
    f,
    c,
    _,
    d,
    E,
    w,
    N,
    b,
    m,
    T,
    h,
    i,
    r
  ];
}
class hr extends Jn {
  constructor(t) {
    super(), ir(this, t, fr, ur, lr, {
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
  SvelteComponent: cr,
  append: qe,
  attr: Pe,
  create_component: _r,
  destroy_component: mr,
  detach: dr,
  element: wt,
  init: br,
  insert: gr,
  mount_component: pr,
  safe_not_equal: vr,
  set_data: yr,
  space: Er,
  text: wr,
  toggle_class: Z,
  transition_in: xr,
  transition_out: Tr
} = window.__gradio__svelte__internal;
function Hr(e) {
  let t, n, r, i, s, l;
  return r = new /*Icon*/
  e[1]({}), {
    c() {
      t = wt("label"), n = wt("span"), _r(r.$$.fragment), i = Er(), s = wr(
        /*label*/
        e[0]
      ), Pe(n, "class", "svelte-9gxdi0"), Pe(t, "for", ""), Pe(t, "data-testid", "block-label"), Pe(t, "class", "svelte-9gxdi0"), Z(t, "hide", !/*show_label*/
      e[2]), Z(t, "sr-only", !/*show_label*/
      e[2]), Z(
        t,
        "float",
        /*float*/
        e[4]
      ), Z(
        t,
        "hide-label",
        /*disable*/
        e[3]
      );
    },
    m(o, a) {
      gr(o, t, a), qe(t, n), pr(r, n, null), qe(t, i), qe(t, s), l = !0;
    },
    p(o, [a]) {
      (!l || a & /*label*/
      1) && yr(
        s,
        /*label*/
        o[0]
      ), (!l || a & /*show_label*/
      4) && Z(t, "hide", !/*show_label*/
      o[2]), (!l || a & /*show_label*/
      4) && Z(t, "sr-only", !/*show_label*/
      o[2]), (!l || a & /*float*/
      16) && Z(
        t,
        "float",
        /*float*/
        o[4]
      ), (!l || a & /*disable*/
      8) && Z(
        t,
        "hide-label",
        /*disable*/
        o[3]
      );
    },
    i(o) {
      l || (xr(r.$$.fragment, o), l = !0);
    },
    o(o) {
      Tr(r.$$.fragment, o), l = !1;
    },
    d(o) {
      o && dr(t), mr(r);
    }
  };
}
function Br(e, t, n) {
  let { label: r = null } = t, { Icon: i } = t, { show_label: s = !0 } = t, { disable: l = !1 } = t, { float: o = !0 } = t;
  return e.$$set = (a) => {
    "label" in a && n(0, r = a.label), "Icon" in a && n(1, i = a.Icon), "show_label" in a && n(2, s = a.show_label), "disable" in a && n(3, l = a.disable), "float" in a && n(4, o = a.float);
  }, [r, i, s, l, o];
}
class Sr extends cr {
  constructor(t) {
    super(), br(this, t, Br, Hr, vr, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: Ar,
  append: Pr,
  attr: ze,
  binding_callbacks: Nr,
  create_slot: Ir,
  detach: Cr,
  element: xt,
  get_all_dirty_from_scope: Lr,
  get_slot_changes: Or,
  init: Mr,
  insert: Rr,
  safe_not_equal: Ur,
  toggle_class: W,
  transition_in: Dr,
  transition_out: kr,
  update_slot_base: Gr
} = window.__gradio__svelte__internal;
function Fr(e) {
  let t, n, r;
  const i = (
    /*#slots*/
    e[5].default
  ), s = Ir(
    i,
    e,
    /*$$scope*/
    e[4],
    null
  );
  return {
    c() {
      t = xt("div"), n = xt("div"), s && s.c(), ze(n, "class", "icon svelte-3w3rth"), ze(t, "class", "empty svelte-3w3rth"), ze(t, "aria-label", "Empty value"), W(
        t,
        "small",
        /*size*/
        e[0] === "small"
      ), W(
        t,
        "large",
        /*size*/
        e[0] === "large"
      ), W(
        t,
        "unpadded_box",
        /*unpadded_box*/
        e[1]
      ), W(
        t,
        "small_parent",
        /*parent_height*/
        e[3]
      );
    },
    m(l, o) {
      Rr(l, t, o), Pr(t, n), s && s.m(n, null), e[6](t), r = !0;
    },
    p(l, [o]) {
      s && s.p && (!r || o & /*$$scope*/
      16) && Gr(
        s,
        i,
        l,
        /*$$scope*/
        l[4],
        r ? Or(
          i,
          /*$$scope*/
          l[4],
          o,
          null
        ) : Lr(
          /*$$scope*/
          l[4]
        ),
        null
      ), (!r || o & /*size*/
      1) && W(
        t,
        "small",
        /*size*/
        l[0] === "small"
      ), (!r || o & /*size*/
      1) && W(
        t,
        "large",
        /*size*/
        l[0] === "large"
      ), (!r || o & /*unpadded_box*/
      2) && W(
        t,
        "unpadded_box",
        /*unpadded_box*/
        l[1]
      ), (!r || o & /*parent_height*/
      8) && W(
        t,
        "small_parent",
        /*parent_height*/
        l[3]
      );
    },
    i(l) {
      r || (Dr(s, l), r = !0);
    },
    o(l) {
      kr(s, l), r = !1;
    },
    d(l) {
      l && Cr(t), s && s.d(l), e[6](null);
    }
  };
}
function Vr(e) {
  let t, n = e[0], r = 1;
  for (; r < e.length; ) {
    const i = e[r], s = e[r + 1];
    if (r += 2, (i === "optionalAccess" || i === "optionalCall") && n == null)
      return;
    i === "access" || i === "optionalAccess" ? (t = n, n = s(n)) : (i === "call" || i === "optionalCall") && (n = s((...l) => n.call(t, ...l)), t = void 0);
  }
  return n;
}
function jr(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { size: l = "small" } = t, { unpadded_box: o = !1 } = t, a;
  function u(c) {
    if (!c)
      return !1;
    const { height: h } = c.getBoundingClientRect(), { height: _ } = Vr([
      c,
      "access",
      (d) => d.parentElement,
      "optionalAccess",
      (d) => d.getBoundingClientRect,
      "call",
      (d) => d()
    ]) || { height: h };
    return h > _ + 2;
  }
  function f(c) {
    Nr[c ? "unshift" : "push"](() => {
      a = c, n(2, a);
    });
  }
  return e.$$set = (c) => {
    "size" in c && n(0, l = c.size), "unpadded_box" in c && n(1, o = c.unpadded_box), "$$scope" in c && n(4, s = c.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty & /*el*/
    4 && n(3, r = u(a));
  }, [l, o, a, r, s, i, f];
}
class Xr extends Ar {
  constructor(t) {
    super(), Mr(this, t, jr, Fr, Ur, { size: 0, unpadded_box: 1 });
  }
}
const {
  SvelteComponent: qr,
  append: ie,
  attr: S,
  detach: zr,
  init: Zr,
  insert: Wr,
  noop: Ze,
  safe_not_equal: Qr,
  svg_element: $
} = window.__gradio__svelte__internal;
function Jr(e) {
  let t, n, r, i, s, l, o;
  return {
    c() {
      t = $("svg"), n = $("circle"), r = $("circle"), i = $("circle"), s = $("circle"), l = $("circle"), o = $("path"), S(n, "cx", "20"), S(n, "cy", "4"), S(n, "r", "2"), S(n, "fill", "currentColor"), S(r, "cx", "8"), S(r, "cy", "16"), S(r, "r", "2"), S(r, "fill", "currentColor"), S(i, "cx", "28"), S(i, "cy", "12"), S(i, "r", "2"), S(i, "fill", "currentColor"), S(s, "cx", "11"), S(s, "cy", "7"), S(s, "r", "2"), S(s, "fill", "currentColor"), S(l, "cx", "16"), S(l, "cy", "24"), S(l, "r", "2"), S(l, "fill", "currentColor"), S(o, "fill", "currentColor"), S(o, "d", "M30 3.413L28.586 2L4 26.585V2H2v26a2 2 0 0 0 2 2h26v-2H5.413Z"), S(t, "xmlns", "http://www.w3.org/2000/svg"), S(t, "xmlns:xlink", "http://www.w3.org/1999/xlink"), S(t, "aria-hidden", "true"), S(t, "role", "img"), S(t, "class", "iconify iconify--carbon"), S(t, "width", "100%"), S(t, "height", "100%"), S(t, "preserveAspectRatio", "xMidYMid meet"), S(t, "viewBox", "0 0 32 32");
    },
    m(a, u) {
      Wr(a, t, u), ie(t, n), ie(t, r), ie(t, i), ie(t, s), ie(t, l), ie(t, o);
    },
    p: Ze,
    i: Ze,
    o: Ze,
    d(a) {
      a && zr(t);
    }
  };
}
class dn extends qr {
  constructor(t) {
    super(), Zr(this, t, null, Jr, Qr, {});
  }
}
const Yr = [
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
], Tt = {
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
Yr.reduce(
  (e, { color: t, primary: n, secondary: r }) => ({
    ...e,
    [t]: {
      primary: Tt[t][n],
      secondary: Tt[t][r]
    }
  }),
  {}
);
function ne() {
}
function Kr(e) {
  return e();
}
function $r(e) {
  e.forEach(Kr);
}
function ei(e) {
  return typeof e == "function";
}
function ti(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function bn(e, ...t) {
  if (e == null) {
    for (const r of t)
      r(void 0);
    return ne;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function ni(e) {
  let t;
  return bn(e, (n) => t = n)(), t;
}
const gn = typeof window < "u";
let Ht = gn ? () => window.performance.now() : () => Date.now(), pn = gn ? (e) => requestAnimationFrame(e) : ne;
const oe = /* @__PURE__ */ new Set();
function vn(e) {
  oe.forEach((t) => {
    t.c(e) || (oe.delete(t), t.f());
  }), oe.size !== 0 && pn(vn);
}
function ri(e) {
  let t;
  return oe.size === 0 && pn(vn), {
    promise: new Promise((n) => {
      oe.add(t = { c: e, f: n });
    }),
    abort() {
      oe.delete(t);
    }
  };
}
const se = [];
function ii(e, t) {
  return {
    subscribe: we(e, t).subscribe
  };
}
function we(e, t = ne) {
  let n;
  const r = /* @__PURE__ */ new Set();
  function i(o) {
    if (ti(e, o) && (e = o, n)) {
      const a = !se.length;
      for (const u of r)
        u[1](), se.push(u, e);
      if (a) {
        for (let u = 0; u < se.length; u += 2)
          se[u][0](se[u + 1]);
        se.length = 0;
      }
    }
  }
  function s(o) {
    i(o(e));
  }
  function l(o, a = ne) {
    const u = [o, a];
    return r.add(u), r.size === 1 && (n = t(i, s) || ne), o(e), () => {
      r.delete(u), r.size === 0 && n && (n(), n = null);
    };
  }
  return { set: i, update: s, subscribe: l };
}
function me(e, t, n) {
  const r = !Array.isArray(e), i = r ? [e] : e;
  if (!i.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const s = t.length < 2;
  return ii(n, (l, o) => {
    let a = !1;
    const u = [];
    let f = 0, c = ne;
    const h = () => {
      if (f)
        return;
      c();
      const d = t(r ? u[0] : u, l, o);
      s ? l(d) : c = ei(d) ? d : ne;
    }, _ = i.map(
      (d, E) => bn(
        d,
        (w) => {
          u[E] = w, f &= ~(1 << E), a && h();
        },
        () => {
          f |= 1 << E;
        }
      )
    );
    return a = !0, h(), function() {
      $r(_), c(), a = !1;
    };
  });
}
function Bt(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function tt(e, t, n, r) {
  if (typeof n == "number" || Bt(n)) {
    const i = r - n, s = (n - t) / (e.dt || 1 / 60), l = e.opts.stiffness * i, o = e.opts.damping * s, a = (l - o) * e.inv_mass, u = (s + a) * e.dt;
    return Math.abs(u) < e.opts.precision && Math.abs(i) < e.opts.precision ? r : (e.settled = !1, Bt(n) ? new Date(n.getTime() + u) : n + u);
  } else {
    if (Array.isArray(n))
      return n.map(
        (i, s) => tt(e, t[s], n[s], r[s])
      );
    if (typeof n == "object") {
      const i = {};
      for (const s in n)
        i[s] = tt(e, t[s], n[s], r[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function St(e, t = {}) {
  const n = we(e), { stiffness: r = 0.15, damping: i = 0.8, precision: s = 0.01 } = t;
  let l, o, a, u = e, f = e, c = 1, h = 0, _ = !1;
  function d(w, N = {}) {
    f = w;
    const b = a = {};
    return e == null || N.hard || E.stiffness >= 1 && E.damping >= 1 ? (_ = !0, l = Ht(), u = w, n.set(e = f), Promise.resolve()) : (N.soft && (h = 1 / ((N.soft === !0 ? 0.5 : +N.soft) * 60), c = 0), o || (l = Ht(), _ = !1, o = ri((m) => {
      if (_)
        return _ = !1, o = null, !1;
      c = Math.min(c + h, 1);
      const T = {
        inv_mass: c,
        opts: E,
        settled: !0,
        dt: (m - l) * 60 / 1e3
      }, g = tt(T, u, e, f);
      return l = m, u = e, n.set(e = g), T.settled && (o = null), !T.settled;
    })), new Promise((m) => {
      o.promise.then(() => {
        b === a && m();
      });
    }));
  }
  const E = {
    set: d,
    update: (w, N) => d(w(f, e), N),
    subscribe: n.subscribe,
    stiffness: r,
    damping: i,
    precision: s
  };
  return E;
}
function si(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var li = function(t) {
  return oi(t) && !ai(t);
};
function oi(e) {
  return !!e && typeof e == "object";
}
function ai(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || hi(e);
}
var ui = typeof Symbol == "function" && Symbol.for, fi = ui ? Symbol.for("react.element") : 60103;
function hi(e) {
  return e.$$typeof === fi;
}
function ci(e) {
  return Array.isArray(e) ? [] : {};
}
function ye(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? ae(ci(e), e, t) : e;
}
function _i(e, t, n) {
  return e.concat(t).map(function(r) {
    return ye(r, n);
  });
}
function mi(e, t) {
  if (!t.customMerge)
    return ae;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : ae;
}
function di(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function At(e) {
  return Object.keys(e).concat(di(e));
}
function yn(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function bi(e, t) {
  return yn(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function gi(e, t, n) {
  var r = {};
  return n.isMergeableObject(e) && At(e).forEach(function(i) {
    r[i] = ye(e[i], n);
  }), At(t).forEach(function(i) {
    bi(e, i) || (yn(e, i) && n.isMergeableObject(t[i]) ? r[i] = mi(i, n)(e[i], t[i], n) : r[i] = ye(t[i], n));
  }), r;
}
function ae(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || _i, n.isMergeableObject = n.isMergeableObject || li, n.cloneUnlessOtherwiseSpecified = ye;
  var r = Array.isArray(t), i = Array.isArray(e), s = r === i;
  return s ? r ? n.arrayMerge(e, t, n) : gi(e, t, n) : ye(t, n);
}
ae.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(r, i) {
    return ae(r, i, n);
  }, {});
};
var pi = ae, vi = pi;
const yi = /* @__PURE__ */ si(vi);
var nt = function(e, t) {
  return nt = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, r) {
    n.__proto__ = r;
  } || function(n, r) {
    for (var i in r)
      Object.prototype.hasOwnProperty.call(r, i) && (n[i] = r[i]);
  }, nt(e, t);
};
function Ge(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  nt(e, t);
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
function We(e, t, n) {
  if (n || arguments.length === 2)
    for (var r = 0, i = t.length, s; r < i; r++)
      (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)), s[r] = t[r]);
  return e.concat(s || Array.prototype.slice.call(t));
}
var x;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(x || (x = {}));
var P;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(P || (P = {}));
var ue;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(ue || (ue = {}));
function Pt(e) {
  return e.type === P.literal;
}
function Ei(e) {
  return e.type === P.argument;
}
function En(e) {
  return e.type === P.number;
}
function wn(e) {
  return e.type === P.date;
}
function xn(e) {
  return e.type === P.time;
}
function Tn(e) {
  return e.type === P.select;
}
function Hn(e) {
  return e.type === P.plural;
}
function wi(e) {
  return e.type === P.pound;
}
function Bn(e) {
  return e.type === P.tag;
}
function Sn(e) {
  return !!(e && typeof e == "object" && e.type === ue.number);
}
function rt(e) {
  return !!(e && typeof e == "object" && e.type === ue.dateTime);
}
var An = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, xi = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function Ti(e) {
  var t = {};
  return e.replace(xi, function(n) {
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
var Hi = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function Bi(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(Hi).filter(function(h) {
    return h.length > 0;
  }), n = [], r = 0, i = t; r < i.length; r++) {
    var s = i[r], l = s.split("/");
    if (l.length === 0)
      throw new Error("Invalid number skeleton");
    for (var o = l[0], a = l.slice(1), u = 0, f = a; u < f.length; u++) {
      var c = f[u];
      if (c.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: o, options: a });
  }
  return n;
}
function Si(e) {
  return e.replace(/^(.*?)-/, "");
}
var Nt = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, Pn = /^(@+)?(\+|#+)?[rs]?$/g, Ai = /(\*)(0+)|(#+)(0+)|(0+)/g, Nn = /^(0+)$/;
function It(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(Pn, function(n, r, i) {
    return typeof i != "string" ? (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length) : i === "+" ? t.minimumSignificantDigits = r.length : r[0] === "#" ? t.maximumSignificantDigits = r.length : (t.minimumSignificantDigits = r.length, t.maximumSignificantDigits = r.length + (typeof i == "string" ? i.length : 0)), "";
  }), t;
}
function In(e) {
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
function Pi(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !Nn.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Ct(e) {
  var t = {}, n = In(e);
  return n || t;
}
function Ni(e) {
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
        t.style = "unit", t.unit = Si(i.options[0]);
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
        t = A(A(A({}, t), { notation: "scientific" }), i.options.reduce(function(a, u) {
          return A(A({}, a), Ct(u));
        }, {}));
        continue;
      case "engineering":
        t = A(A(A({}, t), { notation: "engineering" }), i.options.reduce(function(a, u) {
          return A(A({}, a), Ct(u));
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
        i.options[0].replace(Ai, function(a, u, f, c, h, _) {
          if (u)
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
    if (Nn.test(i.stem)) {
      t.minimumIntegerDigits = i.stem.length;
      continue;
    }
    if (Nt.test(i.stem)) {
      if (i.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      i.stem.replace(Nt, function(a, u, f, c, h, _) {
        return f === "*" ? t.minimumFractionDigits = u.length : c && c[0] === "#" ? t.maximumFractionDigits = c.length : h && _ ? (t.minimumFractionDigits = h.length, t.maximumFractionDigits = h.length + _.length) : (t.minimumFractionDigits = u.length, t.maximumFractionDigits = u.length), "";
      });
      var s = i.options[0];
      s === "w" ? t = A(A({}, t), { trailingZeroDisplay: "stripIfInteger" }) : s && (t = A(A({}, t), It(s)));
      continue;
    }
    if (Pn.test(i.stem)) {
      t = A(A({}, t), It(i.stem));
      continue;
    }
    var l = In(i.stem);
    l && (t = A(A({}, t), l));
    var o = Pi(i.stem);
    o && (t = A(A({}, t), o));
  }
  return t;
}
var Ne = {
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
function Ii(e, t) {
  for (var n = "", r = 0; r < e.length; r++) {
    var i = e.charAt(r);
    if (i === "j") {
      for (var s = 0; r + 1 < e.length && e.charAt(r + 1) === i; )
        s++, r++;
      var l = 1 + (s & 1), o = s < 2 ? 1 : 3 + (s >> 1), a = "a", u = Ci(t);
      for ((u == "H" || u == "k") && (o = 0); o-- > 0; )
        n += a;
      for (; l-- > 0; )
        n = u + n;
    } else
      i === "J" ? n += "H" : n += i;
  }
  return n;
}
function Ci(e) {
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
  var i = Ne[r || ""] || Ne[n || ""] || Ne["".concat(n, "-001")] || Ne["001"];
  return i[0];
}
var Qe, Li = new RegExp("^".concat(An.source, "*")), Oi = new RegExp("".concat(An.source, "*$"));
function H(e, t) {
  return { start: e, end: t };
}
var Mi = !!String.prototype.startsWith, Ri = !!String.fromCodePoint, Ui = !!Object.fromEntries, Di = !!String.prototype.codePointAt, ki = !!String.prototype.trimStart, Gi = !!String.prototype.trimEnd, Fi = !!Number.isSafeInteger, Vi = Fi ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, it = !0;
try {
  var ji = Ln("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  it = ((Qe = ji.exec("a")) === null || Qe === void 0 ? void 0 : Qe[0]) === "a";
} catch {
  it = !1;
}
var Lt = Mi ? (
  // Native
  function(t, n, r) {
    return t.startsWith(n, r);
  }
) : (
  // For IE11
  function(t, n, r) {
    return t.slice(r, r + n.length) === n;
  }
), st = Ri ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var r = "", i = t.length, s = 0, l; i > s; ) {
      if (l = t[s++], l > 1114111)
        throw RangeError(l + " is not a valid code point");
      r += l < 65536 ? String.fromCharCode(l) : String.fromCharCode(((l -= 65536) >> 10) + 55296, l % 1024 + 56320);
    }
    return r;
  }
), Ot = (
  // native
  Ui ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, r = 0, i = t; r < i.length; r++) {
        var s = i[r], l = s[0], o = s[1];
        n[l] = o;
      }
      return n;
    }
  )
), Cn = Di ? (
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
), Xi = ki ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Li, "");
  }
), qi = Gi ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Oi, "");
  }
);
function Ln(e, t) {
  return new RegExp(e, t);
}
var lt;
if (it) {
  var Mt = Ln("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  lt = function(t, n) {
    var r;
    Mt.lastIndex = n;
    var i = Mt.exec(t);
    return (r = i[1]) !== null && r !== void 0 ? r : "";
  };
} else
  lt = function(t, n) {
    for (var r = []; ; ) {
      var i = Cn(t, n);
      if (i === void 0 || On(i) || Qi(i))
        break;
      r.push(i), n += i >= 65536 ? 2 : 1;
    }
    return st.apply(void 0, r);
  };
var zi = (
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
          var l = this.parseArgument(t, r);
          if (l.err)
            return l;
          i.push(l.val);
        } else {
          if (s === 125 && t > 0)
            break;
          if (s === 35 && (n === "plural" || n === "selectordinal")) {
            var o = this.clonePosition();
            this.bump(), i.push({
              type: P.pound,
              location: H(o, this.clonePosition())
            });
          } else if (s === 60 && !this.ignoreTag && this.peek() === 47) {
            if (r)
              break;
            return this.error(x.UNMATCHED_CLOSING_TAG, H(this.clonePosition(), this.clonePosition()));
          } else if (s === 60 && !this.ignoreTag && ot(this.peek() || 0)) {
            var l = this.parseTag(t, n);
            if (l.err)
              return l;
            i.push(l.val);
          } else {
            var l = this.parseLiteral(t, n);
            if (l.err)
              return l;
            i.push(l.val);
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
            type: P.literal,
            value: "<".concat(i, "/>"),
            location: H(r, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var s = this.parseMessage(t + 1, n, !0);
        if (s.err)
          return s;
        var l = s.val, o = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !ot(this.char()))
            return this.error(x.INVALID_TAG, H(o, this.clonePosition()));
          var a = this.clonePosition(), u = this.parseTagName();
          return i !== u ? this.error(x.UNMATCHED_CLOSING_TAG, H(a, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: P.tag,
              value: i,
              children: l,
              location: H(r, this.clonePosition())
            },
            err: null
          } : this.error(x.INVALID_TAG, H(o, this.clonePosition())));
        } else
          return this.error(x.UNCLOSED_TAG, H(r, this.clonePosition()));
      } else
        return this.error(x.INVALID_TAG, H(r, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && Wi(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var r = this.clonePosition(), i = ""; ; ) {
        var s = this.tryParseQuote(n);
        if (s) {
          i += s;
          continue;
        }
        var l = this.tryParseUnquoted(t, n);
        if (l) {
          i += l;
          continue;
        }
        var o = this.tryParseLeftAngleBracket();
        if (o) {
          i += o;
          continue;
        }
        break;
      }
      var a = H(r, this.clonePosition());
      return {
        val: { type: P.literal, value: i, location: a },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !Zi(this.peek() || 0)) ? (this.bump(), "<") : null;
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
      return st.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var r = this.char();
      return r === 60 || r === 123 || r === 35 && (n === "plural" || n === "selectordinal") || r === 125 && t > 0 ? null : (this.bump(), st(r));
    }, e.prototype.parseArgument = function(t, n) {
      var r = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(x.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(x.EMPTY_ARGUMENT, H(r, this.clonePosition()));
      var i = this.parseIdentifierIfPossible().value;
      if (!i)
        return this.error(x.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(x.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: P.argument,
              // value does not include the opening and closing braces.
              value: i,
              location: H(r, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(x.EXPECT_ARGUMENT_CLOSING_BRACE, H(r, this.clonePosition())) : this.parseArgumentOptions(t, n, i, r);
        default:
          return this.error(x.MALFORMED_ARGUMENT, H(r, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), r = lt(this.message, n), i = n + r.length;
      this.bumpTo(i);
      var s = this.clonePosition(), l = H(t, s);
      return { value: r, location: l };
    }, e.prototype.parseArgumentOptions = function(t, n, r, i) {
      var s, l = this.clonePosition(), o = this.parseIdentifierIfPossible().value, a = this.clonePosition();
      switch (o) {
        case "":
          return this.error(x.EXPECT_ARGUMENT_TYPE, H(l, a));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var u = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), c = this.parseSimpleArgStyleIfPossible();
            if (c.err)
              return c;
            var h = qi(c.val);
            if (h.length === 0)
              return this.error(x.EXPECT_ARGUMENT_STYLE, H(this.clonePosition(), this.clonePosition()));
            var _ = H(f, this.clonePosition());
            u = { style: h, styleLocation: _ };
          }
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var E = H(i, this.clonePosition());
          if (u && Lt(u == null ? void 0 : u.style, "::", 0)) {
            var w = Xi(u.style.slice(2));
            if (o === "number") {
              var c = this.parseNumberSkeletonFromString(w, u.styleLocation);
              return c.err ? c : {
                val: { type: P.number, value: r, location: E, style: c.val },
                err: null
              };
            } else {
              if (w.length === 0)
                return this.error(x.EXPECT_DATE_TIME_SKELETON, E);
              var N = w;
              this.locale && (N = Ii(w, this.locale));
              var h = {
                type: ue.dateTime,
                pattern: N,
                location: u.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? Ti(N) : {}
              }, b = o === "date" ? P.date : P.time;
              return {
                val: { type: b, value: r, location: E, style: h },
                err: null
              };
            }
          }
          return {
            val: {
              type: o === "number" ? P.number : o === "date" ? P.date : P.time,
              value: r,
              location: E,
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
            return this.error(x.EXPECT_SELECT_ARGUMENT_OPTIONS, H(m, A({}, m)));
          this.bumpSpace();
          var T = this.parseIdentifierIfPossible(), g = 0;
          if (o !== "select" && T.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(x.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, H(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var c = this.tryParseDecimalInteger(x.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, x.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (c.err)
              return c;
            this.bumpSpace(), T = this.parseIdentifierIfPossible(), g = c.val;
          }
          var j = this.tryParsePluralOrSelectOptions(t, o, n, T);
          if (j.err)
            return j;
          var d = this.tryParseArgumentClose(i);
          if (d.err)
            return d;
          var X = H(i, this.clonePosition());
          return o === "select" ? {
            val: {
              type: P.select,
              value: r,
              options: Ot(j.val),
              location: X
            },
            err: null
          } : {
            val: {
              type: P.plural,
              value: r,
              options: Ot(j.val),
              offset: g,
              pluralType: o === "plural" ? "cardinal" : "ordinal",
              location: X
            },
            err: null
          };
        }
        default:
          return this.error(x.INVALID_ARGUMENT_TYPE, H(l, a));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(x.EXPECT_ARGUMENT_CLOSING_BRACE, H(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var r = this.char();
        switch (r) {
          case 39: {
            this.bump();
            var i = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(x.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, H(i, this.clonePosition()));
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
        r = Bi(t);
      } catch {
        return this.error(x.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: ue.number,
          tokens: r,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? Ni(r) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, r, i) {
      for (var s, l = !1, o = [], a = /* @__PURE__ */ new Set(), u = i.value, f = i.location; ; ) {
        if (u.length === 0) {
          var c = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var h = this.tryParseDecimalInteger(x.EXPECT_PLURAL_ARGUMENT_SELECTOR, x.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (h.err)
              return h;
            f = H(c, this.clonePosition()), u = this.message.slice(c.offset, this.offset());
          } else
            break;
        }
        if (a.has(u))
          return this.error(n === "select" ? x.DUPLICATE_SELECT_ARGUMENT_SELECTOR : x.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        u === "other" && (l = !0), this.bumpSpace();
        var _ = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? x.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : x.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, H(this.clonePosition(), this.clonePosition()));
        var d = this.parseMessage(t + 1, n, r);
        if (d.err)
          return d;
        var E = this.tryParseArgumentClose(_);
        if (E.err)
          return E;
        o.push([
          u,
          {
            value: d.val,
            location: H(_, this.clonePosition())
          }
        ]), a.add(u), this.bumpSpace(), s = this.parseIdentifierIfPossible(), u = s.value, f = s.location;
      }
      return o.length === 0 ? this.error(n === "select" ? x.EXPECT_SELECT_ARGUMENT_SELECTOR : x.EXPECT_PLURAL_ARGUMENT_SELECTOR, H(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !l ? this.error(x.MISSING_OTHER_CLAUSE, H(this.clonePosition(), this.clonePosition())) : { val: o, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var r = 1, i = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (r = -1);
      for (var s = !1, l = 0; !this.isEOF(); ) {
        var o = this.char();
        if (o >= 48 && o <= 57)
          s = !0, l = l * 10 + (o - 48), this.bump();
        else
          break;
      }
      var a = H(i, this.clonePosition());
      return s ? (l *= r, Vi(l) ? { val: l, err: null } : this.error(n, a)) : this.error(t, a);
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
      var n = Cn(this.message, t);
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
      for (; !this.isEOF() && On(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), r = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return r ?? null;
    }, e;
  }()
);
function ot(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Zi(e) {
  return ot(e) || e === 47;
}
function Wi(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function On(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function Qi(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function at(e) {
  e.forEach(function(t) {
    if (delete t.location, Tn(t) || Hn(t))
      for (var n in t.options)
        delete t.options[n].location, at(t.options[n].value);
    else
      En(t) && Sn(t.style) || (wn(t) || xn(t)) && rt(t.style) ? delete t.style.location : Bn(t) && at(t.children);
  });
}
function Ji(e, t) {
  t === void 0 && (t = {}), t = A({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new zi(e, t).parse();
  if (n.err) {
    var r = SyntaxError(x[n.err.kind]);
    throw r.location = n.err.location, r.originalMessage = n.err.message, r;
  }
  return t != null && t.captureLocation || at(n.val), n.val;
}
function Je(e, t) {
  var n = t && t.cache ? t.cache : ns, r = t && t.serializer ? t.serializer : ts, i = t && t.strategy ? t.strategy : Ki;
  return i(e, {
    cache: n,
    serializer: r
  });
}
function Yi(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function Mn(e, t, n, r) {
  var i = Yi(r) ? r : n(r), s = t.get(i);
  return typeof s > "u" && (s = e.call(this, r), t.set(i, s)), s;
}
function Rn(e, t, n) {
  var r = Array.prototype.slice.call(arguments, 3), i = n(r), s = t.get(i);
  return typeof s > "u" && (s = e.apply(this, r), t.set(i, s)), s;
}
function ct(e, t, n, r, i) {
  return n.bind(t, e, r, i);
}
function Ki(e, t) {
  var n = e.length === 1 ? Mn : Rn;
  return ct(e, this, n, t.cache.create(), t.serializer);
}
function $i(e, t) {
  return ct(e, this, Rn, t.cache.create(), t.serializer);
}
function es(e, t) {
  return ct(e, this, Mn, t.cache.create(), t.serializer);
}
var ts = function() {
  return JSON.stringify(arguments);
};
function _t() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
_t.prototype.get = function(e) {
  return this.cache[e];
};
_t.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var ns = {
  create: function() {
    return new _t();
  }
}, Ye = {
  variadic: $i,
  monadic: es
}, fe;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(fe || (fe = {}));
var Fe = (
  /** @class */
  function(e) {
    Ge(t, e);
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
    Ge(t, e);
    function t(n, r, i, s) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(r, '". Options are "').concat(Object.keys(i).join('", "'), '"'), fe.INVALID_VALUE, s) || this;
    }
    return t;
  }(Fe)
), rs = (
  /** @class */
  function(e) {
    Ge(t, e);
    function t(n, r, i) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(r), fe.INVALID_VALUE, i) || this;
    }
    return t;
  }(Fe)
), is = (
  /** @class */
  function(e) {
    Ge(t, e);
    function t(n, r) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(r, '"'), fe.MISSING_VALUE, r) || this;
    }
    return t;
  }(Fe)
), C;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(C || (C = {}));
function ss(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var r = t[t.length - 1];
    return !r || r.type !== C.literal || n.type !== C.literal ? t.push(n) : r.value += n.value, t;
  }, []);
}
function ls(e) {
  return typeof e == "function";
}
function Le(e, t, n, r, i, s, l) {
  if (e.length === 1 && Pt(e[0]))
    return [
      {
        type: C.literal,
        value: e[0].value
      }
    ];
  for (var o = [], a = 0, u = e; a < u.length; a++) {
    var f = u[a];
    if (Pt(f)) {
      o.push({
        type: C.literal,
        value: f.value
      });
      continue;
    }
    if (wi(f)) {
      typeof s == "number" && o.push({
        type: C.literal,
        value: n.getNumberFormat(t).format(s)
      });
      continue;
    }
    var c = f.value;
    if (!(i && c in i))
      throw new is(c, l);
    var h = i[c];
    if (Ei(f)) {
      (!h || typeof h == "string" || typeof h == "number") && (h = typeof h == "string" || typeof h == "number" ? String(h) : ""), o.push({
        type: typeof h == "string" ? C.literal : C.object,
        value: h
      });
      continue;
    }
    if (wn(f)) {
      var _ = typeof f.style == "string" ? r.date[f.style] : rt(f.style) ? f.style.parsedOptions : void 0;
      o.push({
        type: C.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (xn(f)) {
      var _ = typeof f.style == "string" ? r.time[f.style] : rt(f.style) ? f.style.parsedOptions : r.time.medium;
      o.push({
        type: C.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (En(f)) {
      var _ = typeof f.style == "string" ? r.number[f.style] : Sn(f.style) ? f.style.parsedOptions : void 0;
      _ && _.scale && (h = h * (_.scale || 1)), o.push({
        type: C.literal,
        value: n.getNumberFormat(t, _).format(h)
      });
      continue;
    }
    if (Bn(f)) {
      var d = f.children, E = f.value, w = i[E];
      if (!ls(w))
        throw new rs(E, "function", l);
      var N = Le(d, t, n, r, i, s), b = w(N.map(function(g) {
        return g.value;
      }));
      Array.isArray(b) || (b = [b]), o.push.apply(o, b.map(function(g) {
        return {
          type: typeof g == "string" ? C.literal : C.object,
          value: g
        };
      }));
    }
    if (Tn(f)) {
      var m = f.options[h] || f.options.other;
      if (!m)
        throw new Rt(f.value, h, Object.keys(f.options), l);
      o.push.apply(o, Le(m.value, t, n, r, i));
      continue;
    }
    if (Hn(f)) {
      var m = f.options["=".concat(h)];
      if (!m) {
        if (!Intl.PluralRules)
          throw new Fe(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, fe.MISSING_INTL_API, l);
        var T = n.getPluralRules(t, { type: f.pluralType }).select(h - (f.offset || 0));
        m = f.options[T] || f.options.other;
      }
      if (!m)
        throw new Rt(f.value, h, Object.keys(f.options), l);
      o.push.apply(o, Le(m.value, t, n, r, i, h - (f.offset || 0)));
      continue;
    }
  }
  return ss(o);
}
function os(e, t) {
  return t ? A(A(A({}, e || {}), t || {}), Object.keys(e).reduce(function(n, r) {
    return n[r] = A(A({}, e[r]), t[r] || {}), n;
  }, {})) : e;
}
function as(e, t) {
  return t ? Object.keys(e).reduce(function(n, r) {
    return n[r] = os(e[r], t[r]), n;
  }, A({}, e)) : e;
}
function Ke(e) {
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
function us(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Je(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.NumberFormat).bind.apply(t, We([void 0], n, !1)))();
    }, {
      cache: Ke(e.number),
      strategy: Ye.variadic
    }),
    getDateTimeFormat: Je(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, We([void 0], n, !1)))();
    }, {
      cache: Ke(e.dateTime),
      strategy: Ye.variadic
    }),
    getPluralRules: Je(function() {
      for (var t, n = [], r = 0; r < arguments.length; r++)
        n[r] = arguments[r];
      return new ((t = Intl.PluralRules).bind.apply(t, We([void 0], n, !1)))();
    }, {
      cache: Ke(e.pluralRules),
      strategy: Ye.variadic
    })
  };
}
var fs = (
  /** @class */
  function() {
    function e(t, n, r, i) {
      var s = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(l) {
        var o = s.formatToParts(l);
        if (o.length === 1)
          return o[0].value;
        var a = o.reduce(function(u, f) {
          return !u.length || f.type !== C.literal || typeof u[u.length - 1] != "string" ? u.push(f.value) : u[u.length - 1] += f.value, u;
        }, []);
        return a.length <= 1 ? a[0] || "" : a;
      }, this.formatToParts = function(l) {
        return Le(s.ast, s.locales, s.formatters, s.formats, l, void 0, s.message);
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
      this.formats = as(e.formats, r), this.formatters = i && i.formatters || us(this.formatterCache);
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
    }, e.__parse = Ji, e.formats = {
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
function hs(e, t) {
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
const Q = {}, cs = (e, t, n) => n && (t in Q || (Q[t] = {}), e in Q[t] || (Q[t][e] = n), n), Un = (e, t) => {
  if (t == null)
    return;
  if (t in Q && e in Q[t])
    return Q[t][e];
  const n = Ve(t);
  for (let r = 0; r < n.length; r++) {
    const i = n[r], s = ms(i, e);
    if (s)
      return cs(e, t, s);
  }
};
let mt;
const xe = we({});
function _s(e) {
  return mt[e] || null;
}
function Dn(e) {
  return e in mt;
}
function ms(e, t) {
  if (!Dn(e))
    return null;
  const n = _s(e);
  return hs(n, t);
}
function ds(e) {
  if (e == null)
    return;
  const t = Ve(e);
  for (let n = 0; n < t.length; n++) {
    const r = t[n];
    if (Dn(r))
      return r;
  }
}
function bs(e, ...t) {
  delete Q[e], xe.update((n) => (n[e] = yi.all([n[e] || {}, ...t]), n));
}
me(
  [xe],
  ([e]) => Object.keys(e)
);
xe.subscribe((e) => mt = e);
const Oe = {};
function gs(e, t) {
  Oe[e].delete(t), Oe[e].size === 0 && delete Oe[e];
}
function kn(e) {
  return Oe[e];
}
function ps(e) {
  return Ve(e).map((t) => {
    const n = kn(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function ut(e) {
  return e == null ? !1 : Ve(e).some(
    (t) => {
      var n;
      return (n = kn(t)) == null ? void 0 : n.size;
    }
  );
}
function vs(e, t) {
  return Promise.all(
    t.map((r) => (gs(e, r), r().then((i) => i.default || i)))
  ).then((r) => bs(e, ...r));
}
const ve = {};
function Gn(e) {
  if (!ut(e))
    return e in ve ? ve[e] : Promise.resolve();
  const t = ps(e);
  return ve[e] = Promise.all(
    t.map(
      ([n, r]) => vs(n, r)
    )
  ).then(() => {
    if (ut(e))
      return Gn(e);
    delete ve[e];
  }), ve[e];
}
const ys = {
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
}, Es = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: ys,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, ws = Es;
function he() {
  return ws;
}
const $e = we(!1);
var xs = Object.defineProperty, Ts = Object.defineProperties, Hs = Object.getOwnPropertyDescriptors, Ut = Object.getOwnPropertySymbols, Bs = Object.prototype.hasOwnProperty, Ss = Object.prototype.propertyIsEnumerable, Dt = (e, t, n) => t in e ? xs(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, As = (e, t) => {
  for (var n in t || (t = {}))
    Bs.call(t, n) && Dt(e, n, t[n]);
  if (Ut)
    for (var n of Ut(t))
      Ss.call(t, n) && Dt(e, n, t[n]);
  return e;
}, Ps = (e, t) => Ts(e, Hs(t));
let ft;
const Ue = we(null);
function kt(e) {
  return e.split("-").map((t, n, r) => r.slice(0, n + 1).join("-")).reverse();
}
function Ve(e, t = he().fallbackLocale) {
  const n = kt(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...kt(t)])] : n;
}
function re() {
  return ft ?? void 0;
}
Ue.subscribe((e) => {
  ft = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const Ns = (e) => {
  if (e && ds(e) && ut(e)) {
    const { loadingDelay: t } = he();
    let n;
    return typeof window < "u" && re() != null && t ? n = window.setTimeout(
      () => $e.set(!0),
      t
    ) : $e.set(!0), Gn(e).then(() => {
      Ue.set(e);
    }).finally(() => {
      clearTimeout(n), $e.set(!1);
    });
  }
  return Ue.set(e);
}, Te = Ps(As({}, Ue), {
  set: Ns
}), je = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (r) => {
    const i = JSON.stringify(r);
    return i in t ? t[i] : t[i] = e(r);
  };
};
var Is = Object.defineProperty, De = Object.getOwnPropertySymbols, Fn = Object.prototype.hasOwnProperty, Vn = Object.prototype.propertyIsEnumerable, Gt = (e, t, n) => t in e ? Is(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, dt = (e, t) => {
  for (var n in t || (t = {}))
    Fn.call(t, n) && Gt(e, n, t[n]);
  if (De)
    for (var n of De(t))
      Vn.call(t, n) && Gt(e, n, t[n]);
  return e;
}, de = (e, t) => {
  var n = {};
  for (var r in e)
    Fn.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
  if (e != null && De)
    for (var r of De(e))
      t.indexOf(r) < 0 && Vn.call(e, r) && (n[r] = e[r]);
  return n;
};
const Ee = (e, t) => {
  const { formats: n } = he();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, Cs = je(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = de(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return r && (i = Ee("number", r)), new Intl.NumberFormat(n, i);
  }
), Ls = je(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = de(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return r ? i = Ee("date", r) : Object.keys(i).length === 0 && (i = Ee("date", "short")), new Intl.DateTimeFormat(n, i);
  }
), Os = je(
  (e) => {
    var t = e, { locale: n, format: r } = t, i = de(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return r ? i = Ee("time", r) : Object.keys(i).length === 0 && (i = Ee("time", "short")), new Intl.DateTimeFormat(n, i);
  }
), Ms = (e = {}) => {
  var t = e, {
    locale: n = re()
  } = t, r = de(t, [
    "locale"
  ]);
  return Cs(dt({ locale: n }, r));
}, Rs = (e = {}) => {
  var t = e, {
    locale: n = re()
  } = t, r = de(t, [
    "locale"
  ]);
  return Ls(dt({ locale: n }, r));
}, Us = (e = {}) => {
  var t = e, {
    locale: n = re()
  } = t, r = de(t, [
    "locale"
  ]);
  return Os(dt({ locale: n }, r));
}, Ds = je(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = re()) => new fs(e, t, he().formats, {
    ignoreTag: he().ignoreTag
  })
), ks = (e, t = {}) => {
  var n, r, i, s;
  let l = t;
  typeof e == "object" && (l = e, e = l.id);
  const {
    values: o,
    locale: a = re(),
    default: u
  } = l;
  if (a == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = Un(e, a);
  if (!f)
    f = (s = (i = (r = (n = he()).handleMissingMessage) == null ? void 0 : r.call(n, { locale: a, id: e, defaultValue: u })) != null ? i : u) != null ? s : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!o)
    return f;
  let c = f;
  try {
    c = Ds(f, a).format(o);
  } catch (h) {
    h instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      h.message
    );
  }
  return c;
}, Gs = (e, t) => Us(t).format(e), Fs = (e, t) => Rs(t).format(e), Vs = (e, t) => Ms(t).format(e), js = (e, t = re()) => Un(e, t), Xs = me([Te, xe], () => ks);
me([Te], () => Gs);
me([Te], () => Fs);
me([Te], () => Vs);
me([Te, xe], () => js);
ni(Xs);
function le(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let r = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + r;
}
const {
  SvelteComponent: qs,
  append: R,
  attr: B,
  component_subscribe: Ft,
  detach: zs,
  element: Zs,
  init: Ws,
  insert: Qs,
  noop: Vt,
  safe_not_equal: Js,
  set_style: Ie,
  svg_element: U,
  toggle_class: jt
} = window.__gradio__svelte__internal, { onMount: Ys } = window.__gradio__svelte__internal;
function Ks(e) {
  let t, n, r, i, s, l, o, a, u, f, c, h;
  return {
    c() {
      t = Zs("div"), n = U("svg"), r = U("g"), i = U("path"), s = U("path"), l = U("path"), o = U("path"), a = U("g"), u = U("path"), f = U("path"), c = U("path"), h = U("path"), B(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), B(i, "fill", "#FF7C00"), B(i, "fill-opacity", "0.4"), B(i, "class", "svelte-43sxxs"), B(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), B(s, "fill", "#FF7C00"), B(s, "class", "svelte-43sxxs"), B(l, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), B(l, "fill", "#FF7C00"), B(l, "fill-opacity", "0.4"), B(l, "class", "svelte-43sxxs"), B(o, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), B(o, "fill", "#FF7C00"), B(o, "class", "svelte-43sxxs"), Ie(r, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), B(u, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), B(u, "fill", "#FF7C00"), B(u, "fill-opacity", "0.4"), B(u, "class", "svelte-43sxxs"), B(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), B(f, "fill", "#FF7C00"), B(f, "class", "svelte-43sxxs"), B(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), B(c, "fill", "#FF7C00"), B(c, "fill-opacity", "0.4"), B(c, "class", "svelte-43sxxs"), B(h, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), B(h, "fill", "#FF7C00"), B(h, "class", "svelte-43sxxs"), Ie(a, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), B(n, "viewBox", "-1200 -1200 3000 3000"), B(n, "fill", "none"), B(n, "xmlns", "http://www.w3.org/2000/svg"), B(n, "class", "svelte-43sxxs"), B(t, "class", "svelte-43sxxs"), jt(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(_, d) {
      Qs(_, t, d), R(t, n), R(n, r), R(r, i), R(r, s), R(r, l), R(r, o), R(n, a), R(a, u), R(a, f), R(a, c), R(a, h);
    },
    p(_, [d]) {
      d & /*$top*/
      2 && Ie(r, "transform", "translate(" + /*$top*/
      _[1][0] + "px, " + /*$top*/
      _[1][1] + "px)"), d & /*$bottom*/
      4 && Ie(a, "transform", "translate(" + /*$bottom*/
      _[2][0] + "px, " + /*$bottom*/
      _[2][1] + "px)"), d & /*margin*/
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
      _ && zs(t);
    }
  };
}
function $s(e, t, n) {
  let r, i, { margin: s = !0 } = t;
  const l = St([0, 0]);
  Ft(e, l, (h) => n(1, r = h));
  const o = St([0, 0]);
  Ft(e, o, (h) => n(2, i = h));
  let a;
  async function u() {
    await Promise.all([l.set([125, 140]), o.set([-125, -140])]), await Promise.all([l.set([-125, 140]), o.set([125, -140])]), await Promise.all([l.set([-125, 0]), o.set([125, -0])]), await Promise.all([l.set([125, 0]), o.set([-125, 0])]);
  }
  async function f() {
    await u(), a || f();
  }
  async function c() {
    await Promise.all([l.set([125, 0]), o.set([-125, 0])]), f();
  }
  return Ys(() => (c(), () => a = !0)), e.$$set = (h) => {
    "margin" in h && n(0, s = h.margin);
  }, [s, r, i, l, o];
}
class el extends qs {
  constructor(t) {
    super(), Ws(this, t, $s, Ks, Js, { margin: 0 });
  }
}
const {
  SvelteComponent: tl,
  append: te,
  attr: k,
  binding_callbacks: Xt,
  check_outros: jn,
  create_component: nl,
  create_slot: rl,
  destroy_component: il,
  destroy_each: Xn,
  detach: v,
  element: V,
  empty: be,
  ensure_array_like: ke,
  get_all_dirty_from_scope: sl,
  get_slot_changes: ll,
  group_outros: qn,
  init: ol,
  insert: y,
  mount_component: al,
  noop: ht,
  safe_not_equal: ul,
  set_data: M,
  set_style: J,
  space: G,
  text: I,
  toggle_class: O,
  transition_in: ce,
  transition_out: _e,
  update_slot_base: fl
} = window.__gradio__svelte__internal, { tick: hl } = window.__gradio__svelte__internal, { onDestroy: cl } = window.__gradio__svelte__internal, _l = (e) => ({}), qt = (e) => ({});
function zt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r[40] = n, r;
}
function Zt(e, t, n) {
  const r = e.slice();
  return r[38] = t[n], r;
}
function ml(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), r, i, s;
  const l = (
    /*#slots*/
    e[29].error
  ), o = rl(
    l,
    e,
    /*$$scope*/
    e[28],
    qt
  );
  return {
    c() {
      t = V("span"), r = I(n), i = G(), o && o.c(), k(t, "class", "error svelte-14miwb5");
    },
    m(a, u) {
      y(a, t, u), te(t, r), y(a, i, u), o && o.m(a, u), s = !0;
    },
    p(a, u) {
      (!s || u[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      a[1]("common.error") + "") && M(r, n), o && o.p && (!s || u[0] & /*$$scope*/
      268435456) && fl(
        o,
        l,
        a,
        /*$$scope*/
        a[28],
        s ? ll(
          l,
          /*$$scope*/
          a[28],
          u,
          _l
        ) : sl(
          /*$$scope*/
          a[28]
        ),
        qt
      );
    },
    i(a) {
      s || (ce(o, a), s = !0);
    },
    o(a) {
      _e(o, a), s = !1;
    },
    d(a) {
      a && (v(t), v(i)), o && o.d(a);
    }
  };
}
function dl(e) {
  let t, n, r, i, s, l, o, a, u, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && Wt(e)
  );
  function c(m, T) {
    if (
      /*progress*/
      m[7]
    )
      return pl;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return gl;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return bl;
  }
  let h = c(e), _ = h && h(e), d = (
    /*timer*/
    e[5] && Yt(e)
  );
  const E = [wl, El], w = [];
  function N(m, T) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = N(e)) && (l = w[s] = E[s](e));
  let b = !/*timer*/
  e[5] && sn(e);
  return {
    c() {
      f && f.c(), t = G(), n = V("div"), _ && _.c(), r = G(), d && d.c(), i = G(), l && l.c(), o = G(), b && b.c(), a = be(), k(n, "class", "progress-text svelte-14miwb5"), O(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), O(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(m, T) {
      f && f.m(m, T), y(m, t, T), y(m, n, T), _ && _.m(n, null), te(n, r), d && d.m(n, null), y(m, i, T), ~s && w[s].m(m, T), y(m, o, T), b && b.m(m, T), y(m, a, T), u = !0;
    },
    p(m, T) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? f ? f.p(m, T) : (f = Wt(m), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), h === (h = c(m)) && _ ? _.p(m, T) : (_ && _.d(1), _ = h && h(m), _ && (_.c(), _.m(n, r))), /*timer*/
      m[5] ? d ? d.p(m, T) : (d = Yt(m), d.c(), d.m(n, null)) : d && (d.d(1), d = null), (!u || T[0] & /*variant*/
      256) && O(
        n,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!u || T[0] & /*variant*/
      256) && O(
        n,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let g = s;
      s = N(m), s === g ? ~s && w[s].p(m, T) : (l && (qn(), _e(w[g], 1, 1, () => {
        w[g] = null;
      }), jn()), ~s ? (l = w[s], l ? l.p(m, T) : (l = w[s] = E[s](m), l.c()), ce(l, 1), l.m(o.parentNode, o)) : l = null), /*timer*/
      m[5] ? b && (b.d(1), b = null) : b ? b.p(m, T) : (b = sn(m), b.c(), b.m(a.parentNode, a));
    },
    i(m) {
      u || (ce(l), u = !0);
    },
    o(m) {
      _e(l), u = !1;
    },
    d(m) {
      m && (v(t), v(n), v(i), v(o), v(a)), f && f.d(m), _ && _.d(), d && d.d(), ~s && w[s].d(m), b && b.d(m);
    }
  };
}
function Wt(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = V("div"), k(t, "class", "eta-bar svelte-14miwb5"), J(t, "transform", n);
    },
    m(r, i) {
      y(r, t, i);
    },
    p(r, i) {
      i[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (r[17] || 0) * 100 - 100}%)`) && J(t, "transform", n);
    },
    d(r) {
      r && v(t);
    }
  };
}
function bl(e) {
  let t;
  return {
    c() {
      t = I("processing |");
    },
    m(n, r) {
      y(n, t, r);
    },
    p: ht,
    d(n) {
      n && v(t);
    }
  };
}
function gl(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), r, i, s, l;
  return {
    c() {
      t = I("queue: "), r = I(n), i = I("/"), s = I(
        /*queue_size*/
        e[3]
      ), l = I(" |");
    },
    m(o, a) {
      y(o, t, a), y(o, r, a), y(o, i, a), y(o, s, a), y(o, l, a);
    },
    p(o, a) {
      a[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      o[2] + 1 + "") && M(r, n), a[0] & /*queue_size*/
      8 && M(
        s,
        /*queue_size*/
        o[3]
      );
    },
    d(o) {
      o && (v(t), v(r), v(i), v(s), v(l));
    }
  };
}
function pl(e) {
  let t, n = ke(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = Jt(Zt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = be();
    },
    m(i, s) {
      for (let l = 0; l < r.length; l += 1)
        r[l] && r[l].m(i, s);
      y(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        n = ke(
          /*progress*/
          i[7]
        );
        let l;
        for (l = 0; l < n.length; l += 1) {
          const o = Zt(i, n, l);
          r[l] ? r[l].p(o, s) : (r[l] = Jt(o), r[l].c(), r[l].m(t.parentNode, t));
        }
        for (; l < r.length; l += 1)
          r[l].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && v(t), Xn(r, i);
    }
  };
}
function Qt(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), r, i, s = " ", l;
  function o(f, c) {
    return (
      /*p*/
      f[38].length != null ? yl : vl
    );
  }
  let a = o(e), u = a(e);
  return {
    c() {
      u.c(), t = G(), r = I(n), i = I(" | "), l = I(s);
    },
    m(f, c) {
      u.m(f, c), y(f, t, c), y(f, r, c), y(f, i, c), y(f, l, c);
    },
    p(f, c) {
      a === (a = o(f)) && u ? u.p(f, c) : (u.d(1), u = a(f), u && (u.c(), u.m(t.parentNode, t))), c[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && M(r, n);
    },
    d(f) {
      f && (v(t), v(r), v(i), v(l)), u.d(f);
    }
  };
}
function vl(e) {
  let t = le(
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
      128 && t !== (t = le(
        /*p*/
        r[38].index || 0
      ) + "") && M(n, t);
    },
    d(r) {
      r && v(n);
    }
  };
}
function yl(e) {
  let t = le(
    /*p*/
    e[38].index || 0
  ) + "", n, r, i = le(
    /*p*/
    e[38].length
  ) + "", s;
  return {
    c() {
      n = I(t), r = I("/"), s = I(i);
    },
    m(l, o) {
      y(l, n, o), y(l, r, o), y(l, s, o);
    },
    p(l, o) {
      o[0] & /*progress*/
      128 && t !== (t = le(
        /*p*/
        l[38].index || 0
      ) + "") && M(n, t), o[0] & /*progress*/
      128 && i !== (i = le(
        /*p*/
        l[38].length
      ) + "") && M(s, i);
    },
    d(l) {
      l && (v(n), v(r), v(s));
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
      n && n.c(), t = be();
    },
    m(r, i) {
      n && n.m(r, i), y(r, t, i);
    },
    p(r, i) {
      /*p*/
      r[38].index != null ? n ? n.p(r, i) : (n = Qt(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && v(t), n && n.d(r);
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
    m(s, l) {
      y(s, t, l), y(s, r, l), y(s, i, l);
    },
    p(s, l) {
      l[0] & /*formatted_timer*/
      1048576 && M(
        t,
        /*formatted_timer*/
        s[20]
      ), l[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && M(r, n);
    },
    d(s) {
      s && (v(t), v(r), v(i));
    }
  };
}
function El(e) {
  let t, n;
  return t = new el({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      nl(t.$$.fragment);
    },
    m(r, i) {
      al(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      r[8] === "default"), t.$set(s);
    },
    i(r) {
      n || (ce(t.$$.fragment, r), n = !0);
    },
    o(r) {
      _e(t.$$.fragment, r), n = !1;
    },
    d(r) {
      il(t, r);
    }
  };
}
function wl(e) {
  let t, n, r, i, s, l = `${/*last_progress_level*/
  e[15] * 100}%`, o = (
    /*progress*/
    e[7] != null && Kt(e)
  );
  return {
    c() {
      t = V("div"), n = V("div"), o && o.c(), r = G(), i = V("div"), s = V("div"), k(n, "class", "progress-level-inner svelte-14miwb5"), k(s, "class", "progress-bar svelte-14miwb5"), J(s, "width", l), k(i, "class", "progress-bar-wrap svelte-14miwb5"), k(t, "class", "progress-level svelte-14miwb5");
    },
    m(a, u) {
      y(a, t, u), te(t, n), o && o.m(n, null), te(t, r), te(t, i), te(i, s), e[30](s);
    },
    p(a, u) {
      /*progress*/
      a[7] != null ? o ? o.p(a, u) : (o = Kt(a), o.c(), o.m(n, null)) : o && (o.d(1), o = null), u[0] & /*last_progress_level*/
      32768 && l !== (l = `${/*last_progress_level*/
      a[15] * 100}%`) && J(s, "width", l);
    },
    i: ht,
    o: ht,
    d(a) {
      a && v(t), o && o.d(), e[30](null);
    }
  };
}
function Kt(e) {
  let t, n = ke(
    /*progress*/
    e[7]
  ), r = [];
  for (let i = 0; i < n.length; i += 1)
    r[i] = rn(zt(e, n, i));
  return {
    c() {
      for (let i = 0; i < r.length; i += 1)
        r[i].c();
      t = be();
    },
    m(i, s) {
      for (let l = 0; l < r.length; l += 1)
        r[l] && r[l].m(i, s);
      y(i, t, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        n = ke(
          /*progress*/
          i[7]
        );
        let l;
        for (l = 0; l < n.length; l += 1) {
          const o = zt(i, n, l);
          r[l] ? r[l].p(o, s) : (r[l] = rn(o), r[l].c(), r[l].m(t.parentNode, t));
        }
        for (; l < r.length; l += 1)
          r[l].d(1);
        r.length = n.length;
      }
    },
    d(i) {
      i && v(t), Xn(r, i);
    }
  };
}
function $t(e) {
  let t, n, r, i, s = (
    /*i*/
    e[40] !== 0 && xl()
  ), l = (
    /*p*/
    e[38].desc != null && en(e)
  ), o = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && tn()
  ), a = (
    /*progress_level*/
    e[14] != null && nn(e)
  );
  return {
    c() {
      s && s.c(), t = G(), l && l.c(), n = G(), o && o.c(), r = G(), a && a.c(), i = be();
    },
    m(u, f) {
      s && s.m(u, f), y(u, t, f), l && l.m(u, f), y(u, n, f), o && o.m(u, f), y(u, r, f), a && a.m(u, f), y(u, i, f);
    },
    p(u, f) {
      /*p*/
      u[38].desc != null ? l ? l.p(u, f) : (l = en(u), l.c(), l.m(n.parentNode, n)) : l && (l.d(1), l = null), /*p*/
      u[38].desc != null && /*progress_level*/
      u[14] && /*progress_level*/
      u[14][
        /*i*/
        u[40]
      ] != null ? o || (o = tn(), o.c(), o.m(r.parentNode, r)) : o && (o.d(1), o = null), /*progress_level*/
      u[14] != null ? a ? a.p(u, f) : (a = nn(u), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null);
    },
    d(u) {
      u && (v(t), v(n), v(r), v(i)), s && s.d(u), l && l.d(u), o && o.d(u), a && a.d(u);
    }
  };
}
function xl(e) {
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
      y(r, n, i);
    },
    p(r, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[38].desc + "") && M(n, t);
    },
    d(r) {
      r && v(n);
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
      y(n, t, r);
    },
    d(n) {
      n && v(t);
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
      y(i, n, s), y(i, r, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && M(n, t);
    },
    d(i) {
      i && (v(n), v(r));
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
      n && n.c(), t = be();
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
      ] != null ? n ? n.p(r, i) : (n = $t(r), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(r) {
      r && v(t), n && n.d(r);
    }
  };
}
function sn(e) {
  let t, n;
  return {
    c() {
      t = V("p"), n = I(
        /*loading_text*/
        e[9]
      ), k(t, "class", "loading svelte-14miwb5");
    },
    m(r, i) {
      y(r, t, i), te(t, n);
    },
    p(r, i) {
      i[0] & /*loading_text*/
      512 && M(
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
function Tl(e) {
  let t, n, r, i, s;
  const l = [dl, ml], o = [];
  function a(u, f) {
    return (
      /*status*/
      u[4] === "pending" ? 0 : (
        /*status*/
        u[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = a(e)) && (r = o[n] = l[n](e)), {
    c() {
      t = V("div"), r && r.c(), k(t, "class", i = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-14miwb5"), O(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), O(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), O(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), O(
        t,
        "border",
        /*border*/
        e[12]
      ), J(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), J(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(u, f) {
      y(u, t, f), ~n && o[n].m(t, null), e[31](t), s = !0;
    },
    p(u, f) {
      let c = n;
      n = a(u), n === c ? ~n && o[n].p(u, f) : (r && (qn(), _e(o[c], 1, 1, () => {
        o[c] = null;
      }), jn()), ~n ? (r = o[n], r ? r.p(u, f) : (r = o[n] = l[n](u), r.c()), ce(r, 1), r.m(t, null)) : r = null), (!s || f[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      u[8] + " " + /*show_progress*/
      u[6] + " svelte-14miwb5")) && k(t, "class", i), (!s || f[0] & /*variant, show_progress, status, show_progress*/
      336) && O(t, "hide", !/*status*/
      u[4] || /*status*/
      u[4] === "complete" || /*show_progress*/
      u[6] === "hidden"), (!s || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && O(
        t,
        "translucent",
        /*variant*/
        u[8] === "center" && /*status*/
        (u[4] === "pending" || /*status*/
        u[4] === "error") || /*translucent*/
        u[11] || /*show_progress*/
        u[6] === "minimal"
      ), (!s || f[0] & /*variant, show_progress, status*/
      336) && O(
        t,
        "generating",
        /*status*/
        u[4] === "generating"
      ), (!s || f[0] & /*variant, show_progress, border*/
      4416) && O(
        t,
        "border",
        /*border*/
        u[12]
      ), f[0] & /*absolute*/
      1024 && J(
        t,
        "position",
        /*absolute*/
        u[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && J(
        t,
        "padding",
        /*absolute*/
        u[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(u) {
      s || (ce(r), s = !0);
    },
    o(u) {
      _e(r), s = !1;
    },
    d(u) {
      u && v(t), ~n && o[n].d(), e[31](null);
    }
  };
}
let Ce = [], et = !1;
async function Hl(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (Ce.push(e), !et)
      et = !0;
    else
      return;
    await hl(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let r = 0; r < Ce.length; r++) {
        const s = Ce[r].getBoundingClientRect();
        (r === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = r);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), et = !1, Ce = [];
    });
  }
}
function Bl(e, t, n) {
  let r, { $$slots: i = {}, $$scope: s } = t, { i18n: l } = t, { eta: o = null } = t, { queue: a = !1 } = t, { queue_position: u } = t, { queue_size: f } = t, { status: c } = t, { scroll_to_output: h = !1 } = t, { timer: _ = !0 } = t, { show_progress: d = "full" } = t, { message: E = null } = t, { progress: w = null } = t, { variant: N = "default" } = t, { loading_text: b = "Loading..." } = t, { absolute: m = !0 } = t, { translucent: T = !1 } = t, { border: g = !1 } = t, { autoscroll: j } = t, X, ge = !1, Ae = 0, Y = 0, Xe = null, bt = 0, K = null, pe, q = null, gt = !0;
  const Zn = () => {
    n(25, Ae = performance.now()), n(26, Y = 0), ge = !0, pt();
  };
  function pt() {
    requestAnimationFrame(() => {
      n(26, Y = (performance.now() - Ae) / 1e3), ge && pt();
    });
  }
  function vt() {
    n(26, Y = 0), ge && (ge = !1);
  }
  cl(() => {
    ge && vt();
  });
  let yt = null;
  function Wn(p) {
    Xt[p ? "unshift" : "push"](() => {
      q = p, n(16, q), n(7, w), n(14, K), n(15, pe);
    });
  }
  function Qn(p) {
    Xt[p ? "unshift" : "push"](() => {
      X = p, n(13, X);
    });
  }
  return e.$$set = (p) => {
    "i18n" in p && n(1, l = p.i18n), "eta" in p && n(0, o = p.eta), "queue" in p && n(21, a = p.queue), "queue_position" in p && n(2, u = p.queue_position), "queue_size" in p && n(3, f = p.queue_size), "status" in p && n(4, c = p.status), "scroll_to_output" in p && n(22, h = p.scroll_to_output), "timer" in p && n(5, _ = p.timer), "show_progress" in p && n(6, d = p.show_progress), "message" in p && n(23, E = p.message), "progress" in p && n(7, w = p.progress), "variant" in p && n(8, N = p.variant), "loading_text" in p && n(9, b = p.loading_text), "absolute" in p && n(10, m = p.absolute), "translucent" in p && n(11, T = p.translucent), "border" in p && n(12, g = p.border), "autoscroll" in p && n(24, j = p.autoscroll), "$$scope" in p && n(28, s = p.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (o === null ? n(0, o = Xe) : a && n(0, o = (performance.now() - Ae) / 1e3 + o), o != null && (n(19, yt = o.toFixed(1)), n(27, Xe = o))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, bt = o === null || o <= 0 || !Y ? null : Math.min(Y / o, 1)), e.$$.dirty[0] & /*progress*/
    128 && w != null && n(18, gt = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (w != null ? n(14, K = w.map((p) => {
      if (p.index != null && p.length != null)
        return p.index / p.length;
      if (p.progress != null)
        return p.progress;
    })) : n(14, K = null), K ? (n(15, pe = K[K.length - 1]), q && (pe === 0 ? n(16, q.style.transition = "0", q) : n(16, q.style.transition = "150ms", q))) : n(15, pe = void 0)), e.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Zn() : vt()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && X && h && (c === "pending" || c === "complete") && Hl(X, j), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, r = Y.toFixed(1));
  }, [
    o,
    l,
    u,
    f,
    c,
    _,
    d,
    w,
    N,
    b,
    m,
    T,
    g,
    X,
    K,
    pe,
    q,
    bt,
    gt,
    yt,
    r,
    a,
    h,
    E,
    j,
    Ae,
    Y,
    Xe,
    s,
    i,
    Wn,
    Qn
  ];
}
class Sl extends tl {
  constructor(t) {
    super(), ol(
      this,
      t,
      Bl,
      Tl,
      ul,
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
function zn(e, t, n) {
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
      i === null ? r.push(null) : r.push(zn(i, t, n));
    return r;
  } else
    e.is_file ? e.data = Pl(e.name, t, n) : e.is_stream && (n == null ? e.data = t + "/stream/" + e.name : e.data = "/proxy=" + n + "stream/" + e.name);
  return e;
}
function Al(e) {
  try {
    const t = new URL(e);
    return t.protocol === "http:" || t.protocol === "https:";
  } catch {
    return !1;
  }
}
function Pl(e, t, n) {
  return e == null ? n ? `/proxy=${n}file=` : `${t}/file=` : Al(e) ? e : n ? `/proxy=${n}file=${e}` : `${t}/file=${e}`;
}
new Intl.Collator(0, { numeric: 1 }).compare;
const {
  SvelteComponent: Nl,
  assign: Il,
  attr: ee,
  check_outros: ln,
  create_component: He,
  destroy_component: Be,
  detach: Me,
  element: Cl,
  empty: Ll,
  get_spread_object: Ol,
  get_spread_update: Ml,
  group_outros: on,
  init: Rl,
  insert: Re,
  mount_component: Se,
  noop: an,
  safe_not_equal: Ul,
  space: un,
  src_url_equal: fn,
  transition_in: D,
  transition_out: F
} = window.__gradio__svelte__internal;
function hn(e) {
  let t, n;
  const r = [
    {
      autoscroll: (
        /*gradio*/
        e[10].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      e[10].i18n
    ) },
    /*loading_status*/
    e[9]
  ];
  let i = {};
  for (let s = 0; s < r.length; s += 1)
    i = Il(i, r[s]);
  return t = new Sl({ props: i }), {
    c() {
      He(t.$$.fragment);
    },
    m(s, l) {
      Se(t, s, l), n = !0;
    },
    p(s, l) {
      const o = l & /*gradio, loading_status*/
      1536 ? Ml(r, [
        l & /*gradio*/
        1024 && {
          autoscroll: (
            /*gradio*/
            s[10].autoscroll
          )
        },
        l & /*gradio*/
        1024 && { i18n: (
          /*gradio*/
          s[10].i18n
        ) },
        l & /*loading_status*/
        512 && Ol(
          /*loading_status*/
          s[9]
        )
      ]) : {};
      t.$set(o);
    },
    i(s) {
      n || (D(t.$$.fragment, s), n = !0);
    },
    o(s) {
      F(t.$$.fragment, s), n = !1;
    },
    d(s) {
      Be(t, s);
    }
  };
}
function Dl(e) {
  let t, n;
  return t = new Xr({
    props: {
      unpadded_box: !0,
      size: "large",
      $$slots: { default: [Gl] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      He(t.$$.fragment);
    },
    m(r, i) {
      Se(t, r, i), n = !0;
    },
    p(r, i) {
      const s = {};
      i & /*$$scope*/
      32768 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (D(t.$$.fragment, r), n = !0);
    },
    o(r) {
      F(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Be(t, r);
    }
  };
}
function kl(e) {
  let t, n, r;
  return {
    c() {
      t = Cl("iframe"), fn(t.src, n = /*new_value*/
      e[11].data) || ee(t, "src", n), ee(
        t,
        "title",
        /*label*/
        e[0]
      ), ee(t, "height", r = /*height*/
      e[1] + "px"), ee(t, "class", "svelte-1orump4");
    },
    m(i, s) {
      Re(i, t, s);
    },
    p(i, s) {
      s & /*new_value*/
      2048 && !fn(t.src, n = /*new_value*/
      i[11].data) && ee(t, "src", n), s & /*label*/
      1 && ee(
        t,
        "title",
        /*label*/
        i[0]
      ), s & /*height*/
      2 && r !== (r = /*height*/
      i[1] + "px") && ee(t, "height", r);
    },
    i: an,
    o: an,
    d(i) {
      i && Me(t);
    }
  };
}
function Gl(e) {
  let t, n;
  return t = new dn({}), {
    c() {
      He(t.$$.fragment);
    },
    m(r, i) {
      Se(t, r, i), n = !0;
    },
    i(r) {
      n || (D(t.$$.fragment, r), n = !0);
    },
    o(r) {
      F(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Be(t, r);
    }
  };
}
function Fl(e) {
  let t, n, r, i, s, l, o, a = (
    /*loading_status*/
    e[9] && hn(e)
  );
  n = new Sr({
    props: {
      show_label: !0,
      Icon: dn,
      label: (
        /*label*/
        e[0] || "Folium Map"
      )
    }
  });
  const u = [kl, Dl], f = [];
  function c(h, _) {
    return (
      /*value*/
      h[5] ? 0 : 1
    );
  }
  return i = c(e), s = f[i] = u[i](e), {
    c() {
      a && a.c(), t = un(), He(n.$$.fragment), r = un(), s.c(), l = Ll();
    },
    m(h, _) {
      a && a.m(h, _), Re(h, t, _), Se(n, h, _), Re(h, r, _), f[i].m(h, _), Re(h, l, _), o = !0;
    },
    p(h, _) {
      /*loading_status*/
      h[9] ? a ? (a.p(h, _), _ & /*loading_status*/
      512 && D(a, 1)) : (a = hn(h), a.c(), D(a, 1), a.m(t.parentNode, t)) : a && (on(), F(a, 1, 1, () => {
        a = null;
      }), ln());
      const d = {};
      _ & /*label*/
      1 && (d.label = /*label*/
      h[0] || "Folium Map"), n.$set(d);
      let E = i;
      i = c(h), i === E ? f[i].p(h, _) : (on(), F(f[E], 1, 1, () => {
        f[E] = null;
      }), ln(), s = f[i], s ? s.p(h, _) : (s = f[i] = u[i](h), s.c()), D(s, 1), s.m(l.parentNode, l));
    },
    i(h) {
      o || (D(a), D(n.$$.fragment, h), D(s), o = !0);
    },
    o(h) {
      F(a), F(n.$$.fragment, h), F(s), o = !1;
    },
    d(h) {
      h && (Me(t), Me(r), Me(l)), a && a.d(h), Be(n, h), f[i].d(h);
    }
  };
}
function Vl(e) {
  let t, n;
  return t = new hr({
    props: {
      visible: (
        /*visible*/
        e[4]
      ),
      elem_id: (
        /*elem_id*/
        e[2]
      ),
      elem_classes: (
        /*elem_classes*/
        e[3]
      ),
      container: (
        /*container*/
        e[6]
      ),
      scale: (
        /*scale*/
        e[7]
      ),
      min_width: (
        /*min_width*/
        e[8]
      ),
      $$slots: { default: [Fl] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      He(t.$$.fragment);
    },
    m(r, i) {
      Se(t, r, i), n = !0;
    },
    p(r, [i]) {
      const s = {};
      i & /*visible*/
      16 && (s.visible = /*visible*/
      r[4]), i & /*elem_id*/
      4 && (s.elem_id = /*elem_id*/
      r[2]), i & /*elem_classes*/
      8 && (s.elem_classes = /*elem_classes*/
      r[3]), i & /*container*/
      64 && (s.container = /*container*/
      r[6]), i & /*scale*/
      128 && (s.scale = /*scale*/
      r[7]), i & /*min_width*/
      256 && (s.min_width = /*min_width*/
      r[8]), i & /*$$scope, new_value, label, height, value, gradio, loading_status*/
      36387 && (s.$$scope = { dirty: i, ctx: r }), t.$set(s);
    },
    i(r) {
      n || (D(t.$$.fragment, r), n = !0);
    },
    o(r) {
      F(t.$$.fragment, r), n = !1;
    },
    d(r) {
      Be(t, r);
    }
  };
}
function cn(e, t) {
  return e ?? t();
}
function jl(e, t, n) {
  let { elem_id: r = "" } = t, { elem_classes: i = [] } = t, { visible: s = !0 } = t, { value: l } = t, { label: o } = t, { container: a = !0 } = t, { scale: u = null } = t, { min_width: f = void 0 } = t, { loading_status: c } = t, { root: h } = t, { root_url: _ } = t, { height: d = null } = t, { gradio: E } = t, w;
  async function N() {
    E.dispatch("change");
  }
  return e.$$set = (b) => {
    "elem_id" in b && n(2, r = b.elem_id), "elem_classes" in b && n(3, i = b.elem_classes), "visible" in b && n(4, s = b.visible), "value" in b && n(5, l = b.value), "label" in b && n(0, o = b.label), "container" in b && n(6, a = b.container), "scale" in b && n(7, u = b.scale), "min_width" in b && n(8, f = b.min_width), "loading_status" in b && n(9, c = b.loading_status), "root" in b && n(12, h = b.root), "root_url" in b && n(13, _ = b.root_url), "height" in b && n(1, d = b.height), "gradio" in b && n(10, E = b.gradio);
  }, e.$$.update = () => {
    e.$$.dirty & /*label*/
    1 && n(0, o = cn(o, () => "Folium Map")), e.$$.dirty & /*height*/
    2 && n(1, d = cn(d, () => 500)), e.$$.dirty & /*value, root, root_url*/
    12320 && n(11, w = { ...zn(l, h, _) }), e.$$.dirty & /*new_value*/
    2048 && N();
  }, [
    o,
    d,
    r,
    i,
    s,
    l,
    a,
    u,
    f,
    c,
    E,
    w,
    h,
    _
  ];
}
class Xl extends Nl {
  constructor(t) {
    super(), Rl(this, t, jl, Vl, Ul, {
      elem_id: 2,
      elem_classes: 3,
      visible: 4,
      value: 5,
      label: 0,
      container: 6,
      scale: 7,
      min_width: 8,
      loading_status: 9,
      root: 12,
      root_url: 13,
      height: 1,
      gradio: 10
    });
  }
}
export {
  Xl as default
};
