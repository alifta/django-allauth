from django.contrib import admin
from django.urls import include, path

from core.views import CustomSignupView

# URL configuration for the Django project
# Defines the root URL patterns that route incoming requests to appropriate views/apps
# Order matters: Django matches URLs from top to bottom, so more specific patterns should come first
urlpatterns = [
    # Django admin interface
    # Accessible at /admin/ - provides web-based admin panel for managing site content
    path("admin/", admin.site.urls),
    # REST API endpoints
    # Includes all API routes defined in api/urls.py
    # Accessible at /api/... (e.g., /api/token/, /api/todos/, etc.)
    # Placed early to ensure API routes are matched before catch-all patterns
    path("api/", include("api.urls", namespace="api")),
    # Django Silk profiling interface
    # Development tool for profiling SQL queries and request/response performance
    # Accessible at /silk/ - only available when django-silk is installed
    # Placed before catch-all patterns but after API routes
    path("silk/", include("silk.urls", namespace="silk")),
    # Custom signup view override
    # Customizes the default allauth signup process with additional form fields/logic
    # Must come before general accounts/ pattern to ensure custom signup is matched first
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    # django-allauth authentication URLs
    # Includes all allauth routes: login, logout, password reset, email verification, etc.
    # Accessible at /accounts/login/, /accounts/logout/, /accounts/password/reset/, etc.
    path("accounts/", include("allauth.urls")),
    # Multi-factor authentication (currently disabled)
    # Uncomment to enable MFA routes at /accounts/mfa/
    # path("accounts/mfa/", include("allauth.mfa.urls")),  # MFA disabled
    # Core application URLs (catch-all)
    # Includes all core app routes (homepage, todos, transactions, etc.)
    # Accessible at /... (root level routes like /, /about/, /todo/, etc.)
    # Placed last as it includes root-level routes that could match many paths
    path("", include("core.urls", namespace="core")),
]
