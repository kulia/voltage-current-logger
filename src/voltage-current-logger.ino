// This is a short arduino program used to log the current and voltage on a microgrid

const int voltage_pin = 0;
const int currnet_pin = 1;
long t = 0;
int v = 0;
int i = 0;


void setup() {
  // Start communication with the logger
  Serial.begin(250000);
  // Serial.begin(115200);
}

void loop() {
  t = micros();
  v = analogRead(voltage_pin);
  i = analogRead(currnet_pin);
  Serial.print(t); // Get timestamp on the measurement
  Serial.print(' ');
  Serial.print(v); // Send voltage measurement
  Serial.print(' ');
  // The minus symbol is used to distinguish the volt measurements from the current measurements
  Serial.println(i); // Send current measurement
}
