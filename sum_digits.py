#!/usr/bin/env python
num=input("Enter a number)
sum=0     
while(num!=0):
          tmp=num%10
          num=num/10
          sum=sum+tmp
 print("sum is :" +sum)
