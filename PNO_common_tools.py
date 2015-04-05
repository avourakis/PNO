'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer(PNO)
Creation Date: April 3rd, 2015
Version: 1.0
Last Edited:
Known bugs: 
    1) It doesn't retrieve the last chapter of a file because it can't find the divider at the end. 
       It needs to find EOF. It gets stuck in an infinite loop
    2) It adds a divider in the list of titles because there are 3 consecutive dividers in the notes.
Contributors: 
'''

#PNO_common_tools.py

'''
Default Patterns:
1) Introduction: Title (Starts at the very top) and paragraph.
2) Divider: '------------------------------------------------------------------------------'
3) Chapters: Title (After and empty line) and paragraph (Might contain other dividers).
4) End of line(eol): "\r\n"

NOTE: These are common patterns found in most notes. Some notes may not contain all of them, or might
contain others not mentioned.
'''

'''
High level description:
This module collects information about the know patterns in the text file that would make it easier to organize.
The user can enter their own known patterns or use the Default (works only with Pattis's notes)
'''

EMPTY_LINE = '\r\n'
DIVIDER = '------------------------------------------------------------------------------' + EMPTY_LINE


#import urllib.request as urlreq

class PNO_common_tools:
    def __init__(self, default = None):
        if default == None:
            self._divider = DIVIDER
            self._intro = True #There exists an introduction
            self._chap_titles = True
            self._eof = EMPTY_LINE #End of file 
        else:
            ''' This section will assign known patterns entered by user to variables
            '''
            pass
    
    def find_chapt_titles(self, file: 'file to scan')->'Returns a list of titles':
        ''' Given an open file to scan it returns a list of titles found by following the patters.
        '''
        titles = []
        for line in file:
            lineStr = self.decode_line(line)
            if lineStr == self._divider:
                next_line = file.readline()
                if next_line == EMPTY_LINE:
                    pass
                else:
                    titles.append(self.decode_line(file.readline()))
        return titles
    
    def find_chapt_par(self, title: str, file: 'file to scan')->'Paragraph that follows title':
        ''' Given a title, it returns the paragraph/s (as a string) that follow it until it encounters a divider. 
        '''
        paragraph = ''
        for line in file:
            lineStr = self.decode_line(line)
            if lineStr == title: #self._add_eol(title):
                while True:
                    test_line = self.decode_line(file.readline())
                    if test_line != self._divider: paragraph += test_line #Stops reading lines when it finds divider
                    else: break
        return paragraph 
                
    
    def decode_line(self, line: 'Line to decode')->'Decoded Line':
        try:
            return str(line.decode("utf-8"))
        except UnicodeDecodeError:
            return str(line)
        
    def _add_eol(self, line: str)->'String with eol added':
        ''' Adds end of line to a string.
            Default eof: "\r\n"
        '''
        return line + EMPTY_LINE

                    