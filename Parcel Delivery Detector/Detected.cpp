#include <SPI.h>
#include <Ethernet.h>
#define THRESHOLD 400

unsigned char fsr = 0; //The sensor pin
int check_pressure = 0;
int room = 2;

boolean is_delivered = true;
boolean email_sent = false;

byte mac[] = { 0xDE, 0xAD, 0xBB, 0xEF, 0xFE, 0xED };
char server[] = "192.168.3.4";
IPAddress ip(192,168,3,6);
EthernetClient client;



void setup() {
 Serial.begin(9600);
 Ethernet.begin(mac, ip);
 pinMode(fsr, INPUT);
}


void loop() 
{
 
 check_pressure = analogRead(fsr); 
 Serial.println(check_pressure);
 
 if(is_delivered) {
	if(check_pressure > THRESHOLD) {
		is_delivered = true;
 
			if(!email_sent){ 
			notify_parcel();
			}
 
		email_sent = true;
		}
	} else {
		if(check_pressure < THRESHOLD) {
			is_delivered = false; //reset system.
			email_sent = false;
			Serial.println(is_delivered);
		} 
	}
}

void notify_parcel() {
 //update raspberry Pi
 String data = "{\"room\":";
 data += room;
 data += "}";
 if (client.connect(server, 8081)) {
 Serial.println("connected");
 client.println("POST / HTTP/1.1");
 client.println("Host: 192.168.3.6");
 client.println("Content-Type: application/json;charset=utf-8");
 client.print("Content-Length: ");
 client.println(data.length());
 client.println();
 client.println(data);
 client.println("Connection: close");
 client.println();
 } 
 else {
 Serial.println("connection failed");
 } 
}
