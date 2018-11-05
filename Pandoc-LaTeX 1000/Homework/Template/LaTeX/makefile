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

clean:
	$(RM) $(NAME:=.out) $(NAME:=.idx) $(NAME:=.bib) $(NAME:=.aux) $(NAME:=.log) $(NAME:=.txt)

distclean: clean
	$(RM) $(NAME:=.pdf) body.tex ../*.pdf
