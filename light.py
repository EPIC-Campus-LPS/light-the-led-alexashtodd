import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18 ,GPIO.OUT)
led=18

for i in range(10):
	GPIO.output(led,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(led,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()

