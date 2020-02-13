# TRIANGLE 
import math
a=float(input("Enter side1 of triangle: "))
b=float(input("Enter side2 of triangle: "))
c=float(input("Enter side3 of triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
l=[a,b,c,s,area]
l.sort()
a,b,c,s,area=l
h=(2*area)/c # Actual Height value
h1=h/2 # for the image only
A=math.degrees(math.asin(h/b))
B=math.degrees(math.asin(h/a))
C = (180-(A+B))
print('\na=',a,' ∠A=',A,'°\t','b=',b,' ∠B=',B,'°\t','c=',c,' ∠C=',C,'°\n',sep='')
for i in range((int(h1)+1)):
    L1=int(2*i/((math.tan(math.radians(A)))))
    L2=int(c-(2*i/((math.tan(math.radians(B))))))
    if i == 0:
        print("*"*int(c),sep='')
    elif i<int(h1):
        print(" "*(L1-1),"*","*"*(L2-L1),"*",sep='')
    else :
        print(" "*(L1),"*",sep='')
        #print(L1,L2)
