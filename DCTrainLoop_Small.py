#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import PiMotor

GPIO.setmode(GPIO.BOARD)
GPIO.setup([38, 40], GPIO.OUT)
GPIO.output([38, 40], GPIO.LOW)

track1 = PiMotor.Motor("MOTOR1",1)

sen1 = 33 #track 1
sen2 = 35 #track 2
sen3 = 37 #points

T1 = 38
T2 = 40

def points(pin):
    
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)


def sensor (pin):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    
    print("Starting loop in 5 seconds")
    
    
    time.sleep(5)
    
    while True:
        
        #make sure train is stopped before starting loop
        track1.stop()
        
        speed = 35
        
        #make sure points are thrown to track 1/train 1 (T1)
        print("")
        print("Points set to T1")
        points(T1)
        time.sleep(3)
        
        #move train slowly out towards sen3
        print("")
        print("Moving forward slowly")
        track1.forward(speed)
        
        #wait for sen3 to be triggered
        while (sensor(sen3)) < 500:
            #continue moving
            pass
        #sen3 triggered
        print("")
        print("Sensor 3 triggered, stopping train")
        #stop train
        track1.stop()
        time.sleep(3)

###############################################

        #Change points to T2
        print("")
        print("Points set to T2")
        points(T2)
        time.sleep(3)
        
        #Move train slowly in reverse
        print("")
        print("Reversing Slowly")
        track1.reverse(speed)
        
        #wait for sen2 to be triggered T2
        while (sensor(sen2)) < 1000:
            #continue moving
            pass
        #sen2 triggered
        print("")
        print("Sensor 2 triggered, stopping train")
        #stop train
        track1.stop()
        time.sleep(6)
        
###############################################
        
        #move train slowly out towards sen3
        print("")
        print("Moving forward slowly")
        track1.forward(speed)
        
        #wait for sen3 to be triggered
        while (sensor(sen3)) < 500:
            #continue moving
            pass
        #sen3 triggered
        print("")
        print("Sensor 3 triggered, stopping train")
        #stop train
        track1.stop()
        time.sleep(3)
        
###############################################
        
        #change points to T1
        print("")
        print("Points set to T1")
        points(T1)
        time.sleep(3)
        
        #Move train slowly in reverse
        print("")
        print("Reversing Slowly")
        track1.reverse(speed)
        
        #wait for sen1 to be triggered T1
        while (sensor(sen1)) < 1000:
            #continue moving
            pass
        #sen1 triggered
        print("")
        print("Sensor 1 triggered, stopping train")
        #stop train
        track1.stop()
        time.sleep(3)
        
        
        
        print("")
        print("Loop ended, starting again in 5 seconds")
        print("")
        print("")
        time.sleep(5)
            
except KeyboardInterrupt:
    track1.stop()
finally:
    GPIO.cleanup()