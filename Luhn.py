import sys
# Luhn.py 896588081210001114

# Main function to call other functions.
def main():
    # Get arguements from the command line 
    argList = sys.argv
    # Input is passed to validate
    # Valid input passed to split
    # Split input passed to luhn
    # Luhn returns the check digit
    num = luhn(split(validate(argList[1])))
    print("The calculated check digit is: " + str(num))
    print("Add the check digit to the end and re-run the script to check if it is valid (should equal 0)")


# Function to check input is correct
def validate(argStr):
    # Try block
    try:
        # Cast str to int
        argInt = int(argStr)
    # Catch block
    except:
        print("Only enter numerical characters only")
    return argInt


def split(argInt):
    luhnList = list(map(int, str(argInt)))
    return luhnList


def luhn(luhnList):
    counter = 0
    for element in luhnList:
        # If an odd element from the list
        if(counter % 2 ==0) != True: # Odd
            # Multiply by 2
            luhnList[counter] *= 2
            if len(str(luhnList[counter])) > 1: 
                # Split the number into its digits
                luhnItem = list(map(int, str(luhnList[counter])))
                # Sum the digits
                luhnList[counter] = luhnItem[0] + luhnItem[1]
        # Increment counter
        counter += 1
    # Add all the digits together
    luhnTotal = sum(luhnList)
    # Multiply by 9
    luhnTotal *= 9
    # Div by 10 and present the remainder(the check digit)
    luhnTotal %= 10
    return luhnTotal

    
# If the .py is executed directly it will run as a script, otherwise allows
# other .py files to call its functions.
if __name__ == "__main__":
   main()
