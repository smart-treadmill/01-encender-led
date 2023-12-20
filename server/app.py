from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/encender")
async def encender():
  return {
    "message": "Encendida",
    "encendida": True
  }


@app.get("/apagar")
async def apagar():
  return {
    "message": "Apagada",
    "encendida": False
  }