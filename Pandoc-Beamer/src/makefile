TEX = pdflatex  # xelatex
PANDOC = pandoc
TFLAGS = -interaction=batchmode
PFLAGS = -t beamer --slide-level=2 --variable="institute:University of Wyoming" --variable="shortinstitute:UWyo" --variable="shorttitle:PRML" --variable="shortauthor:L. Jin" --template=template.tex
PTFLAGS = -t beamer --slide-level=2
ETHEME = -V colortheme:crane -V theme:metropolis -V fonttheme:professionalfonts
MTHEME = -V colortheme:crane -V theme:Madrid -V fonttheme:professionalfonts
RTHEME = -V colortheme:crane -V theme:Rochester -V fonttheme:professionalfonts
WTHEME = -V colortheme:crane -V theme:Warsaw -V fonttheme:professionalfonts
OUTPUTFOLDER = ..

PDFFILES = slide_main slide slide_warsaw slide_rochester slide_metropolis slide_madrid

TEXFILES = body

.DEFAULT_GOAL := slide_madrid

all: $(PDFFILES)

clean: 
	rm -rf $(TEXFILES:=.out) $(TEXFILES:=.aux) $(TEXFILES:=.txt) $(TEXFILES:=.idx) $(TEXFILES:=.log) $(TEXFILES:=.nav) $(TEXFILES:=.toc) $(TEXFILES:=.snm) $(TEXFILES:=.tex)

distclean: clean
	rm -rf $(PDFFILES:=.out) $(PDFFILES:=.aux) $(PDFFILES:=.txt) $(PDFFILES:=.idx) $(PDFFILES:=.log) $(addprefix $(OUTPUTFOLDER)/, $(PDFFILES:=.pdf)) $(PDFFILES:=.nav) $(PDFFILES:=.toc) $(PDFFILES:=.snm)  $(addprefix $(OUTPUTFOLDER)/, $(TEXFILES:=.pdf))

slide: body.pdc
	$(PANDOC) $(PFLAGS) $(RTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_rochester: body.pdc
	$(PANDOC) $(PFLAGS) $(RTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_madrid: body.pdc
	$(PANDOC) $(PFLAGS) $(MTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_metropolis: body.pdc
	$(PANDOC) $(PFLAGS) $(ETHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_warsaw: body.pdc
	$(PANDOC) $(PFLAGS) $(WTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

body: body.pdc
	$(PANDOC) $(PTFLAGS) $< -o $@.tex

slide_main: main.tex body
	$(TEX) $(TFLAGS) --jobname=$@ $<
	$(TEX) $(TFLAGS) --jobname=$@ $<
	mv $@.pdf $(OUTPUTFOLDER)/$@.pdf
	rm -rf $(@:=.log) $(@:=.out) $(@:=.aux) $(@:=.txt) $(@:=.idx) $(@:=.log) $(@:=.nav) $(@:=.toc) $(@:=.snm)

