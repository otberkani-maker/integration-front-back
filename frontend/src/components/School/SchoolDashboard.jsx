import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logout } from "../../api/auth";
import "./SchoolDashboard.css";

export default function SchoolDashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    setTimeout(() => navigate("/login"), 500);
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>School Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </header>

      <main className="dashboard-content">
        <section className="dashboard-section">
          <h2>Welcome, School Administrator!</h2>
          <p>Here you can manage student data and academic predictions.</p>
        </section>

        <section className="dashboard-section">
          <h3>Student Management</h3>
          <p>Coming soon: Manage students, view predictions, and generate reports</p>
        </section>

        <section className="dashboard-section">
          <h3>Analytics</h3>
          <p>Coming soon: School-wide analytics and insights</p>
        </section>
      </main>
    </div>
  );
}
