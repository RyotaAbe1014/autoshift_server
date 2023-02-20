from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings.custom_route import CustomRoute
from auth import auth
from routers import organization, user

app = FastAPI()
app.router.route_class = CustomRoute

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(organization.router)
app.include_router(user.router)
