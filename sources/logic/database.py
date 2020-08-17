from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import logic.settings as app_settings


def init_database_in_api(app: FastAPI):
    register_tortoise(
        app,
        db_url=app_settings.DB_URL,
        modules={
            'models': ['logic.tables']
        },
        generate_schemas=True,
        add_exception_handlers=True
    )

