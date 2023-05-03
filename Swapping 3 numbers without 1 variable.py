a=int(input())
b=int(input())
c=int(input())
c=a+b+c
b=c-(a+b)
a=c-(b+a)
c=c-(a+b)
print(a,b,c)
