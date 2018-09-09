def pattern1_2():
    n = int(input("Enter the number: "))
    print("*"*2*n)
    for i in range(2, n+1):
        print("*"*i + " "*2*(n-i) + "*"*i)
        
pattern1_2()

"""

**********
**      **
***    ***
****  ****
**********


"""
