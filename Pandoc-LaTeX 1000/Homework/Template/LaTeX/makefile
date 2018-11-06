#
# makefile
# Libao Jin, 2018-11-05 14:51
#

PLATEX = pdflatex
XLATEX = xelatex
BLATEX = bibtex
PANDOC = pandoc
LFLAG = -interaction=batchmode
PFLAG = -f markdown
RM = rm -rf
ROOT = https://raw.githubusercontent.com/jinlibao/Pandoc_LaTeX_Templates/master/Pandoc-LaTeX%201000/Homework/Template/LaTeX
PY = compile.py
MAIN = main.tex
MF = makefile

NAME = main

ALLPROGS = $(NAME)

# .DEFAULT_GOAL := all
.DEFAULT_GOAL := compile

all: $(ALLPROGS) clean

body.tex: body.pdc
	$(PANDOC) $(PFLAG) -o $@ $<

mainp: main.tex body.tex
	$(PLATEX) $(LFLAG) $<
	$(PLATEX) $(LFLAG) $<

main: main.tex body.tex
	$(XLATEX) $(LFLAG) $<
	$(XLATEX) $(LFLAG) $<

mainbib: main.tex body.tex
	$(XLATEX) $(LFLAG) $<
	$(BLATEX) $(NAME)
	$(XLATEX) $(LFLAG) $<
	$(XLATEX) $(LFLAG) $<

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

update_makefile:
	mv main.tex main.tex.old
	wget -q $(ROOT)/$(MF)
	if [ -f $(MF) ]; then rm $(MF).old; else mv $(MF).old $(MF); fi

update: update_main update_compile

clean:
	$(RM) $(NAME:=.out) $(NAME:=.blg) $(NAME:=.bbl)  $(NAME:=.bib) $(NAME:=.idx) $(NAME:=.aux) $(NAME:=.log) $(NAME:=.txt)

distclean: clean
	$(RM) $(NAME:=.pdf) body.tex ../*.pdf
