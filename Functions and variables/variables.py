#Ask the user to enter there name as input
name = input("Hello there what is your name ")

#Remove the white space 
name = name.strip()

#Captilize the first letter in the user input
name = name.title()

#Print the result
print(f"Hello, {name}")