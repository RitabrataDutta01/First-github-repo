import os, tabula, pandas as pd
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

root = tk.Tk()

fn1 = ' '
fn1_label = tk.Label(root, text= "")
fn1_label.grid(row=0, column=2)

def onclose():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit the application?")
    if response:
        root.destroy()

def oc():
    global fn1
    fn1 = fd.askopenfilename(title= "Select PDF file", filetypes= [("PDF files", "*.pdf")])
    fn1_label.config(text= os.path.basename(fn1))

def oc1():
    global fn1
    if fn1:
        dir = os.path.dirname(fn1)
        csv_path = os.path.join(dir, os.path.splitext(os.path.basename(fn1))[0] + ".csv")
        excel_path = os.path.join(dir, os.path.splitext(os.path.basename(fn1))[0] + ".xlsx")
        
        tabula.convert_into(fn1, csv_path, output_format="csv", pages="all")
        
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
        
            try:
                df = pd.read_csv(csv_path)
                df.to_excel(excel_path, index=False)
                print(f"PDF has been successfully converted to {excel_path}")
        
            except Exception as e:
                print(f"Error reading CSV file: {e}")
        
        else:
            print("Failed to extract data from PDF or CSV file is empty.")
            
            
lbl1 = tk.Label(root, text="Choose the appropriate PDF File:")
btn1 = tk.Button(root, text="Choose", command=oc)

lbl1.grid(row=0, column=0)
btn1.grid(row=0, column=1)

lbl = tk.Label(root, text="\n")
lbl.grid(row=1,column=0)

lbl3 = tk.Label(root, text="The converted pdf will be present in the same directory as the original excel spreadsheet with the name <name of pdf>.xlsx")
lbl3.grid(row=2, column=0)

lbl4 = tk.Label(root, text="\n")
lbl4.grid(row=3,column=0)

lbl2 = tk.Label(root, text="Click to convert to Excel spreadsheet")
btn2 = tk.Button(root, text="Convert", command=oc1)

lbl2.grid(row=4, column=0)
btn2.grid(row=4, column=1)

root.title("PDF to XLXS")

root.geometry("650x360")

root.protocol("WM_DELETE_WINDOW", onclose)

root.mainloop()