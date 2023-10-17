#This file is in module_2 and takes input from run.py as file
# It outputs a processed file into the processed folder as comments.txt
# The whole code is to get the raw file and extract the comments and put them in the processed folder.
import sys
import os
from pathlib import Path
def Ext_com(file):

    Incom = False
    root_dir = Path(__file__).resolve().parent.parent
    save_path = root_dir /"Data"/ "processed"
    completeName = os.path.join(save_path, "comments.txt")

    with open(completeName, "w", encoding="utf-8") as fl:
        #fl.write(html.decode('utf-8'))
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                res = line.split()
                for i in res:
                    if(i[:3] == '<p>'):
                        Incom = True
                    if(i[-4:] == '</p>'):
                        Incom = False

                    if((Incom == True) and (i[:3] == '<p>')):
                        #print(i[3:], end=" ")
                        fl.write(i[3:])
                    elif (Incom == True):
                        #print(i, end=" ")
                        fl.write(i)
                    elif ((Incom == False) and (i[-4:] == '</p>')):
                        #print(i[:-4])
                        fl.write(i[:-4])
                    