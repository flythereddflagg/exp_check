CC = javac
CFLAGS = -g -Werror

SRC_FILES = src/slave/LsMan.java\
	src/main.java


all: $(SRC_FILES)
	$(CC) $(CFLAGS) $(SRC_FILES) -d .

.PHONY: clean
clean:
	rm -f *.class
	rm -f *.txt
	rm -rf ./slave/

