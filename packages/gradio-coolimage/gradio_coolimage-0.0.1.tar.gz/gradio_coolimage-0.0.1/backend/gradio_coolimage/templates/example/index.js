const { setContext: ee, getContext: v } = window.__gradio__svelte__internal, y = "WORKER_PROXY_CONTEXT_KEY";
function k() {
  return v(y);
}
async function f(s) {
  if (s == null)
    return s;
  const e = new URL(s);
  if (e.host !== window.location.host && e.host !== "localhost:7860" && e.host !== "127.0.0.1:7860" || e.protocol !== "http:" && e.protocol !== "https:")
    return s;
  const r = k();
  if (r == null)
    return s;
  const n = e.pathname;
  return r.httpRequest({
    method: "GET",
    path: n,
    headers: {},
    query_string: ""
  }).then((t) => {
    if (t.status !== 200)
      throw new Error(`Failed to get file ${n} from the Wasm worker.`);
    const l = new Blob([t.body], {
      type: t.headers["Content-Type"]
    });
    return URL.createObjectURL(l);
  });
}
const {
  SvelteComponent: w,
  append: C,
  assign: i,
  compute_rest_props: d,
  detach: u,
  element: b,
  empty: E,
  exclude_internal_props: R,
  get_spread_update: q,
  handle_promise: g,
  init: O,
  insert: m,
  noop: c,
  safe_not_equal: T,
  set_attributes: h,
  set_data: P,
  set_style: U,
  src_url_equal: W,
  text: K,
  toggle_class: p,
  update_await_block_branch: X
} = window.__gradio__svelte__internal;
function Y(s) {
  let e, r = (
    /*error*/
    s[3].message + ""
  ), n;
  return {
    c() {
      e = b("p"), n = K(r), U(e, "color", "red");
    },
    m(t, l) {
      m(t, e, l), C(e, n);
    },
    p(t, l) {
      l & /*src*/
      1 && r !== (r = /*error*/
      t[3].message + "") && P(n, r);
    },
    d(t) {
      t && u(e);
    }
  };
}
function L(s) {
  let e, r, n = [
    {
      src: r = /*resolved_src*/
      s[2]
    },
    /*$$restProps*/
    s[1]
  ], t = {};
  for (let l = 0; l < n.length; l += 1)
    t = i(t, n[l]);
  return {
    c() {
      e = b("img"), h(e, t), p(e, "svelte-1k8xp4f", !0);
    },
    m(l, o) {
      m(l, e, o);
    },
    p(l, o) {
      h(e, t = q(n, [
        o & /*src*/
        1 && !W(e.src, r = /*resolved_src*/
        l[2]) && { src: r },
        o & /*$$restProps*/
        2 && /*$$restProps*/
        l[1]
      ])), p(e, "svelte-1k8xp4f", !0);
    },
    d(l) {
      l && u(e);
    }
  };
}
function N(s) {
  return { c, m: c, p: c, d: c };
}
function S(s) {
  let e, r, n = {
    ctx: s,
    current: null,
    token: null,
    hasCatch: !0,
    pending: N,
    then: L,
    catch: Y,
    value: 2,
    error: 3
  };
  return g(r = f(
    /*src*/
    s[0]
  ), n), {
    c() {
      e = E(), n.block.c();
    },
    m(t, l) {
      m(t, e, l), n.block.m(t, n.anchor = l), n.mount = () => e.parentNode, n.anchor = e;
    },
    p(t, [l]) {
      s = t, n.ctx = s, l & /*src*/
      1 && r !== (r = f(
        /*src*/
        s[0]
      )) && g(r, n) || X(n, s, l);
    },
    i: c,
    o: c,
    d(t) {
      t && u(e), n.block.d(t), n.token = null, n = null;
    }
  };
}
function j(s, e, r) {
  const n = ["src"];
  let t = d(e, n), { src: l = void 0 } = e;
  return s.$$set = (o) => {
    e = i(i({}, e), R(o)), r(1, t = d(e, n)), "src" in o && r(0, l = o.src);
  }, [l, t];
}
class I extends w {
  constructor(e) {
    super(), O(this, e, j, S, T, { src: 0 });
  }
}
const {
  SvelteComponent: x,
  attr: z,
  create_component: B,
  destroy_component: F,
  detach: G,
  element: A,
  init: D,
  insert: H,
  mount_component: J,
  safe_not_equal: M,
  toggle_class: _,
  transition_in: Q,
  transition_out: V
} = window.__gradio__svelte__internal;
function Z(s) {
  let e, r, n;
  return r = new I({
    props: {
      src: (
        /*samples_dir*/
        s[1] + /*value*/
        s[0]
      ),
      alt: ""
    }
  }), {
    c() {
      e = A("div"), B(r.$$.fragment), z(e, "class", "container svelte-1iqucjz"), _(
        e,
        "table",
        /*type*/
        s[2] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        s[2] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        s[3]
      );
    },
    m(t, l) {
      H(t, e, l), J(r, e, null), n = !0;
    },
    p(t, [l]) {
      const o = {};
      l & /*samples_dir, value*/
      3 && (o.src = /*samples_dir*/
      t[1] + /*value*/
      t[0]), r.$set(o), (!n || l & /*type*/
      4) && _(
        e,
        "table",
        /*type*/
        t[2] === "table"
      ), (!n || l & /*type*/
      4) && _(
        e,
        "gallery",
        /*type*/
        t[2] === "gallery"
      ), (!n || l & /*selected*/
      8) && _(
        e,
        "selected",
        /*selected*/
        t[3]
      );
    },
    i(t) {
      n || (Q(r.$$.fragment, t), n = !0);
    },
    o(t) {
      V(r.$$.fragment, t), n = !1;
    },
    d(t) {
      t && G(e), F(r);
    }
  };
}
function $(s, e, r) {
  let { value: n } = e, { samples_dir: t } = e, { type: l } = e, { selected: o = !1 } = e;
  return s.$$set = (a) => {
    "value" in a && r(0, n = a.value), "samples_dir" in a && r(1, t = a.samples_dir), "type" in a && r(2, l = a.type), "selected" in a && r(3, o = a.selected);
  }, [n, t, l, o];
}
class te extends x {
  constructor(e) {
    super(), D(this, e, $, Z, M, {
      value: 0,
      samples_dir: 1,
      type: 2,
      selected: 3
    });
  }
}
export {
  te as default
};
