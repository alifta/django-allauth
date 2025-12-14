from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("secret/", views.secret, name="secret"),
    path("fragments/signup/", views.signup_fragment, name="signup_fragment"),
    path("fragments/signin/", views.signin_fragment, name="signin_fragment"),
]
