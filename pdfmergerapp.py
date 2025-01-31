import tkinter as tk
from tkinter import filedialog
import os, PyPDF2

root = tk.Tk()

root.title("Simple PDF Merger")

root.geometry('350x200')

fn1=" "
fn2=" "

fn1_label = tk.Label(root, text="")
fn1_label.grid(row=0, column=2)

fn2_label = tk.Label(root, text="")
fn2_label.grid(row=2, column=2)

def oc1():
    global fn1
    fn1=filedialog.askopenfilename(title="Select PDF File 1", filetypes=[("PDF Files", "*.pdf")])
    fn1_label.config(text=os.path.basename(fn1))

def oc0():
    global fn2
    fn2=filedialog.askopenfilename(title="Select PDF File 1", filetypes=[("PDF Files", "*.pdf")])
    fn2_label.config(text=os.path.basename(fn2))

merger = PyPDF2.PdfMerger()

def oc2():
    global fn1, fn2
    i=0
    for i in range(0,1):
        merger.append(fn1)
        merger.append(fn2)
    mpp =os.path.join(os.path.dirname(fn1), "merged.pdf")
    with open(mpp, "wb") as f:
        merger.write(f)


lbl1 = tk.Label(root, text="Choose File 1")
btn1 = tk.Button(root, text="File 1", command=oc1)

lbl1.grid(row=0, column=0)
btn1.grid(row=0, column=1)

lbl2 = tk.Label(root, text="Choose File 2")
btn2 = tk.Button(root, text="File 2", command=oc0)

lbl2.grid(row=2, column=0)
btn2.grid(row=2, column=1)

lbl3 = tk.Label(root, text="Merge PDF")
btn3 = tk.Button(root, text="Merge", command=oc2)

lbl3.grid(row= 4, column= 0)
btn3.grid(row= 4, column= 1)

s

root.mainloop()
