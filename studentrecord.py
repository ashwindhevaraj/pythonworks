import pickle
import os
import csv
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
    def csvwrite(self):
        f1=open("test.csv","w+",newline="")
        wob=csv.writer(f1)
        n=int(input('enter no of records'))
        for i in range(n):
            username=input('enter your username')
            pword=input('enter your password')
            a=[username,pword]
            wob.writerow(a)
        f1.close()
    def csvread(self,text):
        f1=open('test.csv','r')
        rob=csv.reader(f1)
        for i in rob:
            if i[0]==text:
                print("password is ",i[1])
                break
            else:
                print("record not present")


s1=student()
#s1.adddata()
#s1.searchdata()
s1.csvwrite()
s1.csvread("1111")


