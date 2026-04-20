import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logout } from "../../api/auth";
import "./AdminDashboard.css";

export default function AdminDashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    setTimeout(() => navigate("/login"), 500);
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Admin Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </header>

      <main className="dashboard-content">
        <section className="dashboard-section">
          <h2>Welcome, Administrator!</h2>
          <p>Here you can manage the system and monitor all activities.</p>
        </section>

        <section className="dashboard-section">
          <h3>System Management</h3>
          <p>Coming soon: Manage users, schools, and system settings</p>
        </section>

        <section className="dashboard-section">
          <h3>Monitoring</h3>
          <p>Coming soon: System logs and monitoring tools</p>
        </section>
      </main>
    </div>
  );
}
