length = int(input("Enter the length of the pyramid :"))

n = length

for i in range(n):
    for j in range(i):
        print("*" ,end="")
    print("*")