n = int(input("enter number \n"))
for i in range(0, n + 1):
    for j in range(n - i, 0, -1):
        print(j, end=" ")
