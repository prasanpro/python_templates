import json
import time
import random
import datetime
#0. import the supporting library for Azure IoT Hub/Device
from azure.iot.device import IoTHubDeviceClient

#1. declare iothub device client instance
device_connection_string = "XXXX"
myClient = IoTHubDeviceClient.create_from_connection_string(device_connection_string)

#2. start iothub device client
myClient.connect()

def message_handler(message):
    print("Message received from cloud: ")
    print(message.data)


myClient.on_message_received = message_handler

while(True):
    try:
        timestamp = time.mktime(datetime.datetime.now().timetuple())
        temp1 = random.uniform(0.0,35.0)
        temperature = float("{:.2f}".format(temp1))
        hum1 = random.uniform(30.0,80.0)
        humidity = float("{:.2f}".format(hum1))

        sensordata={}
        sensordata['timestamp'] = timestamp
        sensordata['temperature'] = temperature
        sensordata['humidity'] = humidity
        #convert string into json format
        sensorjsondata = json.dumps(sensordata)
        print(sensorjsondata)
        #3. send the data to Azure IoT Hub
        myClient.send_message(sensorjsondata)
        time.sleep(2)

    except KeyboardInterrupt:
        #disconnect the client
        myClient.disconnect()
        print("graceful exit")
        break