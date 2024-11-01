from fastapi import FastAPI
from app.routes import health
import os
app = FastAPI()

# Include routers from separate route modules
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
async def startup():
    return "Api is working fine v1"

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)