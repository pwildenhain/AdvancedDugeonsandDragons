import os
import inspect
parentdir = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#change system path if we're not in the main directory (MakeCharacter.py)
#so that I can run this both in the main and lib directories
if parentdir.endswith("lib") == True:
    os.sys.path.insert(0,os.path.dirname(parentdir))
#Import libs
import lib.typeit as tp
import lib.charSheetGlobals as csg
from time import sleep
#Function to assign race
def pick_sex():
    while True:
        tp.typeit('Would you like to play a male or female character?')
        csg.sex = input().lower()
        if csg.sex in csg.sex_list:
            break
        else:
            tp.typeit('That\'s not an option here...')
            sleep(1.5)
            continue


