# area of Triangle program. Modify the program after receiving input from the user for
# the length of the base and the height of the triangle

# program will be verified the values entered are not 0 or negative.
# if they are, program will output a useful message, re-ask user again for the correct input

#get the base value first

base = int( input("Enter the length of the base:") )
while base <= 0 :
    print("**Error - the base length must be a positive number. You entered ", base)
    base = int(input("Enter the length of the base: "))
    
height = int( input("Enter the height:") )
while height <= 0 :
    print("**Error - the height must be a positive number. You entered ", height)
    height = int(input("Enter the height: "))
               
area = 1 / 2 * base * height

print("The area of the triangel is", round (area/10000, 2) , "square metres")
