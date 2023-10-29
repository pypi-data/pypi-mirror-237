from django.db import models
from django.db.utils import DEFAULT_DB_ALIAS

DEFAULT_CONSTRAINT_NAME = "row_level_security"


class RowLevelSecurityConstraint(models.BaseConstraint):
    def __init__(self, field, name=None):
        super().__init__(name=name or DEFAULT_CONSTRAINT_NAME)
        self.target_field = field

    def constraint_sql(self, model, schema_editor):
        return ""

    def create_sql(self, model, schema_editor):
        return schema_editor._activate_rls(model, self.target_field, self.name)

    def remove_sql(self, model, schema_editor):
        return schema_editor._deactivate_rls(model, self.target_field, self.name)

    def validate(self, model, instance, exclude=None, using=DEFAULT_DB_ALIAS):
        pass

    def deconstruct(self):
        path = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        return (
            path,
            (),
            {"field": self.target_field, "name": self.name},
        )
