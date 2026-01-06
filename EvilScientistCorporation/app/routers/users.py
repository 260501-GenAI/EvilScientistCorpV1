# I want all user-based HTTP endpoints to live here
from fastapi import APIRouter

from app.models.user_model import UserModel

# Set up this module as a FastAPI router.
# We'll import this in main to make these endpoints accessible
router = APIRouter(
    prefix="/users", # HTTP requests ending in /users will be directed to this router
    tags=["users"] # This groups this routers endpoints under "users" in the /docs UI
)

# Temporary DB - just a python map of User models
user_database = {
    1: UserModel(
        id=1,
        username="Doofenshmirtz",
        password="password",
        email="platypushater@gmail.com"
    ),
    2: UserModel(
        id=2,
        username="BigFrank",
        password="password",
        email="whofurted@aol.com"
    ),
    3: UserModel(
        id=3,
        username="JumbaGuy",
        password="password",
        email="jookiba@yahoo.com"
    )
}

# Create new users (POST request)
@router.post("/")
async def create_user(user:UserModel):
    user_database[999] = user
    return {
        "message":user.username + " created successfully!",
        "inserted_user":user
    }

# Get all users (GET request)
@router.get("/")
async def get_all_users():
    return user_database

# Delete a specific user by ID (DELETE request + path variable)

# Update a specific user's info by ID (PUT request + path variable)