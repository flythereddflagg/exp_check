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
INSTALL_MAKER = makensis
INSTALL_SCRIPT = install_script.nsi
INSTALL_FLAGS = /V4

all: compile installer

compile:
	$(CC) $(CFLAGS) $(SRC)
    
installer:
	$(INSTALL_MAKER) $(INSTALL_FLAGS) $(INSTALL_SCRIPT)

# clean and reset
.PHONY: clean
clean: $(CLEANER)

clean-unix:
	rm -rf ./build ./dist ./__pycache__

clean-windows:
	rmdir /Q/S .\build
	rmdir /Q/S .\dist
	del *.exe
	rmdir /Q/S .\__pycache__

