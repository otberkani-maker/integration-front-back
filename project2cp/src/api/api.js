const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

function parseDetail(detail) {
  if (!detail) return "Something went wrong";
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) return detail.map((e) => e.msg).join(", ");
  return "Something went wrong";
}

async function apiPost(endpoint, data) {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(parseDetail(json.detail));
  return json;
}

async function apiPostQuery(endpoint, params) {
  const url = new URL(`${BASE_URL}${endpoint}`);
  Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));

  const res = await fetch(url.toString(), { method: "POST" });
  const json = await res.json();
  if (!res.ok) throw new Error(parseDetail(json.detail));
  return json;
}

// ── Sign Ups ──────────────────────────────────────────
export const signUpStudent = (data) => apiPost("/students/register", data);
export const signUpParent  = (data) => apiPost("/parents/register", data);
export const signUpSchool  = (data) => apiPost("/schools/register", data);
export const signUpAdmin   = (data) => apiPost("/admins/register", data);

// ── Login ─────────────────────────────────────────────
export async function login(email, password) {
  const roles = [
    { endpoint: "/students/login", role: "student" },
    { endpoint: "/parents/login",  role: "parent"  },
    { endpoint: "/schools/login",  role: "school"  },
    { endpoint: "/admins/login",   role: "admin"   },
  ];

  for (const { endpoint, role } of roles) {
    const url = new URL(`${BASE_URL}${endpoint}`);
    url.searchParams.set("email", email);
    url.searchParams.set("password", password);

    const res = await fetch(url.toString(), { method: "POST" });
    if (res.ok) {
      const data = await res.json();
      return { ...data, role };
    }
  }

  throw new Error("Invalid email or password");
}