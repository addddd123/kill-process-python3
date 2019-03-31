import os, time



try:
   
    os.system("top")
    par=input(" enter process name which u which u want to kill \n")
    
    pk="pgrep "+par
    
    if (os.system("pk")):
        k="pkill "+par
        if os.system("pkill "+par)==0:
            print(" process has been killed ")
        else:
            print("process has not been killed ")
    else:
        print(" process not found ")
   
except:
    print( "error")

