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
import lib.redo as re
import lib.pickrace as race
import lib.assignstats as assign
import lib.adjuststats as adjust
from time import sleep
#function to test limits by race
def check_race_lim():
    csg.has_limit = ''
    for stat in range(6):
        if csg.stats_chosen_dict[csg.stat_blocks[stat]] not in csg.race_limits[csg.race][csg.stat_blocks[stat]]:
            tp.typeit(csg.race.capitalize() + ' ' + csg.stat_names[stat] + ' techincally can\'t be ' + str(csg.stats_chosen_dict[csg.stat_blocks[stat]]))
            sleep(0.5)
            csg.has_limit = 'yes'

def race_lim_loop():
    while csg.has_limit == 'yes':
        tp.typeit('What would you like to do:')
        tp.typeit('a) continue')
        tp.typeit('b) pick another race')
        tp.typeit('c) re-assign stats')
        answer = ''
        answer = input().lower()
        while not answer in ['a','b','c']:
            tp.typeit('Please type a, b, or c')
            answer = input().lower()
        if answer == 'a':
            csg.has_limit = 'no'
        elif answer == 'b':
            re.redo_loop(race.pick_race,'Is that your final answer?')
            adjust.adjust_stats()
            check_race_lim()
        elif answer == 'c':
            re.redo_loop(assign.assign_stats,'Are these choices correct?')
            adjust.adjust_stats()
            check_race_lim()
                
            
            
        
        

