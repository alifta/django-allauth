from django import forms
from core.models import UserProfile


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        label="Phone Number",
        widget=forms.TextInput(attrs={"placeholder": "Phone Number"}),
    )
    bio = forms.CharField(
        max_length=500,
        required=False,
        label="Bio",
        widget=forms.Textarea(attrs={"placeholder": "Tell us about yourself"}),
    )
    birth_date = forms.DateField(required=False, label="Birth Date")

    def signup(self, request, user):
        """Called after user is created but before saved to handle additional fields."""
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        # Create associated Profile
        profile = UserProfile(user=user)
        profile.phone = self.cleaned_data.get("phone", "")
        profile.bio = self.cleaned_data.get("bio", "")
        profile.birth_date = self.cleaned_data.get("birth_date", None)
        profile.save()
        return user