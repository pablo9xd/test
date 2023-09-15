from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def get_username(self, claims):
        return claims.get("preferred_username") or claims.get("username")

    def create_user(self, claims):
        user = super().create_user(claims)
        user.firstname = claims.get("given_name", "")
        user.lastname = claims.get("family_name", "")
        user.save()
        return user

    def update_user(self, user, claims):
        user.firstname = claims.get("given_name", "")
        user.lastname = claims.get("family_name", "")
        user.save()
        return user

    def authenticate(self, request, **kwargs):
        user = super().authenticate(request, **kwargs)
        return user
