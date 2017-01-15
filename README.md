# Pandoc_LaTeX_Templates

This repository contains various templates for homework and etc.

## Basic Information

**Maintainer**: [Libao Jin](http://libao.in/)

**Email**: [jinlibao@outlook.com](mailto:jinlibao@outlook.com)

**Create date**: January 13, 2017

**Update date**: January 14, 2017

**Latest version**:  [v1.1.0](https://github.com/jinlibao/Pandoc_LaTeX_Templates/releases/tag/v1.1.0)

## Template 1: Pandoc LaTeX Template for Homework (Pandoc-LaTeX 1000)

### Folder Structure

Here is the basic structure of the folder:

```
.
├── LICENSE
├── Pandoc-LaTeX\ 1000
│   └── Homework
│       └── Template
│           └── LaTeX.Codes
│               ├── abs.vim
│               ├── body.pdc
│               ├── compile.py
│               ├── hw.tex
│               └── hw_template.tex
└── README.md
```

Ideally, the folder `Pandoc-LaTeX\ 1000` can be extended as follows:

```
MATH5200
├── Homework
│   ├── 1
│   │   ├── LaTeX.Codes
│   │   │   ├── abs.vim
│   │   │   ├── body.pdc
│   │   │   ├── body.tex
│   │   │   ├── compile.py
│   │   │   ├── hw.tex
│   │   │   └── hw_template.tex
│   │   └── MATH.5200.Homework.1_Libao.Jin.pdf
│   ├── 2
│   │   ├── LaTeX.Codes
│   │   │   ├── abs.vim
│   │   │   ├── body.pdc
│   │   │   ├── body.tex
│   │   │   ├── compile.py
│   │   │   ├── hw.tex
│   │   │   └── hw_template.tex
│   │   └── MATH.5200.Homework.2_Libao.Jin.pdf
│   └── 3
│       ├── LaTeX.Codes
│       │   ├── abs.vim
│       │   ├── body.pdc
│       │   ├── body.tex
│       │   ├── compile.py
│       │   ├── hw.tex
│       │   └── hw_template.tex
│       └── MATH5200.Homework.3_Libao.Jin.pdf
├── Lecture.Notes
└── Problem.Sets
```

The root folder can be a folder for one specific course, say MATH5200 (Real Variables), which contains several subfolders, like `Homework`, `Lecture.Notes`, `Problem.Sets`, etc. And in the folder Homework, there are also several different subfolders such `1`, `2`, `3`, … which refers to all the homework in the semester.

### Usage

Enter the content into the Pandoc file `body.pdc`, then use `compile.py` to compile to generate the PDF document. Here is the syntax of using the `compile.py`.

```Python
python compile.py [option] # option: empty, 1, 2.
```

or

```Python
./compile.py [option] # option: empty, 1, 2.
```

Note: `hw.tex` and `hw_template.tex` are LaTeX templates if you wish to modify the details of the style.
