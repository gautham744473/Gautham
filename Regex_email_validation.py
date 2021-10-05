# Verifying/validating an User's mail

# import regular expressions module
import re 

# gautham74473@gmail.com
pattern ="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

# user input 
user_input =input()

if (re.search(pattern,user_input)):    # returns Boolean value True --> executes the code block 
    print("Valid e-mail ")

else:
    print("Invalid e-mail")