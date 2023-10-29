from django.db import models

from django_pgrls.constraints import RowLevelSecurityConstraint
from django_pgrls.managers import TenantBoundManager, TenantBypassManager
from django_pgrls.state import TenantConstraint, activate, deactivate, get_current_tenant
from django_pgrls.utils import get_tenant_model_path


class TenantMixin(models.Model):
    class Meta:
        abstract = True

    def __enter__(self):
        self._previous_tenant = get_current_tenant()
        if self._previous_tenant is not TenantConstraint.ALL:
            activate(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        _previous_tenant = getattr(self, "_previous_tenant", TenantConstraint.NONE)
        if _previous_tenant is TenantConstraint.NONE:
            deactivate()
        elif _previous_tenant is not TenantConstraint.ALL:
            activate(_previous_tenant)


class TenantBoundMixin(models.Model):
    tenant = models.ForeignKey(
        get_tenant_model_path(),
        on_delete=models.CASCADE,
        related_name="+",
    )

    objects = TenantBoundManager()
    unbound_objects = TenantBypassManager()

    class Meta:
        abstract = True
        constraints = [
            RowLevelSecurityConstraint("tenant"),
        ]

    def save(self, *args, **kwargs):
        if self.tenant is None:
            self.tenant = get_current_tenant()

        super().save(*args, **kwargs)
