import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../../api/api";
import { saveToken } from "../../../api/auth";
import "./Login.css";
import loginImg  from "../../../assets/images/LoginImages/login.png";
import vectLeft  from "../../../assets/images/LoginImages/vectleft.png";
import vectRight from "../../../assets/images/LoginImages/vectright.png";

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm]       = useState({ email: "", password: "" });
  const [error, setError]     = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const data = await login(form.email, form.password);
      saveToken(data.access_token);

      // Redirect based on role returned from backend
      switch (data.role) {
        case "student": navigate("/student/settings"); break;
        case "parent":  navigate("/parent/dashboard");  break;
        case "school":  navigate("/school/dashboard");  break;
        case "admin":   navigate("/admin/dashboard");   break;
        default:        navigate("/");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogle = () => console.log("Login with Google");

  return (
    <div className="login-page">

      <img src={vectLeft} className="deco deco-left" alt="" />

      <div className="deco-right-wrapper">
        <img src={vectRight} className="deco-right-blob" alt="" />
        <img src={loginImg}  className="deco-right-img" alt="Login illustration" />
      </div>

      <div className="login-card">
        <h1 className="login-title">Log in</h1>

        <button className="google-btn" onClick={handleGoogle}>
          <img
            src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
            alt="Google"
            className="google-icon"
          />
          Login with Google
        </button>

        <div className="divider">
          <span className="divider-line" />
          <span className="divider-text">OR</span>
          <span className="divider-line" />
        </div>

        {error && <p style={{ color: "red", marginBottom: "8px" }}>{error}</p>}

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label>E-mail</label>
            <input type="email" name="email" placeholder="example@gmail.com"
              value={form.email} onChange={handleChange} />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input type="password" name="password" placeholder="xxxxxxxxxxx"
              value={form.password} onChange={handleChange} />
          </div>

          <div className="submit-row">
            <button type="submit" className="login-btn" disabled={loading}>
              {loading ? "Logging in..." : "Log in"}
            </button>
          </div>
        </form>

        <div className="login-footer">
          <p>Forgot your password ?</p>
          <p>Don't have an account? <a href="/signup" className="signup-link">Sign up</a></p>
        </div>
      </div>
    </div>
  );
}