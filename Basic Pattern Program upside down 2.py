def pattern_rev_2():
    n = int(input("Enter the number: "))
    for i in range(n, 0, -1):
        print(" "*(n-i) + "*"*i)

    #OR
    for i in range(n):
        print(" "*i + "*"*(n-i))

    #OR
    for i in range(1, n+1):
        print(" "*(i-1) + "*"*(n-i+1))
        
pattern_rev_2()

"""

*****
 ****
  ***
   **
    *

"""
