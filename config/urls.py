from django.contrib import admin
from django.urls import include, path

from core.views import CustomSignupView

# URL configuration for the Django project
# Defines the root URL patterns that route incoming requests to appropriate views/apps
urlpatterns = [
    # Django admin interface
    # Accessible at /admin/ - provides web-based admin panel for managing site content
    path("admin/", admin.site.urls),
    # Custom signup view override
    # Customizes the default allauth signup process with additional form fields/logic
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    # django-allauth authentication URLs
    # Includes all allauth routes: login, logout, password reset, email verification, etc.
    # Accessible at /accounts/login/, /accounts/logout/, /accounts/password/reset/, etc.
    path("accounts/", include("allauth.urls")),
    # Multi-factor authentication (currently disabled)
    # Uncomment to enable MFA routes at /accounts/mfa/
    # path("accounts/mfa/", include("allauth.mfa.urls")),  # MFA disabled
    # REST API endpoints
    # Includes all API routes defined in api/urls.py
    # Accessible at /api/... (e.g., /api/token/, /api/todos/, etc.)
    path("api/", include("api.urls", namespace="api")),
    # Django Silk profiling interface
    # Development tool for profiling SQL queries and request/response performance
    # Accessible at /silk/ - only available when django-silk is installed
    path("silk/", include("silk.urls", namespace="silk")),
    # Core application URLs
    # Includes all core app routes (homepage, todos, transactions, etc.)
    # Accessible at /... (root level routes)
    path("", include("core.urls", namespace="core")),
]
