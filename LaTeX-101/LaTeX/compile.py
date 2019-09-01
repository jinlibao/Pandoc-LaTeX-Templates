#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import platform

__author__ = 'Libao Jin'
__create_date__ = '01/13/2017'
__last_update_date__ = '09/01/2019'
__copyright__ = "Copyright (c) 2019 Libao Jin"
__license__ = "MIT"
__version__ = "2.0.1"
__maintainer__ = "Libao Jin"
__email__ = "jinlibao@outlook.com"
__status__ = "Complete"


class Compiler():
    '''Compile pandoc file to PDF, M$ Word documents etc.'''
    folder = '.'
    metadata = ''
    filename = []
    source_file_body = 'body.tex'
    source_files = ['problem.tex', 'solution.tex', 'main.tex']
    output_files = ['problem.pdf', 'solution.pdf', 'main.pdf']
    title = ''
    last_name = 'Libao'
    first_name = 'Jin'
    email = 'ljin1@uwyo.edu'
    author = r'{0} {1}'.format(last_name, first_name)
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
        if self.platform == 'Windows':
            strings = [
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d+)\\([\w\d\s.-]+)\\([\w\d]+)\\LaTeX',
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d+)\\([\w\d\s.-]+)\\LaTeX',
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d+)\\LaTeX', '([\w-]+)\\LaTeX'
            ]
        else:
            strings = [
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d*)/([\w\d\s.-]+)/([\w\d]+)/LaTeX',
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d*)/([\w\d\s.-]+)/LaTeX',
                '([^\d\W/]+?[^\d/-]*){1,1}-?(\d*)/LaTeX', '([\w-]+)/LaTeX'
            ]
        for string in strings:
            pattern = re.compile(string)
            metadata = re.findall(pattern, pathname)
            if len(metadata) > 0:
                self.metadata = metadata
                print(self.metadata)
                break

    def generate_filename(self):
        '''Generate filename for output file.'''
        metadata = self.metadata[0]
        print(metadata)
        subject = metadata[0]
        subject = subject.replace('_', '.')
        subject = subject.replace(' ', '.')
        subject = subject.replace('-', '.')
        if len(metadata) == 1 or (len(metadata) == 2 and len(metadata[1] == 0)):
            self.filename = [
                '{0}.pdf'.format(subject),
                '{0}.{1}.{2}.pdf'.format(subject, self.last_name,
                                         self.first_name),
                '{0}_{1}.{2}.pdf'.format(subject, self.last_name,
                                         self.first_name)
            ]
        if len(metadata) == 2:
            course_number = metadata[1]
            self.filename = [
                '{0}.{1}.pdf'.format(subject, course_number),
                '{0}.{1}.{2}.{3}.pdf'.format(subject, course_number,
                                             self.last_name, self.first_name),
                '{0}.{1}_{2}.{3}.pdf'.format(subject, course_number,
                                             self.last_name, self.first_name)
            ]
        elif len(metadata) == 3:
            course_number = metadata[1]
            doc_type = metadata[2].replace(' ', '.')
            self.filename = [
                '{0}.{1}.{2}.pdf'.format(subject, course_number, doc_type),
                '{0}.{1}.{2}.{3}.{4}.pdf'.format(subject, course_number,
                                                 doc_type, self.last_name,
                                                 self.first_name),
                '{0}.{1}.{2}_{3}.{4}.pdf'.format(subject, course_number,
                                                 doc_type, self.last_name,
                                                 self.first_name)
            ]
        elif len(metadata) == 4:
            course_number = metadata[1]
            doc_type = metadata[2].replace(' ', '.')
            doc_number = metadata[3]
            self.filename = [
                '{0}.{1}.{2}.{3}.pdf'.format(subject, course_number, doc_type,
                                             doc_number),
                '{0}.{1}.{2}.{3}.{4}.{5}.pdf'.format(subject, course_number,
                                                     doc_type, doc_number,
                                                     self.last_name,
                                                     self.first_name),
                '{0}.{1}.{2}.{3}_{4}.{5}.pdf'.format(subject, course_number,
                                                     doc_type, doc_number,
                                                     self.last_name,
                                                     self.first_name)
            ]
        for filename in self.filename:
            filename = filename.replace('..', '.')

    def update_author(self):
        '''Update author information in the source file to be compiled.'''
        for source_file in self.source_files:
            if not os.path.exists(source_file):
                continue
            author = self.author
            f = open(source_file, 'r')
            content = f.read()
            string = r'\\author{[{}()@\\\.\w\d\s]*}\n'
            p = re.compile(string)
            content = p.sub(r'\\author{{{0}}}\n'.format(author), content)
            f.close()
            f = open(source_file, 'w')
            f.write(content)
            f.close()

    def update_title(self):
        '''Update title in the source file to be compiled.'''
        for source_file in self.source_files:
            if not os.path.exists(source_file):
                continue
            title = self.title
            print(title)
            title = title.replace('LaTeX', r'\\LaTeX{}')
            title = title.replace('.', r' ')
            title = title.replace('_', r' ')
            title = title.replace('  ', r' ')
            print(title)
            f = open(source_file, 'r')
            content = f.read()
            string = r'\\title{[{{}}/\\:&\w\d .-]*}\n'
            p = re.compile(string)
            content = p.sub(r'\\title{{{0}}}\n'.format(title), content)
            f.close()
            f = open(source_file, 'w')
            f.write(content)
            f.close()

    def compile(self):
        '''Compile files by calling pandoc, pdflatex and rm commands to keep the file structure organized.'''

        if len(sys.argv) == 2:
            if sys.argv[1] == 'problem.tex' or sys.argv[1] == '0':
                self.compile_pdf([0])
            elif sys.argv[1] == 'solution.tex' or sys.argv[1] == '1':
                self.compile_pdf([1])
            elif sys.argv[1] == 'main.tex' or sys.argv[1] == '2':
                self.compile_pdf([2])
        else:
            self.compile_pdf([0, 1, 2])

    def compile_pdf(self, index):
        for i in index:
            if self.platform == 'Windows':
                path = '..\\' + self.filename[i]
            else:
                path = '../' + self.filename[i]
            # if os.path.exists(path):
            #     os.remove(path)
            if not os.path.exists(self.source_files[i]):
                continue
            if self.platform == 'Windows':
                os.system('latexmk -silent -xelatex {0}'.format(
                    self.source_files[i]))
                os.system('latexmk -c')
                os.system('del *.xdv')
                os.rename('{0}'.format(self.output_files[i]), path)
            else:
                print(i, self.output_files[i])
                os.system('make {0}'.format(self.output_files[i]))
                os.system('make clean')
                os.rename('{0}'.format(self.output_files[i]), path)

    def run(self):
        '''By a series commands to compile the tex file and clean up the unnecessary files.'''
        self.get_metadata()
        self.generate_filename()
        self.generate_title()
        self.update_author()
        self.update_title()
        self.compile()

    def generate_title(self):
        '''Generate title for the article/document.'''
        metadata = self.metadata[0]
        subject = metadata[0]
        if len(metadata) == 1:
            self.title = '{0}'.format(subject)
            return
        course_number = metadata[1]
        if course_number == '5290':
            course_name = 'Stochastic Processes \& Applications'
        elif course_number == '5200':
            course_name = 'Computational Complexity'
        elif course_number == '5555':
            course_name = 'Machine Learning'
        elif course_number == '5590':
            course_name = 'Convex Geometry'
        elif course_number == '5605':
            course_name = 'Algebraic Topology'
        elif course_number == '5490':
            course_name = 'Mathematics of Flow in Porous Media'
        elif course_number == '5290':
            course_name = 'Stochastic Processes \& Applications'
        elif course_number == '5450':
            course_name = 'Computer Graphics'
        elif course_number == '5010':
            course_name = 'Blockchain Design and Programming'
        elif course_number == '5110':
            course_name = 'Analysis of Algorithms'
        elif course_number == '5590':
            course_name = 'Topic: Cyclotomic Fields \& Applications'
        elif course_number == '5200':
            course_name = 'Real Variables'
        elif course_number == '5255':
            course_name = 'Math Theory of Probability'
        elif course_number == '5590':
            course_name = 'Applied Graph Theory'
        elif course_number == '5290':
            course_name = 'Operator Algebras \& K-Theory'
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
        elif course_number == '5490':
            course_name = 'Dynamic Big Data'
        elif course_number == '5340':
            course_name = 'Computational Methods II'
        elif course_number == '5270':
            course_name = 'Functional Analysis'
        elif course_number == '5590':
            course_name = 'Combinatorics Inverse Problems'
        elif course_number == '101':
            course_name = r'LaTeX Template'
        else:
            course_name = 'Unknown Course Name'

        if len(metadata) == 2:
            self.title = '{0} {1} - {2}'.format(subject, course_number,
                                                course_name)
        elif len(metadata) == 3:
            doc_type = metadata[2].replace('.', ' ')
            self.title = '{0} {1} - {2} {3}'.format(subject, course_number,
                                                    course_name, doc_type)
        elif len(metadata) == 4:
            doc_type = metadata[2].replace('.', ' ')
            doc_number = metadata[3]
            self.title = '{0} {1} - {2} {3} {4}'.format(subject, course_number,
                                                        course_name, doc_type,
                                                        doc_number)
        print(self.title)


if __name__ == '__main__':
    compiler = Compiler()
    compiler.run()
