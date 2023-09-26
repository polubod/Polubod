import sys

file = str(sys.argv[1])
Incom = False

with open('comments.txt', "w", encoding="utf-8") as fl:
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
                
                

        #print(line)