from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter as tk

img_list = []
root = Tk()
root.title('Image to PDF')
  
w = Label(root, text ='Multimedia Conversion (Image and PDF)', font = "50") 
w.pack()

# creating the Function which converts the jpg_to_png
def jpg_to_png():
    global im1
 
    # import the image from the folder
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".jpg"):
 
        im1 = Image.open(import_filename)
 
        # after converting the image save to desired
        # location with the Extersion .png
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im1.save(export_filename)
 
        # displaying the Messaging box with the Success
        messagebox.showinfo("success ", "your Image converted to Png")
    else:
 
        # if Image select is not with the Format of .jpg
        # then display the Error
        Label_2 = Label(root, text="Error!", width=20,
                        fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)
        messagebox.showerror("Fail!!", "Something Went Wrong...")

# creating the Function which converts the png_to_jpg
def png_to_jpg():
    global im1
    import_filename = fd.askopenfilename()
 
    if import_filename.endswith(".png"):
        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")
        im1.save(export_filename)
 
        messagebox.showinfo("success ", "your Image converted to jpg ")
    else:
        Label_2 = Label(root, text="Error!", width=20,
                        fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)
 
        messagebox.showerror("Fail!!", "Something Went Wrong...")

#Image to pdf
def open_file():
    global page
    img_exts = r"*.jpg  *.png *.gif"
    root.filename = filedialog.askopenfilenames(initialdir=".s",
                                                title="Select a file",
                                                filetypes=(
                                                ("PNG Files", img_exts),
                                                ("All files", "*.*")))

    file_list = list(root.filename)

    for name in file_list:
        page = Image.open(name)
        page = page.convert("RGB")
        img_list.append(page)
        my_label = Label(text=name).pack()


def generate_pdf():
    global page
    global img_list
    page.save(r"new_file.pdf", save_all=True,
              append_images=img_list)

    print(img_list)


frame = tk.Frame(root)
frame.pack(pady = 10, padx = 10)
 
button1 = tk.Button(frame, text = "open PDF file",command = open_file)
button1.grid(row = 0, column = 0, padx = 10, pady = 5)
 
button2 = tk.Button(frame, text = "Generate PDF",command = generate_pdf)
button2.grid(row = 0, column = 1, padx = 10, pady = 5)

button3 = tk.Button(frame, text = "JPG_to_PNG",command = jpg_to_png)
button3.grid(row = 1, column = 0, padx = 5, pady = 5)
 
button4 = tk.Button(frame, text = "PNG_to_JPG",command = png_to_jpg)
button4.grid(row = 1, column = 1, padx = 5, pady = 5)

# button5 = tk.Button(frame, text = "Button 5")
# button5.grid(row = 2, column = 0, padx = 5, pady = 5)



b5 = Button(root, text = "Exit",command = exit,activebackground = "red",pady = 10)  


  
b5.pack(side = BOTTOM)

root.geometry("300x150")
root.mainloop()

pages_to_delete = [0] 
infile = PdfFileReader('New_File.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open('file.pdf', 'wb') as f:
    output.write(f)


