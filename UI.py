__author__ = 'Admin'
from tkinter import *


class Button_process():
    def __init__(self, workspace, text_var, process):
        self.but = Button(workspace, text=text_var)
        self.but.pack()
        self.but.bind(process, self.func)
        self.workspace = workspace
        self.text_var = text_var
        self.process = process

    def func(self, event):
        self.new_but = Button(self.workspace, text=self.text_var)
        self.new_but.pack()
        self.new_but.bind(self.process, self.func)


class Label_process():
    def __init__(self, workspace, text_var, font_var):
        self.label = Label(workspace, text=text_var, font=font_var)
        self.label.pack()


class Menu_process():
    def __init__(self, workspace):
        self.workspace = workspace
        self.menu_base = Menu(self.workspace)
        self.workspace.config(menu=self.menu_base)


    def menu_col(self, title, *args):
        self.menu_col_1 = Menu(self.menu_base)
        self.title = title
        self.menu_base.add_cascade(label=self.title, menu=self.menu_col_1)
        for i in args:
            self.menu_col_1.add_command(label=i)
        return self.menu_col_1


    def menu_ins(self, menu_from, title, *args):
        self.menu_from = menu_from
        self.menu_col_2 = Menu(self.menu_from)
        self.title = title
        self.menu_from.add_cascade(label=title, menu=self.menu_col_2)
        for i in args:
            self.menu_col_2.add_command(label=i)


root = Tk()

BaseMenu = Menu_process(root)

under_menu = BaseMenu.menu_col('File', 'Exit')
# under_2_menu = BaseMenu.menu_col('Help')

und_under_menu = BaseMenu.menu_ins(under_menu, 'Model', 'Create rectangle', 'Create Oval')
# und_under_menu = BaseMenu.menu_ins(under_2_menu, 'Version', 'Check for updates', 'Title')

Present_1 = Label_process(root, 'Женечка уже ушел спать?', 'Arial 20')
Button_1 = Button_process(root, 'Нет, он - няша', "<Button-1>")
Button_1 = Button_process(root, 'Да, пойду налимоню ему очко!', "<Button-1>")

root.mainloop()

