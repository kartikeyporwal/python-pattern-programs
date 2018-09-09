def pattern_num_pyramid():
    n = int(input("Enter the number: "))
    b = ""
    for i in range(1, n+1):
        a = i
        print(str(b) + str(a))
        b += str(a)
        a += 1
    for j in range(n-1, 0, -1):
        print(b[:j])
        
     
pattern_num_pyramid()

"""

1
12
123
1234
123
12
1

"""
