from api.src.controller.example_controller import example_router
from fastapi.middleware.cors import CORSMiddleware
import os

from fastapi import FastAPI
import uvicorn;

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router)

@app.get("/")
async def root():
    return {"It works!"}

if __name__ == '__main__':
    if os.getenv('APP_ENV') == 'production':
        uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", workers=4)
    elif os.getenv('APP_ENV') == 'development':
        uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)