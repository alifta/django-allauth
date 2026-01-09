import { apiClient } from './api';
import { z } from 'zod';

// Zod schemas for validation
export const loginSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
});

export const signupSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
  firstName: z.string().min(1, 'First name is required'),
  lastName: z.string().min(1, 'Last name is required'),
});

export type LoginInput = z.infer<typeof loginSchema>;
export type SignupInput = z.infer<typeof signupSchema>;

export interface AuthResponse {
  user: {
    id: string;
    email: string;
    firstName: string;
    lastName: string;
  };
  token: string;
}

export const authService = {
  login: async (credentials: LoginInput): Promise<AuthResponse> => {
    const { data } = await apiClient.post<AuthResponse>('/api/auth/login/', credentials);
    return data;
  },

  signup: async (userData: SignupInput): Promise<AuthResponse> => {
    const { data } = await apiClient.post<AuthResponse>('/api/auth/signup/', userData);
    return data;
  },

  logout: async (): Promise<void> => {
    await apiClient.post('/api/auth/logout/');
  },

  getCurrentUser: async () => {
    const { data } = await apiClient.get('/api/auth/user/');
    return data;
  },
};
