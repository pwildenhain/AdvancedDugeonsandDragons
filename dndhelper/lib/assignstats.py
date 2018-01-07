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
#Function to assign stats
def assign_stats():
    csg.all_stats_ordered = []
    all_stats_unordered = list(csg.all_stats)
    stat = 0
    #Check to make sure all the values in all_stats_unordered are unique
    while all(x==all_stats_unordered[0] for x in all_stats_unordered)==False:
        tp.typeit('Pick a number for ' + csg.stat_names[stat] + ': ' + str(all_stats_unordered))
        while True:
            try:
                choice = int(input())
                if choice in all_stats_unordered:
                    csg.all_stats_ordered.append(choice)
                    all_stats_unordered.remove(choice)
                    break
                else:
                    tp.typeit('I don\'t see that number. Choose ' + csg.stat_names[stat] + ' from these values:' + str(all_stats_unordered))
                    continue
            except ValueError:
                    tp.typeit('Numbers only please. Choose ' + csg.stat_names[stat] + ' from these values:' + str(all_stats_unordered))
                    continue
        #Move on to next stat
        stat = stat + 1
    #If all the values in all_stats_unordered are the same, then assign the rest automatically        
    for stat in range(len(all_stats_unordered)):
        csg.all_stats_ordered.insert(5,all_stats_unordered[stat])
    #Print their stats    
    for stat in range(6):
        tp.typeit(csg.stat_blocks[stat] + ': ' + str(csg.all_stats_ordered[stat]))
