# GPM - Google Play Music Reborn 🎵

Eski Google Play Music'i yeniden canlandıran Android uygulaması!

## Özellikler

✅ **Mood-Based Playlists**
- Cuma Gecesi 🎉 (18:00+)
- Pazartesi Sabahı ☕ (06:00-09:00)
- Gece Müzikleri 🌙 (22:00-06:00)
- Sabah Enerjisi ⚡ (06:00-09:00)
- Öğle Arası 🍽️ (12:00-14:00)
- Akşam Atmosferi 🌅 (18:00-20:00)

✅ **Kendi Sunucudan Müzik Çalma**
- Google bağımlılığı yok
- YouTube Music API entegrasyonu
- Nuvider/Render'de barındırılan API

✅ **MediaPlayer Desteği**
- Oynat / Duraklat / Devam Et
- İleri / Geri sarma
- Şarkı sırası

## Kurulum

### Backend (Render)

```bash
pip install flask yt-dlp
python backend/app.py
```

API: `https://gpm-finally.onrender.com`

### Android App

```bash
./gradlew build
./gradlew installDebug
```

## API Endpoints

- `GET /api/playlists` - Mevcut mood'a göre playlist
- `GET /api/mood` - Sadece mood bilgisi
- `GET /api/songs` - Tüm şarkılar
- `GET /health` - API durumu

## Teknoloji

- **Android**: Kotlin, Jetpack
- **Backend**: Python, Flask
- **Sunucu**: Render / Nuvider
- **Müzik**: YouTube Music API

---

**Kodlayan:** asimkiyikci3-rgb
**Başlangıç:** 2026-06-12
