import random
print("welcome for fun")
f = open("d.txt")
content =f.read()
print(content)
f.close()
lst=[ 1,2,3]
 
#choice=random.choice(lst)

#3a= int(input("Enter one of the 1/2/3"))
n=1

#1=stone,2=paper,3=scissor
while n<10:
 choice=random.choice(lst)
  
 a= int(input("Enter one of the 1/2/3"))
 if choice == a :
  print("tie")
 elif choice==1 and a== 3:
    print("you loose")
 elif choice == 1 and a==2:
     print("you win")
 elif choice==2 and a== 3:
    print("you loose")
 elif choice ==2 and a==1:
        print("you win")
 elif choice==3 and a== 2:
    print("you loose")
 elif choice == 3 and a==1:
     print("you win")

