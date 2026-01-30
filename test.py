from LedLab import LedLab
from time import sleep

red_led = LedLab(8, name="red led")
yellow_led = LedLab(7, name="yellow led")
green_led = LedLab(6, name="green led")

try:
    while True:
        green_led.off()
        red_led.on()
        sleep(0.5)
        red_led.off()
        yellow_led.on()
        sleep(0.5)
        yellow_led.off()
        green_led.on()

        sleep(0.5)

        red_led.on()
        sleep(0.5)
        red_led.off()
        yellow_led.on()

        sleep(0.5)

        red_led.on()

        sleep(1)

        red_led.off()
        yellow_led.off()
        green_led.off()

except KeyboardInterrupt:
    red_led.off()
    yellow_led.off()
    green_led.off()