

"""
Date Check on Food Storage

This script checks the expiration dates from a food list then
reports via message box what foods are expired or will expire
soon.

author: Mark Redd
last modified: June, 2015
"""

from tkMessageBox import showinfo
from datetime import date, timedelta
from sys import exit

try:
	list = open("food_list.txt")
	list_1 = list.readlines()
	list.close()

except IOError:
	new_list = open("food_list.txt", 'w')
	new_list.close()
	list = open("food_list.txt")
	list_1 = list.readlines()
	list.close()

today = date.today()

format_list = []
exp_list = []
mo_exp_list = []
twowk_exp_list = []

for line in list_1:
	try:
		list_2 = []
		line2 = line.replace('-', ' ')
		for s in line2.split():
			if s.isdigit():
				x1 = int(s)
				list_2.append(x1)
		if list_2[2] < 2000:
			raise
		expdate = date(list_2[2], list_2[1], list_2[0])
		
		if expdate < today:
			exp_list.append(line)
		elif expdate - today <= timedelta(30) and\
			expdate - today >= timedelta(15):
			mo_exp_list.append(line)
		elif expdate - today < timedelta(15):
			twowk_exp_list.append(line)
		else:
			pass
	except:
		format_list.append(line)


if exp_list == [] and mo_exp_list == [] and twowk_exp_list == [] and\
	format_list == []:
	exit()

w00 = "".join(format_list)
x11 = "".join(exp_list)
y22 = "".join(mo_exp_list)
z33 = "".join(twowk_exp_list)

if format_list == []:
	ww = ""
else:
	ww = """
Error! The following Items have been formatted incorrectly:
%s
Please delete and re-enter these Items to remove them from this list.
""" % w00

if exp_list == []:
	xx = ""
else:
	xx = """
The following items are expired:
%s
""" % x11

if mo_exp_list == []:
	yy = ""
else:
	yy = """
The following items will expire in 30 days:
%s
""" % y22

if twowk_exp_list == []:
	zz = ""
else:
	zz = """
The following items will expire in 14 days:
%s
""" % z33


seq = (ww, xx, yy, zz)
message1 = "\n".join(seq)

showinfo("Expiration Information", message1)