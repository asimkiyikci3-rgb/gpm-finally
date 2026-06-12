from datetime import datetime
from enum import Enum

class Mood(Enum):
    FRIDAY_NIGHT = "friday-night"
    MONDAY_MORNING = "monday-morning"
    NIGHT_CHILL = "night-chill"
    MORNING_ENERGY = "morning-energy"
    LUNCH_BREAK = "lunch-break"
    EVENING_VIBES = "evening-vibes"
    DEFAULT = "default"

def get_current_mood() -> Mood:
    """Günün saati ve gününe göre mood belirle"""
    now = datetime.now()
    hour = now.hour
    day_of_week = now.weekday()  # 0=Monday, 4=Friday, 6=Sunday
    
    # Cuma gecesi (18:00 - 06:00)
    if day_of_week == 4 and hour >= 18:
        return Mood.FRIDAY_NIGHT
    if day_of_week == 5 and hour < 6:  # Cumartesi sabahı 6'den önce
        return Mood.FRIDAY_NIGHT
    
    # Pazartesi sabahı (06:00 - 09:00)
    if day_of_week == 0 and 6 <= hour < 9:
        return Mood.MONDAY_MORNING
    
    # Gece müzikleri (22:00 - 06:00)
    if hour >= 22 or hour < 6:
        return Mood.NIGHT_CHILL
    
    # Sabah enerjisi (06:00 - 09:00)
    if 6 <= hour < 9:
        return Mood.MORNING_ENERGY
    
    # Öğle arası (12:00 - 14:00)
    if 12 <= hour < 14:
        return Mood.LUNCH_BREAK
    
    # Akşam vibes (18:00 - 20:00)
    if 18 <= hour < 20:
        return Mood.EVENING_VIBES
    
    return Mood.DEFAULT

def get_playlist_for_mood(mood: Mood) -> dict:
    """Her mood için özel playlist döndür"""
    playlists = {
        Mood.FRIDAY_NIGHT: {
            "name": "Cuma Gecesi 🎉",
            "description": "Partiye gitmek için müzikler",
            "tempo": "fast",
            "genre": ["dance", "electronic", "pop"]
        },
        Mood.MONDAY_MORNING: {
            "name": "Pazartesi Sabahı ☕",
            "description": "Haftaya enerjik başla",
            "tempo": "moderate",
            "genre": ["pop", "rock", "indie"]
        },
        Mood.NIGHT_CHILL: {
            "name": "Gece Müzikleri 🌙",
            "description": "Sakin ve huzurlu müzikler",
            "tempo": "slow",
            "genre": ["ambient", "lo-fi", "soul"]
        },
        Mood.MORNING_ENERGY: {
            "name": "Sabah Enerjisi ⚡",
            "description": "Güne iyi başla",
            "tempo": "fast",
            "genre": ["pop", "dance", "electronic"]
        },
        Mood.LUNCH_BREAK: {
            "name": "Öğle Arası 🍽️",
            "description": "Hafif ve keyifli müzikler",
            "tempo": "moderate",
            "genre": ["jazz", "pop", "indie"]
        },
        Mood.EVENING_VIBES: {
            "name": "Akşam Atmosferi 🌅",
            "description": "Günün sonuna uygun müzikler",
            "tempo": "moderate",
            "genre": ["soul", "rnb", "indie"]
        },
        Mood.DEFAULT: {
            "name": "Müzik Kütüphanesi 🎵",
            "description": "Tüm müzikler",
            "tempo": "mixed",
            "genre": ["all"]
        }
    }
    return playlists.get(mood, playlists[Mood.DEFAULT])
