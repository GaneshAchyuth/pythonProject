def add_twonumbere(a,b):
    return a+b

def sub_twonumbers(c,d):
    return c-d

def mul_twonumbers(x,y):
    return  x*y

def div_twonumbers(e,f):
    g=0
    if(f>0):
      g =  e % f
      return g
    else:
      return g



print(add_twonumbere(10,20))
print(sub_twonumbers(20,10))
print(mul_twonumbers(4,4))
print(div_twonumbers(30,0))
