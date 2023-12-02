package com.example.wisataku.data.repository

import com.example.wisataku.data.pref.UserModel
import com.example.wisataku.data.pref.UserPreference
import kotlinx.coroutines.flow.Flow

class UserRepository private constructor(
    private val userPreference: UserPreference,
//    private val apiService: ApiService?
) {
//    fun register(name: String, email: String, password: String) {
//        apiService?.register(name, email, password)
//    }

//    suspend fun saveSession(user: UserModel) {
//        userPreference.saveSession(user)
//    }

    fun getSession(): Flow<UserModel> {
        return userPreference.getSession()
    }

    suspend fun logout() {
        userPreference.logout()
    }

    companion object {
        @Volatile
        private var instance: UserRepository? = null
        fun getInstance(
            userPreference: UserPreference,
        ): UserRepository =
            instance ?: synchronized(this) {
                instance ?: UserRepository(userPreference)
//                instance ?: UserRepository(userPreference, apiService = null)
            }.also { instance = it }
    }
}