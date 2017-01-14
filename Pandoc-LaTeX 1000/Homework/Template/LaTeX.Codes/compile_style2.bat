del "..\Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
pdflatex -quiet hw_template.tex
pdflatex -quiet hw_template.tex
del *.log
del *.aux
del *.idx
del *.out
del *~
rename hw_template.pdf "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
sumatraPDF "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
