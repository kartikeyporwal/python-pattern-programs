def pattern_rev12_12_mod():
    n = int(input("Enter the number: "))

    for i in range(n, 1, -1):
        print("*"*i + " "*2*(n-i) + "*"*i)
    print("*"*2*n)
    print("*"*2*n)
    
    for j in range(2, n+1):
        print("*"*j + " "*2*(n-j) + "*"*j)


        
pattern_rev12_12_mod()

"""

**********
****  ****
***    ***
**      **
**********
**********
**      **
***    ***
****  ****
**********

"""
