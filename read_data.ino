#include<Servo.h>                                            //Importing servo motor library.
#include <ThingSpeak.h>                                      //Importing ThingSpeak library.
#include <ESP8266WiFi.h>                                     // Importing esp8266 library.


const char* ssid = "Your WiFi User Name";                      //Write your WiFi name here.
const char* pass = "Your WiFi Password";                       //Write your WiFi password here.

char* server = "api.thingspeak.com";                          //ThingSpeak server address.
unsigned long channelID =  Your ThingSpeak channel id;        //Your ThingSpeak channel Id.
const char* readAPIKey = "Your channel read API key";         //Your Thingspeak channel read key.

const int field1 = 1;                                          //Declaring field1 equal to ThingSpeak channel field1 and as a constant integer value.
const int field2 = 2;                                          //Declaring field2 equal to ThingSpeak channel field2 and as a constant integer value.
const int field3 = 3;                                          //Declaring field3 equal to ThingSpeak channel field3 and as a constant integer value.
const int field4 = 4;                                          //Declaring field4 equal to ThingSpeak channel field4 and as a constant integer value.
const int field5 = 5;                                          //Declaring field5 equal to ThingSpeak channel field5 and as a constant integer value.

const int inputPin1  = 16;                                     //Declaring inputPin1 as a constant integer and making it read values comming from GPIO Pin 16 of node mcu.
const int inputPin2  = 5;                                      //Declaring inputPin2 as a constant integer and making it read values comming from GPIO Pin 5 of node mcu.

const int inputPin3  = 0;                                      //Declaring inputPin3 as a constant integer and making it read values comming from GPIO Pin 0 of node mcu.
const int inputPin4  = 2;                                      //Declaring inputPin4 as a constant integer and making it read values comming from GPIO Pin 2 of node mcu.

const int red = 14;                                            //Declaring red as a constant integer and making it read values comming from GPIO Pin 14 of node mcu.
const int blue = 12;                                           //Declaring blue as a constant integer and making it read values comming from GPIO Pin 12 of node mcu.
const int green = 13;                                          //Declaring green as a constant integer and making it read values comming from GPIO Pin 13 of node mcu.
int i = 0;                                                     //Declaring i as a integer and equal to 0.
int led1 = 4;                                                  //Declaring led1 as a constant integer and making it read values comming from GPIO Pin 4 of node mcu.                                                     

Servo servo_1;                                                 //Declaring name of the servo as servo_1.
WiFiClient client;                                             //Initializing WiFi as a client.

void setup() {
// put your setup code here, to run once:
pinMode(inputPin1, OUTPUT);                                     // Declaring inputPin1 as a OUTPUT Pin.           
pinMode(inputPin2, OUTPUT);                                     // Declaring inputPin2 as a OUTPUT Pin. 
pinMode(inputPin3, OUTPUT);                                     // Declaring inputPin3 as a OUTPUT Pin. 
pinMode(inputPin4, OUTPUT);                                     // Declaring inputPin4 as a OUTPUT Pin. 
pinMode(red, OUTPUT);                                           // Declaring red as a OUTPUT Pin. 
pinMode(blue, OUTPUT);                                          // Declaring blue as a OUTPUT Pin. 
pinMode(green, OUTPUT);                                         // Declaring green as a OUTPUT Pin. 
pinMode(led1, OUTPUT);                                          // Declaring led1 as a OUTPUT Pin. 

servo_1.attach(15);                                             //Attaching servo to GPIO pin 15 of node mcu.

digitalWrite(inputPin3, HIGH);                                  // Making inputpin3 as HIGH.
digitalWrite(inputPin4, HIGH);                                  // Making inputpin4 as HIGH.
digitalWrite(inputPin1, HIGH);                                  // Making inputpin1 as HIGH.
digitalWrite(inputPin2, HIGH);                                  // Making inputpin2 as HIGH.
delay(100);
digitalWrite(red, HIGH);                                         // Making red as HIGH.
digitalWrite(blue, HIGH);                                        // Making red as HIGH. 
digitalWrite(green, HIGH);                                       // Making red as HIGH.
 

ThingSpeak.begin(client);                                         // Declaring ThingSpeak as a client.
Serial.begin(115200);                                             // Making read and write speed on Serial equal to 115200 hz.                
delay(10);
Serial.println("CONNECTING TO ");                                 // Making our nodemcu to connect with wifi.    
Serial.println(ssid);

WiFi.begin(ssid, pass);

while (WiFi.status() != WL_CONNECTED)
{
  delay(500);
  Serial.print(".");
}
Serial.print("");
Serial.println("WiFi Connected");


if (WiFi.status() == WL_CONNECTED)
{
digitalWrite(led1, HIGH);                                          // If our node mcu will connect to WiFi then a led attached to GPIO pin 4 will glow up.        
}

delay(1000);
}


void loop() {
  // put your main code here, to run repeatedly:

  delay(6000);                                                                                   //After a loop is completed the we are making a delay of 6 seconds because our ThingSpeak server use to take some time to update itself.
  Serial.print("\n Fetching values from ThingSpeak server.........");
  long fieldone = ThingSpeak.readLongField(channelID, field1 ,  readAPIKey);                     // Fetching value from ThingSpeak server for field1 and making it equal to fieldone. 
  long fieldtwo = ThingSpeak.readLongField(channelID, field2 ,  readAPIKey);                     // Fetching value from ThingSpeak server for field2 and making it equal to fieldtwo. 
  long fieldthree = ThingSpeak.readLongField(channelID, field3 ,  readAPIKey);                   // Fetching value from ThingSpeak server for field3 and making it equal to fieldthree. 
  long fieldfour = ThingSpeak.readLongField(channelID, field4 ,  readAPIKey);                    // Fetching value from ThingSpeak server for field4 and making it equal to fieldfour. 
  long fieldfive = ThingSpeak.readLongField(channelID, field5 ,  readAPIKey);                    // Fetching value from ThingSpeak server for field5 and making it equal to fieldfive. 
  
  fieldfour = fieldfour * 1000;                                                                  // Multiplying the value coming from fieldfour with 1000 because in arduino time is written in milliseconds. 
  
  Serial.print("\n Value from field 1 : ");                                                      // Printing field1 value.
  Serial.print(fieldone);
  Serial.print("\n Value from field 2 : ");                                                       // Printing field2 value.
  Serial.print(fieldtwo);
  Serial.print("\n Value from field 3 : ");                                                      // Printing field3 value.
  Serial.print(fieldthree);
  Serial.print("\n Value from field 4 : ");                                                       // Printing field4 value.
  Serial.print(fieldfour);
  Serial.print("\n Value from field 5 : ");                                                       // Printing field5 value.
  Serial.print(fieldfive); 

// Motor values  

if(fieldone == 1  && fieldfour == 0){                                                             // fieldone will denote the rotation values of motor i.e a motor will move in clockwise or anticlockwise direction or it has to stop 
   digitalWrite(inputPin3, HIGH);                                                                 // fieldone = 1 means that motor should move in clockwise direction.
   delay(10);                                                                                     // fieldone = 2 means that motor should move in anticlockwise direction.
   digitalWrite(inputPin4, HIGH);                                                                 // fieldone = 3 means that motor should stop.
   delay(200);                                                                                    
   digitalWrite(inputPin1, LOW);                                                                  // fieldfour will denote the delay time i.e. for how much time a led or motor should run. 
   digitalWrite(inputPin2, LOW);                                                                   // If a user want to run a led or motor continously then he/she will give delay time = 0.
}
  
else if(fieldone == 1 && fieldfour > 0 )
  {
   digitalWrite(inputPin3, HIGH); 
   delay(10);
   digitalWrite(inputPin4, HIGH);
   delay(200); 
   digitalWrite(inputPin1, LOW);
   digitalWrite(inputPin2, LOW);
   delay(fieldfour);  
   digitalWrite(inputPin1, HIGH);
   digitalWrite(inputPin2, HIGH);
   }

else if(fieldone == 2 && fieldfour > 0){
    digitalWrite(inputPin1, HIGH);
    delay(10);
    digitalWrite(inputPin2, HIGH); 
    delay(200);
   digitalWrite(inputPin3, LOW); 
   digitalWrite(inputPin4, LOW); 
   delay(fieldfour); 
   digitalWrite(inputPin3, HIGH); 
   digitalWrite(inputPin4, HIGH); 
  }

else if(fieldone == 2 && fieldfour == 0){
  digitalWrite(inputPin1, HIGH);
    delay(10);
    digitalWrite(inputPin2, HIGH); 
    delay(200);
   digitalWrite(inputPin3, LOW); 
   delay(10);
   digitalWrite(inputPin4, LOW);
}
  else if(fieldone == 3){
    digitalWrite(inputPin3, HIGH); 
   digitalWrite(inputPin4, HIGH); 
   digitalWrite(inputPin1, HIGH);
    digitalWrite(inputPin2, HIGH); 
  }

// Lights control

if(fieldtwo == 1 && fieldfour > 0)                                 // fieldtwo denotes values for led's i.e. for different values of fieldfour different colour of led will glow up 
{                                                                  // fieldfour will denote the delay time i.e. for how much time a led or motor should run.
    digitalWrite(blue, HIGH);                                      // If a user want to run a led or motor continously then he/she will give delay time = 0.
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    delay(fieldfour);
    digitalWrite(red, HIGH);
  }
else if(fieldtwo == 1 && fieldfour == 0 )
{
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
}
  else if(fieldtwo == 2 && fieldfour > 0)
  {
    digitalWrite(red, HIGH);
    digitalWrite(green, HIGH);
    digitalWrite(blue, LOW);
    delay(fieldfour);
    digitalWrite(blue, HIGH);
  }
else if(fieldtwo == 2 && fieldfour == 0)
  {
    digitalWrite(red, HIGH);
    digitalWrite(green, HIGH);
    digitalWrite(blue, LOW);
    
} 
else if(fieldtwo == 3 && fieldfour > 0)
 {
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green, LOW);
    delay(fieldfour);
    digitalWrite(green, HIGH);
}
else if(fieldtwo == 3 && fieldfour == 0)
 {
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green, LOW);
}
  else if(fieldtwo == 4 && fieldfour > 0)
  {
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    digitalWrite(green, LOW);
    delay(fieldfour);
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
  }
else if(fieldtwo == 4 && fieldfour == 0)
  {
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    digitalWrite(green, LOW);
  }
else if(fieldtwo == 5 && fieldfour >0)
{
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    delay(fieldfour);
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    
}
else if(fieldtwo == 5 && fieldfour == 0)
{
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    
}
else if(fieldtwo == 6 && fieldfour > 0)
{
    digitalWrite(red, HIGH);
    digitalWrite(blue, LOW);
    digitalWrite(green,LOW);
    delay(fieldfour);
    digitalWrite(blue, HIGH);
    digitalWrite(green,HIGH);
  }
else if(fieldtwo == 6 && fieldfour == 0)
{
    digitalWrite(red, HIGH);
    digitalWrite(blue, LOW);
    digitalWrite(green,LOW);
}
else if(fieldtwo == 7 && fieldfour > 0)
{
    digitalWrite(blue, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
    delay(fieldfour);
    digitalWrite(red, HIGH);
    digitalWrite(green, HIGH);
}
else if(fieldtwo == 7 && fieldfour == 0)
{
    digitalWrite(blue, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
  }
else if(fieldtwo == 8){
    digitalWrite(red, HIGH);
  }
else if(fieldtwo == 9){
    digitalWrite(blue,HIGH);
  }
else if(fieldtwo == 10){
    digitalWrite(green, HIGH);
  }
else if(fieldtwo == 11){
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
  }
  else if(fieldtwo == 12){
    digitalWrite(red, HIGH);
    digitalWrite(blue,HIGH);
  }
  else if(fieldtwo == 13){
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
  }
  else if(fieldtwo == 14){
    digitalWrite(red, HIGH);
    digitalWrite(green, HIGH);
  }
  else if(fieldtwo == 15){
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green,HIGH);
  }

// Servo motor control

if(fieldthree >= 1 && fieldfour > 0 && fieldfive > 0)                                  //fieldthree denotes values for servo motor controlling.
{ 
  for(i=1; i<=fieldfive; i++)                                                          // fieldfive will denote that for how many times you want to run a process.
  {                                                                                    // fieldfour will denote the delay time i.e. for how much time a led or motor should run.
  Serial.print("\n loop has started");                                                 // If a user want to run a led, motor or servo motor continously then he/she will give delay time = 0.
  servo_1.write(0);
  delay(fieldfour);
  servo_1.write(fieldthree);
  delay(fieldfour);
}
}
else if(fieldthree >= 1 && fieldfour == 0 && fieldfive == 0)
{ 

  Serial.print("\n loop 2 has started");
  servo_1.write(0);
  delay(1000);
  servo_1.write(fieldthree);
  delay(1000);
}
}
