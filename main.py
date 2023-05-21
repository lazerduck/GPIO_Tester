import GPIO
import GPIODisplay

gpio = GPIO.GPIO()
display = GPIODisplay.GPIODisplay(gpio)

while True:
    display.draw()
    print("pin to change: ")
    pinNo = int(input())
    if pinNo not in range(1,41):
        print("pin not found")
        continue
    pin = gpio.pins[pinNo -1]
    print("change type? (y/n)")
    changeType = input()
    if changeType == 'y':
        print("select type: input(1), output(2), pwm(3)")
        pinType = int(input())
        if pinType == 1:
            pin.setType("input")
        if pinType == 2:
            pin.setType("output")
        if pinType == 3:
            pin.setType("PWM")
    if pin.type == "output":
        print("set value: ")
        value = int(input())
        pin.setValue(value)
    if pin.type == "PWM":
        print("set duty:")
        duty = int(input())
        print("set freq:")
        freq = int(input())
        pin.setPWM(freq,duty)
