def pattern_12_rev12():
    n = int(input("Enter the number: "))

    print("*"*2*n)
    for i in range(2, n+1):
        print("*"*i + " "*2*(n-i) + "*"*i)
    
    for i in range(1, n):
        print("*"*(n-i+1) + " "*2*(i-1) + "*"*(n-i+1))
    print("*"*2*n)


    


        
pattern_12_rev12()

"""

**********
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
**********


"""
