'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer (PNO)
Creation Date: April 3rd, 2015
Version: 1.0
Known bugs: 
    1) It doesn't retrieve the last chapter of a file because it can't find the divider at the end. 
       It needs to find EOF. It gets stuck in an infinite loop
    2) It adds a divider in the list of titles because there are 3 consecutive dividers in the notes.
Contributors: 
'''

#PNO_online.py

import urllib.request as urlreq
import PNO_common_tools as ctools

'''
High level description:
This module is able to create a table of contents from notes online and retrieve each paragraph in organized manner.
'''

class PNO_online:
    def __init__(self, address: str):
        ''' It takes the address of the notes
        '''
        self._address = address
        self._tools = ctools.PNO_common_tools()
        pass
    
    def open_notes(self)->'Connection Response':
        ''' Uses the "Notes address" to open the notes online. It returns the "response" after connection.
        '''
        try:
            response = urlreq.urlopen(self._address)
            return response
        except:
            print("Can't connect to address, Please enter a valid address")
    
    def close_notes(self, file: 'Open File to close'):
        ''' Closes the open file passed as a parameter. 
        '''
        file.close()
        
    def chapt_par(self, title: 'Title to search for', file: 'File to search in')->'Paragraph':
        ''' Given a title to search for it return the paragraph that follows it as a string.
        '''
        return self._tools.find_chapt_par(title, file)
        
    def chapt_titles(self, file: 'File to search in')-> 'List of Paragraph Titles':
        ''' It finds the titles of each paragraph, based on the information of known patterns 
            that appear before titles, as well l, and saves the titles in a list. It then returns the list.
        '''
        return self._tools.find_chapt_titles(file)

    
    