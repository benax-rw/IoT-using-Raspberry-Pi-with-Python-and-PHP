
'''
Created by BAZIRAMWABO GABRIEL from Rwanda, a country of Thousand Hills, on 2017-Feb-06.
This file is a part of basic IoT project. 
It is a contribution the community of coders which made me who I am now in matter of coding.
Use this code as your own. 
If you feel you need to contact me, my email is baziramwabo@gmail.com

'''

import RPi.GPIO as GPIO
import urllib.request
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

os.system("clear")

print ("Receiver is listening...\n")
true = 1
while(true):
                try:
                        request = urllib.request.urlopen('http://yellowpagesrwanda.com/iot/commands.txt')
                        status = request.read().decode('utf-8')
                        

                        
                except urllib.error.URLError as e:
                                        print (e.reason)

                

                if status=='TurnOn':
                                GPIO.output(7,True)
                                f=open('ledStatus.txt', 'w')
                                f.write("ON")
                                f.close()   

  
                                
                elif status=='TurnOff':
                                GPIO.output(7,False)
                                f=open('ledStatus.txt', 'w')
                                f.write("OFF")
                                f.close()   
                     
                

              

GPIO.cleanup() 
