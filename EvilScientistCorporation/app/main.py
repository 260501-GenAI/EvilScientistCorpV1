from fastapi import FastAPI, HTTPException

from starlette.requests import Request
from starlette.responses import JSONResponse

from app.routers import users

# Set up FastAPI. We'll use this "app" variable to do FastAPI stuff below
app = FastAPI()

# Global custom Exception Handler
# All Exceptions raised in the routers get handled here
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request:Request, exception:HTTPException):
    return JSONResponse(
        status_code=exception.status_code,
        content={"message":exception.detail}
    )


# Import routers here
app.include_router(users.router)

# Generic sample endpoint (GET request that just returns a message)
@app.get("/")
async def sample_endpoint():
    return {"message":"Hello FastAPI!"}