#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: ppgen.py
Author: Spectre
Date: 2026-10-10
Version: 0.2
Description: This script generates a pass phrase.  Optionally can be seeded by a starting acronym and has options for changing characters to [hopefully] add entropy that avoids dictionary attacks.

This uses the "Small Spelling Dictionary" from Dr. Phillip M. Feldman, https://phillipmfeldman.org/English/spelling%20dictionaries.html
"""

#Let's brainstorm inputs for a moment - length (if random; this should be function that generates random and calls main generator) or seed;
# leetify (+weighting); case options - capitalize first, capitalize random (+weighting)
#  Some other inputs for consideration - inject numbers and letters at random?  Perhaps as part of the random seed?

import word_list, leetify, secrets, argparse, string

#Define some handy constants
PASSPHRASE_COUNT = "count"
SEED_WORD = "seed"
CAPITALIZE_FIRST = "capFirst"
CAPITALIZE_RANDOM = "capRandom"
LEET_RANDOM = "leetRandom"
PASSPHRASE_WORD_DELIMITER = "wordDelimiter"
USE_LARGE_DICTIONARY = "useLargeDic"

LARGE_DICTIONARY_FILENAME = "word_list_large.txt"

def generate_random_string(length:int)->str:
    #Generate a random length string of specified length to use as a seed word
    string_buffer = ""
    for i in range(length):
        string_buffer += secrets.choice(string.ascii_lowercase)
    return string_buffer

def capitalize_random(word:str, capitalize_chance:int=10)->str:
    #convert word to a list
    word_buffer = list(word)

    #loop through each character, capitalize if the odds favor it
    for i in range(1, len(word_buffer)):
        if (secrets.randbelow(99)+1) <= capitalize_chance:
            #We win! Capitalize
            word_buffer[i] = word_buffer[i].upper()

    #return the new string
    return ''.join(word_buffer)

def generate_passphrase(words:word_list.WordList, seed:str, capitalize_first:bool, capitalize_random_weight:int, leetify_weight:int, word_delimiter:str)->str:
    

    #String to hold the WIP passphrase
    passphrase = ""

    #loop over each letter in the seed
    for index, character in enumerate(seed):
        #is it a letter?
        if character.isalpha():
            #Is a letter, get a word starting with that letter
            word = words.get_word(character.lower())
            
            #if first letter should be capitalized, do that now
            if capitalize_first:
                word = word.capitalize()
            
            #Do leetify next, since it always assumes lower case letters
            if leetify_weight > 0:
                #Non-zero, so run it
                word = leetify.Leetify.leetify_word(word, leetify_weight)

            #Random capitalization
            if capitalize_random_weight > 0:
                #Non-zero, run it
                word = capitalize_random(word, capitalize_random_weight)

            #Finaly, update the passphrase
            passphrase += word

        else:
            #Not a letter, just write it and continue
            passphrase += character
        
        #Check if this is the last time through the loop.  If not, append the delimiter.
        if index < (len(seed)-1):
            passphrase += word_delimiter

    #All done, write out the generated passphrase
    return passphrase

def parse_arguments():
    #This will parse our arguments, get the results, and return a dictionary with the user's settings
    parser = argparse.ArgumentParser(description="Generate a passphrase based on a seed word.")

    #setup the options
    parser.add_argument("-c", "--count", type=int, help="If specified, output multiple possible passphrases", default=1)
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-l","--length",type=int,help="Specify the length for a random seed",default=6)  #changed to 6, per EFF: https://www.eff.org/dice
    group1.add_argument("-s","--seed",type=str,help="Specify a seed word to use")
    parser.add_argument("-a", action="store_false", help="Suppress capitalizing the first letter of each word.  (Default capitalizes first word)")
    parser.add_argument("-b", action="store_true",help="If specified, capitalize random letters.")
    parser.add_argument("-B", type=int, help="Specify the percent chance of a random letter being capitalized. (0-100)", default=25)
    parser.add_argument("-d","--delimiter",type=str,help="Specify a delimiter to appear between each word of the passphrase.  (Default is no character)", default="")
    parser.add_argument("-e",action="store_true",help="If specified, uses the large, extended dictionary.  This adds significantly more words, but some may be less common or offensive.")
    parser.add_argument("-z",action="store_true",help="If specified, randomly convert letters to '1337'.")
    parser.add_argument("-Z",type=int,help="Specify the percent change of a random letter being turned to '1337'. (0-100)", default=10)
    

    #parse the arguments
    args = parser.parse_args()

    #turn that into a dictionary
    user_options = {}

    user_options[PASSPHRASE_COUNT] = args.count

    #check if random or seed
    if args.seed != None:
        #A seed was specified
        user_options[SEED_WORD] = args.seed
    else:
        #no seed specified, use a random one
        user_options[SEED_WORD] = generate_random_string(args.length)

    user_options[CAPITALIZE_FIRST] = args.a

    #Check if we should randomly capitalize and at what percent
    if args.b:
        user_options[CAPITALIZE_RANDOM] = args.B
    else:
        user_options[CAPITALIZE_RANDOM] = 0

    #Check if we should convert to 1337 and at what percent
    if args.z:
        user_options[LEET_RANDOM] = args.Z
    else:
        user_options[LEET_RANDOM] = 0

    #Specify the delimiter; defaults "" if not specified
    user_options[PASSPHRASE_WORD_DELIMITER] = args.delimiter

    #Check if we should use the large dictionary
    user_options[USE_LARGE_DICTIONARY] = args.e


    return user_options


def main():

    #Run parser on arguments
    user_options = parse_arguments()

    #Make an instance of the word list
    words = word_list.WordList() if not user_options[USE_LARGE_DICTIONARY] else word_list.WordList(LARGE_DICTIONARY_FILENAME)

    for i in range(user_options[PASSPHRASE_COUNT]):
        print(generate_passphrase(words, user_options[SEED_WORD], user_options[CAPITALIZE_FIRST], user_options[CAPITALIZE_RANDOM], user_options[LEET_RANDOM], user_options[PASSPHRASE_WORD_DELIMITER]))


if __name__ == "__main__":
    main()
