#program display names
stat_names = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
#dict keys and chart sheet display names
stat_blocks = ['S','D','C','I','W','Ch']
race_list = ['dwarf','elf','gnome','half-elf','halfling','half-orc','human']
#stats variables to be filled by MakeCharacter.py
all_stats  = []
all_stats_ordered = []
stats_chosen_dict = {}
str_percentile = 0
race = ''
#limitations vars and dicts
has_limit = ''
race_limits = {'dwarf' : {'S':range(8,19),
                          #'Sper':range(100),
                          'D':range(18),
                          'C':range(12,100),
                          'I':range(100),
                          'W':range(100),
                          'Ch':range(17)},
               'elf' : {'S':range(19),
                          #'Sper':range(76),
                          'D':range(7,100),
                          'C':range(6,100),
                          'I':range(8,100),
                          'W':range(100),
                          'Ch':range(8,100)},
               'gnome' : {'S':range(6,19),
                          #'Sper':range(51),
                          'D':range(100),
                          'C':range(8,100),
                          'I':range(7,100),
                          'W':range(100),
                          'Ch':range(100)},
               'half-elf' : {'S':range(19),
                          #'Sper':range(91),
                          'D':range(6,100),
                          'C':range(6,100),
                          'I':range(4,100),
                          'W':range(100),
                          'Ch':range(100)},
               'halfling' : {'S':range(6,18),
                          #'Sper':range(100),
                          'D':range(8,100),
                          'C':range(10,100),
                          'I':range(6,100),
                          'W':range(18),
                          'Ch':range(100)},
               'half-orc' : {'S':range(6,19),
                          #'Sper':range(100),
                          'D':range(15),
                          'C':range(13,100),
                          'I':range(18),
                          'W':range(15),
                          'Ch':range(13)},
               'human' : {'S':range(100),
                          #'Sper':range(101),
                          'D':range(100),
                          'C':range(100),
                          'I':range(100),
                          'W':range(100),
                          'Ch':range(100)}
               }
