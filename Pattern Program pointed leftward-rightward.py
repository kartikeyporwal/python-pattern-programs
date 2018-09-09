def pattern_pointed_r():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        print("  "*(n-i) + "*"*(i) + " "*2*(i-1) + "*"*i)
    for i in range(n-1, 0, -1):
        print("  "*(n-i) + "*"*i + " "*2*(i-1) + "*"*i)

 
    


        
pattern_pointed_r()

"""

      **
    **  **
  ***    ***
****      ****
  ***    ***
    **  **
      **

"""
