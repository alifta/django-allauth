import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Todo {
  id: number;
  user: string;
  description: string;
  is_completed: boolean;
  created_at: string;
  updated_at: string;
}

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private readonly API_URL = 'http://localhost:8000/api/todos';

  constructor(private http: HttpClient) {}

  /**
   * Get all todos for the authenticated user
   */
  getTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(`${this.API_URL}/`);
  }

  /**
   * Get a single todo by ID
   */
  getTodo(id: number): Observable<Todo> {
    return this.http.get<Todo>(`${this.API_URL}/${id}/`);
  }

  /**
   * Create a new todo
   */
  createTodo(description: string, isCompleted: boolean = false): Observable<Todo> {
    return this.http.post<Todo>(`${this.API_URL}/`, {
      description,
      is_completed: isCompleted,
    });
  }

  /**
   * Update an existing todo
   */
  updateTodo(id: number, updates: Partial<Todo>): Observable<Todo> {
    return this.http.patch<Todo>(`${this.API_URL}/${id}/`, updates);
  }

  /**
   * Delete a todo
   */
  deleteTodo(id: number): Observable<void> {
    return this.http.delete<void>(`${this.API_URL}/${id}/`);
  }

  /**
   * Mark a todo as completed
   */
  completeTodo(id: number): Observable<Todo> {
    return this.updateTodo(id, { is_completed: true });
  }
}
