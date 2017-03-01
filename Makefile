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

.PHONY: midterm, clean, view

midterm:
	$(PDFLATEX) $(MIDTERM_NAME).tex
	$(BIBTEX) $(MIDTERM_NAME).aux
	$(PDFLATEX) $(MIDTERM_NAME).tex
	$(PDFLATEX) $(MIDTERM_NAME).tex

view: midterm
	$(VIEWER) $(MIDTERM_NAME).pdf
	rm *.log *.aux *.out *.blg *.bbl
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

clean:
	rm *.log *.aux *.dvi *.out *.blg *.bbl *.ps *.bak
