n = int(input("Enter the length of the sequence: ")) # Do not change this line

x=1
y=2
z=3

if n == 1:
    print(1)
elif n== 2:
    print(1)
    print(2)
elif n==3:
    print(1)
    print(2)
    print(3)
else:
    print(1)
    print(2)
    print(3)
    for i in range(3,n):
        
        summa=x+y+z
        x=y
        y=z
        z=summa
        print(summa)





