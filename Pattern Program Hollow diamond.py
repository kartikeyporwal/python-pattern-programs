def pattern_hollow_diamond():
    ch = input("press a to begin: ")
    while(ch!= "s"):

      n= int(input("# rows: "))
      a=((n-1)/2)
      if not (n%2==1):
        print ("please enter an odd value: ")
        continue
      for row in range(n):
        for col in range(n):
          if (row+col==a) or (col-row==a) or (row-col==a) or (row+col==a*3):
            print ("*", end="")
          else:
            print (end=" ")
        print()
      ch = input("if you want to continue, press a \n if you want to stop press s: ")

pattern_hollow_diamond()

"""
  *
 * *
*   *
 * *
  *
  
"""
