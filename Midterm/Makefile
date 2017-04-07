PDFLATEX=pdflatex
LATEX=latex
BIBTEX=bibtex
DVI2PDF=dvipdf
PS2PDF=ps2pdf
UNAME:=$(shell uname -s)
ifeq ($(UNAME),Linux)
	VIEWER=xdg-open
endif
ifeq ($(UNAME), Darwin)
	VIEWER=open -a Preview
endif

MIDTERM_NAME=midterm
FINAL_NAME=final_report

.PHONY: clean, view

midterm:
	$(PDFLATEX) $(MIDTERM_NAME).tex
	$(BIBTEX) $(MIDTERM_NAME).aux
	$(PDFLATEX) $(MIDTERM_NAME).tex
	$(PDFLATEX) $(MIDTERM_NAME).tex

final:
	$(PDFLATEX) $(FINAL_NAME).tex
	$(BIBTEX) $(FINAL_NAME).aux
	$(PDFLATEX) $(FINAL_NAME).tex
	$(PDFLATEX) $(FINAL_NAME).tex

view: final
	$(VIEWER) $(FINAL_NAME).pdf
	rm *.log *.aux *.out *.blg *.bbl
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

clean:
	rm *.log *.aux *.dvi *.out *.blg *.bbl *.ps *.bak
