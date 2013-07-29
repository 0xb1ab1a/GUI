__author__ = 'Admin'
from tkinter import *


class ButtonProcess():
    def __init__(self, workspace, text_var, new_text, row, col):
        self.workspace = workspace
        self.new_text = new_text
        self.but = Button(workspace, text=text_var, command=self.func_any)
        self.but.grid(row=row, column=col)


    def func_any(self):
        self.new_but = Button(self.workspace, text=self.new_text, command=self.func_any)
        self.new_but.grid()


class Actions():
    def __init__(self, workspace, action):
        self.workspace = workspace
        self.action = action


    def crt_geom(self):
        """Temp func"""

    pass

    def destroyer(self):
        self.workspace.destroy()


class New_win():
    def __init__(self, workspace):
        self.workspace = workspace

    def main_rect(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        names = ['Name:', 'X:', 'Y:', 'Width:', 'Height:']
        numb_row = 0
        for i in names:
            self.name = LabelProcess(self.new_win, i, 'Tahoma 12', numb_row, 0)
            numb_row += 1

    def main_oval(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        names = ['Name:', 'X:', 'Y:', '[x] Is circle:', 'Radius X:', 'Radius Y: ']
        numb_row = 0
        for i in names:
            self.name = LabelProcess(self.new_win, i, 'Tahoma 12', numb_row, 0)
            numb_row += 1


class LabelProcess():
    def __init__(self, workspace, text_var, font_var, row, col):
        self.label = Label(workspace, text=text_var, font=font_var)
        self.label.grid(row=row, column=col)


class ListProcess():
    def __init__(self, workspace, row, col, name):
        if len(name) == 0:
            self.maximum = 2
        else:
            self.maximum = len(max(name, key=len))
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


if __name__ == "__main__":
    root = Tk()
    root.title('Geometric editor')
    base_menu = MenuProcess(root)
    act = Actions(root, "<Button-1>")
    new_wind = New_win(root)

    under_menu = base_menu.menu_col('File', {'Exit': act.destroyer})
    # THINK how pass an argument "workspace" to destroyer
    # under_2_menu = BaseMenu.menu_col('Help')

    und_under_menu = base_menu.menu_ins(under_menu, 0, 'Model',
                                        {'Create rectangle': new_wind.main_rect,
                                         'Create Oval': new_wind.main_oval,
                                         'Remove': act.crt_geom})

    # und_under_menu = BaseMenu.menu_ins(under_2_menu, 'Version', 'Check for updates', 'Title')

    column_name = LabelProcess(root, 'Name', 'Tahoma 12', 0, 0)
    column_type = LabelProcess(root, 'Type', 'Tahoma 12', 0, 1)
    column_x = LabelProcess(root, 'X', 'Tahoma 12', 0, 2)
    column_y = LabelProcess(root, 'Y', 'Tahoma 12', 0, 3)
    def_name = ListProcess(root, 1, 0, ['Figure 1', 'Figure 2', 'Figure 23421', 'Figure 1'])
    def_name = ListProcess(root, 1, 1, ['    ', '', '', ''])
    def_name = ListProcess(root, 1, 2, ['    ', '', '', ''])
    def_name = ListProcess(root, 1, 3, ['    ', '', '', ''])
    #button_1 = ButtonProcess(root, 'Button name_1', "Button-1", 2, 0)
    #button_1 = ButtonProcess(root, 'Button name_2', "<Button-1>", 2, 1)




    # root.destroy()
    root.mainloop()
