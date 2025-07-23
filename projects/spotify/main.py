from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import time
import os

app = FastAPI()

# Allow your frontend domain for CORS
origins = [
    "https://adamkoplik.com",
    "http://localhost:3000",  # for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Spotify credentials from environment variables (safer)
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise RuntimeError("Spotify client ID and secret must be set as environment variables")

# Cache token to avoid requesting every call
_token = None
_token_expiry = 0

def get_spotify_access_token():
    global _token, _token_expiry
    now = time.time()
    if _token and now < _token_expiry:
        return _token

    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to get Spotify token")

    data = response.json()
    _token = data['access_token']
    _token_expiry = now + data['expires_in'] - 60  # Refresh 1 min before expiry
    return _token

@app.get("/search-artists")
def search_artists(q: str = Query(..., min_length=1), limit: int = 10):
    access_token = get_spotify_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": q,
        "type": "artist",
        "limit": limit
    }
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Spotify API error")

    artists = response.json().get("artists", {}).get("items", [])
    return [{"id": artist["id"], "name": artist["name"]} for artist in artists]
