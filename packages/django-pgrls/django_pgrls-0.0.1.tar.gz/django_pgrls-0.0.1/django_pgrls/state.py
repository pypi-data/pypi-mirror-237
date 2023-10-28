from contextlib import contextmanager

from asgiref.local import Local

from .models import TenantMixin

_active = Local()


def get_current_tenant() -> TenantMixin | None:
    return getattr(_active, "value", None)


def activate(tenant: TenantMixin) -> None:
    _active.value = tenant


def deactivate() -> None:
    if hasattr(_active, "value"):
        del _active.value


@contextmanager
def bypass() -> None:
    current_tenant = get_current_tenant()

    if current_tenant is not None:
        deactivate()

    yield

    if current_tenant is not None:
        activate(current_tenant)
