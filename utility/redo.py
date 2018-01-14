#Import libs
from .typeit import type_it
from time import sleep
def redo_loop(do_func,message,show_func=None):
    answer = ''
    while answer != 'yes':
        sleep(0.5)
        do_func()
        if show_func != None: 
            type_it(show_func())
        sleep(0.5)
        type_it(message)
        answer = input().lower()
        if answer == 'yes':
            break
        elif answer not in ['yes','no']:
            while not answer in ['yes','no']:
                type_it('Please type "yes" or "no"')
                answer = input().lower()
        else:
            continue
