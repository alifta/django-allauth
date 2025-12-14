from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings


class CustomSignupView(SignupView):


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom_message"] = "Join 10,0000+ visionary realestate community using out cutting-edge, AI-powered, blockchain-enabled, cloud-native platform to disrupt the paradigm and synergize realestate investing!"

        return context

    def form_valid(self, form):
        # Add any custom logic here before saving the user
        response = super().form_valid(form)

        if (
            app_settings.EMAIL_VERIFICATION
            == app_settings.EmailVerificationMethod.MANDATORY
        ):
            messages.info(
                self.request,
                "Please verify your email address to complete the registration.",
            )
        else:
            messages.success(
                self.request,
                f"Welcome {form.cleaned_data.get('first_name', '')}! You have signed up successfully.",
            )

        return response


def index(request):
    return render(request, "core/index.html")


@login_required
def secret(request):
    return render(request, "core/secret.html")


def signup_fragment(request):
    return render(request, "core/_signup_fragment.html")


def signin_fragment(request):
    return render(request, "core/_signin_fragment.html")
