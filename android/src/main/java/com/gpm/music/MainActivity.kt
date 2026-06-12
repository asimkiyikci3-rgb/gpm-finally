package com.gpm.music

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainActivity : AppCompatActivity() {
    
    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: PlaylistAdapter
    private val apiClient = ApiClient()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        recyclerView = findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        
        loadPlaylists()
    }
    
    private fun loadPlaylists() {
        apiClient.getPlaylists(object : Callback<List<Playlist>> {
            override fun onResponse(call: Call<List<Playlist>>, response: Response<List<Playlist>>) {
                if (response.isSuccessful) {
                    val playlists = response.body() ?: emptyList()
                    adapter = PlaylistAdapter(playlists)
                    recyclerView.adapter = adapter
                }
            }
            
            override fun onFailure(call: Call<List<Playlist>>, t: Throwable) {
                t.printStackTrace()
            }
        })
    }
}

data class Playlist(
    val id: String,
    val name: String,
    val mood: String,
    val songs: List<Song>
)

data class Song(
    val id: String,
    val title: String,
    val artist: String,
    val url: String
)

class ApiClient {
    private val retrofit = Retrofit.Builder()
        .baseUrl("https://gpm-finally.onrender.com/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()
    
    private val service = retrofit.create(MusicApiService::class.java)
    
    fun getPlaylists(callback: Callback<List<Playlist>>) {
        service.getPlaylists().enqueue(callback)
    }
}

interface MusicApiService {
    @retrofit2.http.GET("api/playlists")
    fun getPlaylists(): Call<List<Playlist>>
}