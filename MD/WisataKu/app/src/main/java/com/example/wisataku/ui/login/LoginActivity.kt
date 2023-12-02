package com.example.wisataku.ui.login

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
import com.example.wisataku.databinding.ActivityLoginBinding
import com.example.wisataku.ui.ViewModelFactory
import com.example.wisataku.ui.main.MainActivity

class LoginActivity : AppCompatActivity() {
    private val viewModel by viewModels<LoginViewModel> {
        ViewModelFactory.getInstance(this)
    }
    private lateinit var binding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
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
//        binding.loginBtn.setOnClickListener {
//            val email = binding.etEmail.text.toString()
//            val password = binding.etPassword.text.toString()
//
//            viewModel.login(email, password)
//
//            viewModel.isError.observe(this) { isError ->
//                viewModel.message.observe(this) { message ->
//                    if (isError == true && message == "Gagal Login") {
//                        AlertDialog.Builder(this).apply {
//                            setTitle("$message")
//                            setMessage("Anda gagal login. Silakan coba lagi.")
//                            setPositiveButton("OK") { _, _ ->
//                                finish()
//                            }
//
//                            show()
//                        }
//                    } else {
//                        AlertDialog.Builder(this).apply {
//                            setTitle("$message")
//                            setMessage("Anda berhasil login. Yuk mulai membagikan cerita Anda!")
//                            setPositiveButton("OK") { _, _ ->
//                                moveActivity()
//                            }
//
//                            show()
//                        }
//                    }
//                }
//            }
//        }
    }

    private fun moveActivity() {
        startActivity(Intent(this, MainActivity::class.java))

        finish()
    }

    private fun playAnimation() {
        ObjectAnimator.ofFloat(binding.ivLogo, View.TRANSLATION_X, -30f, 30f).apply {
            duration = 6000
            repeatCount = ObjectAnimator.INFINITE
            repeatMode = ObjectAnimator.REVERSE
        }.start()

        val title = ObjectAnimator.ofFloat(binding.tvTitle, View.ALPHA, 1f).setDuration(100)
        val desc =
            ObjectAnimator.ofFloat(binding.tvDesc, View.ALPHA, 1f).setDuration(100)
        val emailTextView =
            ObjectAnimator.ofFloat(binding.tvEmail, View.ALPHA, 1f).setDuration(100)
        val emailEditTextLayout =
            ObjectAnimator.ofFloat(binding.etLayoutEmail, View.ALPHA, 1f).setDuration(100)
        val passwordTextView =
            ObjectAnimator.ofFloat(binding.tvPassword, View.ALPHA, 1f).setDuration(100)
        val passwordEditTextLayout =
            ObjectAnimator.ofFloat(binding.etLayoutPassword, View.ALPHA, 1f).setDuration(100)
        val loginButton =
            ObjectAnimator.ofFloat(binding.loginBtn, View.ALPHA, 1f).setDuration(100)

        val together = AnimatorSet().apply {
            playTogether(
                emailTextView,
                emailEditTextLayout,
                passwordTextView,
                passwordEditTextLayout
            )
        }

        AnimatorSet().apply {
            playSequentially(title, desc, loginButton, together)
            start()
        }
    }
}