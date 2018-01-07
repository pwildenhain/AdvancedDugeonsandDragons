#Function to mimic a typewriter in print, at 1100 characters per minute
from time import sleep
def typeit(text):
    for char in range(len(text)):
        print(text[char],end='')
        sleep(0.04)
    print()
