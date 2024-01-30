import pickle
import os
class student:
    def adddata(self):
        f1=open("aswintext.dat","wb+")
        d={}
        n=int(input("enter no of records to add"))
        for i in range(n):
            d["sname"]=input("enter student {} name".format(i))
            d["rno"]=input("enter student rollno")
            pickle.dump(d,f1)
        f1.close()

    def searchdata(self):
        try:
            f1=open("aswintext.dat","rb")
            n=int(input('enter a roll number for search'))
            while True:
                y=pickle.load(f1)
                if y["rno"]==n:
                    print("found in file as well")
                    break
        except:
            f1.close()
        

s1=student()
s1.adddata()
s1.searchdata()

