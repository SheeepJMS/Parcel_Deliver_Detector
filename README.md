# Parcel_Deliver_Detector


There are three parts of the projects.
1. Pressure detected via pressure sensors and ADC.
2. Publish a MQTT message to IFTTT and get email alert.
3. Face-detection and save the picture of who is delivering the package.

For this project, we need:
* A power adaptor/wall wart/battery pack
* A force-sensing resistor (pressure sensor)
* Wires
* MCP3008 chip
* A breadboard
* A 10K ohm resistor
* Your Raspberry Pi control device
* Waterproof casing
* A bin or box to place parcels in
* A USB Camera or Rasp-Cam

## Servo wiring:

![image](https://user-images.githubusercontent.com/115898447/196816115-8a3e8d7d-0d9f-422e-b5d5-22a122689bcb.png)

Common servo wire colors are as follows:
* The brown or black wire connects to GND
* The red wire connects to +5-volts
* The orange, yellow, white, or blue wire is the signal/PWM input wire that connects to a GPIO pin

## Pressure Sensor wiring:

![image](https://user-images.githubusercontent.com/115898447/196816190-d0ecf7e3-cedf-4706-a54b-ea895c1eb9e4.png)

The analog to digital converter code is pretty straightforward, and the tricky part is receiving the value from the MCP3008 chip. 


## IFTTT configuration:

1. Get your key on IFTTT website

![image](https://user-images.githubusercontent.com/115898447/196817223-de87aa8a-3165-4b9e-8cd9-ef565bcfa934.png)

2. Choose a trigger of Webhooks to receive a web request

![image](https://user-images.githubusercontent.com/115898447/196817366-29cef160-89e6-4f47-b788-42ef04120169.png)

3. Set event Name as the one in your code:RPIPressure

![image](https://user-images.githubusercontent.com/115898447/196817995-565cf0b0-cc9a-4340-801f-935a00b07efa.png)

4.Set the Email alert

![image](https://user-images.githubusercontent.com/115898447/196818047-7a375b01-c39e-45d4-9659-8eefb8689df8.png)


Finally, run the Parcel_Detector_EmailAlert!


