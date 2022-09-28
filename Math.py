from ast import If


l=int(input('enter lower range'))
u=int(input('enter upper range'))
n=int(input('enter any number which should divided'))
if(l>u):
  print('upper limit should be greater')
for i in range(l,u+1):
    
    if(i%n==0):
        print(i)
    else:
        print()
