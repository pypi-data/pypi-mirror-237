from collections.abc import Generator, Iterator

from django.db import models

from django_pgrls.state import TenantConstraint, bypass, get_current_tenant


class UnboundUsage(Exception):
    pass


class TenantBoundQueryset(models.QuerySet):
    def _is_unbound(self) -> bool:
        return get_current_tenant() in [TenantConstraint.NONE, TenantConstraint.ALL]

    def _fetch_all(self) -> None:
        if self._is_unbound():
            raise UnboundUsage

        super()._fetch_all()

    def count(self) -> int:
        if self._is_unbound():
            raise UnboundUsage

        return super().count()

    def iterator(self, *args, **kwargs) -> Iterator:
        if self._is_unbound():
            raise UnboundUsage

        return super().iterator(*args, **kwargs)

    def exists(self) -> bool:
        if self._is_unbound():
            raise UnboundUsage

        return super().exists()


class TenantBypassQueryset(models.QuerySet):
    def _fetch_all(self) -> None:
        with bypass():
            super()._fetch_all()

    def count(self) -> int:
        with bypass():
            return super().count()

    def iterator(self, *args, **kwargs) -> Iterator:
        _iterator = super().iterator(*args, **kwargs)

        def generator() -> Generator:
            with bypass():
                yield from _iterator

        return generator()

    def exists(self) -> bool:
        with bypass():
            return super().exists()


class TenantBoundManager(models.Manager.from_queryset(TenantBoundQueryset)):
    pass


class TenantBypassManager(models.Manager.from_queryset(TenantBypassQueryset)):
    pass
