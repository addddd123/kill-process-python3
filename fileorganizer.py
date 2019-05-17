
import os 
from tkinter import *

def organize():
    
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    flag=0
    flag1=0
    flag2=0
    for root,dirs, files in os.walk(dir_path): 
        
        for file in files: 
            if file.endswith('.pdf') : 
                
                if os.path.exists("PDF")!=True and flag==0:
                    
                    os.system("mkdir PDF")
                    flag=1
                else:
                    flag=1
                g="mv "+str(file)+" PDF"
                os.system(g)
            if file.endswith('.txt')  : 
                if os.path.exists("TEXT")!=True and flag1==0 :
                    
                    os.system("mkdir TEXT")
                    flag1=1
                else:
                    flag1=1
                g="mv "+str(file)+" TEXT"
                os.system(g)
            if file.endswith('.html')  : 
                if os.path.exists("HTML")!=True and flag2==0 :
                    
                    os.system("mkdir HTML")
                    flag2=1
                else:
                    flag2=1
                g="mv "+str(file)+" HTML"
                os.system(g)
def seccaller():
    organize()
   
root=Tk()
root.title("Welcome to the junk organizer")
root.geometry("700x450")
root.configure(background="powder blue")
label=Label(root,text='Junk Organizer',fg='chocolate',bg='powder blue',font=(100,100),height=0,width=30)
label.pack(side=TOP)
root1=Frame(root,bg='powder blue')

btn1=Button(root,text="Start organizing Junk",command=seccaller,fg="black", width=50,height=7,bg="green" ) #ok

btn1.pack()

btn2=Button(root,text="Exit",command=exit,fg="black", width=50,height=7,bg="red" ) #ok
btn2.pack()

root.mainloop()