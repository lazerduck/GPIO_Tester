import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

grounPins = [6,9,14,20,25,30,34,39, 27, 28]
volt = [1,2,4,17]

class pinInterface:
    def __init__(self, pinNo) -> None:
        self.type = "input"
        self.state = 0
        self.pinNo = pinNo
        self.duty = 50
        self.freq = 512
        self.isGround = False
        self.isVolt = False
        self.pwm = None
        if pinNo in grounPins:
            self.isGround = True
        if pinNo in volt:
            self.isVolt = True
        if not self.isGround and not self.isVolt:
            print("setting pin " + str(pinNo))
            GPIO.setup(pinNo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def getValue(self):
        if self.type == "input":
            return GPIO.input(self.pinNo)
        return self.state
    
    def setType(self, type):
        if self.isGround or self.isVolt:
            return
        if type == "input":
            GPIO.setup(self.pinNo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        if type == "output":
            GPIO.setup(self.pinNo, GPIO.OUT)
        if type == "PWM":
            GPIO.setup(self.pinNo, GPIO.OUT)
            self.pwm = GPIO.PWM(self.pinNo, self.freq)
            self.pwm.start(self.duty)
        self.type = type

    def setValue(self, val):
        if self.type == "output" and (val == 0 or val == 1):
            self.state = val
            if self.state == 0:
                GPIO.output(self.pinNo, GPIO.LOW)
            else:
                GPIO.output(self.pinNo, GPIO.HIGH) 

    def setPWM(self, freq, duty):
        if self.type == "PWM":
            self.freq = freq
            self.duty = duty
            self.pwm.ChangeFrequency(freq)
            self.pwm.ChangeDutyCycle(duty)