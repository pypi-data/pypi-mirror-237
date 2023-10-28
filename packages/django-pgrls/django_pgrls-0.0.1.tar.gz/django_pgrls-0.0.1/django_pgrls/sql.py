from typing import Any

from django.db.migrations.operations.models import ModelOperation

CREATE_POLICY = """
CREATE POLICY tenant_row_level_security ON %s USING (
    CASE
        WHEN current_setting('app.tenant_id', True) is null
        OR current_setting('app.tenant_id', True) = '' THEN True
        ELSE tenant_id = current_setting('app.tenant_id')::int
    END
)
"""

DROP_POLICY = "DROP POLICY IF EXISTS tenant_row_level_security on %s"

ENABLE_RLS = "ALTER TABLE %s ENABLE ROW LEVEL SECURITY;"
FORCE_RLS = "ALTER TABLE %s FORCE ROW LEVEL SECURITY;"
DISABLE_RLS = "ALTER TABLE %s DISABLE ROW LEVEL SECURITY;"


class TenantRowLevelSecurity(ModelOperation):
    """Enables RLS for a model."""

    def state_forwards(self, app_label: str, state: Any) -> None:
        pass

    def database_forwards(
        self, app_label: str, schema_editor: Any, from_state: Any, to_state: Any
    ) -> None:
        from_state.clear_delayed_apps_cache()
        table_name = from_state.apps.get_model(app_label, self.name)._meta.db_table

        schema_editor.execute(CREATE_POLICY % table_name)
        schema_editor.execute(ENABLE_RLS % table_name)
        schema_editor.execute(FORCE_RLS % table_name)

    def database_backwards(
        self, app_label: str, schema_editor: Any, from_state: Any, to_state: Any
    ) -> None:
        from_state.clear_delayed_apps_cache()
        table_name = from_state.apps.get_model(app_label, self.name)._meta.db_table

        schema_editor.execute(DISABLE_RLS % table_name)
        schema_editor.execute(DROP_POLICY % table_name)
