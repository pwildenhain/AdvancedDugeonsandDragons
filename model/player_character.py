# Imports
from time import sleep
from random import randint
# Define the Player Character Classification
class PlayerCharacter(object):
    """The character to be created for playing Advanced Dungeons and Dragons
       with the following properties:

    Attributes:
        all_stats:
        all_stats_ordered:
        stats_chosen_dict:
        str_percentile:
        race:
        sex:
        has_limit:
    """
    def __init__(self, all_stats  = [], all_stats_ordered = [], stats_chosen_dict = {}, str_percentile = 0, race = '', sex = '', adjust_stat_nums = False, has_limit = '',
                 stat_names = [], stat_blocks = [], race_list = [], sex_list = [], racesex_limits = {}):
        """Return a PlayerCharacter object with all empty attributes"""
        self.all_stats = all_stats
        self.all_stats_ordered = all_stats_ordered
        self.stats_chosen_dict = stats_chosen_dict
        self.str_percentile = str_percentile
        self.race = race
        self.sex = sex
        self.adjust_stat_nums = adjust_stat_nums
        self.has_limit = has_limit
        self.stat_names = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
        self.stat_blocks = ['S','D','C','I','W','Ch']
        self.race_list = ['dwarf','elf','gnome','half-elf','halfling','half-orc','human']
        self.sex_list = ['male','female']
        self.racesex_limits = {
                'dwarf' : {'S':{'male':range(8,19), 'female':range(8,18)}, #'Sper':{'male':range(100),'female':range(0)},
                          'D':range(3,18),
                          'C':range(12,26),
                          'I':range(3,26),
                          'W':range(3,26),
                          'Ch':range(3,17)},
               'elf' : {'S':{'male':range(3,19), 'female':range(3,17)}, #'Sper':{'male':range(76), 'female':range(0)},
                          'D':range(7,26),
                          'C':range(6,26),
                          'I':range(8,26),
                          'W':range(3,26),
                          'Ch':range(8,26)},
               'gnome' : {'S':{'male':range(6,19), 'female':range(6,16)}, #'Sper':{'male':range(51), 'female':range(0)},
                          'D':range(3,26),
                          'C':range(8,26),
                          'I':range(7,26),
                          'W':range(3,26),
                          'Ch':range(3,26)},
               'half-elf' : {'S':{'male':range(3,19), 'female':range(3,18)}, #'Sper':{'male':range(91),'female':range(0)},
                          'D':range(6,26),
                          'C':range(6,26),
                          'I':range(4,26),
                          'W':range(3,26),
                          'Ch':range(3,26)},
               'halfling' : {'S':{'male':range(6,18), 'female':range(6,15)}, #'Sper':{'male':range(0),'female':range(0)},
                          'D':range(8,26),
                          'C':range(10,26),
                          'I':range(6,26),
                          'W':range(3,18),
                          'Ch':range(3,26)},
               'half-orc' : {'S':{'male':range(6,19), 'female':range(6,19)}, #'Sper':{'male':range(100), 'female':range(76)},
                          'D':range(3,15),
                          'C':range(13,26),
                          'I':range(3,18),
                          'W':range(3,15),
                          'Ch':range(3,13)},
               'human' : {'S':{'male':range(3,26), 'female':range(3,26)}, #'Sper':{'male':range(101),'female':range(51)},
                          'D':range(3,26),
                          'C':range(3,26),
                          'I':range(3,26),
                          'W':range(3,26),
                          'Ch':range(3,26)}
               }
    def roll_stats(self):
        """Roll the initial stats for the PlayerCharacter, and then assign it to the all_stats attribute"""
        # Empty the list in case there are previous results
        self.all_stats = []
        for result in range(6):
            all_dice = []
            for d6 in range(4):
                d6 = randint(1,6)
                all_dice.insert(0,d6)
                min_roll = min(int(die) for die in all_dice)
                result = sum(all_dice) - min_roll
            self.all_stats.append(result)
    def show_rolled_stats(self):
        return ", ".join([str(num) for num in self.all_stats])
    def pick_stats(self,func):
        """Directly assign the initial stats for the PlayerCharacter in order, and then assign it to the all_stats_ordered attribute"""
        # Empty the list in case there are previous results
        self.all_stats_ordered = []
        for stat in range(6):
            stat = self.stat_names[stat]
            # stat_names exists in charSheetGlobals for reference
            func(f'Enter a number for {stat}: ')
            while True:
                try: 
                    choice = int(input())
                    if choice not in range(3,26):
                        func(f'Just integers between 3 and 25 for now. Enter a number for {stat}: ')
                        continue
                    else:
                        self.all_stats_ordered.append(choice)
                        break
                except ValueError: 
                    func(f'Whoops, integers only please. Enter a number for {stat}: ')
                    continue
        self.all_stats = self.all_stats_ordered 

        return ", ".join(picked_stats)
    def assign_stats(self,func):
        self.all_stats_ordered = []
        all_stats_unordered = list(self.all_stats)
        stat = 0
        # Check to make sure all the values in all_stats_unordered are unique
        while all(x==all_stats_unordered[0] for x in all_stats_unordered)==False:
            func('Pick a number for ' + self.stat_names[stat] + ': ' + ", ".join([str(num) for num in all_stats_unordered]))
            while True:
                try:
                    choice = int(input())
                    if choice in all_stats_unordered:
                        self.all_stats_ordered.append(choice)
                        all_stats_unordered.remove(choice)
                        break 
                    else:
                        func('I don\'t see that number. Choose ' + self.stat_names[stat] + ' from these values:' + ", ".join([str(num) for num in all_stats_unordered]))
                        continue
                except ValueError:
                    func('Numbers only please. Choose ' + self.stat_names[stat] + ' from these values:' + ", ".join([str(num) for num in all_stats_unordered]))
                    continue
                # Move on to next stat
            stat = stat + 1
        # If all the values in all_stats_unordered are the same, then assign the rest automatically        
        for stat in range(len(all_stats_unordered)):
            self.all_stats_ordered.insert(5,all_stats_unordered[stat])
    def show_assigned_stats(self):
        assigned_stats = []
        for stat in range(6):
            assigned_stats.append(self.stat_blocks[stat] + ': ' + str(self.all_stats_ordered[stat]))
        return ", ".join(assigned_stats)
    def pick_race(self,func): 
        while True: 
            func('Pick a race from the following list:') 
            func(", ".join(self.race_list))
            self.race = input().lower()
            if self.race in self.race_list:
                break
            elif 'half' in self.race and 'orc' in self.race:
                self.race = 'half-orc'
                break
            elif 'half' in self.race and 'elf' in self.race:
                self.race = 'half-elf'
                break
            else:
                func('Hmmm I didn\'t catch that')
                sleep(1.5)
                continue
    def pick_sex(self,func): 
        while True: 
            func('Would you like to play a male or female character?')
            self.sex = input().lower()
            if self.sex in self.sex_list:
                break
            else:
                func('That\'s not an option here...')
                sleep(1.5)
                continue
    def adjust_stats(self):
        # Create the stat dict here, in case we choose a new race
        self.stats_chosen_dict = dict(zip(self.stat_blocks,self.all_stats_ordered))
        # reset our "has adjusted stats" variable, in case we loop back through
        self.adjust_stat_nums = False
        # Then adjust for new race if appropriate
        if self.race in ['dwarf','elf','halfling','half-orc']:
            self.adjust_stat_nums = True
            if self.race == 'dwarf':
                self.stats_chosen_dict['C'] = self.stats_chosen_dict['C'] + 1
                self.stats_chosen_dict['Ch'] = self.stats_chosen_dict['Ch'] - 1
            elif self.race == 'elf':
                self.stats_chosen_dict['D'] = self.stats_chosen_dict['D'] + 1
                self.stats_chosen_dict['C'] = self.stats_chosen_dict['C'] - 1
            elif self.race == 'halfling':
                self.stats_chosen_dict['D'] = self.stats_chosen_dict['D'] + 1
                self.stats_chosen_dict['S'] = self.stats_chosen_dict['S'] - 1
            elif self.race == 'half-orc':
                self.stats_chosen_dict['S'] = self.stats_chosen_dict['S'] + 1
                self.stats_chosen_dict['C'] = self.stats_chosen_dict['C'] + 1
                self.stats_chosen_dict['Ch'] = self.stats_chosen_dict['Ch'] - 2
    def show_adjusted_stats(self): 
        return ", ".join("{}: {}".format(stat, num) for stat, num in self.stats_chosen_dict.items())
    def check_racesex_lim(self,func):
        self.has_limit = False
        for stat in range(6):
            if stat == 0:
                if self.stats_chosen_dict[self.stat_blocks[stat]] not in self.racesex_limits[self.race][self.stat_blocks[stat]][self.sex]:
                    func(self.sex.capitalize() + ' ' + self.race.capitalize() + ' ' + self.stat_names[stat] + ' techincally can\'t be ' + str(self.stats_chosen_dict[self.stat_blocks[stat]]))
                    sleep(0.5)
                    self.has_limit = True
            else:
                if self.stats_chosen_dict[self.stat_blocks[stat]] not in self.racesex_limits[self.race][self.stat_blocks[stat]]:
                    func(self.race.capitalize() + ' ' + self.stat_names[stat] + ' techincally can\'t be ' + str(self.stats_chosen_dict[self.stat_blocks[stat]]))
                    sleep(0.5)
                    self.has_limit = True
    def racesex_lim_loop(self,func):
        while self.has_limit == True:
            func('What would you like to do:')
            func('a) continue')
            func('b) pick another sex')
            func('c) pick another race')
            func('d) re-assign stats')
            answer = ''
            answer = input().lower()
            while not answer in ['a','b','c','d']:
                func('Please type a, b, or c')
                answer = input().lower()
            if answer == 'a':
                self.has_limit = False
            elif answer == 'b':
                self.pick_sex(func)
                self.check_racesex_lim(func)
            elif answer == 'c':
                self.pick_race(func)
                self.adjust_stats()
                if self.adjust_stat_nums == True:
                    func('You get some perks! Here\'s a peek at your adjusted stats.') 
                    func(self.show_adjusted_stats())                
                self.check_racesex_lim(func)
            elif answer == 'd':
                self.assign_stats(func)
                func(self.show_assigned_stats())
                self.adjust_stats()
                if self.adjust_stat_nums == True:
                    func('Here\'s a peek at your adjusted stats.')
                    func(self.show_adjusted_stats())
                self.check_racesex_lim(func)
    def str_18(self,answer,func):
        if answer == 'yes': 
            str_percentile = randint(1,100)
        elif answer == 'no':
            while True: 
                func('Enter a number for your Strength Percentile:')
                try: 
                    str_percentile = int(input())
                    if str_percentile not in range(1,101): 
                        func('Hmmm, only integers between 1 and 100 are accepted.')
                        continue
                    else:
                        break
                except ValueError: 
                    func('Whoops, integers only please.')
                    continue