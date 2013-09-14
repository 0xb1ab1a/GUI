from tkinter import *
import tkinter.messagebox


class View():
    def __init__(self):
        self.root = Tk()
        self.root.title('Geometric editor')
        self.mainframe = Frame(self.root)
        self.mainframe.pack()

        self.lstbox_name = Listbox(self.mainframe, selectmode='extended')
        self.lstbox_name.grid(row=1, column=0)
        Label(self.mainframe, text='Name', font='Tahoma 10').grid(column=0, row=0, stick=N)
        self.lstbox_type = Listbox(self.mainframe, selectmode='extended')
        self.lstbox_type.grid(row=1, column=1)
        Label(self.mainframe, text='Type', font='Tahoma 10').grid(column=1, row=0, stick=N)
        self.lstbox_X = Listbox(self.mainframe, selectmode='extended')
        self.lstbox_X.grid(row=1, column=2)
        Label(self.mainframe, text='X', font='Tahoma 10').grid(column=2, row=0, stick=N)
        self.lstbox_Y = Listbox(self.mainframe, selectmode='extended')
        self.lstbox_Y.grid(row=1, column=3)
        Label(self.mainframe, text='Y', font='Tahoma 10').grid(column=3, row=0, stick=N)

        self.menu_main = Menu(self.root, tearoff=0)
        self.root.config(menu=self.menu_main)

        self.menu_file = Menu(self.menu_main, tearoff=0)
        self.menu_main.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', command=self.root.quit)

        self.menu_create = Menu(self.menu_file, tearoff=0)
        self.menu_file.insert_cascade(0, label='Model', menu=self.menu_create)
        self.menu_create.add_command(label='Create rectangle', command=self.rect_win)
        self.menu_create.add_command(label='Create oval', command=self.oval_win)
        self.menu_create.add_command(label='Remove', command=main_controller.remover)


    def hold(self):
        self.root.mainloop()

    def newwin(self):
        self.new_win = Toplevel(self.root)
        self.new_win.title('Create')
        self.nw_frame = Frame(self.new_win)
        self.nw_frame.pack()

        Label(self.nw_frame, text='Name:', font='Tahoma 10').grid(column=0, row=0, stick=W)
        self.name_entry = Entry(self.nw_frame)
        self.name_entry.grid(column=1, row=0, sticky=N)
        Label(self.nw_frame, text='X:', font='Tahoma 10').grid(column=0, row=1, stick=W)
        self.x_entry = Entry(self.nw_frame)
        self.x_entry.grid(column=1, row=1, sticky=N)
        Label(self.nw_frame, text='Y:', font='Tahoma 10').grid(column=0, row=2, stick=W)
        self.y_entry = Entry(self.nw_frame)
        self.y_entry.grid(column=1, row=2, sticky=N)
        Label(self.nw_frame, text=' ', font='Tahoma 10').grid(column=0, row=19)

        Button(self.nw_frame, text='Save', width=6, command=main_controller.savebutton_whatdo).grid(column=0, row=20,
                                                                                                     columnspan=2)
        Button(self.nw_frame, text='Cancel', width=6, command=self.new_win.destroy).grid(column=1, row=20, stick=E)




    def rect_win(self):
        self.newwin()

        Label(self.nw_frame, text='Width:', font='Tahoma 10').grid(column=0, row=3, stick=W)
        self.width_entry = Entry(self.nw_frame)
        self.width_entry.grid(column=1, row=3, sticky=N)
        Label(self.nw_frame, text='Height: ', font='Tahoma 10').grid(column=0, row=4, stick=W)
        self.heigth_entry = Entry(self.nw_frame)
        self.heigth_entry.grid(column=1, row=4, sticky=N)

        main_model.save_entryes()
        main_model.lst_entryes.insert(1, 'Rectangle')
        main_model.lst_entryes.extend([self.width_entry,self.heigth_entry])


    def oval_win(self):
        self.newwin()

        Label(self.nw_frame, text='[x] Is circle:', font='Tahoma 10').grid(column=0, row=3, sticky=W)
        Checkbutton(self.nw_frame, command=main_controller.checkbutton_whatdo, var=main_model.checkbutton_var).grid(
            column=1, row=3, stick=W)
        self.lbl_radx = Label(self.nw_frame, text='Radius X:', font='Tahoma 10')
        self.lbl_radx.grid(column=0, row=4, sticky=W)
        self.radx_entry = Entry(self.nw_frame)
        self.radx_entry.grid(column=1, row=4)
        self.lbl_rady = Label(self.nw_frame, text='Radius Y:', font='Tahoma 10')
        self.lbl_rady.grid(column=0, row=5, sticky=W)
        self.rady_entry = Entry(self.nw_frame)
        self.rady_entry.grid(column=1, row=5)

        main_model.save_entryes()
        main_model.lst_entryes.insert(1, 'Oval')
        main_model.lst_entryes.extend([self.radx_entry,self.rady_entry])



class Model():
    def __init__(self):
        self.lstbox_lst = [main_view.lstbox_name, main_view.lstbox_type, main_view.lstbox_X, main_view.lstbox_Y]
        self.checkbutton_var = IntVar()
        print(self.lstbox_lst)

    def save_entryes(self):
        self.lst_entryes = [main_view.name_entry, main_view.x_entry, main_view.y_entry]


class Controller():
    def __init__(self):
        pass

    def remover(self):
        self.selected_strings = main_model.lstbox_lst[0].curselection()
        for selected_string in range(len(main_model.lstbox_lst[0].curselection())):
            for listbox_numb in range(4):
                main_model.lstbox_lst[listbox_numb].delete(self.selected_strings[-1 - selected_string])
        print('check')


    def checkbutton_whatdo(self):
        if main_model.checkbutton_var.get():
            main_view.rady_entry.grid_remove()
            main_view.lbl_rady.grid_remove()
            main_view.lbl_radx.config(text='Radius:')
            del main_model.lst_entryes[-1]
        else:
            main_view.rady_entry.grid()
            main_view.lbl_rady.grid()
            main_view.lbl_radx.config(text='Radius X:')
            main_model.lst_entryes.append(main_view.rady_entry)

    def savebutton_whatdo(self):
        print(main_model.lst_entryes)
        values_entry = []
        for val_entry in main_model.lst_entryes:
            if isinstance(val_entry, str):
                values_entry.append(val_entry)
            else:
                values_entry.append(val_entry.get())

        for numb_entry in range(len(values_entry)):
            if numb_entry > 1:
                try:
                    int(values_entry[numb_entry])
                    if numb_entry > 3:
                        if values_entry[numb_entry].isdigit():
                            pass
                        else:
                            tkinter.messagebox.showerror('Input error', 'Check that last entered values is positive')
                            break
                except ValueError:
                    tkinter.messagebox.showerror('Input error', 'Check entered values')
                    break
        else:
            for lstbox, val in zip(main_model.lstbox_lst, values_entry):
                lstbox.insert(END, val)
            main_view.new_win.destroy()


if __name__ == "__main__":
    main_controller = Controller()
    main_view = View()
    main_model = Model()
    main_view.hold()
