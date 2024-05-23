"""
This module acts as the front end for our app,
pulling information from the Database
"""

import tkinter as tk
from Database import Database

class Application(tk.Frame):
        
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x400")
        self.master.title("Database Example")
        

        self.catalog = Database()

    def create_widgets(self):
        self.button_GET = tk.Button(self.master,
                               text="Get by ID",
                               command=self.getById)
        self.button_GET.place(x=20, y=20)


        self.appStr = tk.StringVar()
        self.appEntry = tk.Entry(self.master, textvariable=self.appStr, width=27, font=("Calibri 16"))
        self.appEntry.place(x=20, y=60)

    def getById(self):
        #print(self.appStr.get())   
        id = self.appStr.get()
        row = self.catalog.findById(id)
        #print(row)

        info = "Title: " + row["title"] + "\n"
        info += "Course: " + row["course"] + "\n"
        info += "Credits: " + str(row["credits"]) + "\n"
        

        infoLabel = tk.Label(self.master, text=info, font=("Calibri 16")).place(x=20, y=100)
      

mainWindow = tk.Tk()
app = Application(master=mainWindow)
app.create_widgets()
app.mainloop()