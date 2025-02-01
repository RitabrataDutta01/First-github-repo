import os, openpyxl
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()

root.title("XLXS to PDF")
root.geometry("650x360")

fn1 = ' '
fn1_label = tk.Label(root, text="")
fn1_label.grid(row= 0, column= 2)

def oc1():
    global fn1
    fn1 = fd.askopenfilename(title = "Select the Excel Spreadsheet")
    fn1_label.config(text= os.path.basename(fn1))
    
def oc():
    global fn1
    
    wb = openpyxl.load_workbook(fn1)
    
    pdf = FPDF()
    
    pdf.add_page()
    
    pdf.set_font("Arial", size= 15)
    
    for row in wb['Sheet1'].rows:
        for cell in row:
            pdf.cell(200, 10, txt= str(cell.value), ln= True, align= 'L')
    
    file_dir = os.path.dirname(fn1)
    file_name = "converted.pdf"
    file_path = os.path.join(file_dir, file_name)
    pdf.output(file_path)



lbl1 = tk.Label(root, text="Choose the appropriate word document:")
btn1 = tk.Button(root, text="Choose", command=oc1)

lbl1.grid(row=0, column=0)
btn1.grid(row=0, column=1)

lbl = tk.Label(root, text="\n")
lbl.grid(row=1,column=0)

lbl3 = tk.Label(root, text="The converted pdf will be present in the same directory as the original excel spreadsheet with the name converted.pdf")
lbl3.grid(row=2, column=0)

lbl4 = tk.Label(root, text="\n")
lbl4.grid(row=3,column=0)

lbl2 = tk.Label(root, text="Click to convert to PDF")
btn2 = tk.Button(root, text="Convert", command=oc)

lbl2.grid(row=4, column=0)
btn2.grid(row=4, column=1)

root.mainloop()