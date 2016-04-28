#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# jobJournal.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import time as t
import csv


class MainApp:

    def __init__(self, master):

        master.title("DAILY JOB JOURNAL")
        self.style = ttk.Style()
        master.configure(background='#ececec', padx=30, pady=20)
        master.resizable(False, False)

        # job label
        ttk.Label(master, text="Job #:").grid(
            row=0, column=0, padx=10, pady=10, sticky="W")
        # job text entry box
        self.job = ttk.Entry(master)
        self.job.grid(row=1, column=0, padx=10, sticky="W")

        # project label
        ttk.Label(master, text="Project:").grid(
            row=0, column=1, padx=10, pady=10, sticky="W")
        # project text entry box
        self.project = ttk.Entry(master)
        self.project.grid(row=1, column=1, padx=10, sticky="W")

        # date label
        ttk.Label(master, text="Date (MM/DD/YY):").grid(
            row=2, column=0, padx=10, pady=10, sticky="W")
        # date entry
        self.date = ttk.Entry(master)
        self.date.grid(row=3, column=0, padx=10, sticky="W")

        # hours label
        ttk.Label(master, text="Hours:").grid(
            row=2, column=1, padx=10, pady=10, sticky="W")
        # hours entry
        self.hours = ttk.Entry(master)
        # self.hours.set("ie. 1.5")
        self.hours.grid(row=3, column=1, padx=10, sticky="W")

        # notes label
        ttk.Label(master, text="Notes:").grid(
            row=5, column=0, padx=10, pady=10, sticky="W")
        # notes text entry box
        self.notes = tk.Text(master, width=75, height=10)
        self.notes.config(borderwidth=1)
        self.notes.grid(row=6, column=0, columnspan=2, padx=10,
                        ipadx=5, ipady=5, sticky="W")

        # submit button
        self.submit_button = ttk.Button(
            master, text="Submit", command=self.checkJob)
        self.submit_button.grid(
            row=7, column=1, padx=10, pady=10, sticky="W")

        # clear button
        self.clear_button = ttk.Button(
            master, text="Clear", command=self.clear)
        self.clear_button.grid(row=7, column=1, padx=10, pady=10, sticky="E")

    def checkJob(self):
        jobLen = len(self.job.get())
        if jobLen > 0:
            self.checkProject()
        else:
            mb.showinfo(title="Whoops!", message="Please enter a job number.")

    def checkProject(self):
        projLen = len(self.project.get())
        if projLen > 0:
            self.checkDate()
        else:
            mb.showinfo(title="Whoops!",
                        message="Please enter information about the project")

    def checkDate(self):
        try:
            t.strptime(self.date.get(), "%m/%d/%y")
            self.checkHours()
        except ValueError:
            mb.showinfo(title="Whoops!",
                        message="Please enter date as 'MM/DD/YY'.")

    def checkHours(self):
        try:
            float(self.hours.get())
            self.checkNotes()
        except ValueError:
            mb.showinfo(
                title="Whoops!", message="Please enter hours as a decimal (For example: '1.5'")

    def checkNotes(self):
        if len(self.notes.get(1.0, "end")) > 1:
            self.submit()
        else:
            mb.askquestion(
                title="Whoops!", message="You haven't entered any notes. Would you like to submit your job journal anyway?")
            return False

    def submit(self):
        csvPath = "/Users/danielkawamoto/Documents/TTA/Old Courses/Python/Drills/JobJournal/JobJournal.csv"
        job = self.job.get()
        project = self.project.get()
        date = self.date.get()
        hours = self.hours.get()
        notes = self.notes.get(1.0, "end")
        with open(csvPath, 'a') as csvfile:
            fieldnames = ['JOB', 'PROJECT', 'DATE', 'HOURS', 'NOTES']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'JOB': job, 'PROJECT': project,
                             'DATE': date, 'HOURS': hours, 'NOTES': notes})
        mb.showinfo(title="Success!", message="You've submitted:\n{}hours for '{}' on {}.".format(
            self.hours.get(), self.project.get(), self.date.get()))
        self.clear()

    def clear(self):
        self.job.delete(0, "end")
        self.project.delete(0, "end")
        self.date.delete(0, "end")
        self.hours.delete(0, "end")
        self.notes.delete(1.0, "end")


def main():
    root = tk.Tk()
    MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
