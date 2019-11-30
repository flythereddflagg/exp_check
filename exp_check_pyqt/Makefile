PYCC = pyqtdeploy-build
TARGET_FLAG = --target android-64

CFLAGS = --verbose $(TARGET_FLAG)

CONFIG = ./config/app_build.pdy

PYTHON_VERSION = 3.7.2
SIP_VERSION = 4.19.15
QT_MAJOR_VERSION = 5.12
QT_MINOR_VERSION = .2
PYQT5_VERSION = 5.12.1

all: download sysroot build

paths:
	export ANDROID_NDK_ROOT=$HOME/Android/NDK/android-ndk-r20b
	export ANDROID_SDK_ROOT=$HOME/Android/Sdk
	export ANDROID_NDK_PLATFORM=android-24

sysroot:
	pyqtdeploy-sysroot $(CFLAGS) ./config/qt_config.json

download:
ifeq (,$(wildcard ./*tar*))
	wget http://download.qt.io/official_releases/qt/$(QT_MAJOR_VERSION)/$(QT_MAJOR_VERSION)$(QT_MINOR_VERSION)/single/qt-everywhere-src-$(QT_MAJOR_VERSION)$(QT_MINOR_VERSION).tar.xz
	wget https://www.python.org/ftp/python/$(PYTHON_VERSION)/Python-$(PYTHON_VERSION).tar.xz
	wget https://www.riverbankcomputing.com/static/Downloads/sip/$(SIP_VERSION)/sip-$(SIP_VERSION).tar.gz
	wget https://www.riverbankcomputing.com/static/Downloads/PyQt5/$(PYQT5_VERSION)/PyQt5_gpl-$(PYQT5_VERSION).tar.gz
endif

build:
	$(PYCC) $(CONFIG) $(CFLAGS)


.PHONY: clean
clean:
	rm -rf ./sysroot*
	rm -rf ./build*


clean_download:
	rm -f *tar*
