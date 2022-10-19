

import spidev
from datetime import datetime
from time import sleep
import requests
import logging
from SimpleCV import Camera, Display
from time import sleep
import servo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



POLL_INTERVAL_SECS = 60*10  # 10 Minutes

#Define Variables
delay = 0.5
pad_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

# IFTTT Configuration
EVENT = "RPIPressure" # <<<< Add your IFTTT Event name                                      
API_KEY = "<ADD YOUR IFTTT API KEY HERE>" # <<<< Add your IFTTT API Key


# At what high pressure will we send an email
HIGH_PRESSURE_TRIGGER = 20 #   

# To track when a high pressure event has been triggered
triggered_high = False


# Configuration check
if not EVENT or not API_KEY:
  print("\nCONFIGURATION REQUIRED\nPlease update {} and add your EVENT name and API_KEY\n".format(__file__))
  quit(1)


# Create the IFTTT Webhook URL
URL = "https://maker.ifttt.com/trigger/{}/with/key/{}".format(EVENT, API_KEY)               

# HTTP headers used with Webhook request.
REQUEST_HEADERS = {"Content-Type": "application/json"}


#camera configuration
myCamera = Camera(prop_set={'width':320, 'height': 240})
myDisplay = Display(resolution=(320, 240))


#read pressure data via ADC
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def send_ifttt_event(pressure, message):
    """ Call the IFFF Webhook URL """

    # In IFTTT, the dict/JSON key names must be value1
    data = {
      "value1": result['temp_c'],
      "value2": message
    }

    # Make IFTTT request - it can be either a HTTP GET or POST
    response = requests.post(URL, headers=REQUEST_HEADERS, params=data)

    # IFTTT Response is plain text
    logger.info("Response {}".format(response.text))

    if response.status_code == requests.codes.ok:
        logger.info("Successful Request.")
    else:
        logger.info("Unsuccessful Request. Code:{}".format(response.status_code))


if __name__ == "__main__":

    try:
        logger.info("Press Control + C To Exit.")

        while True:
            try:
                while True:
                    pad_value = readadc(pad_channel)
                    print("---------------------------------------")
                    print("Pressure Pad Value: %d" % pad_value)
                    time.sleep(delay)
                    
                
                result = dht.read(retries=5) # Singe data read (faster)
                #result = dht.sample()       # Multiple data reads, then take mean (slower)

            except Exception as e:
                # Failed to get reading from sensor
                logger.error("Failed to read sensor. Error: {}".format(e), exc_info=True)
                continue

            if not pad_value['valid']:
                # We got a reading, but it has failed a checksum test
                # So re will try again.
                logger.warn("Data Checksum Invalid. Retrying.")
                continue

            # We have a reading, 
            logger.info("Sensor result {}".format(pad_value))

            humidity = pad_value

            if not triggered_high and humidity >= HIGH_PRESSURE_TRIGGER:
                # Trigger IFTTT Event (eg that will send email)
                logger.info("Pressure {} is >= {}, triggering event {}".format(humidity, HIGH_PRESSURE_TRIGGER, EVENT))
                triggered_high = True
                send_ifttt_event(humidity, "High Pressure Trigger")
           
           #When detected a face, save it in face.xml.
            frame = myCamera.getImage()
            faces = frame.findHaarFeatures('face.xml')
            center()#Servo starting position
            
                if faces:
                    for face in faces:
                        print "Face at: " + str(face.coordinates())
                        center()
                    else:
                        print "No faces detected."
                        angle(20)
                    frame.save(myDisplay)
                sleep(.1)
            

            sleep(POLL_INTERVAL_SECS)

    except KeyboardInterrupt:
        print("Bye")
