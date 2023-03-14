num = int(input("Ingrese un número entero: "))

for i in range(1, num+1):
    for j in range(i, 0, -1):
        print(2*j-1, end=" ")
    print()
