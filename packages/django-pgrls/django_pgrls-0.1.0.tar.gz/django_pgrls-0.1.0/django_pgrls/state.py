from contextlib import contextmanager
from enum import Enum
from typing import TYPE_CHECKING

from asgiref.local import Local

if TYPE_CHECKING:
    from django_pgrls.models import TenantMixin

_active = Local()


class TenantConstraint(Enum):
    ALL = "__ALL__"
    NONE = "__NONE__"


def get_current_tenant() -> "TenantMixin | TenantConstraint":
    return getattr(_active, "value", TenantConstraint.NONE)


def activate(tenant: "TenantMixin") -> None:
    _active.value = tenant


def deactivate() -> None:
    if hasattr(_active, "value"):
        del _active.value


@contextmanager
def bypass() -> None:
    current_tenant = get_current_tenant()

    if current_tenant is not TenantConstraint.ALL:
        _active.value = TenantConstraint.ALL

    yield

    if current_tenant is not TenantConstraint.ALL:
        activate(current_tenant)
