pandoc -f markdown -o body.tex body.pdc
pdflatex hw.tex
rm *.out *.idx *.bib *.aux *.log
