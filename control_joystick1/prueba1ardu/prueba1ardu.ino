#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  Serial.begin(9600);
  servo1.attach(9);  // Ajusta pins según tu conexión
  servo2.attach(10);
  servo3.attach(8);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');  // Leer línea serial
    int values[3] = {90, 90, 90}; // Valores por defecto
    
    int index1 = data.indexOf(',');
    int index2 = data.lastIndexOf(',');

    if (index1 > 0 && index2 > index1) {
      String s1 = data.substring(0, index1);
      String s2 = data.substring(index1 + 1, index2);
      String s3 = data.substring(index2 + 1);

      values[0] = s1.toInt();
      values[1] = s2.toInt();
      values[2] = s3.toInt();

      // Limitar valores a 0-180 grados para seguridad
      for (int i = 0; i < 3; i++) {
        if (values[i] < 0) values[i] = 0;
        if (values[i] > 180) values[i] = 180;
      }

      servo1.write(values[0]);
      servo2.write(values[1]);
      servo3.write(values[2]);
    }
  }
}
