from django.shortcuts import redirect
from django.urls import reverse
from allauth.mfa.utils import is_mfa_enabled


class MFARequiredMiddleware:
    """
    Middleware to enforce MFA at login.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            reverse("mfa_index"),
            reverse("mfa_activate_totp"),
            reverse("account_logout"),
        ]

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the current path
            path = request.path_info
            # Check if the current path is exempted
            is_exempt = any(path.startswith(url) for url in self.exempt_urls)

            # If not exempt, check MFA status
            if not is_exempt:
                # Check if the user has not set up MFA
                if not is_mfa_enabled(request.user):
                    # Redirect to MFA setup page
                    return redirect("mfa_index")

        # Proceed the request normally
        response = self.get_response(request)
        return response
