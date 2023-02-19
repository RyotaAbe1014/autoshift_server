from fastapi import FastAPI
from settings.custom_route import CustomRoute
from auth import auth
from routers import organization

app = FastAPI()
app.router.route_class = CustomRoute

app.include_router(auth.router)
app.include_router(organization.router)