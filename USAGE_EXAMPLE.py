# Import the module
from LedLab import LedLab

# Creating a LED Object
# First parameter: the pin of the LED
# Second paramneter (optional): the name it will be displayed in the `get_available_leds` method
led1 = LedLab(1, name="test_led")

# Turn it on or off
led1.on()
led1.off()

# Make it blink
# First parameter: how many times to blink
# Second parameter: the delay between blinking
led1.blink(5, 1)

# Get the registered LEDs
LedLab.get_available_leds()

# See if one LED is active or not
led1.is_active
# e.g. `print(led1.is_active)`

# Toggle the LED on or off
led1.toggle()

# Get the target LED by its name
LedLab.get_led_by_name("test_led")
# e.g. `LedLab.get_led_by_name("test_led").on()`