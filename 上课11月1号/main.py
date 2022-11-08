n=eval(input())
a=1
b=2
s=0
for x in range(n):
    s=s+b/a
    b=a+b
    a=b-a
print(s)

