import inspect

# Constant to turn debugging output on and off
DEBUG = True


def debug(variable):
    """
    Basic debug function to output <DEBUG> followed by
    the name of the variable and it's value

    This function:
        Gets the previous frame (caller)
        Gets the source code line that called debug
        Extract the variable name from inside the parentheses

    Parameters
    ----------
    variable : string : the variable to display

    """
    if DEBUG:
        frame = inspect.currentframe().f_back
        code_line = inspect.getframeinfo(frame).code_context[0].strip()
        start = code_line.find('(') + 1
        end = code_line.rfind(')')
        variable_name = code_line[start:end].strip()
        value = variable

        print(f"<DEBUG> {variable_name} => {value}")


name = input("What is your name?")

debug(name)

message = "Hello. Enjoy your Python"

if name == "fred":
    message = "Hello Fred! How are you today?"

debug(message)

print(message)
