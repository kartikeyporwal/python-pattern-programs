def pattern_12_rev12():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        print("*"*i + " "*2*(n-i) + "*"*i)
    for i in range(1, n+1):
        print("*"*(n-i+1) + " "*2*(i-1) + "*"*(n-i+1))


    


        
pattern_12_rev12()

"""

*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *


"""
