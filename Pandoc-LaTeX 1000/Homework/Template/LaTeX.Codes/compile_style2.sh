rm "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
pdflatex -interaction=batchmode hw_template.tex
pdflatex -interaction=batchmode hw_template.tex
rm *.log
rm *.aux
rm *.idx
rm *.out
rm *~
mv hw_template.pdf "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
open "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
