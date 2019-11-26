PYCC = pyqtdeploy-build

CFLAGS = --interpreter /usr/bin/python3 --verbose --target android

CONFIG = app_build.pdy

all: download
	pyqtdeploy-sysroot --verbose ./qt_config.json
	$(PYCC) $(CONFIG) $(CFLAGS)

download:
ifeq (,$(wildcard ./*tar*))
	./download.sh
endif

.PHONY: clean
clean:
	rm -rf ./sysroot*
	rm -rf ./build*
	rm -f *tar*
