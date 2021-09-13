from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("Typing")
image = ImageTk.PhotoImage(Image.open("resource.png"))
mylabel = Label(image=image)
mylabel.grid(row=0,column=0,columnspan=3)
window.attributes("-topmost", TRUE)
window.resizable(0,0)
window.mainloop()