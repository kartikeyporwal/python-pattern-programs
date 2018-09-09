def pattern_rev_1():
    n = int(input("Enter the number: "))
    for i in range(1, n+1):
        print("*"*(n-i+1))

    #OR
    for i in range(n, 0, -1):
        print("*"*i)

    #OR
    for i in range(n):
        print("*"*(n-i))
    
        
pattern_rev_1()

"""

*****
****
***
**
*

"""
