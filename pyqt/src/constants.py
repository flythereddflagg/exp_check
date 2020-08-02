import os
import sys
import json
from PyQt5.QtWidgets import (QApplication, QLabel, QGridLayout,
    QTableWidget, QPushButton, QWidget, QStackedWidget,
    QCalendarWidget, QDateEdit, QLineEdit)


SRC_PATH = os.path.dirname(os.path.abspath(__file__))
LAYOUT_FILENAME = SRC_PATH + "/layout.json"
WIDGET_DICT = {
    "label"    : QLabel,
    "table"    : QTableWidget,
    "button"   : QPushButton,
    "calendar" : QCalendarWidget,
    "entry"    : QLineEdit
}

with open(LAYOUT_FILENAME, 'r') as f:
    LAYOUT_INFO = json.load(f)
