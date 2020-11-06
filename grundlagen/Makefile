NAME=foliensatz
TEXOPTIONS = --lualatex --output-directory=build --interaction=nonstopmode --halt-on-error

all: $(NAME).pdf

# latexmk does its own dependency management, so we always run it
# by stating an impossible prerequesite FORCE
$(NAME).pdf: FORCE | build
	TEXINPUTS=../style: latexmk $(TEXOPTIONS) $(NAME).tex


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

splithandout:
	pdftk "build/${NAME}.pdf" cat "1-22" output "Grundlagen_des_Klimawandels_-_Teil-I_-_Das_Erdsystem.pdf"
	pdftk "build/${NAME}.pdf" cat "23-51" output "Grundlagen_des_Klimawandels_-_Teil-II_-_Faktoren_des_Klimasystems.pdf"
	pdftk "build/${NAME}.pdf" cat "52-77" output "Grundlagen_des_Klimawandels_-_Teil-III_-_Stoffkreislaeufe_Restbudget_und_Kipppunkte.pdf"

.PHONY: all clean FORCE
