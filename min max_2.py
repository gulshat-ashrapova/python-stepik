a = int(input())
b = int(input())
c = int(input())
if a>=b>=c:
    print(a,'\n',c,'\n',b)
elif a>=c>=b:
    print(a,'\n',b,'\n',c)
elif b>=a>=c:
    print(b,'\n',c,'\n',a)
elif b>=c>=a:
    print(b,'\n',a,'\n',c)
elif c>=a>=b:
    print(c,'\n',b,'\n',a)
elif c>=b>=a:
    print(c,'\n',a,'\n',b)