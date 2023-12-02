package com.example.wisataku.ui.register

import androidx.lifecycle.ViewModel
import com.example.wisataku.data.repository.UserRepository

class RegisterViewModel(private val repository: UserRepository) : ViewModel() {

    companion object {
        private const val TAG = "SignupViewModel"
    }
}