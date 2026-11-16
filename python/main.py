

from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timezone
from pathlib import Path


import os
import json

# Polaczenie z Firebase
klucz_online = os.getenv("FIREBASE_CREDENTIALS")

if klucz_online:
    # Na Vercel - klucz ze zmiennej srodowiskowej
    cred = credentials.Certificate(json.loads(klucz_online))
else:
    # Lokalnie - klucz z pliku na komputerze
    plik_klucza = Path(__file__).parent / "serviceAccountKey.json"
    cred = credentials.Certificate(str(plik_klucza))

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://microbit-reflex-game-default-rtdb.europe-west1.firebasedatabase.app"
})

app = FastAPI()

# Format danych od wykladowcy
class Wynik(BaseModel):
    id: str
    wynik: int

# Zapisywanie wyniku w Firebase
@app.post("/results")
def dodaj_wynik(dane: Wynik):
    rekord = {
        "id": dane.id,
        "wynik": dane.wynik,
        "data": datetime.now(timezone.utc).isoformat()
    }

    db.reference("wyniki").push(rekord)

    return {"status": "OK", "zapisano": rekord}

# Sprawdzenie API
@app.get("/")
def start():
    return {"message": "Microbit Reflex Game API dziala!"}
