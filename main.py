from fastapi import FastAPI
from app.routes import health

app = FastAPI()

# Include routers from separate route modules
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
async def startup():
    return "Api is working fine v1"