TEX = pdflatex  # xelatex
PANDOC = pandoc
TFLAGS = -interaction=batchmode
PFLAGS = -t beamer --slide-level=2 --variable="shorttitle:PRML" --variable="shortauthor:L. Jin" --template=template.tex
PTFLAGS = -t beamer --slide-level=2
WTHEME = -V colortheme:crane -V theme:Warsaw -V fonttheme:professionalfonts
RTHEME = -V colortheme:rose -V theme:Rochester -V fonttheme:professionalfonts
ETHEME = -V colortheme:rose -V theme:metropolis -V fonttheme:professionalfonts

PDFFILES = slide_main slide slide_warsaw slide_rochester slide_metropolis

TEXFILES = body

.DEFAULT_GOAL := all

all: $(PDFFILES)

clean: 
	rm -rf $(TEXFILES:=.out) $(TEXFILES:=.aux) $(TEXFILES:=.txt) $(TEXFILES:=.idx) $(TEXFILES:=.log) $(TEXFILES:=.nav) $(TEXFILES:=.toc) $(TEXFILES:=.snm) $(TEXFILES:=.tex)

distclean: clean
	rm -rf $(PDFFILES:=.out) $(PDFFILES:=.aux) $(PDFFILES:=.txt) $(PDFFILES:=.idx) $(PDFFILES:=.log) $(PDFFILES:=.pdf) $(PDFFILES:=.nav) $(PDFFILES:=.toc) $(PDFFILES:=.snm) $(TEXFILES:=.pdf)

slide_rochester: body.pdc
	$(PANDOC) $(PFLAGS) $(RTHEME) $< -o $@.pdf

slide_warsaw: body.pdc
	$(PANDOC) $(PFLAGS) $(WTHEME) $< -o $@.pdf

slide_metropolis: body.pdc
	$(PANDOC) $(PFLAGS) $(ETHEME) $< -o $@.pdf

slide: body.pdc
	$(PANDOC) $(PFLAGS) $(WTHEME) $< -o $@.pdf

body: body.pdc
	$(PANDOC) $(PTFLAGS) $< -o $@.tex

slide_main: main.tex body
	$(TEX) $(TFLAGS) --jobname=$@ $<
	rm -rf $(@:=.log) $(@:=.out) $(@:=.aux) $(@:=.txt) $(@:=.idx) $(@:=.log) $(@:=.nav) $(@:=.toc) $(@:=.snm)

