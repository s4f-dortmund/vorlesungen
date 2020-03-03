NAME=foliensatz

all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex content/*.tex tex/*.tex
	mkdir -p build
	TEXINPUTS=build:.: lualatex --output-directory=build $(NAME).tex
	#BIBINPUTS=build:.  biber build/$(NAME).bcf
	TEXINPUTS=build:.: lualatex --output-directory=build $(NAME).tex
	TEXINPUTS=build:.: lualatex --output-directory=build $(NAME).tex
	mv build/$(NAME).pdf $(NAME).pdf

clean:
	rm -rf build
