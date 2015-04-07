'''
Author: Andres Vourakis 
Project Name: Pattis's Notes Organizer(PNO)
Creation Date: April 3rd, 2015
Version: 1.0
Last Edited: April 6th, 2015
Known bugs: 
    1) Doesn't recognize the section for lambdas as a chapter in review.txt
Contributors: Nina Volkmuth
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

    def read_file(self, file: 'file to scan') -> (['titles'], ['chapters']):
        ''' Reads through a file once, splitting the titles and corresponding chapters
            into two separate lists
        '''
        titles = ['Intro']
        chapters = []
        divider_found = False # First divider found
        intro = ''

        for line in file:
            lineStr = self.decode_line(line)

            # If the file doesn't start with a divider, count the first
            #    section as the introduction
            
            if lineStr.rstrip() == self._divider.rstrip() or divider_found:
                
                # Adds the introduction as the first chapter
                if len(chapters) == 0 and len(intro) > 0:
                    chapters.append(intro)
                    
                next_line = file.readline()
                dnext_line = self.decode_line(next_line) # Decoded next line
                if dnext_line == self._eof:
                    dnext_line = self.decode_line(file.readline())
                if dnext_line.rstrip() != self._divider.rstrip():
                    titles.append(dnext_line)
                    paragraph = ''
                    for test_line in file:
                        test_line = self.decode_line(test_line)
                        if test_line.rstrip() != self._divider.rstrip():
                            paragraph += test_line
                        elif test_line.rstrip() == self._divider.rstrip():
                            divider_found = True
                            break
                    chapters.append(paragraph)
                    
            elif not divider_found:
                intro += lineStr
        return (titles, chapters)

    # Sorta optomized the following code above
    """
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
    """
                
    
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

class HTMLConverter():
    
    def __init__(self):
        pass

    def create_html_file(self, notesName, titles, chapters):
        ''' Formats and creates an html file based off of the base file
        '''
        base = open('base.html', 'r')
        out = open(notesName, 'w')
        line = ''

        # Sets up the page
        while line != '<!-- Table of Contents -->\n':
            line = base.readline()
            if line == '<!-- Header -->\n':
                line = base.readline()
                out.write('<h2>{}</h2>'.format(notesName[:-5]))
            out.write(line)

        # Creates table of contents
        out.write(self._create_ToC(titles))

        # Creates chapters
        i = 0
        for t, c in zip(titles, chapters):
            out.write(self._create_chapter(i, t, c))
            i += 1

        # End of the html file(mostly just closing tags)
        while line != '<!-- End -->\n':
            line = base.readline()
            out.write(line)
        base.close()
        out.close()

    def _create_ToC(self, titles) -> str:
        ''' Creates the Table of Contents links, returning all the html as a str
        '''
        result = ''
        for i, title in enumerate(titles):
            result += self._create_link(i, str(i + 1) + " " + title.strip()) + '<br>'
        return result

    def _create_chapter(self, anchor, title, chapter) -> str:
        ''' Puts in an html anchor at the top of each chapter followed by the title
            and then the rest of the chapter. Returns all the html as a str
        '''
        result = '<a name="{}"></a><h1>{}</h1>'.format(anchor, title.strip())
        for line in chapter.split('\n'):
            result += line
        return result

    def _create_link(self, href, text) -> str:
        ''' Creates a link based off of the href and text link text passed in as parameters
        '''
        return '<a href="#{}">{}</a>'.format(href, text)
                    
