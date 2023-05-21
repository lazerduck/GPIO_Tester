grounPins = [6,9,14,20,25,30,34,39]
volt = [1,2,3,17]

class pin:
    def __init__(self, pinNo) -> None:
        self.state = 0
        self.type = "input"
        self.pinNo = pinNo
        self.isGround = False
        if pinNo in grounPins:
            self.isGround = True

    def setType(self, type):
        if self.isGround:
            return
        if type == "input" or type == "output" or type == "PWM":
            self.type = type
        else:
            print("Incorrect type provided")

    def getValue(self):
        return self.state
    
    def setValue(self, val):
        if self.type == "output" and (val == 0 or val == 1):
            self.state = val

    def setPWM(self, freq, duty):
        if self.type == "PWM":
            self.freq = freq
            self.duty = duty

class GPIO:
    def __init__(self) -> None:
        self.pins = []
        for i in range(1,41):
            self.pins.append(pin(i))

    
