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
def str_18_roll():
    csg.str_percentile = rd.randint(1,100)
    tp.typeit('Strength Percentile: ' + str(csg.str_percentile))
