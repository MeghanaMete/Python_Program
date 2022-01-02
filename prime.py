n=int((input("Enter the Number::"))
flag=1
for i in range(2,n):
    if n%i==0:
    flag=1
    if flag==0:
       prinr("Number is Prime")
    else:
      print("Number is not Prime")
