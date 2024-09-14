import tkinter as tk
import tkinter.font as tk_font

from display import display
from delete import delete_record
from add import add_record
from mark_attendance import mark_attendance

# <-------Tkinter Code (GUI)-------->

root = tk.Tk()
# setting title
root.title("Face Recognition and Attendance System")
# setting window size
width = 578
height = 388
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# <--------------------------------->

btn_add = tk.Button(root)
btn_add["bg"] = "#f0f0f0"
ft = tk_font.Font(family='Times', size=18)
btn_add["font"] = ft
btn_add["fg"] = "#000000"
btn_add["justify"] = "center"
btn_add["text"] = "Add"
btn_add.place(x=68, y=190, width=115, height=50)
btn_add["command"] = lambda: add_record(tb_id.get().strip(), tb_name.get().strip())

btn_delete = tk.Button(root)
btn_delete["bg"] = "#f0f0f0"
ft = tk_font.Font(family='Times', size=18)
btn_delete["font"] = ft
btn_delete["fg"] = "#000000"
btn_delete["justify"] = "center"
btn_delete["text"] = "Delete"
btn_delete.place(x=240, y=190, width=115, height=50)
btn_delete["command"] = lambda: delete_record(tb_id.get().strip(), tb_name.get().strip())

btn_nonattendance = tk.Button(root)
btn_nonattendance["bg"] = "#f0f0f0"
ft = tk_font.Font(family='Times', size=18)
btn_nonattendance["font"] = ft
btn_nonattendance["fg"] = "#000000"
btn_nonattendance["justify"] = "center"
btn_nonattendance["text"] = "Mark Attendance"
btn_nonattendance.place(x=190, y=270, width=220, height=72)
btn_nonattendance["command"] = mark_attendance

tb_id = tk.Entry(root)
tb_id["borderwidth"] = "1px"
ft = tk_font.Font(family='Times', size=18)
tb_id["font"] = ft
tb_id["fg"] = "#333333"
tb_id["justify"] = "center"
tb_id["text"] = "Enter ID"
tb_id.place(x=170, y=40, width=350, height=45)

tb_name = tk.Entry(root)
tb_name["borderwidth"] = "1px"
ft = tk_font.Font(family='Times', size=18)
tb_name["font"] = ft
tb_name["fg"] = "#333333"
tb_name["justify"] = "center"
tb_name["text"] = "Enter Name"
tb_name.place(x=170, y=110, width=350, height=45)

GLabel_525 = tk.Label(root)
ft = tk_font.Font(family='Times', size=18)
GLabel_525["font"] = ft
GLabel_525["fg"] = "#333333"
GLabel_525["justify"] = "center"
GLabel_525["text"] = "Enter ID"
GLabel_525.place(x=20, y=40, width=128, height=44)

GLabel_354 = tk.Label(root)
ft = tk_font.Font(family='Times', size=18)
GLabel_354["font"] = ft
GLabel_354["fg"] = "#333333"
GLabel_354["justify"] = "center"
GLabel_354["text"] = "Enter Name"
GLabel_354.place(x=20, y=110, width=131, height=44)

btn_display = tk.Button(root)
btn_display["bg"] = "#f0f0f0"
ft = tk_font.Font(family='Times', size=18)
btn_display["font"] = ft
btn_display["fg"] = "#000000"
btn_display["justify"] = "center"
btn_display["text"] = "Display"
btn_display.place(x=410, y=190, width=116, height=50)
btn_display["command"] = display

root.mainloop()
