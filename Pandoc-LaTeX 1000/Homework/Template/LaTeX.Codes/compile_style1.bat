del "..\Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
pdflatex -quiet hw.tex
pdflatex -quiet hw.tex
del *.log
del *.aux
del *.idx
del *.out
del *~
rename hw.pdf "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
sumatraPDF "../Pandoc-LaTeX.1000.Homework.Template_Libao.Jin.pdf"
