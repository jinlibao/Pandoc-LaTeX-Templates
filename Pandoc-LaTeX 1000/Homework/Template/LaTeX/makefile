#
# makefile
# Libao Jin, 2018-11-05 14:51
#

LATEX = pdflatex
# LATEX = xelatex
PANDOC = pandoc
LFLAG = -interaction=batchmode
PFLAG = -f markdown
RM = rm -rf
ROOT = https://raw.githubusercontent.com/jinlibao/Pandoc_LaTeX_Templates/master/Pandoc-LaTeX%201000/Homework/Template/LaTeX
PY = compile.py
MAIN = main.tex

NAME = main

ALLPROGS = $(NAME:=.tex)

# .DEFAULT_GOAL := all
.DEFAULT_GOAL := compile

all: $(ALLPROGS) clean

body.tex: body.pdc
	$(PANDOC) $(PFLAG) -o $@ $<

main.tex: body.tex
	$(LATEX) $(LFLAG) $@
	$(LATEX) $(LFLAG) $@

compile:
	./compile.py

update_main:
	mv main.tex main.tex.old
	wget -q $(ROOT)/$(MAIN)
	if [ -f $(MAIN) ]; then rm $(MAIN).old; else mv $(MAIN).old $(MAIN); fi

update_compile:
	mv compile.py compile.py.old
	wget -q $(ROOT)/$(PY)
	if [ -f $(PY) ]; then rm $(PY).old; chmod 755 $(PY); else mv $(PY).old $(PY); fi

update: update_main update_compile

clean:
	$(RM) $(NAME:=.out) $(NAME:=.idx) $(NAME:=.bib) $(NAME:=.aux) $(NAME:=.log) $(NAME:=.txt)

distclean: clean
	$(RM) $(NAME:=.pdf) body.tex ../*.pdf *.old
