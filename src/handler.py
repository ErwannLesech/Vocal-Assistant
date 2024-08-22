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

def list_devices():
    devices = sp.devices()
    if devices['devices']:
        return [device['id'] + ": " + device['name'] for device in devices['devices']]
    else:
        return ["No devices found"]

def play_music():
    try:
        sp.start_playback(device_id=spotify_device_id)
    except spotipy.exceptions.SpotifyException as e:
        return f"Error playing music: {e}"

def pause_music():
    try:
        sp.pause_playback(device_id=spotify_device_id)
    except spotipy.exceptions.SpotifyException as e:
        return f"Error pausing music: {e}"

def next_track():
    try:
        sp.next_track(device_id=spotify_device_id)
    except spotipy.exceptions.SpotifyException as e:
        return f"Error skipping to next track: {e}"

def previous_track():
    try:
        sp.previous_track(device_id=spotify_device_id)
    except spotipy.exceptions.SpotifyException as e:
        return f"Error going back to previous track: {e}"

def get_current_song():
    try:
        current_track = sp.current_playback()
        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            return f"Currently playing '{track_name}' by {artist_name}"
        else:
            return "No music is currently playing"
    except spotipy.exceptions.SpotifyException as e:
        return f"Error getting current song: {e}"

def get_handled_response(transcript):
    response = ""
    
    if "time" in transcript:
        date = datetime.datetime.now().strftime('%A %B %d, %Y')
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"We are on {date}. It is {time}."

    elif "weather" in transcript:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_api_key}"
        res = requests.get(url)
        weather_data = res.json()
        description = weather_data["weather"][0]["description"]
        temperature = round(weather_data["main"]["temp"] - 273.15)
        response = f"The weather in {city} is {description} and the temperature is {temperature} degrees Celsius."

    elif "play" in transcript:
        response = play_music()

    elif "pause" in transcript or "stop" in transcript:
        response = pause_music()

    elif "next" in transcript:
        response = next_track()

    elif "previous" in transcript:
        response = previous_track()

    elif "music" in transcript:
        response = get_current_song()
    
    else:
        response = get_written_response(transcript)
    
    return response