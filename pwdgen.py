# Password Generator
# by Spectre
# ver. 0.2 (15-Oct-26)
#
# This script will generate a random password based on length and desired characters

import secrets, argparse, sys

#Defining constants
EXCLUDE_SIMILAR = "excludeSimilar"
INCLUDE_FORBIDDEN = "includeForbidden"
PASSWORD_COUNT = "passwordCount"
PASSWORD_LENGTH = "passwordLength"
INCLUDE_LOWER = "includeLower"
INCLUDE_UPPER = "includeUpper"
INCLUDE_NUMBER = "includeNumber"
INCLUDE_SYMBOL = "includeSymbol"

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
def include_symbols(include_possibly_forbidden = False):
    global possible_characters
    possible_characters += "!@#$%^&*()<>?+=-_/~"
    if include_possibly_forbidden:
        possible_characters += "'\"\\"

#Function to get one character from the list of possible characters
def get_character():
    return secrets.choice(possible_characters)

#Function to generate a password of defined length
def generate_password(length):
    generated_password = ""
    for i in range(length):
        generated_password += get_character()
    return generated_password

#Parse the command line arguments
def parse_arguments():
    #This will parse our arguments, get the results, and return a dictionary with the user's settings
    parser = argparse.ArgumentParser(description="Generate a randomly generated password.")

    #setup the options
    parser.add_argument("-c", "--count", type=int, help="If specified, output multiple passwords", default=1)
    parser.add_argument("-l","--length",type=int,help="Specify the length for the password [Default=12]",default=12)
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-i","--include", type=str, help="Specify which characters to include- a=lower case, A=upper case, n=numbers, s=symbols.",default="aAns")
    group1.add_argument("-x","--exclude",type=str, help="Specify which characters to exclude- a=lower case, A=upper case, n=numbers, s=symbols [Default=all]")
    parser.add_argument("-f","--forbidden", action="store_true", help="Include potentially forbidden symbols, such as \". [Default=false]")
    parser.add_argument("-s","--no_similar", action="store_true",help="Exclude similar characters, e.g., O and 0. [Default=false]")

    #parse the arguments
    args = parser.parse_args()

    #turn that into a dictionary
    user_options = {}

    user_options[PASSWORD_COUNT] = args.count
    user_options[PASSWORD_LENGTH] = args.length
    user_options[EXCLUDE_SIMILAR] = args.no_similar
    user_options[INCLUDE_FORBIDDEN] = args.forbidden

    #Process the include/exclude characters
    if args.exclude != None:
        #User specified EXCLUDE, which means we will include all BUT what is specified
        user_options[INCLUDE_LOWER] = False if 'a' in args.exclude else True
        user_options[INCLUDE_UPPER] = False if 'A' in args.exclude else True
        user_options[INCLUDE_NUMBER] = False if 'n' in args.exclude else True
        user_options[INCLUDE_SYMBOL] = False if 's' in args.exclude else True
    else:
        #User must have done INCLUDE, which means we only include what they specified
        user_options[INCLUDE_LOWER] = True if 'a' in args.include else False
        user_options[INCLUDE_UPPER] = True if 'A' in args.include else False
        user_options[INCLUDE_NUMBER] = True if 'n' in args.include else False
        user_options[INCLUDE_SYMBOL] = True if 's' in args.include else False


    return user_options

    
#***MAIN***
def main():
    #Get the command line arguments
    user_options = parse_arguments()

    #Generate the list of possible characters
    if user_options[INCLUDE_LOWER]:
        include_lower(user_options[EXCLUDE_SIMILAR])
    if user_options[INCLUDE_UPPER]:
        include_upper(user_options[EXCLUDE_SIMILAR])
    if user_options[INCLUDE_NUMBER]:
        include_numbers(user_options[EXCLUDE_SIMILAR])
    if user_options[INCLUDE_SYMBOL]:
        include_symbols(user_options[INCLUDE_FORBIDDEN])
    
    #Generate the passwords
    for i in range(user_options[PASSWORD_COUNT]):
        print(generate_password(user_options[PASSWORD_LENGTH]))


if __name__ == "__main__":
    main()