a=[0]*int(input('Elementlerin sayi: '))
k=0
for i in range(len(a)):
    a[i]=int(input("daxil et:"))
print('A:',a)
for x in a:
    if x > 0:
        k+=x

print(k)