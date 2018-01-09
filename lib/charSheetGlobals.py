#program display names
stat_names = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
#dict keys and chart sheet display names
stat_blocks = ['S','D','C','I','W','Ch']
race_list = ['dwarf','elf','gnome','half-elf','halfling','half-orc','human']
sex_list = ['male','female']
#stats variables to be filled by MakeCharacter.py
all_stats  = []
all_stats_ordered = []
stats_chosen_dict = {}
str_percentile = 0
race = ''
sex = ''
#limitations vars and dicts
has_limit = ''
racesex_limits = {'dwarf' : {'S':{'male':range(8,19), 'female':range(8,18)},
                          #'Sper':{'male':range(100),'female':range(0)},
                          'D':range(3,18),
                          'C':range(12,26),
                          'I':range(3,26),
                          'W':range(3,26),
                          'Ch':range(3,17)},
               'elf' : {'S':{'male':range(3,19), 'female':range(3,17)},
                          #'Sper':{'male':range(76), 'female':range(0)},
                          'D':range(7,26),
                          'C':range(6,26),
                          'I':range(8,26),
                          'W':range(3,26),
                          'Ch':range(8,26)},
               'gnome' : {'S':{'male':range(6,19), 'female':range(6,16)},
                          #'Sper':{'male':range(51), 'female':range(0)},
                          'D':range(3,26),
                          'C':range(8,26),
                          'I':range(7,26),
                          'W':range(3,26),
                          'Ch':range(3,26)},
               'half-elf' : {'S':{'male':range(3,19), 'female':range(3,18)},
                          #'Sper':{'male':range(91),'female':range(0)},
                          'D':range(6,26),
                          'C':range(6,26),
                          'I':range(4,26),
                          'W':range(3,26),
                          'Ch':range(3,26)},
               'halfling' : {'S':{'male':range(6,18), 'female':range(6,15)},
                          #'Sper':{'male':range(0),'female':range(0)},
                          'D':range(8,26),
                          'C':range(10,26),
                          'I':range(6,26),
                          'W':range(3,18),
                          'Ch':range(3,26)},
               'half-orc' : {'S':{'male':range(6,19), 'female':range(6,19)},
                          #'Sper':{'male':range(100), 'female':range(76)},
                          'D':range(3,15),
                          'C':range(13,26),
                          'I':range(3,18),
                          'W':range(3,15),
                          'Ch':range(3,13)},
               'human' : {'S':{'male':range(3,26), 'female':range(3,26)},
                          #'Sper':{'male':range(101),'female':range(51)},
                          'D':range(3,26),
                          'C':range(3,26),
                          'I':range(3,26),
                          'W':range(3,26),
                          'Ch':range(3,26)}
               }
