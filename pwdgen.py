# Password Generator
# by Spectre
# ver. 0.1 (4-Sep-25)
#
# This script will generate a random password based on length and desired characters

import random, sys

#Create a string that will hold the possible characters
possible_characters = ""

#Function to include lower case characters
def include_lower(exclude_similar = False):
    global possible_characters
    possible_characters += "abcdefghijkmnopqrstuvwxyz"
    if not exclude_similar:
        possible_characters += "l"

#Function to include upper case characters
def include_upper(exclude_similar = False):
    global possible_characters
    possible_characters += "ABCDEFGHJKLMNPQRSTUVWXYZ"
    if not exclude_similar:
        possible_characters += "IO"

#Function to include numbers
def include_numbers(exclude_similar = False):
    global possible_characters
    possible_characters += "23456789"
    if not exclude_similar:
        possible_characters += "01"

#Function to include symbols
def include_symbols(exclude_possibly_forbidden = True):
    global possible_characters
    possible_characters += "!@#$%^&*()<>?+=-_/~"
    if not exclude_possibly_forbidden:
        possible_characters += "'\"\\"

#Function to get one character from the list of possible characters
def get_character():
    return random.choice(possible_characters)

#Function to generate a password of defined length
def generate_password(length):
    generated_password = ""
    for i in range(length):
        generated_password += get_character()
    return generated_password

#Function to display help
def display_help():
    print("Random Password Generator")
    print("by Spectre")
    print("")
    print("Usage: python pwdgen.py [option]")
    print("Option\t\tDescription")
    print("-------\t\t-----------")
    print("-c [num]\tSpecify number of passwords to generate")
    print("-f\t\tInclude potentially forbidden symbols, such as \". [Default=False]")
    print("--help\t\tThis help screen")
    print("-i [code]\tInclude only the types of characters specified")
    print("-l [num]\tGenerate password(s) of the specified length. [Default=12]")
    print("-s\t\tExclude similar characters, e.g., O and 0. [Default=False]")
    print("-x [code]\tExclude the specified types from the default.")
    print("")
    print("Codes:")
    print("\ta\tLower case letters")
    print("\tA\tUpper case letters")
    print("\tn\tNumbers")
    print("\ts\tSymbols")



#***Main Program***

#For now, set some defaults
password_length = 12
number_passwords = 1
use_lower = True
use_upper = True
use_numbers = True
use_symbols = True
exclude_similar = False
exclude_possibly_forbidden = True

##DEBUG
#print(sys.argv)

#Let's get some command line arguments
#   Valid arguments:
#       --help
#       -x [codes]      use defaults, but exclude the provided options
#       -i [codes]      use only specified codes
#       -l [num]        password length
#       -c [num]        number of passwords
#       -s              exclude similar characters
#       -f              include possibly forbidden symbols
#   where, [codes]:
#       a               lower case letters
#       A               upper case letters
#       n               numbers
#       s               symbols
#Check if they passed any arguments, otherwise we'll use the defaults
if len(sys.argv) > 1:
    i = 1
    while i < len(sys.argv):
        buffer = sys.argv[i]
        match buffer:
            case "--help":
                display_help()
                sys.exit()
            case "-s":
                #exclude similar characters
                exclude_similar = True
            case "-f":
                #include possibly forbidden symbols
                exclude_possibly_forbidden = False
            case "-x":
                #User wants to EXCLUDE certain options from the defaults
                #Get next argument to parse
                #Check for buffer overrun
                if (i+1) >= len(sys.argv):
                    #Not another argument, throw an error and exit
                    print("No option provided for argument \'-x\'.\nUse \"--help\" to display usage.")
                    sys.exit()
                buffer_next = sys.argv[i+1]
                for j in range(len(buffer_next)):
                    #Step through each character and compare to our known codes
                    match buffer_next[j]:
                        case "a":
                            use_lower = False
                        case "A":
                            use_upper = False
                        case "n":
                            use_numbers = False
                        case "s":
                            use_symbols = False
                        case _:
                            #unknown code, throw an error
                            print(f"Unknown code: {buffer_next[j]}.\nUse \"--help\" for display usage.")
                            sys.exit()
                #increment i twice to skip the next argument since we just parsed it
                i += 1
            case "-i":
                #User wants to INCLUDE only certain options
                #Get next argument to parse
                #Check for buffer overrun
                if (i+1) >= len(sys.argv):
                    #Not another argument, throw an error and exit
                    print("No option provided for argument \'-i\'.\nUse \"--help\" to display usage.")
                    sys.exit()
                #We need to set all options to false since the user is specifying what they want
                use_lower = False
                use_upper = False
                use_numbers = False
                use_symbols = False

                buffer_next = sys.argv[i+1]
                for j in range(len(buffer_next)):
                    #Step through each character and compare to our known codes
                    match buffer_next[j]:
                        case "a":
                            use_lower = True
                        case "A":
                            use_upper = True
                        case "n":
                            use_numbers = True
                        case "s":
                            use_symbols = True
                        case _:
                            #unknown code, throw an error
                            print(f"Unknown code: {buffer_next[j]}.\nUse \"--help\" to display usage.")
                            sys.exit()
                #increment i twice to skip the next argument since we just parsed it
                i += 1
            case "-l":
                #User is specifying length of password, next arg is a number
                #Get next argument to parse
                #Check for buffer overrun
                if (i+1) >= len(sys.argv):
                    #Not another argument, throw an error and exit
                    print("No option provided for argument \'-l\'.\nUse \"--help\" to display usage.")
                    sys.exit()
                buffer_next = sys.argv[i+1]

                if buffer_next.isnumeric():
                    #it is a number, convert it
                    password_length = int(buffer_next)
                else:
                    #non-numeric, throw an error
                    print(f"Numeric value expected: {buffer_next}\nUse \"--help\" to display usage.")
                    sys.exit()

                #increment twice because it consumes the next argument
                i += 1
            case "-c":
                #User is specifying numer of passwords, next arg is a number
                #Get next argument to parse
                #Check for buffer overrun
                if (i+1) >= len(sys.argv):
                    #Not another argument, throw an error and exit
                    print("No option provided for argument \'-c\'.\nUse \"--help\" to display usage.")
                    sys.exit()
                buffer_next = sys.argv[i+1]

                if buffer_next.isnumeric():
                    #it is a number, convert it
                    number_passwords = int(buffer_next)
                else:
                    #non-numeric, throw an error
                    print(f"Numeric value expected: {buffer_next}\nUse \"--help\" to display usage.")
                    sys.exit()

                #increment twice because it consumes the next argument
                i += 1
            case _:
                print("Unknown option.\nUse \"--help\" to display usage.")
                sys.exit()


        i += 1 #don't forget to increment!


if use_lower:
    include_lower(exclude_similar)
if use_upper:
    include_upper(exclude_similar)
if use_numbers:
    include_numbers(exclude_similar)
if use_symbols:
    include_symbols(exclude_possibly_forbidden)

##DEBUG##
#print(possible_characters)

for i in range(number_passwords):
    print(generate_password(password_length))