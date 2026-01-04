from django.contrib import admin
from django.urls import path, include
from core.views import CustomSignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path("accounts/", include("allauth.urls")),
    # path("accounts/mfa/", include("allauth.mfa.urls")),  # MFA disabled
    path("", include("core.urls", namespace="core")),
    # path("api/", include("core.api_urls", namespace="core_api")),
]
