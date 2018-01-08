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
#functions to adjust character stats based on the race they chose

def adjust_stats():
    #Create the stat dict here, in case we choose a new race
    csg.stats_chosen_dict = dict(zip(csg.stat_blocks,csg.all_stats_ordered))
    #Then adjust for new race if appropriate
    if csg.race in ['dwarf','elf','halfling','half-orc']:
        if csg.race == 'dwarf':
            csg.stats_chosen_dict['C'] = csg.stats_chosen_dict['C'] + 1
            csg.stats_chosen_dict['Ch'] = csg.stats_chosen_dict['Ch'] - 1
        elif csg.race == 'elf':
            csg.stats_chosen_dict['D'] = csg.stats_chosen_dict['D'] + 1
            csg.stats_chosen_dict['C'] = csg.stats_chosen_dict['C'] - 1
        elif csg.race == 'halfling':
            csg.stats_chosen_dict['D'] = csg.stats_chosen_dict['D'] + 1
            csg.stats_chosen_dict['S'] = csg.stats_chosen_dict['S'] - 1
        elif csg.race == 'half-orc':
            csg.stats_chosen_dict['S'] = csg.stats_chosen_dict['S'] + 1
            csg.stats_chosen_dict['C'] = csg.stats_chosen_dict['C'] + 1
            csg.stats_chosen_dict['Ch'] = csg.stats_chosen_dict['Ch'] - 2
        tp.typeit('You get some perks! Here\'s a peek at your adjusted stats.')
        sleep(0.5)
        tp.typeit(str(csg.stats_chosen_dict))
        sleep(0.5)
