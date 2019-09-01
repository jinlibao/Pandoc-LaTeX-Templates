# Pandoc LaTeX Templates

This repository contains various templates for homework and etc.

## Basic Information

* **Maintainer**: [Libao Jin](https://libaoj.in/)
* **Email**: [jinlibao@outlook.com](mailto:jinlibao@outlook.com)
* **Create date**: 01/13/2017
* **Update date**: 09/01/2019
* **Latest version**:  [v2.0.1](https://github.com/jinlibao/Pandoc_LaTeX_Templates/releases/tag/v2.0.1)

## Template 1: LaTeX-101

This is a pure LaTeX template with `latexmk` builder system, updated Python script `compile.py`, and `Makefile`.

### Prerequisite

This template requires

* LaTeX (texlive, miktex, etc.) being installed on your system
* Python 3
* Make

### Folder Structure

```
LaTeX-101
├── Homework
│   └── 0
│       ├── LaTeX
│       │   ├── Makefile
│       │   ├── body.tex
│       │   ├── compile.py
│       │   ├── main.tex
│       │   ├── problem.tex
│       │   └── solution.tex
│       ├── LaTeX.101.Homework.0.Libao.Jin.pdf
│       ├── LaTeX.101.Homework.0.pdf
│       └── LaTeX.101.Homework.0_Libao.Jin.pdf
├── LaTeX
│   ├── Makefile
│   ├── body.tex
│   ├── compile.py
│   ├── main.tex
│   ├── problem.tex
│   └── solution.tex
├── LaTeX.101.Libao.Jin.pdf
├── LaTeX.101.pdf
└── LaTeX.101_Libao.Jin.pdf
```

The depth of the folder ranges from 1 to 3. As shown above, the `LaTeX` folder can be either located at `Root/LaTeX`, or `Root/Homework/0/LaTeX`. Running `./compile.py` which compile `problem.tex`, `solution.tex`, and `main.tex`, and the filename and title of the generated PDFs will be updated based on the folder structure.

The intents of the predefined `.tex` files are

* `body.tex`: where the main content is located. It is included in  `problem.tex`, `solution.tex`, and `main.tex`.
* `problem.tex`: serves as a problem statement which will ignore the content embraced in the `solution` environment in `body.tex`.
* `solution.tex`: serves as a solution manual.
* `main.tex`: serves as a report.

### Usage

* `compile.py`

  ```Python
  python3 compile.py [option] # option: empty, 1, 2, 3, problem.tex, solutiont.tex, main.tex
  ```

  or

  ```Python
  ./compile.py [option] # option: empty, 1, 2, 3, problem.tex, solutiont.tex, main.tex
  ```

* `Makefile`

  ```shell
  make compile      # same as ./compile.py
  make update       # updates Makefile, compile.py, problem.tex, solution.tex, main.tex
  make problem.pdf  # compiles problem.tex
  make solution.pdf # compiles solution.tex
  make main.pdf     # compiles main.tex
  ```

## Template 2: Pandoc LaTeX Template for Homework (Pandoc-LaTeX 1000)

### Folder Structure

Here is the basic structure of the folder:

```
.
├── LICENSE
├── Pandoc-LaTeX\ 1000
│   └── Homework
│       └── Template
│           └── LaTeX
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
│   │   ├── LaTeX
│   │   │   ├── body.pdc
│   │   │   ├── body.tex
│   │   │   ├── compile.py
│   │   │   ├── hw.tex
│   │   │   └── hw_template.tex
│   │   └── MATH.5200.Homework.1_Libao.Jin.pdf
│   ├── 2
│   │   ├── LaTeX
│   │   │   ├── body.pdc
│   │   │   ├── body.tex
│   │   │   ├── compile.py
│   │   │   ├── hw.tex
│   │   │   └── hw_template.tex
│   │   └── MATH.5200.Homework.2_Libao.Jin.pdf
│   └── 3
│       ├── LaTeX
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


