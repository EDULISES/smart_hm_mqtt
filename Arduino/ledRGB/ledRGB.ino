#define pinR 3
#define pinG 5
#define pinB 6

void setColor(byte color[]);

void setup() {
  Serial.begin(115200);
}

void loop() {
  byte color[3];
  color[0] = 100;
  color[1] = 157;
  color[2] = 225;
  setColor(color);
}

void setColor(byte color[]){
  analogWrite(pinB, color[0]);
  analogWrite(pinG, color[1]);
  analogWrite(pinR, color[2]);
}


