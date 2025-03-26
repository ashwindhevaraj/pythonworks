'''k=[]
m=["aswin","risk","solver","life","saver"]
for x in m:
  if "a" in x:
    k.append(x)
print(k)'''
'''m=["aswin","risk","solver","life","saver"]
k=[x for x in m if "a" in x]
print(k)'''

'''k=[1,2,3,4,5]
k.sort(reverse=True)
print(k)'''

'''dictcheck={"id":1,"name":"aswin"}
print(dictcheck["id"])'''

'''#replace in python
a=input("enter a string")
b=input("enter a source string in file to be replaced")
c=input("enter a destination string in file to be replaced")
c=a.replace(b,c)
print(c)'''

'''#reverse word in python
a=input("enter a string")
b=a[-1:-(len(a)+1):-1]
print(b)'''

'''def check1(*argument):
  print("i am priting "+argument[0]+"also printing "+argument[1])
  
check1("aswin","loves")'''
'''txt=0
def recurse(i):
  if i>0:
    txt=i+recurse(i-1)
    return txt
  else:
    return 0

check=recurse(5)
print(check)'''

'''l=["aswin","checking","iterable","data"]
k=iter(l)
print(next(k))
s="aswin"
k=iter(s)
print(next(k))
# iterator concept explained.
for x in s:
  print(x)
  
  
class itercheck:
  def __iter__(self):
    self.a=1
    return self
  def __next__(self):
    if self.a<=20:
      x=self.a
      self.a += 1
      return x
    else:
      raise StopIteration
      
myc=itercheck()
myc1=iter(myc)
for x in myc1:
  print (x)'''
  
'''class bus:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("bus {} having {} moved".format(self.brand,self.model))
  
class train:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("train {} having {} moved".format(self.brand,self.model))
    
class boat:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("boat {} having {} moved".format(self.brand,self.model))
    
bus1=bus("AL","TN09")
train1=train("BHEL","WAP027")
boat1=boat("Vikram","LPSLIN-2034")

for x in (bus1,train1,boat1):
  x.move()  '''
  
'''class vehicle:
  def __init__(self,brand,model):
     self.brand=brand
     self.model=model
  def move(self):
     print("move man")
     
class bus(vehicle):
  pass
   
class train(vehicle):
  def move(self):
    print("move train")
     
class boat(vehicle):
  def move(self):
    print("move boat")
   
bus1=bus("AL","TN09")
train1=train("BHEL","WAP027")
boat1=boat("Vikram","LPSLIN-2034")

for x in (bus1,train1,boat1):
  print(x.brand)
  print(x.model)
  x.move()'''
  
'''import test
print(test.person["age"])'''

'''import re
s="beal tree ash000021"
xe=re.findall("[01]",s)
print(xe)'''

'''txt="we have {:.0%} chicken"
k=txt.format(45)
print(k)'''

'''f=open("Meeting notes.txt")
print(f.read(5))
print(f.readline())
print(f.readline())

for x in f:
  print(x)'''
  
  
'''class teest:
  def replaceoptions():
    str=input("enter a string")
    ch=input("enter a actual word to replace")
    ex=input("enter a expected word to replace")
    k=str.replace(ch,ex)
    print(k)

  def reverseoptions():
    str=input("enter a string to reverse")
    print(str[::-1])
  
  while(1):
    print("Enter the number for below options")
    print("1. Replace in string")
    print("2. reverse a word in string")
    print("3. exit")
    ch=input("enter your choice")
    if(ch=="1"):
      replaceoptions()
    elif (ch=="2"):
      reverseoptions()
    elif (ch=="3"):
      break
    else:
      print("kindly enter choices from 1 to 3")'''
      

'''class teest:
  def replication(cr):
    m=cr*2
    print("original data is {}".format(cr))
    print("replicated data is {}".format(m))
    m.sort()
    print("replicated data sorted in order {}".format(m))
    m.sort(reverse=True)
    print("replicated data sorted in reverse as {}".format(m))
    
  def oddeven(cr):
    x=list()
    for items in cr:
      if (items%2!=0):
        continue;
      else:
        x.append(items)
        cr.remove(items)
    cr.extend(x)
    print(cr)
        
  
  while(1):
    print("1. press for exit")
    print("2. press for replication")
    print("3. press for swapping odd and even numbers")
    ch=input("enter your  choice")
    if (ch=="1"):
      break;
    elif (ch=="2"):
      cr=input("enter the string for replication")
      cr=list(cr)
      replication(cr)
    elif (ch=="3"):
      cr=eval(input("enter the list of numbers"))
      oddeven(cr)
      
    else:
      print("please enter valid choice from 1 to 2")'''
      
'''class test3:
  s1=[]
  s2=[]
  s3=[]
  
  def sumkk(s):
    sums=0
    for x in range(len(s)):
      sums+=s[x]
    avg=sums/3
    print("\n student",x+1,"\t marks=",s,"\t total=",sums,"\taverage=",avg)
  
  for x in range(1,4):
    for y in range(1,4):
      
      print('enter student s '+str(x)+'mark of subject '+str(y)) 
      s1.insert(x-1,float(input()))
  
  s2=s1[3:6]
  s3=s1[6:9]
  s1=s1[0:3]
  print('marks of student ',s1)
  print('marks of student ',s2)
  print('marks of student ',s3)
  sumkk(s1)
  sumkk(s2)
  sumkk(s3)'''

'''class filecases:
  def printfile():
    f1=open('aswintext.txt',"r")
    for x in f1:
      f2=x.split()
      for word in f2:
        print(word,"#",end='')
      print()
  def filecopy():
    f1=open('aswintext.txt','r')
    f2=open('aswinoutput.txt','w+')
    for x in f1:
      for y in x:
        if y in "Aa":
          break
      else:
        f2.write(x)
    f1.seek(0)
    f2.seek(0)
    a=f1.read()
    b=f2.read()
    print("Original file",a)
    print("copied file",b)
    f1.close()
    f2.close()
f3=filecases
f3.printfile()
f3.filecopy()'''

class check2:
  def readfile():
    upper=0
    lower=0
    vowels=0
    consonant=0
    y=open("aswintext.txt","r")
    k=y.read()
    for i in k:
      if i.isalpha():
        if i.isupper():
          upper+=1
        else:
          lower+=1
        if i in ['A','E','I','O','U','a','e','i','o','u']:
          vowels+=1
        else:
          consonant+=1
    print("uppercase ",upper,"lowercase ",lower,"vowels ",vowels,"consonant ",consonant)


check=check2
check.readfile()

#iterator learning
a=["asw","cec",21,14,"mon"]
k=iter(a)
print(next(k))
print(next(k))

""" o/p asw
cec
internally for loops implement above """

#polymorphism learning
class vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def move(self):
        print("Move Man")
class bus(vehicle):
    pass
class scooty(vehicle):
    def move(self):
        print("scooty moved here")
        
class car(vehicle):
    def move(self):
        print("car moved here")
        
v1=vehicle("vehicle","rawmodel")
b1=bus("Airbus","Ashokleyland")
s1=scooty("TVSscooty","vespa")
c1=car("car","tatanano")

for x in (v1,b1,s1,c1):
    print(x.name)
    print(x.model)
    x.move()

""" o/p
vehicle
rawmodel
Move Man
Airbus
Ashokleyland
Move Man
TVSscooty
vespa
scooty moved here
car
tatanano
car moved here """

 
  
    
   
  
    

  
  
  
  
  

    
    

  