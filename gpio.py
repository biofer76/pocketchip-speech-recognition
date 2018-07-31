import CHIP_IO.GPIO as GPIO
import time

class Gpio():

    led = {
            "yellow":"XIO-P2",
            "green": "XIO-P3",
            "blue": "XIO-P4",
            "red": "XIO-P5"
          }

    def __init__(self):
        print ('init')
        GPIO.setup("XIO-P2", GPIO.OUT, initial=1)
        GPIO.setup("XIO-P3", GPIO.OUT, initial=1)
        GPIO.setup("XIO-P4", GPIO.OUT, initial=1)
        GPIO.setup("XIO-P5", GPIO.OUT, initial=1)
        GPIO.setwarnings(False)

    """ color available: green, yellow, blue """
    def on(self, color):
        GPIO.output(self.led[color], GPIO.LOW)

    def off(self, color):
        GPIO.output(self.led[color], GPIO.HIGH)

    def start_speech(self):
        self.on("blue")

    def stop_speech(self):
        self.off("blue")

    def say_yes(self):
        self.blink_on("green")

    def say_no(self):
        self.blink_on("yellow")

    def blink_on(self, color):
        self.on(color)
        time.sleep(.4)
        self.off(color)
        time.sleep(.4)
        self.on(color)
        time.sleep(.4)
        self.off(color)
        time.sleep(.4)
        self.on(color)
        time.sleep(3)
        self.off(color)

    def blink_bye(self):
        self.on("green")
        time.sleep(.3)
        self.off("green")
        self.on("yellow")
        time.sleep(.3)
        self.off("yellow")
        self.on("green")
        time.sleep(.3)
        self.off("green")
        self.on("yellow")
        time.sleep(.3)
        self.off("yellow")
        self.on("green")
        time.sleep(.3)
        self.off("green")
        self.on("yellow")
        time.sleep(.3)
        self.off("yellow")

    def cant_understand(self):
        self.blink_on("red")

    def cleanup(self):
        # GPIO.cleanup() << SEGFAULT
        GPIO.output("XIO-P3", GPIO.HIGH)