from fastapi import FastAPI

from app.routers import users

# Set up FastAPI. We'll use this "app" variable to do FastAPI stuff below
app = FastAPI()

# Import routers here
app.include_router(users.router)

# Generic sample endpoint (GET request that just returns a message)
@app.get("/")
async def sample_endpoint():
    return {"message":"Hello FastAPI!"}