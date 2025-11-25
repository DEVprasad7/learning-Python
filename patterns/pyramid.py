length = int(input("Enter the length of the pyramid :"))

n = length

# Square Pattern        
def square(n):
    for i in range(n):
        for j in range(n):
            print("*" ,end="")
        print("")
        
# Sideways Pyramid
def left_side_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*" ,end="")
        print("")

# Descending Pyramid
def left_desc_pyr(n):
    for i in range(n):
        for j in range(i, n):
            print("*" ,end="")
        print("")

# Right Sideways Pyramid
def right_side_triangle(n):
    for i in range(n):
        for j in range(i, n):
            print(" " ,end="")
        for k in range(i+1):
            print("*" ,end="")
        print()

# Right Descending Pyramid
def right_desc_pyr(n):
    for i in range(n):
        for j in range(i+1):
            print(" " ,end="")
        for k in range(i, n):
            print("*" ,end="")
        
        print("")

# Full Pyramid
def pyr(n):
    for i in range(n):
        for j in range(i, n):
            print(" " ,end="")
        for k in range(i):
            print("*" ,end="")
        for k in range(i+1):
            print("*", end="")
        print("")

# Inverted Full Pyramid
def rev_pyr(n):
    for i in range(n):
        for j in range(i+1):
            print(" " ,end="")
        for k in range(i, n-1):
            print("*" ,end="")
        for k in range(i, n):
            print("*" ,end="")
        
        print("")

# Diamond pattern
def diamond(n):
    
    for i in range(n-1):
        for j in range(i, n):
            print(" " ,end="")
        for k in range(i):
            print("*" ,end="")
        for k in range(i+1):
            print("*", end="")
        print("")
        
    for i in range(n):
        for j in range(i+1):
            print(" " ,end="")
        for k in range(i, n-1):
            print("*" ,end="")
        for k in range(i, n):
            print("*" ,end="")
        
        print("")
    
