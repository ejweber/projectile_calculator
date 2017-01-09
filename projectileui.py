'''Calculate the missing variables in a projectile motion problem.'''

import projectile
from tkinter import Tk, DoubleVar, TclError, RIGHT, StringVar
from tkinter.ttk import Frame, Label, Entry, Button


class App:
    def __init__(self, master):
        # create frame within main window to hold widgets
        mainframe = Frame(master)
        mainframe.grid()

        # create template of necessary variables for auto-generation
        dict_list = ['v', 'angle', 'vx', 'viy', 'vfy', 't', 'deltax', 'deltay']

        # create descriptive text labels (can't auto-generate from template)
        Label(mainframe, text='Launch Speed:', justify=RIGHT).grid(column=0, row=0, sticky='e')
        Label(mainframe, text='Launch Angle:').grid(column=0, row=1, sticky='e')
        Label(mainframe, text='Horizontal Velocity:').grid(column=0, row=2, sticky='e')
        Label(mainframe, text='Initial Vertical Velocity:').grid(column=0, row=3, sticky='e')
        Label(mainframe, text='Final Vertical Velocity:').grid(column=0, row=4, sticky='e')
        Label(mainframe, text='Time:').grid(column=0, row=5, sticky='e')
        Label(mainframe, text='Range').grid(column=0, row=6, sticky='e')
        Label(mainframe, text='Vertical Displacement:').grid(column=0, row=7, sticky='e')

        # create compute button
        Button(mainframe, text="Solve", command=self.compute).grid(row=8, columnspan=3, sticky='ew')

        # create dictionaries to store tk DoubleVars
        # user_entries stores information typed by the user
        # display_entries stores information returned from solve method
        self.user_entries = {}
        self.display_entries = {}

        # auto-generate necessary DoubleVars and necessary widgets
        for key in dict_list:
            self.user_entries[key] = DoubleVar(value='')
            self.display_entries[key] = StringVar(value='Not Calculated')
            temp = Entry(mainframe, textvariable=self.user_entries[key], width=10)
            temp.grid(column=1, row=dict_list.index(key))
            temp = Label(mainframe, textvariable=self.display_entries[key])
            temp.grid(column=2, row=dict_list.index(key), sticky='e')

    def compute(self):
        # format empty entries as None for Projectile.solve() method
        entries = {}
        for key, value in self.user_entries.items():
            try:
                entries[key] = value.get()
            except TclError:
                entries[key] = None

        # use Projectile class to attempt to solve and return dictionary
        solution = projectile.Projectile(**entries)
        if solution.solve() == 'success':
            entries = solution.__dict__

            # set DoubleVars to returned values
            for key, value in entries.items():
                valuestring = '{:.2f}'.format(value)
                self.display_entries[key].set(valuestring)

        # display error if calculation unsuccessful
        else:
            for key, value in entries.items():
                self.display_entries[key].set('Error')
            print(solution.__dict__)

# create main window and run tk loop
root = Tk()
root.title('Projectile Motion Calculator')
App(root)
root.mainloop()
