# For windows and linux

ifeq ($(OS), Windows_NT)
	TARGETS = windows
	CLEANER = clean-windows
else
	TARGETS = linux
	CLEANER = clean-linux
endif

CC = javac
CFLAGS = -g -Werror

SRC_FILES = src/slave/LsMan.java\
	src/slave/ShInter.java\
	src/slave/Engine.java\
	src/main.java

all: $(SRC_FILES)
	$(CC) $(CFLAGS) $(SRC_FILES) -d .

.PHONY: clean
clean:


.PHONY: clean-linux
clean-linux:
	rm -f *.class
	rm -f *.txt
	rm -rf ./slave/

.PHONY: clean-windows
clean-windows:
	del *.class
	rmdir .\slave\ /s /q

.PHONY: clean
clean: $(CLEANER)

