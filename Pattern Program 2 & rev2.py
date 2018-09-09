def pattern_1_rev1():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        print("  "*(n-i) + " *"*i)
    for i in range(2, n+1):
        print("  "*(i-1) + " *"*(n-i+1))

 
    


        
pattern_1_rev1()

"""

      *
    * *
  * * *
* * * *
  * * *
    * *
      *

"""
