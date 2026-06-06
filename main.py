from flask import Flask, jsonify, request
from ytmusicapi import YTMusic
import os

app = Flask(__name__)
yt = YTMusic()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    
    query = request.args.get("q") or request.args.get("query")
    if query:
        try:
            
            search_results = yt.search(query, filter="songs")
            
            return jsonify({"tracks": search_results, "status": "ok"}), 200
        except:
            return jsonify({"tracks": [], "status": "ok"}), 200

  
    return jsonify({
        "status": "ok",
        "user": {
            "is_premium": True,
            "name": "GPM Kullanicisi",
            "id": "123456"
        },
        "config": {
            "enable_search": True,
            "enable_explore": True,
            "enable_streaming": True,
            "enable_smart_cards": True,
            "is_internal_user": True
        }
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
