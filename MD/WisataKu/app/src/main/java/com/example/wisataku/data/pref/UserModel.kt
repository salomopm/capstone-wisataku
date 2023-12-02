package com.example.wisataku.data.pref

data class UserModel(
    val email: String,
    val token: String,
    val isLogin: Boolean = false
)

//data class User(
//    val name: String,
//    val email: String,
//    val password: String
//)