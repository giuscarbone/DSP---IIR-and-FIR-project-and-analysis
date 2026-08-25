#include <Ticker.h>

#define ADC_PIN 34

Ticker ticker; //ticker: executes a function with a precise frequency
double ts = 0.03125;

volatile bool flag = false; //volatile cause modified in ISR
volatile int counter = 0;

void ISR_function(){ //defining the ISR function
  flag = true;
  counter++;
}

void setup() {
  delay(10000);
  Serial.begin(115200);
  pinMode(ADC_PIN, INPUT);
  analogSetAttenuation(ADC_11db);

  ticker.attach(ts, ISR_function); //initializing ticker
  
  Serial.println("time,x");

}

void loop() {
  if(flag){
    double value = analogRead(ADC_PIN);
    Serial.print(counter * ts, 5);
    Serial.print(",");
    Serial.println(value);
    flag = false;
  }
}
