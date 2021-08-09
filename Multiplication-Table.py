# Multiplication Table

# Creating multiplication Function
def mult(x, term = 10): # term by default is set to 10 i.e if the user does not specify number of terms, then by default 10 number swill be printed
    for i in range(1, term+1):
        print(f"{x} X {i} = {x * i}")
        
num = int(input("Enter the number : ")) # Taking the value of the number of which multiplication table will be generated
term = input("Enter which number you want to create the table : ") # Number of terms wanted, Empty input value can also be provided

if term == '': # Checking if the term input is Empty or not 
    mult(num)
else: # If not empty then given number of terms will be generated
    mult(num, int(term))
