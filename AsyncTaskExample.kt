package org.bitsilo.itsilo.arasinqroni

import android.app.ProgressDialog
import android.content.Context
import android.os.AsyncTask
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast


class MainActivity : AppCompatActivity() {

    lateinit var btnGo: Button
    lateinit var context: Context

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnGo = findViewById(R.id.btnGo)
        btnGo.setOnClickListener(View.OnClickListener { view ->  RunSomethingSync().execute() })
        context = this

    }

    inner class RunSomethingSync: AsyncTask<Void, Void, String>() {

        lateinit var progress: ProgressDialog

        override fun onPreExecute() {
            progress = ProgressDialog(context)
            progress.setMessage("Hello")
            progress.setCancelable(false)
            progress.show()
        }

        override fun doInBackground(vararg p0: Void?): String {
            Thread.sleep(10000)
            return ""
        }

        override fun onPostExecute(result: String?) {
            Toast.makeText(baseContext, "Bye",  Toast.LENGTH_LONG).show()
            progress.dismiss()
        }
    }

}
