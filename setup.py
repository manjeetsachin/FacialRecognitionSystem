import cv2
import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:\program\python_work\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\program\python_work\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="faceIcon.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["faceIcon.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Rahul Bhola",
    executables = executables
    )
