"""
FastAPI ML Service — Application Entry Point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ML Inference Service",
    description="Serves predictions from the trained machine learning model.",
    version="0.1.0",
)

# ---------------------------------------------------------------------------
# CORS — allow requests from the React dev server
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers — uncomment as you add them
# ---------------------------------------------------------------------------
# from app.api import predict
# app.include_router(predict.router, prefix="/api/v1", tags=["predict"])


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    """Liveness probe endpoint."""
    return {"status": "ok"}
