'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer (PNO)
Creation Date: April 3rd, 2015
Version: 1.0
Last Edited: April 4th, 2015
Known bugs: 
    1) It doesn't retrieve the last chapter of a file because it can't find the divider at the end. 
       It needs to find EOF. It gets stuck in an infinite loop
    2) It adds a divider in the list of titles because there are 3 consecutive dividers in the notes.
    
Contributors: 
'''

#PNO_ui.py

import PNO_online as online

'''
High level description:
This module is the user interface for the PNO online and offline versions.
'''

EQUALS_DIVIDER = '======================================'
PLUS_DIVIDER = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

#PUBLIC FUNCTIONS

def user_interface():
    ''' It prompts the user to enter information to generate the menu
    '''
    running = True
    while running:
        
        banner()
        address = input('Please enter the web address where the notes are located: ')
        notesName = input('Please assign a name to these notes: ')
        
        on = online.PNO_online(address)
        tList = on.chapt_titles(on.open_notes()) #List of titles
        table_contents(notesName, tList)
        
        while True:
            selection = input('Please choose a chapter you would like to read(Enter a number), enter q to quit, or r to restart: ')
            if selection == 'q' or selection == 'Q':
                running = quit_program()
                break
            if selection == 'r' or selection == 'R':
                break
            elif int(selection) >= 1 and int(selection) <= len(tList):
                print_chapter(on.chapt_par(title_selected(int(selection), tList), on.open_notes()))
            else:
                print('Invalid input! Please try again. Try entering a number to select a chapter, enter q to quit the program, or r to restart the pogram')
                    
        
def quit_program()->'False to end program':
    print('Thank you for using this program')
    return False

def table_contents(name: 'Name to assign to notes', tList: 'List of titles'):
    print('\nTABLE OF CONTENTS: {}\n'.format(name))
    _print_titles(tList)
    
def print_chapter(chapter: 'Chapter Paragraph'):
    print('\nCHAPTER SELECTED:')
    print(PLUS_DIVIDER)
    print(chapter)
    print(PLUS_DIVIDER + '\n')
    
def title_selected(num: 'Title number', tList: 'List of titles')->'Selected title from menu':
    return tList[num - 1]
    
def banner():
    print('\n' + EQUALS_DIVIDER)
    print('            Welcome to PNO')
    print("       Pattis's Notes Organizer")
    print(EQUALS_DIVIDER + '\n')

#PRIVATE FUNCTIONS

def _print_titles(tList: 'List of titles'):
    for i, title in enumerate(tList):
        titleFormatted = '{})\t{}'.format(i+1, title)
        print(titleFormatted.strip('\n'))
    print(' ')

if __name__ == "__main__":
    user_interface()
    
    