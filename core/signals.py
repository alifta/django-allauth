from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.utils import timezone


@receiver(email_confirmed)
def email_confirmed_handler(request, email_address, **kwargs):
    user = email_address.user

    user.profile.email_verified_at = timezone.now()
    user.profile.save()
