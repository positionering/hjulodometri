#include <Time.h>
float v_right = 0;
float v_left = 0;
float to_left = millis(); // "old time"
float to_right = millis();  
float dist_pp = 0.55*3.1415926535/29;

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  pinMode(2, INPUT_PULLUP);           // set pin to input
  pinMode(3, INPUT_PULLUP);           // set pin to input
  attachInterrupt(digitalPinToInterrupt(2), updateright, RISING);
  attachInterrupt(digitalPinToInterrupt(3), updateleft, RISING);
 
}


void loop() {
  // put your main code here, to run repeatedly:

  //Serial.println("Left        Right");
  //Serial.print(v_left);
  //Serial.print(" ");
  //Serial.print(v_right);
  //Serial.print("\n");
  //String s = (String) v_left + " " + v_right + " 00000000000000000000000000000000000000000000000000000000";
  String s = (String) v_left + " " + v_right;
  Serial.println(s);
  //Serial.print("        ");
  //Serial.print(v_right);
  //Serial.println("");

  if (millis() - to_left > 1000){
    v_left = 0;
  }

  if (millis() - to_right > 1000){
    v_right = 0;
  }

}

void updateleft(){
  float tc_left = millis();
  float current_mean_v_left = dist_pp/(tc_left - to_left)*1000*3.6;
  to_left = tc_left;

  v_left = current_mean_v_left;
  
}

void updateright(){
  float tc_right = millis();
  float current_mean_v_right = dist_pp/(tc_right - to_right)*1000*3.6;
  to_right = tc_right;

  v_right = current_mean_v_right;
}
