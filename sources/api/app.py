from fastapi import FastAPI

from api.routes import create_routes
from logic.database import init_database_in_api

app = FastAPI()

create_routes(app)

init_database_in_api(app)
