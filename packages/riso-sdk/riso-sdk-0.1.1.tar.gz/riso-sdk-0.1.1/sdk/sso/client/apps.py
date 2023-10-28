from django.apps import AppConfig


class SSOClientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sdk.sso.client"

    def ready(self):
        from . import settings

        assert settings.SSO_PRIVATE_KEY, "As SSO client you must set SSO_PRIVATE_KEY in your settings.py"
        assert settings.SSO_PUBLIC_KEY, "As SSO client you must set SSO_PUBLIC_KEY in your settings.py"
        assert settings.SSO_SERVER, "As SSO client you must set SSO_SERVER in your settings.py"
        assert (
            "http" in settings.SSO_SERVER or "https" in settings.SSO_SERVER,
            "SSO_SERVER must be a valid URL (http:// or https://)"  # noqa
        )
