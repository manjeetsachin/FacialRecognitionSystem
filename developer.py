from tkinter import *
import cv2
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1545x840+0+0")  
        self.root.title("Face Recognition System")
        self.root.iconbitmap("faceIcon.ico")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)

        # --------- bg image -----------
        img_top = Image.open(r"college_images\developer.png")
        img_top = img_top.resize((1545, 795), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1545, height=795)


        

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()