a=int(input())
sum=0
temp=a
while(a!=0):
  rem=a%10
  sum=sum+rem*rem*rem
  a=a//10
if (temp==sum):
  print("yes")
else:
  print("no")
