import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Welcome to React + Django</h1>
          <p className="py-6">
            A modern full-stack application built with React, TypeScript, Redux,
            TanStack Query, and Django backend.
          </p>
          <div className="flex gap-4 justify-center">
            <Link to="/login" className="btn btn-primary">
              Login
            </Link>
            <Link to="/signup" className="btn btn-secondary">
              Sign Up
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
