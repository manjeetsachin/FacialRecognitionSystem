import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from config import MYSQL_PASSWORD

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1545x840+0+0")
        self.root.title("Login")
        self.root.iconbitmap(r"faceIcon.ico")

        # First Image 
        img1 = Image.open(r"college_images\college2.webp")
        img1 = img1.resize((350, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=350, height=130)

        # Second Image
        img2 = Image.open(r"college_images\facialRecognition.jpeg")
        img2 = img2.resize((300, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=350, y=0, width=300, height=130)

        # Third Image
        img3 = Image.open(r"college_images\facialRecognition3.jpeg")
        img3 = img3.resize((300, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=650, y=0, width=300, height=130)
        

        # Fourth Image
        img4 = Image.open(r"college_images\facialRecognition2.jpeg")
        img4 = img4.resize((300, 130), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl4 = Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=950, y=0, width=300, height=130)

        # Fifth Image
        img5 = Image.open(r"college_images\college1.webp")
        img5 = img5.resize((350, 130), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl5 = Label(self.root, image=self.photoimg5)
        f_lbl5.place(x=1250, y=0, width=350, height=130)

        # bg image
        img6 = Image.open(r"college_images\background.jpeg")
        img6 = img6.resize((1545, 710), Image.LANCZOS)
        
        # Adding Opacity
        img6 = img6.convert("RGBA")
        img6.putalpha(128) 
        
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bg_img = Label(self.root, image=self.photoimg6)
        bg_img.place(x=0, y=130, width=1545, height=710)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170,width=340,height=450)

        # Useer Login Image
        img7=Image.open(r"college_images\userLogin.png")
        img7=img7.resize((150,100),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        lblimg7=Label(image=self.photoimg7, bg="black", borderwidth=0)
        lblimg7.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # ---------- Label ------------------
        username = lbl= Label(frame,text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
                           
        password=lbl=Label(frame,text="Password",font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40,y=250,width=270)


        # ----------------- Icon Images ----------------
        img9=Image.open(r"college_images\user.png")
        img9=img9.resize((25, 25),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        lblimg9=Label(image=self.photoimg9, bg="black", borderwidth=0)
        lblimg9.place(x=650, y=323, width=25, height=25)

        img10=Image.open(r"college_images\password.png")
        img10=img10.resize((25, 25),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        lblimg10=Label(image=self.photoimg10, bg="black", borderwidth=0)
        lblimg10.place(x=650, y=393, width=25, height=25)


        #  ---------------- Login button ---------------------
        loginbtn = Button(frame, command=self.login,text="Login",font=("times new roman", 15,"bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ------------------- Register buttob ------------------
        registerbtn = Button(frame, command=self.register_window, text="New User Register",font=("times new roman", 10,"bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # ------------------- Forget Pass ----------------
        loginbtn = Button(frame, command=self.forget_password_window,text="Forget Password",font=("times new roman", 10,"bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Page(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Facial Detection App")
        else:
            conn = mysql.connector.connect(host="127.0.0.1",username="root",password=MYSQL_PASSWORD, database="face_recognizer_register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row== None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #  ---------------------- reset password ----------------------
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror('Error','Please Select Security Question', parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the answer", parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","New Password is Empty", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="127.0.0.1",username="root",password=MYSQL_PASSWORD, database="face_recognizer_register")
            my_cursor= conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row ==None :
                messagebox.showerror("Error","User Not Found", parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                values=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,values)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password Reset Successfully", parent=self.root2)
                self.root2.destroy()



    # ------------------- forget password window -------------------
    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error","Please Enter the Email Addresss to reset password")
        else:
            conn = mysql.connector.connect(host="127.0.0.1",username="root",password=MYSQL_PASSWORD, database="face_recognizer_register")
            my_cursor= conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text= "Forget Password", font=("times new roman", 20,"bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Yuor Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2, text="Security Answer",font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_security.place(x=50, y=180, width=250)

                new_pass=Label(self.root2, text="New Password",font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_pass.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2, command=self.reset_pass, text="Reset", font=("times new roman",15), fg="white", bg="green")
                btn.place(x=100,y=290)




class Register_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # --------- variables ---------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # --------- bg image -----------
        img2 = Image.open(r"college_images\background.jpeg")
        img2 = img2.resize((1545, 900), Image.LANCZOS)
        
        # Adding Opacity
        img2 = img2.convert("RGBA")
        img2.putalpha(128) 
        
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=0, width=1545, height=900)

        # --------- left image ----------
        original_image = Image.open(r"college_images\registerPage.jpeg") # Load the original image
        resized_image = original_image.resize((520, 550), Image.LANCZOS) # Resize the image to fit the box while maintaining the aspect ratio

        # Convert the resized image to PhotoImage
        self.bg1 = ImageTk.PhotoImage(resized_image)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=100, y=100, width=520, height=550)

        # --------- main frame ----------
        frame = Frame(self.root, bg="white")
        frame.place(x=620, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)


        # ---------- label and entry ---------

        # ------ row1
        label_fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        label_fname.place(x=50, y=100)

        self.frame_entry = ttk.Entry(frame, textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        self.frame_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)



        # ------ row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font={"times new roman", 15, "bold"})
        self.txt_contact.place(x=50, y=200,width=250)

        email=Label(frame, text="Email",font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame, textvariable=self.var_email, font=("times new roman",15))
        self.txt_email.place(x=370, y=200, width=250)


        # ------ row3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame, textvariable=self.var_SecurityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Yuor Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame, text="Security Answer",font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman",15))
        self.txt_security.place(x=370, y=270, width=250)


        # ------ row4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame, textvariable=self.var_pass, font={"times new roman", 15, "bold"})
        self.txt_pswd.place(x=50, y=340,width=250)

        confirm_pswd=Label(frame, text="Confirm Password",font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)


        # ---- checkbutton --------------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame, variable=self.var_check, text="I agree The Terms & Conditions",font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=50,y=380)


        # ------- button --------------
        img=Image.open(r"college_images\register.jpeg")
        img=img.resize((180,40),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1=Button(frame, image=self.photoimg, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=470, width=180, height= 40)

        img1=Image.open(r"college_images\login.png")
        img1=img1.resize((180,40),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimg1, command=self.return_login, borderwidth=0, cursor="hand2")
        b2.place(x=370, y=470, width=180, height= 40)

    # ------------ Function Declaration -----------------
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror('Error', 'Password & Confirm Password must be same')
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree out terms and condition")
        else:
            conn = mysql.connector.connect(host="127.0.0.1",username="root",password=MYSQL_PASSWORD, database="face_recognizer_register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_SecurityQ.get(),  
                        self.var_SecurityA.get(),
                        self.var_pass.get()
                    )
                )

            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully", parent=self.root)

    def return_login(self):
        self.root.destroy()









if __name__=="__main__":
    main()