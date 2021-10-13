import tkinter as tk
import threading
from tkinter import ttk
from tkinter import *
from numpy.lib.polynomial import roots

from pandas.core.frame import DataFrame
from backend2 import Scraper
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

from pandastable import Table, TableModel

from PIL import ImageTk, Image

root = tk.Tk()

# Adjust size
root.geometry("1000x1000")

# Add image file
bg = ImageTk.PhotoImage(Image.open("Backgrounds_Triangles.png"))


s = Style()
s.configure('My.TFrame', background='cream')

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=1, y=1)

# Create Frame
frame1 = Frame(root, style='My.TFrame')
frame1.pack(pady=20)

# Progress bar widget
progress = Progressbar(frame1, orient=HORIZONTAL,
                       length=100, mode='indeterminate')


class functions1:
    def submit(self):

        catname = n.get()
        pages = n3.get()
        print(type(pages))
        print("The name of Product is : " + catname)
        t1 = threading.Thread(target=functions1().Bar(pages))
        # t2 = threading.Thread(target=Scraper().dataframe_and_scrap(catname,pages))
        t1.start()
        self.k = Scraper().dataframe_and_scrap(catname, pages)
        # self.k = t2.start()
        t1.join()
        # t2.join()
        self.Take_input(self.k)
        arr.append(self.k)
        n.set("")

    def export(self):
        tag = n2.get()
        print(arr)
        self.m = arr[0]
        if tag == "EXCEL":
            name = asksaveasfile(mode='w', defaultextension=".xls")
            name.write(str(self.m))
            name.close()
        elif tag == "HTML":
            name = asksaveasfile(mode='w', defaultextension=".html")
            name.write(str(self.m))
            name.close()
        else:
            name = asksaveasfile(mode='w', defaultextension=".csv")
            name.write(str(self.m))
            name.close()

    def Take_input(self, k):
        print(k)
        # Output.insert(END,k)
        self.table = pt = Table(frame1, dataframe=k,
                                showtoolbar=True, showstatusbar=True, )
        pt.show()

    def Bar(self, pages):
        import time
        for i in range(pages):
            progress['value'] += (int(100 / pages))
            root.update_idletasks()
            time.sleep(1)


progress.grid(column=3, row=6)

arr = []
# Output = Text(frame1, height = 20,
#              width = 120,
#              bg = "light yellow")

# Output.grid(column=0,row=2000,columnspan=7,rowspan=10)

# label

# label text for title
ttk.Label(frame1, text="Flipkart Scraper",
          background='light gray', foreground="black",
          font=("Times New Roman", 21)).grid(row=0, column=1)

ttk.Label(frame1, text="Select the Product :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=5, padx=10, pady=25, columnspan=1)

ttk.Label(frame1, text="Select the extension :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=6, padx=10, pady=25, columnspan=1)

ttk.Label(frame1, text="Pages :",
          font=("Times New Roman", 12)).grid(column=2,
                                             row=5, padx=10, pady=25, columnspan=1)

# 1 st Combobox creation
n = tk.StringVar()
categorychoosen = ttk.Combobox(frame1, width=27, textvariable=n)

# Adding combobox drop down list
categorychoosen['values'] = (' Skin Cream',
                             ' Perfume',
                             ' Skin Talc',
                             ' Soap',
                             ' Shampoo',
                             ' Skin Oil',
                             ' Hair oil',
                             ' Lipstick',
                             ' Skin Powder',
                             ' Facial products',
                             ' Eyeliner',
                             ' Nail polish')

categorychoosen.grid(column=1, row=5)
categorychoosen.current()

# 2 st Combobox creation
n2 = tk.StringVar()
extensionchoosen = ttk.Combobox(frame1, width=27, textvariable=n2)

# Adding combobox drop down list
extensionchoosen['values'] = (' CSV',
                              ' EXCEL',
                              ' HTML',
                              )

extensionchoosen.grid(column=1, row=6)
extensionchoosen.current()

# 3 st Combobox creation
n3 = tk.IntVar()
pagechoosen = ttk.Combobox(frame1, width=7, textvariable=n3)

# Adding combobox drop down list
pagechoosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

pagechoosen.grid(column=3, row=5)
pagechoosen.current()

btn = Button(frame1, text='Submit',
             command=functions1().submit).grid(column=4, row=5)
btn1 = Button(frame1, text='Export',
              command=functions1().export).grid(column=2, row=6)

# Scraper().dataframe_and_scrap(n)
root.title("FlipKart Scraper")
root.iconbitmap("flipkart_icon-icons.com_62718.ico")
root.wm_minsize(600, 500)
root.resizable(200, 200)
root.wm_maxsize(1000, 600)
root.mainloop()
