__author__ = 'Admin'
from tkinter import *


class ButtonProcess():
    def __init__(self, workspace, text_var, process, row, col):
        self.but = Button(workspace, text=text_var)
        self.but.grid(row=row, column=col)
        self.but.bind(process, act.func)


class Actions():
    def __init__(self, workspace, text_var, process):
        self.workspace = workspace
        self.text_var = text_var
        self.process = process

    def crt_geom(self):
        """Temp func"""

    pass

    def destroyer(self):
        root.destroy()

    def func(self, event):
        self.new_but = Button(self.workspace, text=self.text_var)
        self.new_but.pack()
        self.new_but.bind(self.process, self.func)


class LabelProcess():
    def __init__(self, workspace, text_var, font_var, row, col):
        self.label = Label(workspace, text=text_var, font=font_var)
        self.label.grid(row=row, column=col)


class ListProcess():
    def __init__(self, workspace, row, col, name):
        if len(name) == 1: self.maximum = len(name[0])
        if len(name) == 0: self.maximum = 2
        else:
            first_it = len(name[0])
            for j in range(len(name) - 1):
                if first_it >= len(name[j + 1]):
                    self.maximum = first_it
                else:
                    first_it = len(name[j + 1])
                    self.maximum = first_it
        self.listbox = Listbox(workspace, height=len(name), width=self.maximum)
        for i in name:
            self.listbox.insert(END, i)
        self.listbox.grid(row=row, column=col)


class MenuProcess():
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
        for i, j in inc_dict.items():
            self.menu_internal.add_command(label=i, command=j)


class Windows:
    def __init__(self, workspace):
        self.new_win = Toplevel(workspace)


if __name__ == "__main__":
    root = Tk()

    base_menu = MenuProcess(root)
    act = Actions(root, 'Newbut', "<Button-1>")

    under_menu = base_menu.menu_col('File', {'Exit': act.destroyer})
    # THINK how pass an argument "workspace" to destroyer
    # under_2_menu = BaseMenu.menu_col('Help')

    und_under_menu = base_menu.menu_ins(under_menu, 0, 'Model',
                                        {'Create rectangle': act.crt_geom(), 'Create Oval': act.crt_geom(),
                                         'Remove': act.crt_geom()})

    # und_under_menu = BaseMenu.menu_ins(under_2_menu, 'Version', 'Check for updates', 'Title')

    column_name = LabelProcess(root, 'Name', 'Tahoma 12', 0, 0)
    column_type = LabelProcess(root, 'Type', 'Tahoma 12', 0, 1)
    column_x = LabelProcess(root, 'X', 'Tahoma 12', 0, 2)
    column_y = LabelProcess(root, 'Y', 'Tahoma 12', 0, 3)
    def_name = ListProcess(root, 1, 0, ['Figure 1', 'Figure 2', 'Figure 23421', 'Figure 1'])
    def_name = ListProcess(root, 1, 1, ['    ','','',''])
    def_name = ListProcess(root, 1, 2, ['    ','','',''])
    def_name = ListProcess(root, 1, 3, ['    ','','',''])
    #button_1 = ButtonProcess(root, 'Нет, он - няша', "<Button-1>", 2, 0)
    #button_1 = ButtonProcess(root, 'Да, пойду налимоню ему очко!', "<Button-1>", 2, 1)
    #button_1 = ButtonProcess(root, 'Да, пойду налимоню ему очко!', "<Button-1>", 2, 1)

    # root.destroy()
    root.mainloop()
