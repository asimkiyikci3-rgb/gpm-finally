package com.gpm.music

import android.app.Service
import android.content.Intent
import android.media.MediaPlayer
import android.os.Binder
import android.os.IBinder
import java.util.*

class MusicService : Service() {
    
    private var mediaPlayer: MediaPlayer? = null
    private val binder = LocalBinder()
    private var currentSongUrl: String? = null
    
    inner class LocalBinder : Binder() {
        fun getService(): MusicService = this@MusicService
    }
    
    override fun onBind(intent: Intent): IBinder {
        return binder
    }
    
    fun playSong(url: String) {
        try {
            mediaPlayer?.release()
            mediaPlayer = MediaPlayer().apply {
                setDataSource(url)
                prepare()
                start()
            }
            currentSongUrl = url
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    
    fun pauseSong() {
        mediaPlayer?.pause()
    }
    
    fun resumeSong() {
        mediaPlayer?.start()
    }
    
    fun stopSong() {
        mediaPlayer?.stop()
        mediaPlayer?.release()
        mediaPlayer = null
    }
    
    // Mood-based playlist logic
    fun getMoodBasedPlaylist(): String {
        val calendar = Calendar.getInstance()
        val hour = calendar.get(Calendar.HOUR_OF_DAY)
        val dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK)
        
        return when {
            dayOfWeek == Calendar.FRIDAY && hour >= 18 -> "friday-night"
            dayOfWeek == Calendar.MONDAY && hour in 6..9 -> "monday-morning"
            hour in 22..23 || hour in 0..6 -> "night-chill"
            hour in 6..9 -> "morning-energy"
            hour in 12..14 -> "lunch-break"
            hour in 18..20 -> "evening-vibes"
            else -> "default"
        }
    }
    
    override fun onDestroy() {
        super.onDestroy()
        mediaPlayer?.release()
    }
}