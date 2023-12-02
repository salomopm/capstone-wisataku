package com.example.wisataku.ui.login

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.wisataku.data.pref.UserModel
import com.example.wisataku.data.repository.UserRepository
import kotlinx.coroutines.launch

class LoginViewModel(private val repository: UserRepository) : ViewModel() {
//    private val _isError = MutableLiveData<Boolean?>()
//    val isError: MutableLiveData<Boolean?> = _isError
//
//    private val _message = MutableLiveData<String?>()
//    val message: LiveData<String?> = _message

    companion object {
        private const val TAG = "SigninViewModel"
    }

    //    fun signUp(
//        name: String,
//        email: String,
//        password: String
//    ) {
//        viewModelScope.launch {
//            repository.register(name, email, password)
//        }
//    }

//    fun signUp(
//        name: String,
//        email: String,
//        password: String
//    ) = repository.register(name, email, password)

//    fun login(
//        email: String,
//        password: String
//    ) {
//        val client = ApiConfig.getApiService().login(email, password)
//        client.enqueue(object : Callback<LoginResponse> {
//            override fun onResponse(
//                call: Call<LoginResponse>,
//                response: Response<LoginResponse>
//            ) {
//                if (response.isSuccessful) {
//                    val token = response.body()!!.loginResult.token
//                    _isError.value = response.body()?.error
//                    _message.value = response.body()?.message
//                    saveSession(UserModel(email, token))
//                } else {
//                    _isError.value = true
//                    _message.value = "Gagal Login"
//                }
//            }
//
//            override fun onFailure(call: Call<LoginResponse>, t: Throwable) {
//                Log.e(TAG, "onFailure: ${t.message.toString()}")
//            }
//        })
//    }

//    fun saveSession(user: UserModel) {
//        viewModelScope.launch {
//            repository.saveSession(user)
//        }
//    }
}