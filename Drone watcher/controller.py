import RPi.GPIO as GPIO
import datetime
import dweepy
import time
from threading import Thread
from time import sleep





def getPic():
    for dweet in dweepy.listen_for_dweets_from('deanDronePI'):
        #grabbing the relevant data from dweet
        content1 = dweet["content"]
        How_Big = content1["acres"]
        content = dweet["content"]
        How_long = content["interval"]




        #seting the gpio board numbering convention
        GPIO.setmode(GPIO.BOARD)
        servo=11
        #setting the control gpio pin
        GPIO.setup(servo, GPIO.OUT)
        #reading/reseting the servo for use
        pwm=GPIO.PWM(servo,50)
        pwm.start(7)


        def SetAngle(angle):
            #defining the duty cycle for the servo to read
            #this formula roughly translates into degrees
            duty = angle / 18 + 2
            #sets the gpio pin as an output pin
            GPIO.output(11, True)
            #alters the pwm to follow the duty cycle
            pwm.ChangeDutyCycle(duty)
            sleep(1)
            #closes the pin and resets the pwm
            GPIO.output(11, False)
            pwm.ChangeDutyCycle(0)
        #sets the angle to 55 degrees
        SetAngle(55)

        x = How_Big*3
        flight_time = x*2

        sleep(flight_time)
        SetAngle(45)

        def post (statistics):
        	thing = 'deanDronePI'


        #pushing the alarm data to dweet
        def publishing():
                statistics = {}
                statistics["pic"] = 10
                return statistics
                time.sleep(10)
                statistics = {}
                statistics["pic"] = 0
                return statistics

        SetAngle(35)
        sleep(flight_time)

        #stopping the pulse cycle and cleaning up the pins
        pwm.stop()
        GPIO.cleanup()




while True:
	statistics = publishing();
	post(statistics)
    How_long_sec = How_long*60
	time.sleep(How_long_sec)
