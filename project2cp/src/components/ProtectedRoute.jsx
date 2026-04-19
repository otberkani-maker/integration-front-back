import { Navigate } from 'react-router-dom'
import { isLoggedIn } from '../api/auth'

export default function ProtectedRoute({ children, allowedRoles = [] }) {
  if (!isLoggedIn()) {
    return <Navigate to="/login" replace />
  }

  // If roles are specified, check if user has the role
  // For now, since token doesn't store role, perhaps store in localStorage
  // But for simplicity, assume all logged in users can access
  // Later, decode token to get role

  return children
}