from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1545x840+0+0")  # Adjusted size to match background image
        self.root.title("Face Recognition System")
        self.root.iconbitmap("faceIcon.ico")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)

         # --------- bg image -----------
        img_top = Image.open(r"college_images\trainData.jpeg")
        img_top = img_top.resize((1545, 795), Image.LANCZOS)

        # Adding Opacity
        img_top = img_top.convert("RGBA")
        img_top.putalpha(128) 
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1545, height=795)

        # ------button-----
        b1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="black", fg="white")
        b1.place(x=0, y=380, width=1535, height=60)
    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ------------ Train the classifier -------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")









if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()