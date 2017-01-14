pandoc -f markdown -o body.tex body.pdc
rm "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
pdflatex -interaction=batchmode hw.tex
pdflatex -interaction=batchmode hw.tex
rm *.log
rm *.aux
rm *.idx
rm *.out
rm *~
mv hw.pdf "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
open "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
