from gpt import get_written_response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import datetime
import requests

load_dotenv(dotenv_path="config.conf")

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

spotify_device_id = os.getenv("SPOTIFY_DEVICE_ID")

scope = "user-read-playback-state,user-modify-playback-state"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                client_secret=spotify_client_secret,
                                                redirect_uri="http://localhost:8080",
                                                scope=scope))

open_weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
city = "Lyon"

def get_handled_response(transcript):
    response = ""

    if "play" in transcript:
        # if play is the last word
        if transcript.split()[-1] == "play":
            sp.start_playback(device_id=spotify_device_id)
        else:
            sp.search(q=transcript.split("play")[1], limit=1, type="track")
            sp.start_playback(device_id=spotify_device_id)
        response = None
    elif "stop" in transcript or "pause" in transcript:
        sp.pause_playback(device_id=spotify_device_id)
        response = None
    elif "next music" in transcript:
        sp.next_track(device_id=spotify_device_id)
        response = None
    elif "previous music" in transcript:
        sp.previous_track(device_id=spotify_device_id)
        response = None
    elif "music" in transcript:
        current_music = sp.current_playback()
        response = "The playing music is " + current_music["item"]["name"] + " by " + current_music["item"]["artists"][0]["name"]
        
    elif "time" in transcript:
        date = datetime.datetime.now().strftime('%A %B %d, %Y')
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = "We are the " + date + "It is " + time

    elif "weather" in transcript:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=45.76&lon=4.83&appid=" + open_weather_api_key
        res = requests.get(url)
        response = "The weather at " + city + " is " + res.json()["weather"][0]["description"] + " and the temperature is " + str(round(res.json()["main"]["temp"] - 273.15)) + " degrees celsius"

    else:
        response = get_written_response(transcript)
    
    return response