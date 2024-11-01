from fastapi import FastAPI
from app.routes import health
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


app = FastAPI()

# Include routers from separate route modules
app.include_router(health.router, prefix="/health", tags=["Health"])

scheduler = BackgroundScheduler()

def scheduled_task():
    print(f"Task running at {datetime.now()}")  # Replace with actual task logic

# Define the lifespan context manager
@app.on_event("lifespan")
async def app_lifespan(app):
    # Start the scheduler and add the job on app startup
    scheduler.add_job(scheduled_task, 'interval', minutes=14)
    scheduler.start()

    yield  # Yield here signifies the app is up and running

    # Shutdown the scheduler on app shutdown
    scheduler.shutdown()



@app.get("/")
async def startup():
    return "Api is working fine v1"

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)