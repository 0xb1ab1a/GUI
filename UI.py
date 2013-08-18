__author__ = 'Admin'
from tkinter import *


class MainWin():
    def __init__(self, workspace):
        self.workspace = workspace
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

    def content(self):
        counter, self.columns_lst, column_titles = 0, [], ['Name', 'Type', 'X', 'Y']
        for column_title in column_titles:
            column = Listbox(self.workspace)
            column.grid(row=1, column=counter)
            self.columns_lst.append(column)
            LabelProcess(self.workspace, column_title, 'Tahoma 10', 0, counter, N).table()
            counter += 1


    def lstbox(self):
        return self.columns_lst


class NewWin():
    def __init__(self, workspace):
        self.workspace = workspace

    def new_win_body(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        self.row_counter, self.entrys = 0, []
        LabelProcess(self.new_win, ' ', 'Tahoma 10', 6, 0, NW).table()
        ButtonProcess(self.new_win, 'Save', 100, 1, S, self.button_save_whatdo)
        ButtonProcess(self.new_win, 'Cancel', 100, 1, E, self.new_win.destroy)

    def main_rect(self):
        self.new_win_body()
        labels = ['Name:', 'X:', 'Y:', 'Width:', 'Height:  ']

        for i in labels:
            LabelProcess(self.new_win, i, 'Tahoma 10', self.row_counter, 0, W).table()
            entry = Entry(self.new_win)
            entry.grid(column=1, row=self.row_counter, sticky=N)
            if i == 'Name:' or i == 'X:' or i == 'Y:':
                self.entrys.append(entry)
            self.row_counter += 1
        self.entrys.insert(1, 'Rectangle')


    def main_oval(self):
        self.new_win_body()
        labels, self.checkbutton_var = ['Name:', 'X:', 'Y:', '[x] Is circle:', 'Radius X:', 'Radius Y:'], IntVar()

        for title in labels:
            self.label = Label(self.new_win, text=title, font='Tahoma 10')
            self.label.grid(column=0, row=self.row_counter, sticky=W)
            if title == '[x] Is circle:':
                CheckButtonProcess(self.new_win, 1, self.row_counter, self.checkbutton_whatdo, self.checkbutton_var,
                                   NW)
            else:
                self.entry = Entry(self.new_win)
                self.entry.grid(column=1, row=self.row_counter, sticky=N)
            if title == 'Name:' or title == 'X:' or title == 'Y:':
                self.entrys.append(self.entry)
            self.row_counter += 1
        self.entrys.insert(1, 'Oval')

    def checkbutton_whatdo(self):
        """ TO DO, think how to create method forget in class LabelProcess & EntryProcess"""
        if self.checkbutton_var.get():
            self.entry.grid_remove()
            self.label.grid_remove()
            self.last_title = Label(self.new_win, text='Radius:  ', font='Tahoma 10').grid(column=0, row=4, sticky=W)
        else:
            self.entry.grid()
            self.label.grid()
            self.last_title = Label(self.new_win, text='Radius X:', font='Tahoma 10').grid(column=0, row=4, sticky=W)

    def button_save_whatdo(self):
        self.main_columns = base_win.lstbox()
        for column in range(len(self.main_columns)):
            if column == 1:
                self.main_columns[column].insert(END, self.entrys[column])
            else:
                self.main_columns[column].insert(END, self.entrys[column].get())
        self.new_win.destroy()


# Удалить все классы виджетов ко всем хуям
class ButtonProcess():
    def __init__(self, workspace, text_var, row, col, stick, what_do):
        self.workspace = workspace
        self.but = Button(workspace, text=text_var, command=what_do)
        self.but.grid(row=row, column=col, sticky=stick)

    def func_any(self):
        self.new_but = Button(self.workspace, text='zalupe', command=self.func_any)
        self.new_but.grid()


class LabelProcess():
    def __init__(self, workspace, text_var, font_var, row, col, stick):
        self.row = row
        self.col = col
        self.stick = stick
        self.label = Label(workspace, text=text_var, font=font_var)

    def table(self):
        self.label.grid(column=self.col, row=self.row, sticky=self.stick)


class ListProcess():
    def __init__(self, workspace, row, col, titles):
        # if len(titles) == 0:
        #     self.maximum = 2
        # else:
        #     self.maximum = len(max(titles, key=len))
        self.listbox = Listbox(workspace)
        for i in titles:
            self.listbox.insert(END, i)
        self.listbox.grid(column=col, row=row)


class EntryProcess():
    def __init__(self, workspace, col, row, stick):
        self.txt = Entry(workspace, bd=5)
        self.txt.grid(column=col, row=row, sticky=stick)


class CheckButtonProcess():
    def __init__(self, workspace, col, row, command, var, stick):
        self.checkbutton = Checkbutton(workspace, variable=var, command=command)
        self.checkbutton.grid(column=col, row=row, sticky=stick)


if __name__ == "__main__":
    root = Tk()
    root.title('Geometric editor')
    base_win = MainWin(root)
    base_win.content()
    new_wind = NewWin(root)        #WAGRAAAHHH
    under_menu = base_win.menu_col('File', {'Exit': root.destroy})
    base_win.menu_ins(under_menu, 0, 'Model',
                      {'Create rectangle': new_wind.main_rect,
                       'Create Oval': new_wind.main_oval,
                       'Remove': NewWin.button_save_whatdo})
    root.mainloop()