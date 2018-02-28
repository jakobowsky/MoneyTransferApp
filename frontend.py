from tkinter import *
from backend import Accounts
"""
JakoBank v1 by Jakob Wolitzki
My first project, which helped me to understand basics of 
SQL databases, and GUI in Python
"""

base = Accounts('konta.db')

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("JakoBank")

        l1 = Label(window,text='username')
        l1.grid(row=0,column=0)

        l2 = Label(window, text='account number')
        l2.grid(row=1, column=0)

        l3 = Label(window, text='money')
        l3.grid(row=2, column=0)

        self.username_text=StringVar()
        self.e1 = Entry(window,textvariable=self.username_text)
        self.e1.grid(row=0,column=1)

        self.accnr_text = StringVar()
        self.e2 = Entry(window, textvariable=self.accnr_text)
        self.e2.grid(row=1, column=1)

        self.money_text = StringVar()
        self.e3 = Entry(window, textvariable=self.money_text)
        self.e3.grid(row=2, column=1)

        b1 = Button(window,text="ADD ACC",width=12,command=self.add_command)
        b1.grid(row=3,column=0,columnspan=2)
        b2 = Button(window, text="UPDATE ACC", width=12,command=self.update_command)
        b2.grid(row=4, column=0, columnspan=2)
        b3 = Button(window, text="DELETE ACC", width=12,command=self.delete_command)
        b3.grid(row=5, column=0, columnspan=2)

        l4 = Label(window, text='account number')
        l4.grid(row=6, column=0)

        l5 = Label(window, text='money')
        l5.grid(row=7, column=0)

        self.accnr2_text = StringVar()
        self.e4 = Entry(window, textvariable=self.accnr2_text)
        self.e4.grid(row=6, column=1)

        self.money2_text = StringVar()
        self.e5 = Entry(window, textvariable=self.money2_text)
        self.e5.grid(row=7, column=1)

        b4 = Button(window, text="TRANSFER", width=12,command=self.transfer_command)
        b4.grid(row=8, column=0, columnspan=2)

        self.list1=Listbox(window,height = 15, width = 30)
        self.list1.grid(row = 0 , column = 2,rowspan = 9)

        sb1=Scrollbar(window)
        sb1.grid(row=0,column=3,rowspan=9)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b5=Button(window,text="VIEW ALL",width=12,command=self.view_command)
        b5.grid(row=9,column=0,columnspan=2)

    def get_selected_row(self,event):
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])

    def view_command(self):
        self.list1.delete(0,END)
        for row in base.view():
            self.list1.insert(END,row)

    def add_command(self):
        base.insert(self.username_text.get(),self.accnr_text.get(),self.money_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.username_text.get(),self.accnr_text.get(),self.money_text.get()))

    def update_command(self):
        base.update(self.selected_tuple[0],self.username_text.get(),self.accnr_text.get(),self.money_text.get())

    def delete_command(self):
        base.delete(self.selected_tuple[0])

    def transfer_command(self):
        id2 = base.findID(self.accnr2_text.get())
        # the receiver's money
        moneyR = base.findMoney(self.accnr2_text.get())
        moneyR=int(moneyR)
        base.transfer(self.selected_tuple[0],int(self.money_text.get()),int(self.money2_text.get()),id2,moneyR)



window = Tk()
Window(window)
window.mainloop()