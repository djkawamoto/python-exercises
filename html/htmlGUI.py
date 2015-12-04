#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# htmlGUI.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MainApp:

    def __init__(self, master):
        master.title('Change your (HTML) body!')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, wraplength=500,
                  text=("In the field below, you may enter whatever you wish to have in the body of your html document. Feel free to use whatever html tags you would like. Don't forget closing tags! \nA few examples:\n<h1></h1> creates a large header\n<p></p> creates a paragraph\n<em></em> makes text italic\n<b></b> makes text bold"),
                  justify='left').pack()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.html_body = tk.Text(self.frame_content,
                                 width=78, height=40, font=('Arial', 10))

        self.html_body.pack()

        ttk.Button(self.frame_content, text='Submit',
                   command=self.submit).pack(expand='True', side='left')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).pack(
            expand='True', side='right')

    def writeHtml(self):
        html = "<html>\n<body>\n{}</body>\n</html>".format(
            self.html_body.get(1.0, 'end'))
        open('test.html', 'w').write(html)

    def submit(self):
        self.writeHtml()
        self.clear()
        messagebox.showinfo(title='Success!', message='Body text updated.')

    def clear(self):
        self.html_body.delete(1.0, 'end')

if __name__ == '__main__':
    root = tk.Tk()
    MainApp = MainApp(root)
    root.mainloop()
