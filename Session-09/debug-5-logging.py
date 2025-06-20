import logging
import sys

# logging levels are:
#   DEBUG (10): used to log messages that are useful for debugging.
#   INFO (20): used to log events within the parameters of expected program behavior.
#   WARNING (30): used to log unexpected events which may impede future program function but not severe enough to be an error.
#   ERROR (40): used to log unexpected failures in the program. Often, an exception needs to be raised to avoid further failures, but the program may still be able to run.
#   CRITICAL (50): used to log severe errors that can cause the application to stop running altogether.
#
# use the basic config line below, and change DEBUG to one of the options above
logging.basicConfig(level=logging.CRITICAL)

# Sending output to the logger
#   logging.debug("A debug message")
#   logging.info("An info message")
#   logging.warning("A warning message")
#   logging.error("An error message")
#   logging.critical("A critical message")

logger = logging.getLogger("debugging-log")
stdout = logging.StreamHandler(stream=sys.stdout)
fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s >>> %(message)s"
)

stdout.setFormatter(fmt)
logger.setLevel(logging.DEBUG)

name = input("What is your name?")

logging.info(f"name: {name}")

message = "Hello. Enjoy your Python"

if name == "fred":
    message = "Hello Fred! How are you today?"

logging.debug(f"message: {message}")

print(message)
