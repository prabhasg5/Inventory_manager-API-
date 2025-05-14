from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import inventory
from app.config import API_V1_STR, PROJECT_NAME
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(
    title=PROJECT_NAME,
    description="API for managing inventory items",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    inventory.router,
    prefix=f"{API_V1_STR}/items",
    tags=["inventory"]
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Inventory Manager API, I am Jaya nanda Prabhas",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return HTTPException(
        status_code=500,
        detail="An unexpected error occurred. Please try again later."
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)