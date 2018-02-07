pandoc -f markdown -o body.tex body.pdc
pdflatex main.tex
rm *.out *.idx *.bib *.aux *.log
