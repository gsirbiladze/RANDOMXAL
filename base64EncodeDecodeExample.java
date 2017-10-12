
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private Button btnEncode;
    private Button btnDecode;

    private EditText etPlane;
    private EditText etCoded;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnEncode = (Button) findViewById(R.id.btnEncode);
        btnDecode = (Button) findViewById(R.id.btnDecode);

        etPlane = (EditText) findViewById(R.id.etPlane);
        etCoded = (EditText) findViewById(R.id.etCoded);

        btnEncode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                encodePlaneText();
            }
        });

        btnDecode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                decodeBase64Text();
            }
        });

    }

    protected void encodePlaneText(){
        try {
            etCoded.setText(Base64.encodeToString(etPlane.getText().toString().getBytes("UTF-8"), Base64.NO_WRAP | Base64.URL_SAFE));

        }
        catch (Exception e){
            Toast.makeText(this, "Error During Encryption ...", Toast.LENGTH_LONG).show();
        }


    }

    protected void decodeBase64Text(){
        try {
            byte[] decrData = Base64.decode(etCoded.getText().toString(), Base64.NO_WRAP | Base64.URL_SAFE);
            String decrString = new String(decrData, "UTF-8");
            etPlane.setText(decrString);
        }
        catch (Exception e){
            Toast.makeText(this, "Error During Decryption ...", Toast.LENGTH_LONG).show();
        }

    }

}
