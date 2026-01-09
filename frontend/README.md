# React Frontend

A modern React frontend built with TypeScript, featuring a complete authentication system and integration with Django backend.

## Tech Stack

- **React 19** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Redux Toolkit** - State management
- **TanStack Query (React Query)** - Server state management
- **Axios** - HTTP client
- **Zod** - Schema validation
- **React Hook Form** - Form management
- **Tailwind CSS** - Utility-first CSS framework
- **DaisyUI** - Tailwind component library

## Project Structure

```
src/
├── components/       # Reusable UI components
│   └── ProtectedRoute.tsx
├── pages/           # Page components
│   ├── Home.tsx
│   ├── Login.tsx
│   ├── Signup.tsx
│   └── Dashboard.tsx
├── store/           # Redux store configuration
│   ├── index.ts
│   ├── hooks.ts
│   └── slices/
│       └── authSlice.ts
├── services/        # API services
│   ├── api.ts
│   └── authService.ts
├── hooks/           # Custom React hooks
│   └── useAuth.ts
├── types/           # TypeScript type definitions
├── utils/           # Utility functions
├── App.tsx          # Main app component
└── main.tsx         # App entry point
```

## Getting Started

### Prerequisites

- Bun (package manager)
- Node.js 18+

### Installation

```bash
# Install dependencies
bun install

# Create environment file
cp .env.example .env
```

### Environment Variables

Edit `.env` file:

```
VITE_API_URL=http://localhost:8000
```

### Development

```bash
# Start dev server (http://localhost:5173)
bun dev

# Build for production
bun run build

# Preview production build
bun run preview

# Run linter
bun run lint
```

## Features

### Authentication
- Login with email/password
- User registration with validation
- Protected routes
- JWT token management
- Automatic token refresh

### State Management
- **Redux Toolkit** for global state (auth, user data)
- **TanStack Query** for server state (API calls, caching)
- Type-safe hooks (`useAppDispatch`, `useAppSelector`)

### Form Validation
- Zod schemas for runtime validation
- React Hook Form for form state
- Error handling and display

### Routing
- React Router v7
- Protected routes with authentication check
- Programmatic navigation

### API Integration
- Axios interceptors for auth tokens
- Automatic error handling
- TypeScript types for API responses

## Key Files

### Redux Store Setup
- `src/store/index.ts` - Store configuration
- `src/store/slices/authSlice.ts` - Authentication state
- `src/store/hooks.ts` - Type-safe Redux hooks

### API Services
- `src/services/api.ts` - Axios instance with interceptors
- `src/services/authService.ts` - Authentication API calls with Zod schemas

### Custom Hooks
- `src/hooks/useAuth.ts` - TanStack Query hooks for auth operations

### Pages
- `src/pages/Home.tsx` - Landing page
- `src/pages/Login.tsx` - Login form with validation
- `src/pages/Signup.tsx` - Registration form
- `src/pages/Dashboard.tsx` - Protected dashboard

## Styling

Using Tailwind CSS with DaisyUI component library:
- `tailwind.config.js` - Tailwind configuration
- `src/index.css` - Global styles with Tailwind directives
- DaisyUI themes: light (default) and dark

## Integration with Django

The frontend expects the following Django API endpoints:

- `POST /api/auth/login/` - User login
- `POST /api/auth/signup/` - User registration
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/user/` - Get current user

Configure CORS in Django to allow requests from `http://localhost:5173` during development.

## Scripts

- `bun dev` - Start development server with hot reload
- `bun run build` - Build for production
- `bun run preview` - Preview production build locally
- `bun run lint` - Run ESLint

## Best Practices

- Type-safe Redux with TypeScript
- Centralized API error handling
- Form validation with Zod schemas
- Protected routes for authenticated pages
- Separation of concerns (components, services, state)
- Custom hooks for reusable logic

## Next Steps

- Add more pages (Profile, Settings, etc.)
- Implement todo functionality
- Add loading states and skeletons
- Implement error boundaries
- Add unit tests with Vitest
- Set up E2E tests with Playwright
