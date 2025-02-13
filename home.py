import tkinter as tk
import os
from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox

root =tk.Tk()

root.title("PDF Tools")

def word():
    root.destroy()
    import docs2pdf
    
def ppt():
    root.destroy()
    import ppt2pdf
    
def excel():
    root.destroy()
    import xlxstopdf
    
def images():
    root.destroy()
    import imgtoPdf

def onclose():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit the application?")
    if response:
        root.destroy()


lbl1 = tk.Label(root, text="Word to PDF")
btn1 = tk.Button(root, text = "Word docs", command= word)

lbl1.grid(row=0, column=0)
btn1.grid(row=0, column=1)

lbl2 = tk.Label(root, text="Excel to PDF")
btn2 = tk.Button(root, text = "Excel docs", command= excel)

lbl2.grid(row=1, column=0)
btn2.grid(row=1, column=1)

lbl3 = tk.Label(root, text="PPT to PDF")
btn3 = tk.Button(root, text = "PPT docs", command= ppt)

lbl3.grid(row=2, column=0)
btn3.grid(row=2, column=1)

lbl4 = tk.Label(root, text="Images to PDF")
btn4 = tk.Button(root, text = "Images", command= images)

lbl4.grid(row=3, column=0)
btn4.grid(row=3, column=1)


root.geometry("650x360")

root.protocol("WM_DELETE_WINDOW", onclose)

root.mainloop()