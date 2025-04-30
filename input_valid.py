def get_string_type(prompt):
  
    
 
    while True:
        user_input = input(prompt)
        
        # Check if the input is numeric
        try:
            # Try to convert to float to catch both integers and decimals
            float(user_input)
            print("Invalid input! Please enter a string value, not a number.")
        except ValueError:
            # If conversion fails, it's not a number - which is what we want
            return user_input
       
            
# Check if valid integer type            
def get_integer_type(prompt):
    
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input! Please enter an integer value.")  
            
# Check if valid float type  

def get_float_type(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input! Please enter a float value.")  
