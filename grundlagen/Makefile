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


.PHONY: all clean FORCE
