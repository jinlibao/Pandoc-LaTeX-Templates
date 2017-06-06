#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import time
import platform

__author__ = 'Libao Jin'
__create_date__ = '01/13/2017'
__last_update_date__ = '03/07/2017'
__copyright__ = "Copyright (c) 2017 Libao Jin"
__license__ = "MIT"
__version__ = "1.3.0"
__maintainer__ = "Libao Jin"
__email__ = "jinlibao@outlook.com"
__status__ = "Complete"

class compile():
    '''Compile pandoc file to PDF, M$ Word documents etc.'''
    folder = '.'
    metadata = ''
    filename = ''
    source_file_body = 'body.tex'
    source_file_hw = 'hw.tex'
    output_file_hw = 'hw.pdf'
    title = ''
    last_name = 'Libao'
    first_name = 'Jin'
    email = 'ljin1@uwyo.edu'
    author = r'{0} {1} (\\url{{{2}}})'.format(last_name, first_name, email)
    date = '01/01/2017'
    platform = ''

    def __init__(self):
        '''Initialization of class compile'''
        self.folder = '.'
        self.metadata = [('', '', '', '')]
        self.platform = platform.system()

    def get_metadata(self):
        '''Get information from the folder structure and extract course information, and etc.'''
        folder = self.folder
        pathname = os.path.realpath(folder)
        print(pathname)
        print()
        if self.platform == 'Windows':
            string = r'([\w-]+) *(\d{4,5})\\([\w\d\s.-]+)\\([\w\d]+)\\'
        else:
            string = '([\w-]+) *(\d{4,5})/([\w\d\s.-]+)/([\w\d]+)/'
        pattern = re.compile(string)
        self.metadata = re.findall(pattern, pathname)
        print(self.metadata)

    def generate_filename(self):
        '''Generate filename for output file.'''
        metadata = self.metadata[0]
        print(metadata)
        math = metadata[0]
        course_number = metadata[1]
        doc_type = metadata[2].replace(' ', '.')
        doc_number = metadata[3]
        self.filename = '{0}.{1}.{2}.{3}_{4}.{5}.pdf'.format(math, course_number, doc_type, doc_number, self.last_name, self.first_name)

    def generate_title(self):
        '''Generate title for the article/document.'''
        metadata = self.metadata[0]
        math = metadata[0]
        course_number = metadata[1]
        doc_type = metadata[2].replace('.', ' ')
        print(metadata[2])
        print(doc_type)
        doc_number = metadata[3]
        if course_number == '5200':
            course_name = 'Real Variables'
        elif course_number == '5310':
            course_name = 'Computational Methods'
        elif course_number == '5490':
            course_name = 'Nonlinear Trajectory Gen \& Con'
        elif course_number == '5550':
            course_name = 'Abstract Algebra'
        elif course_number == '5500':
            course_name = 'Advanced Linear Algebra'
        elif course_number == '5230':
            course_name = 'Complex Variables'
        elif course_number == '5400':
            course_name = 'Methods of Applied Mathematics'
        else:
            course_name = 'Unknown Course Name'
        self.title = '{0} {1} - {2} {3} {4}'.format(math, course_number, course_name, doc_type, doc_number)
        print(self.title)

    def update_date(self):
        t = time.localtime()
        day = str(t.tm_mday).zfill(2)
        month = str(t.tm_mon).zfill(2)
        year = str(t.tm_year).zfill(4)
        self.date = '{0}/{1}/{2}'.format(month, day, year)

    def update_author_1(self):
        '''Update author information in the source file to be compiled.'''
        source_file = self.source_file_hw
        author = self.author
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\author{[\w\d\s]*}'
        p = re.compile(string)
        content = p.sub(r'\\author{{{0}}}'.format(author), content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def update_author_2(self):
        '''Update author information in the source file to be compiled.'''
        source_file = self.source_file_hw
        author = self.author
        date = self.date
        metadata = self.metadata[0]
        doc_number = str(metadata[3]).zfill(2)
        print(doc_number + date + author)
        f = open(source_file, 'r')
        content = f.read()
        string = r'#\s[\d\w]+, \d{2}/\d{2}/\d{4}}{[\w\d\s@{}()\\\.-]*}'
        p = re.compile(string)
        content = p.sub('# {0}, {1}}}{{{2}}}'.format(doc_number, date, author), content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def update_title(self):
        '''Update title in the source file to be compiled.'''
        source_file = self.source_file_hw
        title = self.title
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\title{[\w\d\s.-]*}'
        p = re.compile(string)
        content = p.sub(r'\\title{{{0}}}'.format(title), content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def update_source_file_hw(self, replacement='hw_template'):
        '''Update source file name according to the option of the chosen document style'''
        self.source_file_hw = self.source_file_hw.replace('hw', replacement)
        self.output_file_hw = self.output_file_hw.replace('hw', replacement)

    def heading_style_1(self):
        '''Change heading style to not numberred heading.'''
        source_file = self.source_file_body
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\section'
        p = re.compile(string)
        content = p.sub(r'\\textbf', content, count=1)
        content = p.sub(r'\\newpage\n\\textbf', content)
        string = r'}\\label{[\w\d-]+}\n'
        p = re.compile(string)
        content = p.sub('.}', content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def heading_style_2(self):
        '''Change heading style that's consistent to the template'''
        source_file = self.source_file_body
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\section{'
        p = re.compile(string)
        content = p.sub(r'\\section*{}{\\bfseries ', content, count=1)
        content = p.sub(r'\\newpage\n\\section*{}{\\bfseries ', content)
        string = r'\\begin{solution}'
        p = re.compile(string)
        content = p.sub(r'{\\em Ans.}', content)
        string = r'\\end{solution}\n'
        p = re.compile(string)
        content = p.sub(r'', content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def update_package(self, option):
        '''Update title in the source file to be compiled.'''
        source_file = self.source_file_hw
        f = open(source_file, 'r')
        content = f.read()
        if option == 'p':
            string = r'^\\usepackage{fontspec}'
            p = re.compile(string, re.MULTILINE)
            content = p.sub(r'% \\usepackage{fontspec}', content)
            string = r'^\\setmonofont\[Scale=0.8\]{Monaco}'
            p = re.compile(string, re.MULTILINE)
            content = p.sub(r'% \\setmonofont[Scale=0.8]{Monaco}', content)
        elif option == 'x':
            string = r'[% ]*\\usepackage{fontspec}'
            p = re.compile(string)
            content = p.sub(r'\\usepackage{fontspec}', content)
            string = r'[% ]*\\setmonofont\[Scale=0.8\]{Monaco}'
            p = re.compile(string)
            content = p.sub(r'\\setmonofont[Scale=0.8]{Monaco}', content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)
        f.close()

    def compile_pdflatex(self):
        '''Compile files by calling pandoc, pdflatex and rm commands to keep the file structure organized.'''
        if self.platform == 'Windows':
            path = '..\\' + self.filename
        else:
            path = '../' + self.filename
        if os.path.exists(path):
            os.remove(path)
        if self.platform == 'Windows':
            os.system('pdflatex -quiet {0}'.format(self.source_file_hw))
            os.system('pdflatex -quiet {0}'.format(self.source_file_hw))
            os.system('del *.log *.aux *.idx *.out *.toc *~')
            os.rename('{0}'.format(self.output_file_hw), path)
        else:
            os.system('pdflatex -interaction=batchmode {0}'.format(self.source_file_hw))
            os.system('pdflatex -interaction=batchmode {0}'.format(self.source_file_hw))
            os.system('rm *.log *.aux *.idx *.out *.toc *~')
            os.rename('{0}'.format(self.output_file_hw), path)

    def compile_xelatex(self):
        '''Compile files by calling pandoc, pdflatex and rm commands to keep the file structure organized.'''
        if self.platform == 'Windows':
            path = '..\\' + self.filename
        else:
            path = '../' + self.filename
        if os.path.exists(path):
            os.remove(path)
        if self.platform == 'Windows':
            os.system('xelatex -quiet {0}'.format(self.source_file_hw))
            os.system('xelatex -quiet {0}'.format(self.source_file_hw))
            os.system('del *.log *.aux *.idx *.out *.toc *~')
            os.rename('{0}'.format(self.output_file_hw), path)
        else:
            os.system('xelatex -interaction=batchmode {0}'.format(self.source_file_hw))
            os.system('xelatex -interaction=batchmode {0}'.format(self.source_file_hw))
            os.system('rm *.log *.aux *.idx *.out *.toc *~')
            os.rename('{0}'.format(self.output_file_hw), path)

    def generate_source_file_body(self):
        '''Generate source file body.tex from body.pdc by using pandoc'''
        os.system('pandoc -f markdown -o body.tex body.pdc')

    def run(self):
        '''By a series commands to compile the tex file and clean up the unnecessary files.'''
        self.get_metadata()
        self.generate_filename()
        self.generate_title()
        self.generate_source_file_body()

        if len(sys.argv) == 1:
            print('Heading Style: Normal.')
            self.update_author_1()
        elif sys.argv[1] == '1':
            print('Heading Style: Boldface.')
            self.heading_style_1()
            self.update_author_1()
        elif sys.argv[1] == '2':
            print('Heading Style: Template of MATH 5400.')
            self.update_date()
            self.update_source_file_hw()
            self.heading_style_2()
            self.update_author_2()
        else:
            print('Error.')

        self.update_title()
        if len(sys.argv) <= 2:
            self.update_package('x')
            self.compile_xelatex()
            self.update_package('p')
        elif sys.argv[2] == 'p':
            self.compile_pdflatex()
            self.update_package('p')
        elif sys.argv[2] == 'x':
            self.update_package('x')
            self.compile_xelatex()
            self.update_package('p')

if __name__ == '__main__':
    compiler = compile()
    compiler.run()
