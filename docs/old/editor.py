

"""
Food List Editor

This script keeps track of and edits a food storage list in a text file
called 'food_list.txt'. It is designed to be used with the script called
'date_check.py' which acts as a notification system for expired food.

author: Mark Redd
last modified: June 2015
original frame author: Jan Bodnar
www.zetcode.com
"""

from Tkinter import Tk, BOTH, W, Listbox, StringVar, END, Scrollbar,\
    OptionMenu, ACTIVE
from ttk import Frame, Button, Label, Style, Entry
from sys import exit

class FoodGUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Food List Editor")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Food List")
        lbl.grid(sticky=W, pady=4, padx=5)
                
        abtn = Button(self, text="Add Food", command=self.sequence)
        abtn.grid(row=1, column=3)

        dbtn = Button(self, text="Delete Food", command=self.delete_food)
        dbtn.grid(row=2, column=3, pady=4)
		
        upbtn = Button(self, text="Refresh", command=self.update_list)
        upbtn.grid(row=3, column=3)

        cbtn = Button(self, text="Close", command=self.close_program)
        cbtn.grid(row=5, column=3)

        scrollbar = Scrollbar(self, orient="vertical")
        self.lb = Listbox(self, width=50, height=20,\
            yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lb.yview)

        self.make_list()

    def make_list(self):
        while self.lb.size():
            self.lb.delete(0)

        try:
            acts1 = open("food_list.txt")
            acts = acts1.readlines()
            acts1.close()

        except IOError:
            new_list = open("food_list.txt", 'w')
            new_list.close()
            acts1 = open("food_list.txt")
            acts = acts1.readlines()
            acts1.close()

        for i in acts:
            self.lb.insert(END, i)
            
        self.lb.bind("<<ListboxSelect>>")    
            
        self.lb.place(x=5, y=25)

    def sequence(self):
        self.add_food()
        self.update_list()

    def update_list(self):
        del_list = open('food_list.txt')
        del_list2 = del_list.readlines()
        del_list.close()

        new_food_list = open('food_list.txt', 'w')

        for line in del_list2:
            if line != "\n":
                new_food_list.writelines(line)
        new_food_list.close()

        self.make_list()


    def add_food(self):
        if __name__ == '__main__':
            root2 = Tk()
            root2.geometry("500x200+500+300")
            app2 = AddFood(root2, self)
            root2.mainloop()

    def delete_food(self):
        del_f = self.lb.get(ACTIVE)
        del_list = open('food_list.txt')
        del_list2 = del_list.readlines()
        del_list.close()

        new_food_list = open('food_list.txt', 'w')

        for line in del_list2:
            if line != del_f:
                new_food_list.writelines(line)
        new_food_list.close()

        self.update_list()

    def close_program(self):
	    exit(0)



class AddFood(Frame):
  
    def __init__(self, parent, friend):
        Frame.__init__(self, parent)   
        self.friend = friend
        self.parent = parent
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Add Food")
        self.style = Style()
        self.style.theme_use("default")
        self.grid()

        l_name = Label(self.parent, text="Name")
        l_day = Label(self.parent, text="Day")
        l_month = Label(self.parent, text="Month")
        l_year = Label(self.parent, text="Year")

        l_name.grid(row=0, column=3)
        l_day.grid(row=0, column=0)
        l_month.grid(row=0, column=1)
        l_year.grid(row=0, column=2)

        days = []
        months = []
        years = []


        days.extend(range(1, 32))
        months.extend(range(1, 13))
        years.extend(range(2015, 2036))

        days = map(str, days)
        months = map(str, months)
        years = map(str, years)

        self.var_day = StringVar(self.parent)
        self.var_month = StringVar(self.parent)
        self.var_year = StringVar(self.parent)
        self.var_name = StringVar(self.parent)

        self.var_day.set(days[0])
        self.var_month.set(months[0])
        self.var_year.set(years[0])

        f_name = Entry(self.parent, textvariable=self.var_name)
        f_day = apply(OptionMenu, (self.parent, self.var_day) + tuple(days))
        f_month = apply(OptionMenu, (self.parent, self.var_month) +\
            tuple(months))
        f_year = apply(OptionMenu, (self.parent, self.var_year) +\
            tuple(years))

        f_name.grid(row=1, column=3)		
        f_day.grid(row=1, column=0)
        f_month.grid(row=1, column=1)
        f_year.grid(row=1, column=2)


        add_btn = Button(self.parent, text="Add Food", command=self.add_food)
        add_btn.grid(row=0, column=5)

        cancel_btn = Button(self.parent, text="Cancel",\
            command=self.cancel_food)
        cancel_btn.grid(row=1, column=5)



    def add_food(self):
        new_food = "\n%s-%s-%s -- %s" % \
            (self.var_day.get(),
            self.var_month.get(),
            self.var_year.get(),
            self.var_name.get())
        flist = open('food_list.txt', 'a')
        flist.writelines(new_food)
        flist.close()

        self.friend.update_list()

        self.parent.destroy()

    def cancel_food(self):
		self.parent.destroy()

def main():
  
    root = Tk()
    root.geometry("500x400+400+200")
    app = FoodGUI(root)
    root.mainloop()	


if __name__ == '__main__':
    main()
