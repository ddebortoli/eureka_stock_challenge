from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, stock
from uvicorn import run
from logging import basicConfig, Formatter, getLogger, INFO
from logging.handlers import RotatingFileHandler

# Configuración del logger
logger = getLogger()
if not logger.hasHandlers():
    basicConfig(level=INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(filename='eureka_api.log', maxBytes=5*1024*1024, backupCount=1)  # 5 MB
    handler.setLevel(INFO)
    handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(stock.router, prefix="/api")

origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_request_ip(request: Request, call_next):
    ip = request.client.host
    getLogger().info(f"Request from IP: {ip}")
    response = await call_next(request)
    return response

if __name__ == "__main__":
    run("server:app", host="0.0.0.0", port=8000, workers=1)
