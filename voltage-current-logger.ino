// This is a short arduino program used to log the current and voltage on a microgrid

int voltage_pin = 0;
int currnet_pin = 1;
long t = 0;

void setup() {
  // Start communication with the logger
  Serial.begin(250000);
  // Serial.begin(115200);
}

void loop() {
  t = micros();
  Serial.print(t); // Get timestamp on the measurement
  Serial.print(' ');
  Serial.print(analogRead(voltage_pin)); // Send voltage measurement
   Serial.print(' ');
  // The minus symbol is used to distinguish the volt measurements from the current measurements
  Serial.println(analogRead(1)); // Send current measurement
}
