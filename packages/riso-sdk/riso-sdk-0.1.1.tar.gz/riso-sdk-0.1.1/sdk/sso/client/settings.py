from django.conf import settings

SSO_PRIVATE_KEY = settings.SSO_PRIVATE_KEY if hasattr(settings, 'SSO_PRIVATE_KEY') else None
SSO_PUBLIC_KEY = settings.SSO_PUBLIC_KEY if hasattr(settings, 'SSO_PUBLIC_KEY') else None
SSO_SERVER = settings.SSO_SERVER if hasattr(settings, 'SSO_SERVER') else None
