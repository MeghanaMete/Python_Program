n=int(input("Enter the number:"))
sum=0;
n1=n
while(n>0):
  d=n1%10
  n1=int(n/10)
  sum=sum+d*d*d
if(n==sum):
  print("Number is Armstrong")
else:
  print("Number is not Armstrong")

