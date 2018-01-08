##############################Imports and functions
from time import sleep
import lib.charSheetGlobals as csg
import lib.typeit as tp
import lib.redo as re
import lib.checklims as lim
#Main functions for the module
import lib.pickstats as pick
import lib.rollstats as roll
import lib.assignstats as assign
import lib.adjuststats as adjust
import lib.pickrace as race
import lib.str18 as str18
##############################Introduction
tp.typeit('Oh boy a new character!')
sleep(0.5)
##############################Do the initial roll and assign stats
tp.typeit('Would you like me to roll your stats for you?')
answer = ''
answer = input().lower()
#get a yes or no answer
while not answer in ['yes','no']:
    tp.typeit('Please type "yes" or "no"')
    answer = input().lower()
#roll/assign or pick their stats
if answer == 'yes':
    tp.typeit('Ok, here we go!')
    print('*Fingers crossed*')
    re.redo_loop(roll.roll_stats,'Want to keep these numbers?')
    tp.typeit('Great! Let\'s assign these stats.')
    re.redo_loop(assign.assign_stats,'Are these choices correct?')
elif answer == 'no':
    tp.typeit('Sounds good.')
    tp.typeit('Enter below and don\'t adjust for race, we\'ll handle that next.')
    re.redo_loop(pick.pick_stats,'Are these the numbers you want?')
sleep(0.5)
tp.typeit('Awesome. Now let\'s choose a race.')
sleep(0.5)
##############################Choose race
re.redo_loop(race.pick_race,'Is that your final answer?')
#Adjusted stats based on race
adjust.adjust_stats()
#is there a limitation?
lim.check_race_lim()
#if so, allow them to choose what to do next.
lim.race_lim_loop()
#Roll percentiles if they have an 18 strength
if csg.stats_chosen_dict['S'] == 18:
    tp.typeit('Woah, you are strong like bull with that 18 strength. Here\'s the percentile for that.')
    re.redo_loop(str18.str_18_roll,'Want to keep that percentage?')
    sleep(0.5)
tp.typeit('Moving right along--Let\'s pick a class')
sleep(0.5)
##############################Look into tests for my modules
##############################Edit the stats pick to only allow range(1,31)
##############################Building in controls for limitations set by gary gygax, by race,class
#   Only offer to go back so many steps. i.e If you hit a level limit don't allow them to re-roll stats
#   race limitations: to be checked during pick_race, right after they choose.
#       by ability score (min and max for each ability)
#       dict stored in charSheetGlobals
#   class limitations: to be checked during pick_class_es, right after they choose each class
#       by ability score (min and max for each ability)
#       by race (true or false for each race/class combo)
#       dict stored in charSheetGlobals
#   weapon/armor prof:?
#   levels?
#       by race and class
##############################Choose class/classes
#   this needs to be dynamic, and will define
#   the structure of all the other functions moving forward
#   so it's important to get it right
#       class needs to be stored as a dict, whose keys will
#       be the class, and whose items will be the levels
#       then for all future steps that are class/level dependent
#       we'll iterate over the keys() and use the items() and keys()
#       in the appropriate function (THAC0,spells,hp,weapon spec,saving throws, etc)
##############################Choose level
############################Choose languages (based on race, and int)
##############################Assign hp allow to reroll hp
##############################Saving throws
        #Halflings, dwarves: +1 saving throws against spell,rod,staves,wands,poison for every 3.5 pts con
        #gnomes: +1 saving throws against spell,rod,staves,wands,for every 3.5 pts con
        #every 3.5 pts 4-6(+1), 7-10(+2), 11-
##############################THAC0
##############################Weapons/Armor/Weapon specialization
    #should I make proficiencies a thing? would be just another limitations dict
##############################Choose spells
##############################Spells/Skills
#############################Choose Alignment, gender, religion,name,traits and other misc things that don't effect the char sheet
#############################it would be nice for the messages to be a little more random, throughout and not just the same every time




