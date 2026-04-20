import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logout, getRole } from "../../api/auth";
import "./ParentDashboard.css";

export default function ParentDashboard() {
  const navigate = useNavigate();
  const [isLogout, setIsLogout] = useState(false);

  const handleLogout = () => {
    logout();
    setIsLogout(true);
    setTimeout(() => navigate("/login"), 500);
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Parent Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </header>

      <main className="dashboard-content">
        <section className="dashboard-section">
          <h2>Welcome, Parent!</h2>
          <p>Here you can monitor your child's academic progress and predictions.</p>
        </section>

        <section className="dashboard-section">
          <h3>Your Child's Information</h3>
          <p>Coming soon: Student details, grades, and predictions</p>
        </section>

        <section className="dashboard-section">
          <h3>Reports</h3>
          <p>Coming soon: Academic reports and progress tracking</p>
        </section>
      </main>
    </div>
  );
}
