from django.core.exceptions import ImproperlyConfigured
from django.db.utils import DatabaseError

from django_pgrls.state import TenantConstraint, get_current_tenant

from .schema import DatabaseSchemaEditor
from .settings import original_backend

try:
    try:
        import psycopg as _psycopg
    except ImportError:
        import psycopg2 as _psycopg
except ImportError:
    raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")

IntegrityError = _psycopg.IntegrityError


class DatabaseWrapper(original_backend.DatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor

    def __init__(self, *args, **kwargs):
        self.tenant_id = None
        self._setting_tenant_id = False
        super().__init__(*args, **kwargs)

    def close(self):
        self.tenant_id = None
        self._setting_tenant_id = False
        super().close()

    def _handle_tenant(self, cursor=None):
        tenant = get_current_tenant()

        tenant_id = tenant.id if type(tenant) is not TenantConstraint else tenant.value

        skip = self._setting_tenant_id or self.tenant_id == tenant_id

        if not skip:
            self._setting_tenant_id = True
            cursor_for_tenant = self.connection.cursor() if cursor is None else cursor

            try:
                cursor_for_tenant.execute(f"SET app.tenant_id = '{tenant_id}';")
            except (DatabaseError, _psycopg.InternalError):
                self.tenant_id = None
            else:
                self.tenant_id = tenant_id
            finally:
                self._setting_tenant_id = False

            if cursor is None:
                cursor_for_tenant.close()

    def _cursor(self, name=None):
        cursor = super()._cursor(name=name)

        cursor_for_tenant = cursor if name is None else None  # Named cursors cannot be reused
        self._handle_tenant(cursor_for_tenant)

        return cursor
