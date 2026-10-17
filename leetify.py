#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: leetify.py
Author: Spectre
Date: 2026-10-10
Version: 0.2
Description: This script will take a word and convert it to l33t speak based on a given liklihood weighting factor.  The intent is to add entropy
    to a passphrase while retaining human memorable.

"""


import secrets

class Leetify:
    """
    This class takes a word and converts letters to l33t speak based on a weighting factor.
    """

    __leet_dict__ = {
        'a':'@',
        'e':'3',
        'o':'0',
        's':'$',
        't':"+",
        'i':'!',
        'l':'1'
    }

    __leet_chance_default__ = 50

    @classmethod
    def leetify_word(cls, word, leet_chance=__leet_chance_default__, first_letter_chance=False):
        """
        Convert the given word based on the chance of the letters being converted.
            int leet_chance = 0-100, as percent chance of conversion (if 0, why are we here?)
            bool first_letter_chance, if true, if the first letter is leetable, it might return just the first letter leeted without the rest of letters.
        """

        #Check if first letter chance, if so, we might convert the word to a single leet letter
        if first_letter_chance and (word[0] in cls.__leet_dict__):
            #First letter chance is being used and the first letter is leetable, so let's see if the dice roll says to do it?
            if (secrets.randbelow(99)+1) <= leet_chance:
                #Winner!
                return cls.__leet_dict__[word[0]]
        
        #We need to convert the string to a list so we can edit it, we'll then return the list converted back to a string.
        word_as_list = list(word)

        #Loop through each letter, and leetify if the dice say so
        for i in range(1,len(word)):
            if (word[i] in cls.__leet_dict__) and ((secrets.randbelow(99)+1) <= leet_chance):
                #Word is leetable and the dice roll says to do it
                word_as_list[i] = cls.__leet_dict__[word[i]]
        
        return ''.join(word_as_list)
                