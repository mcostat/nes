from typing import Any

from django.http import HttpRequest
from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    oidc_claim_scope = None

    def get_additional_claims(self, request: HttpRequest) -> dict[str, Any]:
        return {
            "first_name": request.user.first_name,
            "username": request.user.get_username(),
            "email": request.user.get_email_field_name(),
        }
