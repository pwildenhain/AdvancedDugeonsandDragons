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
import random as rd
#Function to roll stats (4d6 drop the lowest)
def roll_stats():
    csg.all_stats = [] #Empty the list just to be sure
    for stat in range(6):
        all_dice = []
        for d6 in range(4):
            d6 = rd.randint(1,6)
            all_dice.insert(0,d6)
            min_roll = min(int(die) for die in all_dice)
            result = sum(all_dice) - min_roll
        csg.all_stats.append(result)
    tp.typeit(str(csg.all_stats))
