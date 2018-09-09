def pattern_rev12_12():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        print("*"*(n-i+1) + " "*2*(i-1) + "*"*(n-i+1))
        
    for i in range(2, n+1):
        print("*"*i + " "*2*(n-i) + "*"*i)
    


        
pattern_rev12_12()

"""

**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********


"""
