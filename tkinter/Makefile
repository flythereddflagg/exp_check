# OS agnostic code
ifeq ($(OS),Windows_NT)
CLEANER = clean-windows
else
CLEANER = clean-unix
endif

# python compiler and flags
CC = pyinstaller
CFLAGS = 

SRC = exp_check.spec

all:
	$(CC) $(CFLAGS) $(SRC)


# clean and reset
.PHONY: clean
clean: $(CLEANER)

clean-unix:
	rm -rf ./build ./dist ./__pycache__

clean-windows:
	rmdir /Q/S .\build
	rmdir /Q/S .\dist
	rmdir /Q/S .\__pycache__
