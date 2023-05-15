
import machine
import utime

# GPIO Pin used for the Tesla Coil control
coil_pin = machine.Pin(0, machine.Pin.OUT)

# GPIO Pin used for the button
button_pin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

# Create a PWM object from the pin
coil_pwm = machine.PWM(coil_pin)

# Global variable to track state of the Tesla Coil
coil_state = False

# Function to control the power (duty cycle)
def set_power(power_percentage):
    duty_cycle = int(power_percentage * 1023 / 100)  # Map percentage to 0-1023
    coil_pwm.duty_u16(duty_cycle)  # set duty cycle

# Function to control the frequency
def set_frequency(frequency):
    coil_pwm.freq(frequency)  # set frequency

# Function to handle button presses
def button_handler(pin):
    global coil_state
    if coil_state:
        set_power(0)
        coil_state = False
    else:
        set_power(50)  # set power to 50%
        set_frequency(1000)  # set frequency to 1kHz
        coil_state = True

# Attach the interrupt handler to the button pin
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

# Loop forever
while True:
    pass

