from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gpiozero

luz = gpiozero.LED(15)

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[""],
  allow_credentials=True,
  allow_methods=[""],
  allow_headers=["*"],
)

@app.get("/encender")
async def encender():
  luz.on()
  return {
    "message": "Encendida",
    "encendida": True
  }

@app.get("/apagar")
async def apagar():
  luz.off()
  return {
    "message": "Apagada",
    "encendida": False
  }