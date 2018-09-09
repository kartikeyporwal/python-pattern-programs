def pattern_num_pyramid_rev():
    n = int(input("Enter the number: "))

    b = ""
    for i in range(1, n+1):
        a = n+1-i
        print(b + str(a))
        b += str(a)
    for j in range(n-1, 0, -1):
        print(b[:j])
     
pattern_num_pyramid_rev()

"""
5
54
543
5432
54321
5432
543
54
5

"""
