# Quick demo of using a module

# import all functions/variables from the greeting module
# into the application (script) global namespace
from greeting import *

# import the conversions module into the conversions namespace
import conversions


def main():
    # use the 'print_hi' function from the greetings namespace
    print_hi("Appy")

    temp_c = -40
    unit = "f"
    # use the temperature_convert function from the conversions namespace
    temp_f = conversions.temperature_convert(temp_c, unit)
    print(f"{temp_c}C is {temp_f}F")


if __name__ == "__main__":
    main()
