import re

from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from custom_user.models import UserProfile


class PasswordChangeMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request: HttpRequest):
        if (
            request.user.is_authenticated
            and not re.search(r"/password_change/?", request.path)
            and not re.search(r"/logout/?", request.path)
            and not request.user.is_superuser
            and UserProfile.cached_force_password_change(request.user)
        ):
            return redirect(reverse("password_change"))
