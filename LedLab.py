from telemetrix import telemetrix
from time import sleep
board = telemetrix.Telemetrix()

class LedLab:
    
    """
    *A class to control LEDs*

    ## Methods
    `__init__(pin, name)`: Initialize the LED   
    `on()`: Turn the LED on   
    `off()`: Turn the LED off   
    `blink(times, delay)`: Blink the LED a certain amount of times with a certain delay   
    `toggle()`: Toggles the LED on or off   
    `get_available_leds()`: List the available LEDs  
    `get_led_by_name(name)`: Get an LED by its name

    ## Properties 
    `is_active`: True if the LED is currently ON   
    
    ## Atributes
    `pin`: The digital pin of the LED    
    `name`: The display name of the LED    
    """
    available_leds = []
    """The list of available LEDs"""

    def __init__(self, pin:int, name:str=None) -> None:
        """
        *Initialize the LED*
        
        ## Parameters:
        **pin:** *The digital pin of the LED*   
        **name** **(optional):** *The display name of the LED*
        """
        self.pin = pin
        if name == None:
            self.name = f"led{len(LedLab.available_leds)+1}"
        else:
            self.name = name
        self.is_on = False 
        board.set_pin_mode_digital_output(self.pin)
        LedLab.available_leds.append(self)

    def __repr__(self) -> str:
        return f"{self.name} at pin {self.pin}"


    def on(self) -> None:
        """
        *Turn the LED on*
        """

        self.is_on = True
        board.digital_write(self.pin, 1)

    def off(self) -> None:
        """
        *Turn the LED off*
        """

        self.is_on = False
        board.digital_write(self.pin, 0)

    def blink(self, times:int, delay:float|int) -> None:
        """
        *Turn on and off the LED at a certain amount of times
        and a certain delay between turning on and off the LED*
        
        ## Parameters

        **time:** *The number of times the LED should blink*   
        **delay:** *The delay between turning on and off the LED*
        """

        for i in range(times):
            sleep(delay)
            board.digital_write(self.pin, 1)
            sleep(delay)
            board.digital_write(self.pin, 0)

    def toggle(self) -> None:
        """
        *Toggles the LED on and off depending on its current state*
        """
        if self.is_on:
            self.off()
        else:
            self.on()

    @classmethod
    def get_available_leds(cls) -> str:
        """
        *List the available LEDs*
        """    
        for led in cls.available_leds:
            print(f"<{led}>")

    @classmethod
    def get_led_by_name(cls, name:str) -> None:
        """
        *Get an LED by its name*
        
        ## Parameters:

        **name:** *The name of the LED to get*
        """    
        for led in cls.available_leds:
            if led.name == name:
                return led

    @property
    def is_active(self) -> bool:
        """
        True if the LED is currently ON
        """
        if self.is_on == True:
            return True
        elif self.is_on == False:
            return False