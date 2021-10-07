import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from shutil import copy

from packages.constants.change_constants import get_lines, get_values, put_values # type: ignore
from packages.app import do_app # type: ignore
from packages.helpers.checkers import check_dir # type: ignore
from packages.helpers.manipulators import make_safe_filename # type: ignore



class Application(tk.Frame):
    """
    Main application - this is the GUI for the Form Letter Generator
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.values = get_values(get_lines())
        self.home_folder = os.path.join("FILES", self.values["HOME_FOLDER"])
        self.create_widgets()

    def create_widgets(self):
        """
        Creates all widgets for the GUI interface
        """
        # Set Title
        self.winfo_toplevel().title("Populator")

        # Set information
        information1 = "This program works by taking a CSV file and creating copies of a TXT file with values replaced by the rows on the CSV."
        information2 = "It does so by matching the titles of columns in the CSV to placeholder words in the TXT file."
        information3 = "These titles and placeholders MUST match exactly, they MUST begin with an underscore and MUST be one word (e.g. '_Firstname')."
        information4 = "Two examples have been provided in the FILES directory - PopuList and Georgia Schools."
        information5 = "Due to a weird quirk, please do not include 'Letters' in your folder names."
        self.info1 = tk.Label(self, text=information1)
        self.info2 = tk.Label(self, text=information2)
        self.info3 = tk.Label(self, text=information3)
        self.info4 = tk.Label(self, text=information4)
        self.info5 = tk.Label(self, text=information5)
        self.info1.grid(column=0, columnspan=5, row=0)
        self.info2.grid(column=0, columnspan=5, row=1)
        self.info3.grid(column=0, columnspan=5, row=2)
        self.info4.grid(column=0, columnspan=5, row=3)
        self.info5.grid(column=0, columnspan=5, row=4)

        self.spacer1 = tk.Label(self, text="\n\n")
        self.spacer1.grid(row=5)

        # Create widgets for Folder name
        self.fnameLabel = tk.Label(self, text=f'Change value for folder below, defaults to current value')
        self.fnameLabel.grid(column=0, columnspan=5, row=6)
        self.fnameEntry = tk.Entry(self)
        self.fnameEntry.insert(-1, self.values["HOME_FOLDER"])
        self.fnameEntry.grid(column=2, columnspan=1, row=7)
        self.fnameEntry.bind('<Key-Return>', self.process_folder_name)

        self.submitFname = tk.Button(self)
        self.submitFname["text"] = "Submit new folder name"
        self.submitFname["command"] = self.process_folder_name
        self.submitFname.grid(column=3, columnspan=1, row=7)

        self.spacer2 = tk.Label(self, text="\n")
        self.spacer2.grid(column=0, row=8)

        # Create widgets for csv filename
        self.csvnameLabel = tk.Label(self, text=f'Change value for CSV filename below, defaults to current value')
        self.csvnameLabel.grid(column=0, columnspan=5, row=9)
        self.csvnameEntry = tk.Entry(self)
        self.csvnameEntry.insert(-1, self.values["CSV_FILENAME"])
        self.csvnameEntry.grid(column=2, columnspan=1, row=10)
        self.csvnameEntry.bind('<Key-Return>', self.process_csv_name)

        self.submitCsvname = tk.Button(self)
        self.submitCsvname["text"] = "Submit new CSV name"
        self.submitCsvname["command"] = self.process_csv_name
        self.submitCsvname.grid(column=3, columnspan=1, row=10)

        self.spacer3 = tk.Label(self, text="\n")
        self.spacer3.grid(column=0, row=11)

        # Create widgets for txt filename
        self.txtnameLabel = tk.Label(self, text=f'Change value for TXT filename below, defaults to current value')
        self.txtnameLabel.grid(column=0, columnspan=5, row=12)
        self.txtnameEntry = tk.Entry(self)
        self.txtnameEntry.insert(-1, self.values["TXT_FILENAME"])
        self.txtnameEntry.grid(column=2, columnspan=1, row=13)
        self.txtnameEntry.bind('<Key-Return>', self.process_txt_name)
        
        self.submitTxtname = tk.Button(self)
        self.submitTxtname["text"] = "Submit new TXT name"
        self.submitTxtname["command"] = self.process_txt_name
        self.submitTxtname.grid(column=3, columnspan=1, row=13)

        self.spacer4 = tk.Label(self, text="\n")
        self.spacer4.grid(column=0, columnspan=5, row=14)

        # Create button to create all letters
        self.submitAll = tk.Button(self)
        self.submitAll["text"] = "Create all letters"
        self.submitAll["command"] = self.process_letters
        self.submitAll.grid(column=0, columnspan=5, row=15)

        self.spacer5 = tk.Label(self, text="\n")
        self.spacer5.grid(column=0, row=16)

        # Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(column=0, columnspan=5, row=17)

        self.spacer6 = tk.Label(self, text="\n")
        self.spacer6.grid(column=0, row=18)

    def process_folder_name(self, event=None):
        """
        Retrieves new folder name value and re-writes constants file with it. If the folder doesn't exist,
        it asks the user if they want to create it.
        """
        folder_name = self.fnameEntry.get()
        if check_dir(folder_name, "FILES"):
            answer = messagebox.askyesno(title="Folder Not Found", message="That folder was not found, would you like to create it?")
            if answer:
                path = os.path.join("FILES", make_safe_filename(folder_name))
                os.mkdir(path)
            else:
                messagebox.showerror("Retype Folder Name", "The folder you tried to use does not exist. You either mispelled it or you need to create it. Make sure it is in the FILES directory.")
                return
        self.values["HOME_FOLDER"] = folder_name
        self.home_folder = os.path.join("FILES", self.values["HOME_FOLDER"])
        put_values(self.values)

    def process_csv_name(self, event=None):
        """
        Retrieves new csv name value and re-writes constants file with it. If the file doesn't exist,
        it asks the user if they want to copy another file to use.
        """
        csv_name = self.csvnameEntry.get()
        if check_dir(csv_name, self.home_folder):
            answer = messagebox.askyesno(title="File Note Found", message=f"That CSV file {csv_name} was not found, would you like to choose one to use?")
            if answer:
                filename = filedialog.askopenfilename()
                messagebox.showinfo("Copying File", "Okay, we will copy this file.")
                path = os.path.join(self.home_folder, csv_name)
                copy(filename, path)
            else:
                messagebox.showerror("File Not Found", "You have chosen not to find a file to use. You either mispelled the original name or need to move the proper CSV file into the folder.")
                return
        self.values["CSV_FILENAME"] = csv_name
        put_values(self.values)

    def process_txt_name(self, event=None):
        """
        Retrieves new txt name value and re-writes constants file with it. If the file doesn't exist,
        it asks the user if they want to copy another file to use.
        """
        txt_name = self.txtnameEntry.get()
        if check_dir(txt_name, self.home_folder):
            answer = messagebox.askyesno(title="File Note Found", message=f'That TXT file {txt_name} was not found, would you like to choose one to use?')
            if answer:
                filename = filedialog.askopenfilename()
                messagebox.showinfo("Copying File", "Okay, we will copy this file.")
                path = os.path.join(self.home_folder, txt_name)
                copy(filename, path)
            else:
                messagebox.showerror("File Not Found", "You have chosen not to find a file to use. You either mispelled the original name or need to move the proper TXT file into the folder.")
                return
        self.values["TXT_FILENAME"] = txt_name
        put_values(self.values)

    def process_letters(self, event=None):
        """
        Processes all the letters, checking first that all of the names are updated and valid.
        If successful it will appear with a message telling the user how many letters were created and in which folder
        """
        self.process_folder_name()
        self.process_csv_name()
        self.process_txt_name()

        cont, number_of_letters = do_app(f'FILES/{self.values["HOME_FOLDER"]}', self.values["CSV_FILENAME"], self.values["TXT_FILENAME"])
        if cont: messagebox.showinfo("Success", f"You have successfully created {number_of_letters} letters in the {self.values['HOME_FOLDER']} folder.")
      
        



root = tk.Tk()
app = Application(master=root)
app.mainloop()
