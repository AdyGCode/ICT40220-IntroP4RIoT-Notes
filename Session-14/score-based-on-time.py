import time
import random
from time import sleep

print("There will be a random delay... press enter as soon as you see the prompt")
delay = random.randint(1,5)
sleep(delay)

# Get the time before the game begins
start_time = time.time()

# Do things that you want to time in here
answer = input("Press enter to continue")

# Once all tasks completed, get the end time
end_time = time.time()

# Calculate the score by using the difference in start time and end time,
# and then use this as a basis to calculate a score
time_diff = end_time - start_time
score = 1000 - int(time_diff * 100)


print(score)