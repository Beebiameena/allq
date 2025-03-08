a=8
def m():
   print('Inside m(): ',a)
def p():
   print('Inside p():',a)
def v():
   global a
   a = 4
   print('Inside v():', a)
print('global:',a)
m()
print('global:',a)
p()
print('global:',a)
v()
print('global:',a)