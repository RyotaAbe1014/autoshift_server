from fastapi import FastAPI
from settings.custom_route import CustomRoute
from auth import auth

app = FastAPI()
app.router.route_class = CustomRoute

app.include_router(auth.router)
