export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/" || url.pathname === "/health") {
      return new Response("ok", { status: 200 });
    }

    if (url.pathname === "/receipts" && request.method === "GET") {
      const keys = await env.TR_KV.list({ prefix: "r:" });
      const out = [];
      for (const k of keys.keys) {
        const v = await env.TR_KV.get(k.name, "json");
        if (v) out.push(v);
      }
      out.sort((a,b) => (a.timestamp_utc || "").localeCompare(b.timestamp_utc || ""));
      return Response.json(out);
    }

    if (url.pathname === "/receipts" && request.method === "POST") {
      const body = await request.json();
      if (!body?.receipt_id) return new Response("receipt_id required", { status: 400 });

      const key = "r:" + body.receipt_id;
      const existing = await env.TR_KV.get(key);
      if (existing) return new Response("receipt_id already exists", { status: 409 });

      await env.TR_KV.put(key, JSON.stringify(body));
      return Response.json({ ok: true });
    }

    return new Response("not found", { status: 404 });
  }
};
