def star():
    n = int(input("Enter Number: "))
    n = 5
    c = n - (n+1)
    b = n-3
    while c <= 3:
        for i in range(1, n+1):
            print(" "*c + "*"*i)
            c += 1
    while b >= 0:
        for j in range(n-1, 0, -1):
            print(" "*b + "*"*j)
            b -= 1

star()
