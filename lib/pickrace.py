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
def pick_race():
    while True:
        tp.typeit('Pick a race from the following list: ')
        tp.typeit(str(csg.race_list))
        csg.race = input().lower()
        if csg.race in csg.race_list:
            break
        elif 'half' in csg.race and 'orc' in csg.race:
            csg.race = 'half-orc'
            break
        elif 'half' in csg.race and 'elf' in csg.race:
            csg.race = 'half-elf'
            break
        else:
            tp.typeit('Hmmm I didn\'t catch that')
            sleep(1.5)
            continue


