
from tkinter import N
a="Bright IT Career"
for i in range(9):
    print(a)



i=1
while(i<20):
    print(i)
    i+=1



a=6
b=10
print(a==b)
print(a!=b)



n=[1,2,3,4,5,6,7,8,9,10]
print('Even')
for i in n:
    if i%2==0:
        print(i,end=" ")
print("\nOdd")
for i in n:
    if i%2!=0:
        print(i,end=" ")
print()



k=30
p=20
l=90
if k>=p and k>=l:
    largest=k
elif p>=k and p>=l:
    largest=p
else:
    largest= l
print("largest:",largest)



a=10
b=20
print("Even between 10 to 20:")
while a<=b:
    if(a%2==0):
        print("{0}",(a),end=" ")
    a=a+1
print()



a=1
print("print 1to 10 :",end=" ")
while True:
    print(a,end=" ")
    a=a+1
    if(a>10):
        break
print()



a=int(input('Enter a number'))
sum=0
temp=0
temp=0
while temp>0:
    r=temp%10
    sum+=r**3
    temp//=10
if a==sum:
    print(" Armstong")
else:
    print("not Armstrong")



n=int(input('Enter a number'))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print('prime')
        else:
            print('Not Prime')


n=int(input('Enter a number'))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not palindrome")



a=int(input('Enter a number'))
if a%2==0:
    print('even')
else:
    print('odd')



a=int(input('Enter a gender'))
if a%2==0:
    print('Male')
else:
    print('female')