TEX = pdflatex  # xelatex
PANDOC = pandoc
TFLAGS = -interaction=batchmode
PFLAGS = -t beamer --slide-level=3  --variable="institute:Insitute" --variable="shortinstitute:Inst." --variable="shorttitle:Short title" --variable="shortauthor:F. Lastname" --template=template.tex
PFLAGSS = -t beamer --slide-level=3 --variable="seal:yes" --variable="institute:Insitute" --variable="shortinstitute:Inst." --variable="shorttitle:Short title" --variable="shortauthor:F. Lastname" --template=template.tex
PTFLAGS = -t beamer --slide-level=3
BTHEME = -V colortheme:crane -V theme:Bergen -V fonttheme:professionalfonts
BTHEME = -V colortheme:crane -V theme:Berkeley -V fonttheme:professionalfonts
ETHEME = -V colortheme:crane -V theme:metropolis -V fonttheme:professionalfonts
MTHEME = -V colortheme:crane -V theme:Madrid -V fonttheme:professionalfonts
RTHEME = -V colortheme:crane -V theme:Rochester -V fonttheme:professionalfonts
WTHEME = -V colortheme:crane -V theme:Warsaw -V fonttheme:professionalfonts
THEME = -V colortheme:crane -V theme:Warsaw -V fonttheme:professionalfonts
OUTPUTFOLDER = ..

PDFFILES = slide_main slide slide_warsaw slide_rochester slide_metropolis slide_madrid slide_bergen slide_berkeley

TEXFILES = body

.DEFAULT_GOAL := slide

all: $(PDFFILES)

clean: 
	rm -rf $(TEXFILES:=.out) $(TEXFILES:=.aux) $(TEXFILES:=.txt) $(TEXFILES:=.idx) $(TEXFILES:=.log) $(TEXFILES:=.nav) $(TEXFILES:=.toc) $(TEXFILES:=.snm) $(TEXFILES:=.tex)

distclean: clean
	rm -rf $(PDFFILES:=.out) $(PDFFILES:=.aux) $(PDFFILES:=.txt) $(PDFFILES:=.idx) $(PDFFILES:=.log) $(addprefix $(OUTPUTFOLDER)/, $(PDFFILES:=.pdf)) $(PDFFILES:=.nav) $(PDFFILES:=.toc) $(PDFFILES:=.snm)  $(addprefix $(OUTPUTFOLDER)/, $(TEXFILES:=.pdf))

slide: body.pdc
	$(PANDOC) $(PFLAGS) $(THEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_bergen: body.pdc
	$(PANDOC) $(PFLAGSS) $(BTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_berkeley: body.pdc
	$(PANDOC) $(PFLAGS) $(KTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_madrid: body.pdc
	$(PANDOC) $(PFLAGS) $(MTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_metropolis: body.pdc
	$(PANDOC) $(PFLAGS) $(ETHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_rochester: body.pdc
	$(PANDOC) $(PFLAGS) $(RTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

slide_warsaw: body.pdc
	$(PANDOC) $(PFLAGS) $(WTHEME) $< -o $(OUTPUTFOLDER)/$@.pdf

body: body.pdc
	$(PANDOC) $(PTFLAGS) $< -o $@.tex

slide_main: main.tex body
	$(TEX) $(TFLAGS) --shell-escape --jobname=$@ $<
	$(TEX) $(TFLAGS) --shell-escape --jobname=$@ $<
	mv $@.pdf $(OUTPUTFOLDER)/$@.pdf
	rm -rf $(@:=.log) $(@:=.out) $(@:=.aux) $(@:=.txt) $(@:=.idx) $(@:=.log) $(@:=.nav) $(@:=.toc) $(@:=.snm)

