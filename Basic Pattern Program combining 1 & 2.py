def pattern1_2():
    n = int(input("Enter the number: "))
    for i in range(1, n+1):
        print("*"*i + " "*2*(n-i) + "*"*i)
        
pattern1_2()

"""

*        *
**      **
***    ***
****  ****
**********


"""
