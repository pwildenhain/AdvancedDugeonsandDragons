##############################Imports
#standard modules
from time import sleep
from functools import partial
#data model module
from model.player_character import PlayerCharacter
#utility function modules
from utility.typeit import type_it
from utility.redo import redo_loop
##############################Introduction
NewCharacter = PlayerCharacter()
type_it('Oh boy a new character!')
sleep(0.5)
##############################Do the initial roll and assign stats
type_it('Would you like me to roll your stats for you?')
answer = ''
answer = input().lower()
#get a yes or no answer
while not answer in ['yes','no']:
	type_it('Please type "yes" or "no"')
	answer = input().lower()
#roll/assign or pick their stats
if answer == 'yes':
	type_it('Ok, here we go!')
	print('*Fingers crossed*')
	redo_loop(NewCharacter.roll_stats,'Want to keep these numbers?',
	show_func = NewCharacter.show_rolled_stats)
	redo_loop(
		partial(NewCharacter.assign_stats,type_it),
		'Are these choices correct?',
		show_func = NewCharacter.show_assigned_stats)
elif answer == 'no':
	type_it('Sounds good.')
	type_it('Enter below and don\'t adjust for race, we\'ll handle that next.')
	redo_loop(
		partial(NewCharacter.pick_stats,type_it),
		'Are these the numbers you want?',
		show_func = NewCharacter.show_assigned_stats)
sleep(0.5)
type_it('Awesome. Now let\'s choose a race.')
sleep(0.5)
##############################Choose race + sex
#choices are distinct enough, no need to ask for confirmation
NewCharacter.pick_race(type_it)
NewCharacter.pick_sex(type_it)
#Create the stats dictionary and adjust stats based on race
NewCharacter.adjust_stats()
if NewCharacter.adjust_stat_nums == True:
	type_it('You get some perks! Here\'s a peek at your adjusted stats.') 
	type_it(NewCharacter.show_adjusted_stats()) 
#is there a race/sex limitation?
NewCharacter.check_racesex_lim(type_it)
#if so, allow them to choose what to do next.
NewCharacter.racesex_lim_loop(type_it)
#give/ask them for their str percentile, if they have 18 strength
if NewCharacter.stats_chosen_dict['S'] == 18:
	type_it('Woah there, you are strong like bull with that 18 strength!')
	type_it('Would you like me to roll the percentile for you?')
	answer = input().lower()
	#get a yes or no answer
	while not answer in ['yes','no']:
		type_it('Please type "yes" or "no"')
		answer = input().lower()
	NewCharacter.str_18(answer,type_it)
#need to build checklim funcs for str percentile, after I check the overall str
##############################Look into tests for my modules
##############################Building in controls for limitations set by gary gygax, by race,class
#   Only offer to go back so many steps. i.e If you hit a level limit don't allow them to re-roll stats
#   race limitations: to be checked during pick_race, right after they choose.
#       by ability score (min and max for each ability)
#       dict stored in charSheetGlobals
#   class limitations: to be checked during pick_class_es, right after they choose each class
#       by ability score (min and max for each ability)
#       by race (true or false for each race/class combo)
#       dict stored in charSheetGlobals
# multiclass: levels need to be no more than 1 apart for non humans multiclass, humans can only have two classes
#   levels?
#       by race and class
#   weapon/armor prof:?
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