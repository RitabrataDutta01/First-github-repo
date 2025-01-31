import img2pdf, os, subprocess, sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("Image to PDF")

root.geometry("360x360")

fn1=()
fn1_label = tk.Label(root, text="")
fn1_label.grid(row=0, column=2)

def oc1():
    global fn1
    fn1 = filedialog.askopenfilenames(parent= root, title="Select Image File", filetypes=[("Image Files",".jpg .jpeg .png .bmp")])
    file_names = ', '.join(os.path.basename(file) for file in fn1)
    fn1_label.config(text=file_names)

def oc():
    global fn1
    if fn1:
        pdf_file = "converted.pdf"
        with open(pdf_file, "wb") as f:
            f.write(img2pdf.convert(fn1))
        print("PDF conversion successful!")

        if sys.platform == "win32":
            os.startfile(pdf_file)
        else:
            subprocess.run(['xdg-open', pdf_file])
            
    else:
        print("Please select image files first.")


lbl1 = tk.Label(root, text="Choose the image files:")
btn1 = tk.Button(root, text="Choose", command= oc1)

lbl1.grid(row=0, column=0)
btn1.grid(row=0, column=1)

lbl = tk.Label(root, text="\n")
lbl.grid(row=1,column=0)

lbl3 = tk.Label(root, text="The converted pdf will be present in the same directory as the original image files with the name converted.pdf")
lbl3.grid(row=2, column=0)

lbl4 = tk.Label(root, text="\n")
lbl4.grid(row=3,column=0)

lbl2 = tk.Label(root, text="Click to convert to PDF")
btn2 = tk.Button(root, text="Convert", command=oc)

lbl2.grid(row=4, column=0)
btn2.grid(row=4, column=1)

root.mainloop()

