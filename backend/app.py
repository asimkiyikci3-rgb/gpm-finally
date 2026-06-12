from flask import Flask, jsonify
from mood_service import get_current_mood, get_playlist_for_mood
import yt_dlp
import json

app = Flask(__name__)

# Test müzikleri (YouTube Music'ten çekebilirsin)
TEST_SONGS = [
    {
        "id": "1",
        "title": "Test Song 1",
        "artist": "Artist 1",
        "url": "https://example.com/song1.mp3"
    }
]

@app.route('/api/playlists', methods=['GET'])
def get_playlists():
    """Mevcut mood'a göre playlist döndür"""
    current_mood = get_current_mood()
    playlist_info = get_playlist_for_mood(current_mood)
    
    return jsonify({
        "current_mood": current_mood.value,
        "playlist": playlist_info,
        "songs": TEST_SONGS
    })

@app.route('/api/mood', methods=['GET'])
def get_mood():
    """Sadece mevcut mood'u döndür"""
    current_mood = get_current_mood()
    return jsonify({
        "mood": current_mood.value,
        "playlist_info": get_playlist_for_mood(current_mood)
    })

@app.route('/api/songs', methods=['GET'])
def get_songs():
    """Tüm şarkıları döndür"""
    return jsonify(TEST_SONGS)

@app.route('/health', methods=['GET'])
def health():
    """API sağlık kontrolü"""
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
