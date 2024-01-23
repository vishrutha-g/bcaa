import sys as s 

z={0,1,2,3,4,5,6,7,8,9,10}

def f(a,b):
    return(a+b-1)

#identity axiom
e=90
for a in z:
    for b in z:
        if f(a,b)==b and f(b,a)==b:
            e=a

if e in z:
    print("Identity element=",e)
else:
    print("Identity does not exist")


#inverse axiom
for a in z:
    for b in z:
        if f(a,b)==1 and f(b,a)==1:
            if b==2:
                print("Inversse of",b,"is",a)

