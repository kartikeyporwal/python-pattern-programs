def pattern_num_pyramid_center():
    n = int(input("Enter the number: "))

    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ",end = "")
        for j in range(n, n-i, -1):
            print(j, end = "")
        for j in range(n-i+2, n+1):
            print(j, end = "")
        print()

pattern_num_pyramid_center()

"""
    5
   545
  54345
 5432345
543212345

"""
