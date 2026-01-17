from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h8fbiw9svk5wj4%appv4qwbuh6c6vj9zpd4*(*(a4#tj#%fehn"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django built-in apps
    "django.contrib.admin",  # Admin interface for managing site content
    "django.contrib.auth",  # Authentication framework (users, groups, permissions)
    "django.contrib.contenttypes",  # Content types framework (generic relations)
    "django.contrib.sessions",  # Session framework (user session management)
    "django.contrib.messages",  # Messaging framework (one-time notifications)
    "django.contrib.staticfiles",  # Static files handling (CSS, JS, images)
    # Local apps
    "core",  # Core application with main business logic
    "api",  # REST API application for external integrations
    # Third-party apps
    "django_extensions",  # Additional Django management commands and utilities
    "rest_framework",  # Django REST Framework for building RESTful APIs
    "ninja", # Ninja API framework
    "django_htmx",  # HTMX integration for Django (dynamic HTML interactions)
    "widget_tweaks",  # Widget customization utilities for forms
    "template_partials",  # Template partials support (reusable template fragments)
    "corsheaders",  # CORS (Cross-Origin Resource Sharing) headers support
    # django-allauth: Authentication and account management
    "allauth",  # django-allauth main application
    "allauth.account",  # Account management (signup, login, email verification)
    "allauth.socialaccount",  # Social account providers framework
    "allauth.socialaccount.providers.google",  # Google OAuth provider
    "allauth.socialaccount.providers.github",  # GitHub OAuth provider
    # "allauth.mfa",  # Multi-factor authentication (currently disabled)
    # Profiling and debugging
    "silk",  # Django Silk - SQL query and performance profiling tool
]

MIDDLEWARE = [
    # Security middleware (must be first)
    # Handles security headers, SSL redirects, and other security-related features
    "django.middleware.security.SecurityMiddleware",
    # Profiling middleware (must be early to capture all requests)
    # Django Silk - profiles SQL queries and request/response data for performance analysis
    "silk.middleware.SilkyMiddleware",
    # Session middleware
    # Manages user sessions (must be before any middleware that uses sessions)
    "django.contrib.sessions.middleware.SessionMiddleware",
    # CORS middleware
    # Handles Cross-Origin Resource Sharing headers (must be before CommonMiddleware)
    "corsheaders.middleware.CorsMiddleware",
    # Common middleware
    # Handles URL rewriting, APPEND_SLASH, and other common functionality
    "django.middleware.common.CommonMiddleware",
    # CSRF protection middleware
    # Validates CSRF tokens for POST requests (must be after SessionMiddleware)
    "django.middleware.csrf.CsrfViewMiddleware",
    # Authentication middleware
    # Adds user attribute to request object (must be after SessionMiddleware)
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # MFA middleware (currently disabled)
    # "core.middleware.MFARequiredMiddleware",  # Multi-factor authentication enforcement
    # Messages middleware
    # Handles one-time messages/flash messages (requires sessions and authentication)
    "django.contrib.messages.middleware.MessageMiddleware",
    # Clickjacking protection middleware
    # Sets X-Frame-Options header to prevent clickjacking attacks
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # django-allauth account middleware (should be last)
    # Handles account-related functionality like email verification, account connections
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Global templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # For development

# LOGIN_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "core:secret"

# AUTH_USER_MODEL = 'core.User'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Allauth settings
# Allow login with username or email
ACCOUNT_LOGIN_METHODS = ["username", "email"]
ACCOUNT_EMAIL_VERIFICATION = (
    "optional"  # Change to "optional" for development "mandatory" for production
)
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_SIGNUP_FORM_CLASS = "core.forms.CustomSignupForm"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "EMAIL_AUTHENTICATION": True,
        "SCOPE": [
            "profile",
            "email",
        ],
    },
    "github": {
        "SCOPE": [
            "user",
            "repo",
            "read:org",
            "email",
        ],
    },
}
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

# Django REST Framework configuration
# Configures authentication and permissions for all API endpoints
REST_FRAMEWORK = {
    # Authentication classes tried in order until one succeeds
    # JWTAuthentication: Validates Bearer tokens in Authorization header
    # SessionAuthentication: Falls back to Django session auth (useful for browsable API)
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    # Default permission for all API views (can be overridden per view)
    # IsAuthenticated: Requires user to be logged in (via token or session)
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# JWT (JSON Web Token) settings for djangorestframework-simplejwt
# Tokens are obtained via POST /api/token/ with username and password
SIMPLE_JWT = {
    # How long access tokens remain valid (used for API requests)
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    # How long refresh tokens remain valid (used to get new access tokens)
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # If True, issuing a new refresh token invalidates the old one
    "ROTATE_REFRESH_TOKENS": False,
    # If True, old refresh tokens are added to blacklist after rotation
    "BLACKLIST_AFTER_ROTATION": False,
    # If True, updates user.last_login when token is obtained
    "UPDATE_LAST_LOGIN": False,
    # Cryptographic algorithm used to sign tokens
    "ALGORITHM": "HS256",
    # Secret key used to sign tokens (uses Django SECRET_KEY)
    "SIGNING_KEY": SECRET_KEY,
    # Public key for verifying tokens (None for symmetric algorithms like HS256)
    "VERIFYING_KEY": None,
    # Expected audience claim in token (None = not validated)
    "AUDIENCE": None,
    # Expected issuer claim in token (None = not validated)
    "ISSUER": None,
    # URL to fetch JSON Web Key Set (None = not used)
    "JWK_URL": None,
    # Time leeway for token expiration validation
    "LEEWAY": 0,
    # Authorization header prefix (e.g., "Bearer <token>")
    "AUTH_HEADER_TYPES": ("Bearer",),
    # HTTP header name containing the token
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # User model field used as unique identifier
    "USER_ID_FIELD": "id",
    # JWT claim name that stores the user ID
    "USER_ID_CLAIM": "user_id",
    # Rule for authenticating users from token claims
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    # Token class used for access tokens
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # JWT claim name that stores the token type
    "TOKEN_TYPE_CLAIM": "token_type",
    # Class used to represent authenticated user from token
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    # JWT claim name for unique token identifier (used for blacklisting)
    "JTI_CLAIM": "jti",
    # JWT claim name for sliding token refresh expiration
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # Lifetime of sliding tokens (if using sliding tokens)
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    # Refresh token lifetime for sliding tokens
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# CORS Configuration for Angular frontend
# Allows Angular dev server (http://localhost:4200) to make requests to Django API
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

# Allow credentials (cookies, authorization headers, etc.)
CORS_ALLOW_CREDENTIALS = True

# Allow specific HTTP methods
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# Allow specific headers
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
