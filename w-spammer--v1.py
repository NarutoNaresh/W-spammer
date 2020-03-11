#whatsapp spam script...
#--------Dependencies--------#
from selenium import webdriver
import random,time
from tkinter import *

global li
li=[]

def get_det(det):
    global li
    li.append(det)

def final_move():
    global li #li=['naresh','messages','count]
    a=[]
    driver=webdriver.Chrome("F://1my_creations//w-spammer//chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    name=li[0]
    r=li[1]
    a=r.split(',')
    time.sleep(29)#Delay for loading webpage
    #user=driver.find_element_by_xpath("span[@title='{}']".format(name))
														#span-->type..title-->attribute=value...{}.format()
    #user.click()
    msg_box=driver.find_element_by_class_name('_13mgZ')#changes frequently,so inspect element to update it.   _13mgZ
    n=int(li[2])
    for i in range(n):
            msg_box.send_keys(random.choice(a))
            btn=driver.find_element_by_class_name('_3M-N-')#changes frequently
            btn.click()
    
#--------------------------------------------------------------------------------------------------------#


#relx=relative x (position) in graph
#rely=relative y (position) in graph
#relheight=relative height-->size 
#relwidth=relative width-->size


window=Tk()
window.title("Whats_App_Spammer")
window.geometry("740x520")
#--------To avoid multiple creation of methods------#
global count_break1,count_break2,count_break3
count_break1=0;count_break2=0;count_break3=0;
#----------------Functionality of buttons-------------#
def disp3(z):
    global count_break3;count_break3+=z
    if count_break3==1:
        #To ensure that no multiple instance created(during clicking the button)
        but=Button(window,font=30,bg="red",relief=FLAT,height=2,width=13,text="Spam-Bomb",command=lambda:final_move())
        but.place(relx=0.4,rely=0.75)
def disp2(y):
    global count_break2;count_break2+=y
    if count_break2==1:
        fr3=Frame(window,bg="#0a8219",bd=4)
        fr3.place(relheight=0.15,relwidth=0.85,relx=0.5,rely=0.54,anchor='n')
        b2=Label(fr3,font=10,bg="black",fg="lime green")
        b2.place(relwidth=1,relheight=1)
        entry3=Entry(fr3,font=30,relief=FLAT,bg="black",fg="green yellow")
        entry3.place(relx=0.38,rely=0.35)
        entry3.pack(ipadx=30,ipady=30)
        bu2=Button(fr3,font=30,bg="red",relief=FLAT,height=2,width=13,text="Next",command=lambda:[disp3(1),get_det(entry3.get())])
        bu2.place(relx=0.77,rely=0.14)
        lab2=Label(fr3,text="Spam X ",font=("Courier",13),fg="red",bg="black")
        lab2.place(relx=0,rely=0.35)
def disp1(x):
    global count_break1;count_break1+=x
    if count_break1==1:
        fr2=Frame(window,bg="#0a8219",bd=4)
        fr2.place(relheight=0.15,relwidth=0.85,relx=0.5,rely=0.38,anchor='n')
        b1=Label(fr2,font=10,bg="black",fg="lime green")
        b1.place(relwidth=1,relheight=1)
        entry2=Entry(fr2,font=30,relief=FLAT,bg="black",fg="green yellow")
        entry2.place(relx=0.38,rely=0.35)
        entry2.pack(ipadx=30,ipady=30)
        bu1=Button(fr2,font=30,bg="red",relief=FLAT,height=2,width=13,text="Next",command=lambda:[disp2(1),get_det(entry2.get())])
        bu1.place(relx=0.77,rely=0.14)
        lab1=Label(fr2,text="Messages :",font=("Courier",13),fg="red",bg="black")
        lab1.place(relx=0,rely=0.35)

#----Load image----#        
img = PhotoImage(file = "mat.png")
il=Label(window,image=img)
il.place(relheight=1,relwidth=1)
#-----Banner--------#
fr=Frame(window,bg="red",bd=4)
fr.place(relheight=0.15,relwidth=1,relx=0.5,rely=0,anchor='n')
banner=Label(fr,text="W-Spammer",font=("Showcard Gothic",35),bg="black",fg="lime green")
banner.place(relwidth=1,relheight=1)
#-----Frame------#
fr1=Frame(window,bg="#0a8219",bd=4)
fr1.place(relheight=0.15,relwidth=0.85,relx=0.5,rely=0.22,anchor='n')
#anchor='n'(none) set frame to center
b=Label(fr1,font=10,bg="black",fg="lime green")
b.place(relwidth=1,relheight=1)
#-----Entry_Field-------#
entry1=Entry(fr1,font=30,relief=FLAT,bg="black",fg="green yellow")
entry1.place(relx=0.38,rely=0.35)
entry1.pack(ipadx=30,ipady=30)
#------Buttons----#function inside a button 
bu=Button(fr1,font=30,bg="red",relief=FLAT,height=2,width=13,text="Next",command=lambda:[disp1(1),get_det(entry1.get())])
bu.place(relx=0.77,rely=0.14)
lab1=Label(fr1,text="Enter_Victim_Name :",font=("Courier",13),fg="red",bg="black")
lab1.place(relx=0,rely=0.35)


window.mainloop()

