import cv2
from tkinter import *
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1545x840+0+0")  
        self.root.title("Face Recognition System")
        self.root.iconbitmap("faceIcon.ico")

        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)

        # --------- bg image -----------
        img_top = Image.open(r"college_images\background.jpeg")
        img_top = img_top.resize((1545, 795), Image.LANCZOS)

        # Adding Opacity
        img_top = img_top.convert("RGBA")
        img_top.putalpha(128) 

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1545, height=795)

        dev_label = Label(f_lbl,text="Email: rahulbhola2804@gmail.com", font=("times new roman",20,"bold"))
        dev_label.place(x=550,y=400)


        

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()