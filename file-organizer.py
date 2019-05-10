
import os 


dir_path = os.path.dirname(os.path.realpath(__file__)) 

flag=0
for root,dirs, files in os.walk(dir_path): 
    print(str(root))
    for file in files: 
        if file.endswith('.css'): 
            if os.path.exists("css")!=True and flag==0:
                
                os.system("mkdir css")
                flag=1
            else:
                flag=1
            g="mv "+str(file)+" css"
            os.system(g)



