package com.example.wisataku.ui.register

import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.content.Intent
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.WindowInsets
import android.view.WindowManager
import androidx.activity.viewModels
import androidx.appcompat.app.AlertDialog
import com.example.wisataku.databinding.ActivityRegisterBinding
import com.example.wisataku.ui.ViewModelFactory
import com.example.wisataku.ui.login.LoginActivity

class RegisterActivity : AppCompatActivity() {
    private val viewModel by viewModels<RegisterViewModel> {
        ViewModelFactory.getInstance(this)
    }
    private lateinit var binding: ActivityRegisterBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityRegisterBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setupView()
        setupAction()
        playAnimation()
    }

    private fun setupView() {
        @Suppress("DEPRECATION")
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            window.insetsController?.hide(WindowInsets.Type.statusBars())
        } else {
            window.setFlags(
                WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN
            )
        }
        supportActionBar?.hide()
    }

    private fun setupAction() {
//        binding.registerBtn.setOnClickListener {
//            val name = binding.etName.text.toString()
//            val email = binding.etEmail.text.toString()
//            val password = binding.etPassword.text.toString()
//
//            viewModel.register(name, email, password)
//
//            viewModel.isError.observe(this) { isError ->
//                viewModel.message.observe(this) { message ->
//                    if (isError == true && message == "Gagal Mendaftar") {
//                        AlertDialog.Builder(this).apply {
//                            setTitle("$message")
//                            setMessage("Anda gagal mendaftar. Silakan coba lagi.")
//                            setPositiveButton("OK") { _, _ ->
//                                finish()
//                            }
//
//                            show()
//                        }
//                    } else {
//                        AlertDialog.Builder(this).apply {
//                            setTitle("$message")
//                            setMessage("Anda berhasil mendaftar. Yuk lanjut login!")
//                            setPositiveButton("OK") { _, _ ->
//                                moveActivity()
//                            }
//
//                            show()
//                        }
//                    }
//                }
//            }
//
        //            viewModel.signUp(name, email, password).observe(this) { result ->
//                if (result != null) {
//                    when (result) {
//                        is ResultState.Loading -> {
//                            showLoading(true)
//                        }
//
//                        is ResultState.Success -> {
//                            showToast(result.data.message)
//                            showLoading(false)
//                        }
//
//                        is ResultState.Error -> {
//                            showToast(result.error)
//                            showLoading(false)
//                        }
//                    }
//                }
//            }
//        }
    }

//    private fun moveActivity() {
//        startActivity(Intent(this, LoginActivity::class.java))
//
//        finish()
//    }

    private fun playAnimation() {
        ObjectAnimator.ofFloat(binding.ivLogo, View.TRANSLATION_X, -30f, 30f).apply {
            duration = 6000
            repeatCount = ObjectAnimator.INFINITE
            repeatMode = ObjectAnimator.REVERSE
        }.start()

        val title = ObjectAnimator.ofFloat(binding.tvTitle, View.ALPHA, 1f).setDuration(100)
        val tvDesc = ObjectAnimator.ofFloat(binding.tvDesc, View.ALPHA, 1f).setDuration(100)
        val nameTextView =
            ObjectAnimator.ofFloat(binding.tvName, View.ALPHA, 1f).setDuration(100)
        val nameEditTextLayout =
            ObjectAnimator.ofFloat(binding.etLayoutName, View.ALPHA, 1f).setDuration(100)
        val emailTextView =
            ObjectAnimator.ofFloat(binding.tvEmail, View.ALPHA, 1f).setDuration(100)
        val emailEditTextLayout =
            ObjectAnimator.ofFloat(binding.etLayoutEmail, View.ALPHA, 1f).setDuration(100)
        val passwordTextView =
            ObjectAnimator.ofFloat(binding.tvPassword, View.ALPHA, 1f).setDuration(100)
        val passwordEditTextLayout =
            ObjectAnimator.ofFloat(binding.etLayoutPassword, View.ALPHA, 1f).setDuration(100)
        val registerButton =
            ObjectAnimator.ofFloat(binding.registerBtn, View.ALPHA, 1f).setDuration(100)

        val together = AnimatorSet().apply {
            playTogether(
                nameTextView,
                nameEditTextLayout,
                emailTextView,
                emailEditTextLayout,
                passwordTextView,
                passwordEditTextLayout
            )
        }

        AnimatorSet().apply {
            playSequentially(title, tvDesc, registerButton, together)
            start()
        }
    }
}