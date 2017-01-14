#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re

__author__ = 'Libao Jin'
__create_date__ = '01/13/2017'
__last_update_date__ = '01/14/2017'
__copyright__ = "Copyright (c) 2017 Libao Jin"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Libao Jin"
__email__ = "jinlibao@outlook.com"
__status__ = "Production"

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

    def __init__(self):
        '''Initialization of class compile'''
        self.folder = '.'
        self.metadata = [('', '', '', '')]

    def get_metadata(self):
        '''Get information from the folder structure and extract course information, and etc.'''
        folder = self.folder
        pathname = os.path.realpath(folder)
        print(pathname)
        string = '([\w-]+) *(\d{4,5})/(\w*)/([\w\d]*)/'
        pattern = re.compile(string)
        self.metadata = re.findall(pattern, pathname)
        print(self.metadata)

    def generate_filename(self):
        '''Generate filename for output file.'''
        metadata = self.metadata[0]
        print(metadata)
        math = metadata[0]
        course_number = metadata[1]
        doc_type = metadata[2]
        doc_number = metadata[3]
        self.filename = '{0}.{1}.{2}.{3}_{4}.{5}.pdf'.format(math, course_number, doc_type, doc_number, self.last_name, self.first_name)

    def generate_title(self):
        '''Generate title for the article/document.'''
        metadata = self.metadata[0]
        math = metadata[0]
        course_number = metadata[1]
        doc_type = metadata[2]
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

    def update_author(self):
        '''Update author information in the source file to be compiled.'''
        source_file = self.source_file_hw
        author = self.author
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\author{[\w\d\s]*}'
        p = re.compile(string)
        content = p.sub('\\\\author{{{0}}}'.format(author), content)
        f.close()
        f = open(source_file, 'w')
        f.write(content)

    def update_title(self):
        '''Update title in the source file to be compiled.'''
        source_file = self.source_file_hw
        title = self.title
        f = open(source_file, 'r')
        content = f.read()
        string = r'\\title{[\w\d\s-]*}'
        p = re.compile(string)
        content = p.sub('\\\\title{{{0}}}'.format(title), content)
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
        string = r'}\\label{[\w\d-]+}'
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
        content = p.sub(r'\\section*{}{\\textbf ', content, count=1)
        content = p.sub(r'\\newpage\n\\section*{}{\\textbf ', content)
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

    def compile_default(self):
        '''Compile files by calling pandoc, pdflatex and rm commands to keep the file structure organized.'''
        path = '../' + self.filename
        if os.path.exists(path):
            os.remove(path)
        os.system('pdflatex -interaction=batchmode {0}'.format(self.source_file_hw))
        os.system('pdflatex -interaction=batchmode {0}'.format(self.source_file_hw))
        os.system('rm *.log *.aux *.idx *.out *~')
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
        elif sys.argv[1] == '1':
            print('Heading Style: Boldface.')
            self.heading_style_1()
        elif sys.argv[1] == '2':
            print('Heading Style: Template of MATH 5400.')
            self.update_source_file_hw()
            self.heading_style_2()
        else:
            print('Error.')

        self.update_title()
        self.update_author()
        self.compile_default()

if __name__ == '__main__':
    compiler = compile()
    compiler.run()
