# Creating Marksheet
# Name, std, div, roll no
# Subj , scores
# Percentage
# Full marks

# Student Information
name = input("Enter your Name : ")
std = input("Enter the class of the student : ")
div = input("Enter the Division of the student : ")
roll_no = input("Enter the roll number of student : ")

# Full Marks

fm = int(input("Enter the full marks of the exam : "))

# Score in each subjects

physics = int(input("Enter the acquired score in physics by the student : "))
maths = int(input("Enter the acquired score in maths by the student : "))
chem = int(input("Enter the acquired score in chemistry by the student : "))



# formula of percentage is : marks*100/Full marks

# defining the percentage function
def percentage(x, num):
    return x*100/fm

# Generating the percentage values
physics_percent = percentage(physics, fm)
math_percent = percentage(maths, fm)
chem_percent = percentage(chem, fm)

# Banner :
print('''
 .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || |  _______     | || |  ___  ____   | | | |    _______   | || |  ____  ____  | || |  _________   | || |  _________   | || |  _________   | |
| ||_   \  /   _|| || |     /  \     | || | |_   __ \    | || | |_  ||_  _|  | | | |   /  ___  |  | || | |_   ||   _| | || | |_   ___  |  | || | |_   ___  |  | || | |  _   _  |  | |
| |  |   \/   |  | || |    / /\ \    | || |   | |__) |   | || |   | |_/ /    | | | |  |  (__ \_|  | || |   | |__| |   | || |   | |_  \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | |
| |  | |\  /| |  | || |   / ____ \   | || |   |  __ /    | || |   |  __'.    | | | |   '.___`-.   | || |   |  __  |   | || |   |  _|  _   | || |   |  _|  _   | || |     | |      | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |  \ \_  | | | |  |`\____) |  | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |___/ |  | || |    _| |_     | |
| ||_____||_____|| || ||____|  |____|| || | |____| |___| | || | |____||____| | | | |  |_______.'  | || | |____||____| | || | |_________|  | || | |_________|  | || |   |_____|    | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')
# Showing Student Info
print(f"Information : \n"
      f"Name : {name} "
      f"Class : {std} "
      f"Section : {div} "
      f"Full Marks : {fm} ")
# Printing percentage :
print(f"Percentage : \n"
      f"Physics : {physics_percent} \n"
      f"Maths : {math_percent} \n"
      f"Chemistry : {chem_percent}")





