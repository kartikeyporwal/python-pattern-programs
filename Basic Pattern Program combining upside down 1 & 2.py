def pattern_rev_2():
    n = int(input("Enter the number: "))

    for i in range(n, 0, -1):
        print("*"*i + " "*2*(n-i) + "*"*i)


    #OR
    for i in range(n):
        print("*"*(n-i) + " "*(2*i) + "*"*(n-i))

    #OR
    for i in range(1, n+1):
        print("*"*(n-i+1) + " "*2*(i-1) + "*"*(n-i+1))
    
        
pattern_rev_2()

"""

**********
****  ****
***    ***
**      **
*        *

"""
