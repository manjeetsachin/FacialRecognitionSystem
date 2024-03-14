import cv2
from tkinter import *
import tkinter
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1545x840+0+0")  # Adjusted size to match background image
        self.root.title("Face Recognition System")
        self.root.iconbitmap("faceIcon.ico")

        # bg image
        img6 = Image.open(r"college_images\background.jpg")
        img6 = img6.resize((1545, 840), Image.LANCZOS)
        
        # Adding Opacity
        img6 = img6.convert("RGBA")
        img6.putalpha(128)  # Adjust the alpha value (0 to 255) for the desired opacity
        
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bg_img = Label(self.root, image=self.photoimg6)
        bg_img.place(x=0, y=0, width=1545, height=840)


        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)


        #  ----------------------- time -------------------------
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font =('times new roman',14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0,y=0, width=110,height=50)
        time()

        # student button
        img7 = Image.open(r"college_images\studentDetails.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, command=self.student_details ,cursor="hand2")
        b1.place(x=200, y=150, width=220, height=220)

        self.b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b1_1.place(x=200, y=350, width=220, height=40)

        # Hover effect bindings
        self.b1_1.bind("<Enter>", self.on_enter_b1)
        self.b1_1.bind("<Leave>", self.on_leave_b1)




        # Detect face button
        img8 = Image.open(r"college_images\faceDetector.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=150, width=220, height=220)

        self.b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b2_1.place(x=500, y=350, width=220, height=40)

        # Hover effect bindings
        self.b2_1.bind("<Enter>", self.on_enter_b2)
        self.b2_1.bind("<Leave>", self.on_leave_b2)




        # Attendence face button
        img9 = Image.open(r"college_images\Attendance.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b3 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=150, width=220, height=220)

        self.b3_1 = Button(bg_img, text="Attendence", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b3_1.place(x=800, y=350, width=220, height=40)

        # Hover effect bindings
        self.b3_1.bind("<Enter>", self.on_enter_b3)
        self.b3_1.bind("<Leave>", self.on_leave_b3)




        # Help button
        img10 = Image.open(r"college_images\helpDesk.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b4 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.helpDesk)
        b4.place(x=1100, y=150, width=220, height=220)

        self.b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.helpDesk, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b4_1.place(x=1100, y=350, width=220, height=40)

        # Hover effect bindings
        self.b4_1.bind("<Enter>", self.on_enter_b4)
        self.b4_1.bind("<Leave>", self.on_leave_b4)




        # Train Face button
        img11 = Image.open(r"college_images\trainData.webp")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b5 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=440, width=220, height=220)

        self.b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b5_1.place(x=200, y=650, width=220, height=40)

        # Hover effect bindings
        self.b5_1.bind("<Enter>", self.on_enter_b5)
        self.b5_1.bind("<Leave>", self.on_leave_b5)




        # Photos face button
        img12 = Image.open(r"college_images\photo.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b6 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=440, width=220, height=220)

        self.b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b6_1.place(x=500, y=650, width=220, height=40)

        # Hover effect bindings
        self.b6_1.bind("<Enter>", self.on_enter_b6)
        self.b6_1.bind("<Leave>", self.on_leave_b6)




        # Developer button
        img13 = Image.open(r"college_images\developer.jpg")
        img13 = img13.resize((240, 220), Image.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        b7 = Button(bg_img, image=self.photoimg13, cursor="hand2",command=self.developer)
        b7.place(x=800, y=440, width=220, height=220)

        self.b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b7_1.place(x=800, y=650, width=220, height=40)

        # Hover effect bindings
        self.b7_1.bind("<Enter>", self.on_enter_b7)
        self.b7_1.bind("<Leave>", self.on_leave_b7)




        # Exit face button
        img14 = Image.open(r"college_images\exit.png")
        img14 = img14.resize((220, 220), Image.LANCZOS)
        self.photoimg14 = ImageTk.PhotoImage(img14)

        b8 = Button(bg_img, image=self.photoimg14, cursor="hand2",command=self.exitBtn)
        b8.place(x=1100, y=440, width=220, height=220)

        self.b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exitBtn, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b8_1.place(x=1100, y=650, width=220, height=40)

        # Hover effect bindings
        self.b8_1.bind("<Enter>", self.on_enter_b8)
        self.b8_1.bind("<Leave>", self.on_leave_b8)

    def open_img(self):
        os.startfile("data")


    # -------------Function buttons--------------------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def helpDesk(self):
        self.new_window = Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def exitBtn(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    


 



    def on_enter_b1(self, event):
        self.b1_1.config(bg="gray")

    def on_leave_b1(self, event):
        self.b1_1.config(bg="black")

    def on_enter_b2(self, event):
        self.b2_1.config(bg="gray")

    def on_leave_b2(self, event):
        self.b2_1.config(bg="black")

    def on_enter_b3(self, event):
        self.b3_1.config(bg="gray")

    def on_leave_b3(self, event):
        self.b3_1.config(bg="black")
    
    def on_enter_b4(self, event):
        self.b4_1.config(bg="gray")

    def on_leave_b4(self, event):
        self.b4_1.config(bg="black")

    def on_enter_b5(self, event):
        self.b5_1.config(bg="gray")

    def on_leave_b5(self, event):
        self.b5_1.config(bg="black")

    def on_enter_b6(self, event):
        self.b6_1.config(bg="gray")

    def on_leave_b6(self, event):
        self.b6_1.config(bg="black")

    def on_enter_b7(self, event):
        self.b7_1.config(bg="gray")

    def on_leave_b7(self, event):
        self.b7_1.config(bg="black")

    def on_enter_b8(self, event):
        self.b8_1.config(bg="gray")

    def on_leave_b8(self, event):
        self.b8_1.config(bg="black")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
