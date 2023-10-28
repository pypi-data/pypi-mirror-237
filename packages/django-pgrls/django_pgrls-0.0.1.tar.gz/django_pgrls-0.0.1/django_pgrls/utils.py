from django.apps import apps
from django.conf import settings
from django.db.models import Model

TENANT_MODEL = getattr(settings, "TENANT_MODEL", None)
DOMAIN_MODEL = getattr(settings, "DOMAIN_MODEL", None)


def get_tenant_model(require_ready: bool = True) -> Model | None:
    "Returns the tenant model."
    if TENANT_MODEL is None:
        return None

    return apps.get_model(TENANT_MODEL, require_ready=require_ready)


def get_domain_model(require_ready: bool = True) -> Model | None:
    "Returns the domain model."

    if DOMAIN_MODEL is None:
        return None

    return apps.get_model(DOMAIN_MODEL, require_ready=require_ready)


def remove_www(hostname: str) -> str:
    """
    Removes ``www``. from the beginning of the address. Only for
    routing purposes. ``www.test.com/login/`` and ``test.com/login/`` should
    find the same tenant.
    """
    if hostname.startswith("www."):
        return hostname[4:]
    return hostname


def django_is_in_test_mode() -> bool:
    """
    I know this is very ugly! I'm looking for more elegant solutions.
    See: http://stackoverflow.com/questions/6957016/detect-django-testing-mode
    """
    from django.core import mail

    return hasattr(mail, "outbox")
