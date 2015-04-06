'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer (PNO)
Creation Date: April 3rd, 2015
Version: 1.0
Last Edited: April 6th, 2015
Known bugs: 
    1) Doesn't recognize the section for lambdas as a chapter in review.txt
    
Contributors: Nina Volkmuth
'''

#PNO_ui.py

import PNO_online as online

'''
High level description:
This module is the user interface for the PNO online and offline versions.
'''

EQUALS_DIVIDER = '======================================'
PLUS_DIVIDER = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
COMMANDS = '''
Commands:
    r: read a file
    c: convert a file to html
    q: quit
'''

#PUBLIC FUNCTIONS

def user_interface():
    ''' It prompts the user to enter information to generate the menu
    '''
    banner()
    running = True
    on = online.PNO_online()
    while running:
        print(COMMANDS)
        command = input('Enter a command: ').lower()
        if command == 'r':
            read_file(on)
        elif command == 'c':
            convert_file(on)
        elif command == 'q':
            running = quit_program()
        else:
            print('Invalid input! Please try again.')
                    
def read_file(on: online.PNO_online) -> None:
    file = prompt_for_link(on)
    notesName = input('Please assign a name to these notes: ')
    tList, chapters = on.get_titles_and_chapters(file)
    
    while True:
        table_contents(notesName, tList)
        selection = input('Please choose a chapter you would like to read(Enter a number) or enter b to go back to the main menu: ').lower()
        if selection == 'b':
            running = quit_program()
            break
        try:
            if int(selection) >= 1 and int(selection) <= len(tList):
                print_chapter(chapters[int(selection) - 1])
            else:
                print('Invalid input! Please try again. Try entering a number to select a chapter or enter b to go back to the main menu')
        except:
            print('Invalid input! Please try again. Try entering a number to select a chapter or enter b to go back to the main menu')
        

def convert_file(on: online.PNO_online) -> None:
    file = prompt_for_link(on)
    notesName = input('Please assign a name to these notes: ')
    notesName += '.html'
    print('Creating file...')
    tList, chapters = on.get_titles_and_chapters(file)
    on.create_html(notesName, tList, chapters)
    print('Finished!')
    
def prompt_for_link(on: online.PNO_online) -> 'notes':
    while True:
        address = input('Please enter the web address where the notes are located: ')
        notes = None
        try:
            notes = on.open_notes(address)
            return notes
        except:
            print("Can't connect to address, Please enter a valid address")
            
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
    
    
