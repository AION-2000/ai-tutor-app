from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your routers
from app.routers import questions, auth

# Create the FastAPI app instance
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routers from the 'routers' directory
app.include_router(questions.router, prefix="/api/v1/questions")
app.include_router(auth.router, prefix="/api/v1/auth")

# Add a root endpoint for basic health check
@app.get("/")
async def root():
    return {"status": "API is running"}