// JWT Token Management for API Authentication
// This script handles JWT token acquisition, storage, and automatic inclusion in API requests

/**
 * Get JWT token from localStorage
 * @returns {string|null} JWT access token or null if not found
 */
function getAuthToken() {
  return localStorage.getItem('access_token');
}

/**
 * Set JWT token in localStorage
 * @param {string} accessToken - JWT access token
 * @param {string} refreshToken - JWT refresh token
 */
function setAuthToken(accessToken, refreshToken) {
  localStorage.setItem('access_token', accessToken);
  localStorage.setItem('refresh_token', refreshToken);
}

/**
 * Remove JWT tokens from localStorage
 */
function clearAuthToken() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
}

/**
 * Fetch JWT token from the API using username and password
 * @param {string} username - User's username
 * @param {string} password - User's password
 * @returns {Promise<Object>} Token response with access and refresh tokens
 */
async function fetchJWTToken(username, password) {
  try {
    const response = await fetch('/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      throw new Error('Failed to obtain token');
    }

    const data = await response.json();
    setAuthToken(data.access, data.refresh);
    return data;
  } catch (error) {
    console.error('Error fetching JWT token:', error);
    throw error;
  }
}

/**
 * Refresh the JWT access token using the refresh token
 * @returns {Promise<Object>} New token response
 */
async function refreshJWTToken() {
  const refreshToken = localStorage.getItem('refresh_token');

  if (!refreshToken) {
    throw new Error('No refresh token available');
  }

  try {
    const response = await fetch('/api/token/refresh/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ refresh: refreshToken }),
    });

    if (!response.ok) {
      // If refresh fails, clear tokens and redirect to login
      clearAuthToken();
      throw new Error('Failed to refresh token');
    }

    const data = await response.json();
    localStorage.setItem('access_token', data.access);
    return data;
  } catch (error) {
    console.error('Error refreshing JWT token:', error);
    throw error;
  }
}

/**
 * Check if user is authenticated (has valid token)
 * @returns {boolean} True if user has a token
 */
function isAuthenticated() {
  return !!getAuthToken();
}

// Configure HTMX to automatically include JWT token in all API requests
document.addEventListener('DOMContentLoaded', function() {
  // Add Authorization header to all HTMX requests to /api/
  document.body.addEventListener('htmx:configRequest', function(event) {
    const token = getAuthToken();

    // Only add token for API requests
    if (event.detail.path.startsWith('/api/') && token) {
      event.detail.headers['Authorization'] = `Bearer ${token}`;
    }
  });

  // Handle 401 responses (unauthorized) - attempt to refresh token
  document.body.addEventListener('htmx:responseError', async function(event) {
    if (event.detail.xhr.status === 401 && event.detail.pathInfo.requestPath.startsWith('/api/')) {
      try {
        // Try to refresh the token
        await refreshJWTToken();

        // Retry the original request
        const token = getAuthToken();
        if (token) {
          // Re-issue the request with new token
          htmx.ajax(event.detail.pathInfo.verb, event.detail.pathInfo.requestPath, {
            target: event.detail.target,
            swap: event.detail.pathInfo.swap,
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
        }
      } catch (error) {
        console.error('Token refresh failed:', error);
        // Redirect to login if token refresh fails
        window.location.href = '/accounts/login/';
      }
    }
  });
});

// Automatically fetch token when user logs in via Django allauth
// This looks for a successful login and fetches JWT token
document.addEventListener('DOMContentLoaded', function() {
  // Check if we're on a page after successful login
  // You can customize this based on your needs
  const isLoggedIn = document.querySelector('[data-user-authenticated="true"]');

  if (isLoggedIn && !isAuthenticated()) {
    // User is logged in via session but doesn't have JWT token
    // You'll need to implement a view that converts session auth to JWT
    console.log('User is authenticated but no JWT token found');
    // Option: Show a message or button to "Connect to API"
  }
});
