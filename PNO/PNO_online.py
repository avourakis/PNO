'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer (PNO)
Creation Date: April 3rd, 2015
Version: 1.1
Known bugs: 
    1) Doesn't recognize the section for lambdas as a chapter in review.txt
Contributors: Nina Volkmuth
'''

#PNO_online.py

import urllib.request as urlreq
import PNO_common_tools as ctools

'''
High level description:
This module is able to create a table of contents from notes online and retrieve each paragraph in organized manner.
'''

class PNO_online:
    def __init__(self):
        ''' It takes the address of the notes
        '''
        self._tools = ctools.PNO_common_tools()
        self._converter = ctools.HTMLConverter()
    
    def open_notes(self, address: str)->'Connection Response':
        ''' Uses the "Notes address" to open the notes online. It returns the "response" after connection.
        '''
        response = urlreq.urlopen(address)
        return response

    # Currently not used
    def close_notes(self, file: 'Open File to close'):
        ''' Closes the open file passed as a parameter. 
        '''
        file.close()

    # Currently not used
    """
    def chapt_par(self, title: 'Title to search for', file: 'File to search in')->'Paragraph':
        ''' Given a title to search for it return the paragraph that follows it as a string.
        '''
        return self._tools.find_chapt_par(title, file)
    """

    # Currently not used
    """
    def chapt_titles(self, file: 'File to search in')-> 'List of Paragraph Titles':
        ''' It finds the titles of each paragraph, based on the information of known patterns 
            that appear before titles, as well l, and saves the titles in a list. It then returns the list.
        '''
        return self._tools.find_chapt_titles(file)
    """

    def get_titles_and_chapters(self, file) -> (['titles'], ['chapters']):
        ''' Returns the titles and corresponding chapters of the given file
        '''
        return self._tools.read_file(file)

    def create_html(self, notesName, titles, chapters) -> None:
        ''' Creates the html 
        '''
        self._converter.create_html_file(notesName, titles, chapters)
    
