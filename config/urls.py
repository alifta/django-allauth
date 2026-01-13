from django.contrib import admin
from django.urls import path, include
from core.views import CustomSignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path("accounts/", include("allauth.urls")),
    # path("accounts/mfa/", include("allauth.mfa.urls")),  # MFA disabled
    path("api/", include("api.urls", namespace="api")),
    path("silk/", include("silk.urls", namespace="silk")),  # Django Silk profiling interface
    path("", include("core.urls", namespace="core")),
]
