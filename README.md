# Parcel_Deliver_Detector


For this project, we need:
* An Arduino Uno
* An Ethernet shield 
* A Cat-5 Ethernet cable
* A power adaptor/wall wart/battery pack
* A force-sensing resistor (pressure sensor)
* Wires
* A breadboard
* A 10K ohm resistor
* Your Raspberry Pi control device
* Waterproof casing
* A bin or box to place parcels in

Installation:

![image](https://user-images.githubusercontent.com/115898447/196006784-d976a271-189a-41ba-a641-4c0bd0bb8df9.png)



Run the Arduino sketch (Detected.cpp) to check whether the forced-based resistor 
has enough pressure on it and then triggering an HTTP request.


After writing data to the database, we need to create a small web service that captures the HTTP request and generates a SQL query.


Open control.db in SQLite and run the following query:

> CREATE TABLE Parcel (ID INTEGER PRIMARY KEY AUTOINCREMENT, RoomIDINTEGER, 
DatetimeDATETIME, FOREIGN KEY(RoomID) REFERENCES RoomDetails(ID));


Start the web service by running this expression:
> pythonwebservice.py&
