package com.example.wisataku.di

import android.content.Context
import com.example.wisataku.data.pref.UserPreference
import com.example.wisataku.data.pref.dataStore
import com.example.wisataku.data.repository.UserRepository

object Injection {
    fun provideRepository(context: Context): UserRepository {
        val pref = UserPreference.getInstance(context.dataStore)
//        val user = runBlocking { pref.getUser().first() }
//        val apiService = ApiConfig.getApiService(user.token)

        return UserRepository.getInstance(pref)
//        return StoryRepository.getInstance(apiService, pref)
    }
}