# I want all user-based HTTP endpoints to live here
from fastapi import APIRouter

# Set up this module as a FastAPI router.
# We'll import this in main to make these endpoints accessible
router = APIRouter(
    prefix="/users", # HTTP requests ending in /users will be directed to this router
    tags=["users"] # This groups this routers endpoints under "users" in the /docs UI
)

# Create new users (POST request)
@router.post("/")
async def create_user():
    return {"user":"Bob, 25, Illinois"}

# Get all users (GET request)
@router.get("/")
async def get_all_users():
    return {"users":"Alice, Bob, Jimmy, Jamie, Jerry"}

# Delete a specific user by ID (DELETE request + path variable)

# Update a specific user's info by ID (PUT request + path variable)