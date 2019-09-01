LATEXMK        = latexmk
LMFLAGS        = -xelatex -silent
PLATEX         = pdflatex
XLATEX         = xelatex
BLATEX         = bibtex
PANDOC         = pandoc
LFLAG          = -interaction=batchmode
PFLAG          = -f markdown
RM             = rm -rf
ROOT           = https://raw.githubusercontent.com/jinlibao/Pandoc_LaTeX_Templates/master/LaTeX-101/LaTeX
PY             = compile.py
PROBLEM        = problem.tex
SOLUTION       = solution.tex
MAIN           = main.tex
MF             = Makefile

EXT = *.tex
SRC = $(wildcard $(EXT))
NAME = $(basename $(SRC))
PDF = $(NAME:=.pdf)

# .DEFAULT_GOAL := all
.DEFAULT_GOAL := compile

all: $(PDF) clean

body.pdf:
	pwd

%.pdf: %.tex
	$(LATEXMK) $(LMFLAGS) $<
	$(LATEXMK) -c

compile:
	./compile.py

update_problem:
	mv $(PROBLEM) $(PROBLEM).old
	wget -q $(ROOT)/$(PROBLEM)
	if [ -f $(PROBLEM) ]; then rm $(PROBLEM).old; else mv $(PROBLEM).old $(PROBLEM); fi

update_solution:
	mv $(SOLUTION) $(SOLUTION).old
	wget -q $(ROOT)/$(SOLUTION)
	if [ -f $(SOLUTION) ]; then rm $(SOLUTION).old; else mv $(SOLUTION).old $(SOLUTION); fi

update_main:
	mv $(MAIN) $(MAIN).old
	wget -q $(ROOT)/$(MAIN)
	if [ -f $(MAIN) ]; then rm $(MAIN).old; else mv $(MAIN).old $(MAIN); fi

update_compile:
	mv $(PY) $(PY).old
	wget -q $(ROOT)/$(PY)
	if [ -f $(PY) ]; then rm $(PY).old; chmod 755 $(PY); else mv $(PY).old $(PY); fi

update_makefile:
	mv $(MF) $(MF).old
	wget -q $(ROOT)/$(MF)
	if [ -f $(MF) ]; then rm $(MF).old; else mv $(MF).old $(MF); fi

update: update_problem update_solution update_main update_compile update_makefile

clean:
	$(LATEXMK) -c
	$(RM) $(NAME:=.out) $(NAME:=.blg) $(NAME:=.bbl) $(NAME:=.bib) $(NAME:=.idx) $(NAME:=.aux) $(NAME:=.log) $(NAME:=.txt) $(NAME:=.xdv)

distclean: clean
	$(LATEXMK) -C
	$(RM) $(NAME:=.pdf) ../*.pdf
