from typing import Any

from django.core.checks import Error, Tags, register
from django.db import connection


def user_is_superuser() -> bool:
    with connection.cursor() as cursor:
        cursor.execute("SELECT usesuper FROM pg_user WHERE usename = current_user;")
        return bool(list(cursor.fetchall())[0][0])


@register(Tags.database)
def check_database_user(app_configs: Any, **kwargs: Any) -> list[Error]:
    errors = []

    if user_is_superuser():
        errors.append(
            Error(
                "Database superuser will always bypass row level security",
                hint="Use a database user that has full privileges but is not superuser.",
                id="django_pgrls.E001",
            )
        )

    return errors
