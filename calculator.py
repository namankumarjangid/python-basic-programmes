print ('enter the num a')
a=int(input())
print ('enter the num b')
b=int(input())
print ('enter the operator to be used /,*,-,+,%')
c=input()


if (c=='*') :
    d=a*b
    print ('the multiplication of a and b is ')
    print (d)

elif (c=='+') :
    d=a+b
    print ('the addtion of a and b is ')
    print (d)

elif (c=='-') :
    d=a-b
    print ('the subtraction of a and b is ')
    print (d)
elif (c=='/') :
    d=a/b
    print ('the division of a and b is ')
    print (d)
elif (c=='%') :
    d=a\b*100
    print ('the percent of a on b is')
    print ('d')

