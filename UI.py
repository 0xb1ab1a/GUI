__author__ = 'Admin'
from tkinter import *


def destroyer():
    root.destroy()

def crt_geom():
    """Temp func"""
    pass

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
        self.menu_base = Menu(workspace, tearoff=0)
        workspace.config(menu=self.menu_base)

    def menu_col(self, title, inc_dict):
        self.menu_col_1 = Menu(self.menu_base, tearoff=0)
        self.menu_base.add_cascade(label=title, menu=self.menu_col_1)
        for i, j in inc_dict.items():
            if i == "Exit":
                self.menu_col_1.add_separator()
            self.menu_col_1.add_command(label=i, command=j)
        return self.menu_col_1

    def menu_ins(self, menu_from, index, title, inc_dict):
        self.menu_internal = Menu(menu_from, tearoff=0)
        menu_from.insert_cascade(index, label=title, menu=self.menu_internal)
        for i,j in inc_dict.items():
            self.menu_internal.add_command(label=i, command = j)


class Windows:
    def __init__(self, workspace):
        self.new_win = Toplevel(workspace)


root = Tk()

BaseMenu = Menu_process(root)

under_menu = BaseMenu.menu_col('File', {'Exit': destroyer})
# THINK how pass an argument "workspace" to destroyer
# under_2_menu = BaseMenu.menu_col('Help')

und_under_menu = BaseMenu.menu_ins(under_menu, 0, 'Model', {'Create rectangle':crt_geom(), 'Create Oval':crt_geom()})
# und_under_menu = BaseMenu.menu_ins(under_2_menu, 'Version', 'Check for updates', 'Title')

Present_1 = Label_process(root, 'Женечка уже заебал спать?', 'Arial 20')
Button_1 = Button_process(root, 'Нет, он - няша', "<Button-1>")
Button_1 = Button_process(root, 'Да, пойду налимоню ему очко!', "<Button-1>")

# root.destroy()
root.mainloop()
