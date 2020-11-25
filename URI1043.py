
x,y,z=list(map(float,input().split()))
if(x<y+z and y<z+x and z<x+y):
     print("Perimetro = %0.1f"%(x+y+z))
else:
     print("Area = %0.1f"%((z*(x+y))/2))


'''''
if(((x+y)>z)and((y+z)>x)and((z+x)>y)):
    print("Perimetro = "+str((x+y+z)))
else:
    print("Area = "+str(((x+y)/2)*z))
'''