import RPI.GPIO as GPIO
import time

Trig_PIN=6
Echo_PIN=8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trig_PIN,GPIO.OUT)
GPIO.setup(Echo_PIN,GPIO.IN)

while(True):
    GPIO.output(Trig_PIN,0)

    GPIO.output(Trig_PIN,1)
    time.sleep(10e-6)
    GPIO.output(Trig_PIN,0)

    pluseStart=0.0
    pluseEnd=0.0

    while(GPIO.input(Echo_PIN)==0):
        pluseStart=time.time()

    while(GPIO.input(Echo_PIN)==1):
        pluseEnd=time.time()
    
    delta=pluseEnd-pluseStart
    distance=delta*75000

    print("Distance(in  CM):" +str(distance))
    time.sleep(.3)

GPIO.cleanup()





