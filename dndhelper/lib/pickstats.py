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
#Function to pick stats manually
def pick_stats():
    csg.all_stats_ordered = []
    for stat in range(6):
        tp.typeit('Enter a number for ' + csg.stat_names[stat] + ': ')
        while True:
            try:
                choice = int(input())
                while not choice in range(3,26):
                    tp.typeit('Please enter an integer between 3 and 25')
                    try:
                        choice = int(input())
                    except ValueError:
                        tp.typeit('Whoops, integers only please. Enter a number for ' + csg.stat_names[stat] + ': ')
                        continue
                csg.all_stats_ordered.append(choice)
                break
            except ValueError:
                tp.typeit('Whoops, integers only please. Enter a number for ' + csg.stat_names[stat] + ': ')
                continue
    csg.all_stats = csg.all_stats_ordered
    for stat in range(6):
        tp.typeit(csg.stat_blocks[stat] + ': ' + str(csg.all_stats_ordered[stat]))
