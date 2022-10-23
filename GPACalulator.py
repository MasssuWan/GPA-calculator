#Wansirimanee Wattanasiri 6310742827

from faulthandler import disable
from logging import root
from tkinter import*

root =Tk()
root.title("GPA")
root.geometry("770x450")
root.resizable(0, 0)

COLOR_GRAY = "#3D404E"
COLOR_PINK_RED = "#F35E79"
COLOR_LIGHT_GRAY = "#D8D8DB"
COLOR_LIGHT_PINK = "#FBEFEF"
COLOR_GREEN ="#BEE8B0"

FONT1 = ("FreesiaUPC" , 15)

root.configure(bg=COLOR_GRAY)

#create a file or open a file
def enter_id():
    std_id = str(txt_input_id.get())
    f = open(std_id + ".txt" , "a")
    f.close()
    txt_read()

#write input into txt file
def enter_info():
    std_id = str(txt_input_id.get())
    f = open(std_id + ".txt" , "w")

    sj1 = str(txt_input_sj_1.get())
    sj2 = str(txt_input_sj_2.get())
    sj3 = str(txt_input_sj_3.get())

    nk1 = str(txt_input_nk_1.get())
    nk2 = str(txt_input_nk_2.get())
    nk3 = str(txt_input_nk_3.get())

    g1 = str(txt_input_g_1.get())
    g2 = str(txt_input_g_2.get())
    g3 = str(txt_input_g_3.get())

    #Calculate GPA
    gpa_cal = str(((float(g1) * float(nk1)) + (float(g2) * float(nk2)) + (float(g3) * float(nk3)))/(float(nk1) + float(nk2) + float(nk3)))
    
    f.write( sj1 + "," + nk1 + "," + g1 + "," + sj2 + "," + nk2 + "," + g2 + "," + sj3 + "," + nk3 + "," + g3 + "," + gpa_cal)
    f.close()

#insert GPA
def cal_sc():
    std_id = str(txt_input_id.get())
    f = open(std_id + ".txt" , "r")
    data = f.read().split(",")
    print(data)

    gpa_area.insert(9, data[9])

#split and add each data into their box (load function)
def txt_read():
    std_id = str(txt_input_id.get())
    f = open(std_id + ".txt" , "r")
    data = f.read().split(",")
    print(data)

    input_sj_1.insert(0, data[0])
    input_nk_1.insert(1, data[1])
    input_g_1.insert(2, data[2])

    input_sj_2.insert(3, data[3])
    input_nk_2.insert(4, data[4])
    input_g_2.insert(5, data[5])

    input_sj_3.insert(6, data[6])
    input_nk_3.insert(7, data[7])
    input_g_3.insert(8, data[8])

    f.close()

#delete data and close(destroy) program
def clear():
    std_id = str(txt_input_id.get())
    f = open(std_id + ".txt" , "w")
    f.write("")
    f.close()
    root.destroy()


#id
frame = Frame(root, padx=12, pady=12 ,bg=COLOR_LIGHT_PINK)
frame.pack()

txt_input_lb = Label(frame , text="Student ID" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
txt_input_lb.grid(row=0 , column=0)

txt_input_id = StringVar()
input_id =Entry(frame , textvariable=txt_input_id ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_id.grid(row=0 , column=1)

input_btn = Button(frame , text="  LOAD  " , bg=COLOR_GREEN , fg= COLOR_GRAY , command=enter_id ,font=FONT1 ,bd=0)
input_btn.grid(row=0 , column=2)

#--------------------------------#

txt_input_line_lb = Label(frame , text="--" ,bg=COLOR_LIGHT_PINK)
txt_input_line_lb.grid(row=1 , column=1)

txt_input_line2_lb = Label(frame , text="--" ,bg=COLOR_LIGHT_PINK)
txt_input_line2_lb.grid(row=7 , column=3)

txt_input_line3_lb = Label(frame , text="--" ,bg=COLOR_LIGHT_PINK)
txt_input_line3_lb.grid(row=9 , column=3)

#--------------------------------#

sj_lb1 = Label(frame , text="Subj 1" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
sj_lb1.grid(row=3 , column=0)

sj_lb2 = Label(frame , text="Subj 2" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
sj_lb2.grid(row=4 , column=0)

sj_lb3 = Label(frame , text="Subj 3" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
sj_lb3.grid(row=5 , column=0)

#--------------------------------#

txt_input_sj_lb = Label(frame , text="input Subject" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
txt_input_sj_lb.grid(row=2 , column=1 , padx=2 , pady=2)

txt_input_sj_1 = StringVar()
input_sj_1 = Entry(frame , textvariable=txt_input_sj_1 ,font=FONT1 , bd=0 ,bg=COLOR_LIGHT_GRAY)
input_sj_1.grid(row=3 , column=1 , padx=2 , pady=2)

txt_input_sj_2 = StringVar()
input_sj_2 = Entry(frame , textvariable=txt_input_sj_2 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_sj_2.grid(row=4 , column=1 , padx=2 , pady=2)

txt_input_sj_3 = StringVar()
input_sj_3 = Entry(frame , textvariable=txt_input_sj_3 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_sj_3.grid(row=5 , column=1 , padx=2 , pady=2)

#--------------------------------#

txt_input_nk_lb = Label(frame , text="input Credit" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
txt_input_nk_lb.grid(row=2 , column=2 , padx=2 , pady=2)

txt_input_nk_1 = StringVar()
input_nk_1 = Entry(frame , textvariable=txt_input_nk_1 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_nk_1.grid(row=3 , column=2 , padx=2 , pady=2)

txt_input_nk_2 = StringVar()
input_nk_2 = Entry(frame , textvariable=txt_input_nk_2 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_nk_2.grid(row=4 , column=2 , padx=2 , pady=2)

txt_input_nk_3 = StringVar()
input_nk_3 = Entry(frame , textvariable=txt_input_nk_3 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_nk_3.grid(row=5 , column=2 , padx=2 , pady=2)

#--------------------------------#

txt_input_nk_lb = Label(frame , text="input Grade" +"\n" +"4/3.5/3/2.5/2/1.5/1/0" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
txt_input_nk_lb.grid(row=2 , column=3 , padx=2 , pady=2)

txt_input_g_1 = StringVar()
input_g_1 = Entry(frame , textvariable=txt_input_g_1 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_g_1.grid(row=3 , column=3 , padx=2 , pady=2)

txt_input_g_2 = StringVar()
input_g_2 = Entry(frame , textvariable=txt_input_g_2 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_g_2.grid(row=4 , column=3 , padx=2 , pady=2)

txt_input_g_3 = StringVar()
input_g_3 = Entry(frame , textvariable=txt_input_g_3 ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
input_g_3.grid(row=5 , column=3 , padx=2 , pady=2)

#--------------------------------#

save_btn = Button(frame , text="  Save  " , bg=COLOR_GREEN , fg= COLOR_GRAY , command=enter_info ,font=FONT1 ,bd=0)
save_btn.grid(row=6 , column=1 , padx=2 , pady=2)

cal_btn = Button(frame , text=" Calculate " , bg=COLOR_GREEN , fg= COLOR_GRAY , command=cal_sc ,font=FONT1 ,bd=0)
cal_btn.grid(row=6 , column=2 , padx=2 , pady=2)

clear_btn = Button(frame , text=" Delete data & Close " , command=clear ,bg=COLOR_PINK_RED , fg= COLOR_GRAY ,font=FONT1 ,bd=0)
clear_btn.grid(row=10 , column=3 , padx=2 , pady=2)

#GPA lable
#--------------------------------#

gpa_lb = Label(frame , text="your GPA is :" ,bg=COLOR_LIGHT_PINK ,font=FONT1)
gpa_lb.grid(row=8 , column=2 , padx=2 , pady=2)

txt_gpa = StringVar()
gpa_area = Entry(frame , textvariable=txt_gpa ,font=FONT1 ,bd=0 ,bg=COLOR_LIGHT_GRAY)
gpa_area.grid(row=8 , column=3 , padx=2 , pady=2)

#--------------------------------#

root.mainloop()