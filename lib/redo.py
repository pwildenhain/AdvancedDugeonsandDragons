import os
import inspect
parentdir = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#change system path if we're not in the main directory (MakeCharacter.py)
#so that I can run this both in the main and lib directories
if parentdir.endswith("lib") == True:
    os.sys.path.insert(0,os.path.dirname(parentdir))
#Import libs
import lib.typeit as tp
from time import sleep
def redo_loop(func,message):
    answer = ''
    while answer != 'yes':
        sleep(0.5)
        func()
        sleep(0.5)
        tp.typeit(message)
        answer = input().lower()
        if answer == 'yes':
            break
        elif answer not in ['yes','no']:
            while not answer in ['yes','no']:
                tp.typeit('Please type "yes" or "no"')
                answer = input().lower()
        else:
            continue
