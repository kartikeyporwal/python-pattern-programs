def pattern_pointed_r():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        print(" "*(i-1) + "*"*i)
    for i in range(2, n+1):
        print(" "*(n-i) + "*"*(n-i+1))

 
    


        
pattern_pointed_r()

"""

*
 * *
   * * *
     * * * *
   * * *
 * *
*

"""
