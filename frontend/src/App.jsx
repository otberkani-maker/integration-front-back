import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useRef } from 'react'

import Navbar from './components/LandingPage/Navbar/Navbar.jsx'
import Hero from './components/LandingPage/Hero/Hero.jsx'
import About from './components/LandingPage/About us/About.jsx'
import Services from './components/LandingPage/Services/Services.jsx'
import HowItWorks from './components/LandingPage/How it works/HowItWorks.jsx'
import Contact from './components/LandingPage/Contact us/Contact.jsx'
import Footer from './components/LandingPage/Footer/Footer.jsx'

import SignUpStudent from './components/SignPages/SignUp/SignUpStudent.jsx'
import SignUpSchool from './components/SignPages/SignUp/SignUpSchool.jsx'
import SignUpParent from './components/SignPages/SignUp/SignUpParent.jsx'
import SignUpAdmin from './components/SignPages/SignUp/SignUpAdmin.jsx'
import Login from './components/SignPages/logIn/Login.jsx'
import StudentSettings from './components/Student/StudentSettings'
import ParentDashboard from './components/Parent/ParentDashboard.jsx'
import SchoolDashboard from './components/School/SchoolDashboard.jsx'
import AdminDashboard from './components/Admin/AdminDashboard.jsx'
import ProtectedRoute from './components/ProtectedRoute'

import './App.css'

function HomePage() {
  const heroRef     = useRef(null)
  const aboutRef    = useRef(null)
  const servicesRef = useRef(null)
  const howRef      = useRef(null)
  const contactRef  = useRef(null)

  const scrollTo = (ref) => {
    ref.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const sections = { heroRef, aboutRef, servicesRef, howRef, contactRef }

  return (
    <div className="snap-container">
      <Navbar scrollTo={scrollTo} sections={sections} />

      <div className="snap-section" ref={heroRef}>
        <Hero />
      </div>
      <div className="snap-section" ref={aboutRef}>
        <About />
      </div>
      <div className="snap-section" ref={servicesRef}>
        <Services />
      </div>
      <div className="snap-section" ref={howRef}>
        <HowItWorks />
      </div>
      <div className="snap-section" ref={contactRef}>
        <Contact />
      </div>
      <div className="snap-section">
        <Footer />
      </div>
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/"               element={<HomePage />} />
        <Route path="/signup/student" element={<SignUpStudent />} />
        <Route path="/signup/school"  element={<SignUpSchool />} />
        <Route path="/signup/parent"  element={<SignUpParent />} />
        <Route path="/signup/admin"   element={<SignUpAdmin />} />
        <Route path="/login"          element={<Login />} />
        <Route path="/student/settings" element={
          <ProtectedRoute allowedRoles={['student']}>
            <StudentSettings />
          </ProtectedRoute>
        } />
        <Route path="/parent/dashboard" element={
          <ProtectedRoute allowedRoles={['parent']}>
            <ParentDashboard />
          </ProtectedRoute>
        } />
        <Route path="/school/dashboard" element={
          <ProtectedRoute allowedRoles={['school']}>
            <SchoolDashboard />
          </ProtectedRoute>
        } />
        <Route path="/admin/dashboard" element={
          <ProtectedRoute allowedRoles={['admin']}>
            <AdminDashboard />
          </ProtectedRoute>
        } />
      </Routes>
    </BrowserRouter>
  )
}

export default App