#Function to mimic a typewriter in print, at 1100 characters per minute
from time import sleep
from random import uniform
def type_it(text):
    for char in text:
        print(char,end='',flush=True)
        sleep(uniform(0.0,0.03))
    print()
