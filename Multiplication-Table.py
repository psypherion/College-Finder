# Multiplication Table

### Feature : Even if No term value is provided it will give 10 terms ###

# Creating multiplication Function
def mult(x, term = 10): # term by default is set to 10 i.e if the user does not specify number of terms, then by default 10 number swill be printed
    for i in range(1, term+1):
        print(f"{x} X {i} = {x * i}")
        
num = int(input("Enter the number : ")) # Taking the value of the number of which multiplication table will be generated
term = input("Enter Upto which number you want to create the table : ") # Number of terms wanted, Empty input value can also be provided
print('''

              _ _   _       _ _           _   _                  _____      _     _           
  /\/\  _   _| | |_(_)_ __ | (_) ___ __ _| |_(_) ___  _ __      /__   \__ _| |__ | | ___    _ 
 /    \| | | | | __| | '_ \| | |/ __/ _` | __| |/ _ \| '_ \ _____ / /\/ _` | '_ \| |/ _ \  (_)
/ /\/\ | |_| | | |_| | |_) | | | (_| (_| | |_| | (_) | | | |_____/ / | (_| | |_) | |  __/   _ 
\/    \/\__,_|_|\__|_| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|     \/   \__,_|_.__/|_|\___|  (_)
                     |_|                                                                      

''')
print('*'*20)
if term == '': # Checking if the term input is Empty or not 
    mult(num)
else: # If not empty then given number of terms will be generated
    mult(num, int(term))
print('*'*20)
