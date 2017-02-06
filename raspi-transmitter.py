'''
Created by BAZIRAMWABO GABRIEL from Rwanda, a country of Thousand Hills, on 2017-Feb-06.
This file is a part of basic IoT project. 
It is a contribution the community of coders which made me who I am now in matter of coding.
Use this code as your own. 
If you feel you need to contact me, my email is baziramwabo@gmail.com

'''
import RPi.GPIO as GPIO  
import time              
import http.client, urllib   
import socket           
import os
import netifaces as ni
ni.ifaddresses('eth0')

server = "yellowpagesrwanda.com" 
fields = ["timestamp", "switch_status", "client_ip"] 
buttonPin = 22 #pin15
client_ip_address = ni.ifaddresses('eth0')[2][0]['addr'] 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

os.system("clear")
print("Transmitter is ready!\n")

  
try:
    
    while 1:

        if not (GPIO.input(buttonPin)):
            print(time.strftime("%A %B %d, %Y %H:%M:%S %Z") + ": Packet sent to server")
			
            data = {} 

            f=open("ledStatus.txt", "r")
            ledStatus=f.read()
            f.close()

            data[fields[0]] = time.strftime("%A %B %d, %Y %H:%M:%S %Z") 
            data[fields[1]] = ledStatus 
            data[fields[2]] = client_ip_address
            params = urllib.parse.urlencode(data)


            headers = {} 
			headers["Content-Type"] = "application/x-www-form-urlencoded"
            headers["Connection"] = "close"
            headers["Content-Length"] = len(params) 
           
            c = http.client.HTTPConnection(server)
            c.request("POST", "/iot/server-receiver.php", params, headers) 
			
            time.sleep(1) 

except KeyboardInterrupt: 
    GPIO.cleanup() 
