import GPIO
import os

class GPIODisplay:
    def __init__(self, gpio:GPIO) -> None:
        self.gpio = gpio
        pass

    def draw(self):
        os.system('clear')
        line = "  "
        for i in range(0,40):
            if i%2!=0:
                pin = self.gpio.pins[i]
                if pin.isGround:
                    line += "    "
                    continue
                if pin.type == "PWM":
                    line += str(pin.duty) + " "
                else:
                    line += "    "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2!=0:
                pin = self.gpio.pins[i]
                if pin.isGround:
                    line += "GND "
                    continue
                if pin.type == "PWM":
                    line += str(pin.freq) + " "
                else:
                    line += "("+str(pin.state)+") "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2!=0:
                pin = self.gpio.pins[i]
                line += pin.type[:3] + " "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                line += " |  "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2!=0:
                pin = self.gpio.pins[i]
                if pin.pinNo < 10:
                    line += "_" + str(pin.pinNo) + "__"
                else:
                    line += "_" + str(pin.pinNo) + "_"
        print(line)
        line = " |                                                                                |"
        print (line)
        line = " |                                      GPIO                                      |"
        print (line)
        line = " |                                                                                |"
        print (line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                pin = self.gpio.pins[i]
                if pin.pinNo < 10:
                    line += "_" + str(pin.pinNo) + "__"
                else:
                    line += "_" + str(pin.pinNo) + "_"
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                line += " |  "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                pin = self.gpio.pins[i]
                line += pin.type[:3] + " "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                pin = self.gpio.pins[i]
                if pin.isGround:
                    line += "GND "
                    continue
                if pin.type == "PWM":
                    line += str(pin.freq) + " "
                else:
                    line += "("+str(pin.state)+") "
        print(line)
        line = "  "
        for i in range(0,40):
            if i%2==0:
                pin = self.gpio.pins[i]
                if pin.isGround:
                    line += "    "
                    continue
                if pin.type == "PWM":
                    line += str(pin.duty) + " "
                else:
                    line += "    "
        print(line)