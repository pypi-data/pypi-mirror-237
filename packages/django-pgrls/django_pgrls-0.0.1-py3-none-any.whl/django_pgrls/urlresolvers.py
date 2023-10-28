import re

from django.urls import URLResolver

from .state import get_current_tenant


class TenantPrefixPattern:
    converters = {}

    @property
    def tenant_prefix(self):
        current_tenant = get_current_tenant()
        return f"{current_tenant.folder}/" if current_tenant.folder else "/"

    @property
    def regex(self):
        # This is only used by reverse() and cached in _reverse_dict.
        return re.compile(self.tenant_prefix)

    def match(self, path):
        tenant_prefix = self.tenant_prefix
        if path.startswith(tenant_prefix):
            return path[len(tenant_prefix) :], (), {}
        return None

    def check(self):
        return []

    def describe(self):
        return f"'{self}'"

    def __str__(self):
        return self.tenant_prefix


def tenant_patterns(*urls):
    """
    Add the tenant prefix to every URL pattern within this function.
    This may only be used in the root URLconf, not in an included URLconf.
    """
    return [URLResolver(TenantPrefixPattern(), list(urls))]


def get_dynamic_tenant_prefixed_urlconf(urlconf, dynamic_path):
    """
    Generates a new URLConf module with all patterns prefixed with tenant.
    """
    from types import ModuleType

    from django.utils.module_loading import import_string

    class LazyURLConfModule(ModuleType):
        def __getattr__(self, attr):
            imported = import_string(f"{urlconf}.{attr}")
            if attr == "urlpatterns":
                return tenant_patterns(*imported)
            return imported

    return LazyURLConfModule(dynamic_path)
