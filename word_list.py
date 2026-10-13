#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: word_list.py
Author: Spectre
Date: 2026-10-10
Version: 0.2
Description: This script reads a list of English words and exposes them as a class that contains a dictionary based on the first letter of the word.

This uses both the "Small" and "Large" "Spelling Dictionary" from Dr. Phillip M. Feldman, https://phillipmfeldman.org/English/spelling%20dictionaries.html
"""

import os, secrets

class WordList:
    """
    This class will load a list of common English words.  The loaded list will appear in a dictionary where the key is the first letter of the word(s).
    """
    __DEFAULT_FILENAME = "word_list.txt"

    def __init__(self, filename = __DEFAULT_FILENAME):
        #Define an empty dictionary to store the words
        self.words = {}

        #Check if filename exists
        if not os.path.exists(filename):
            #File not found, throw an error
            raise FileNotFoundError(f"File note found: {filename}")

        #Open the file, and loop
        with open(filename, "rt") as f:
            #Read and parse each line
            for line in f:
                buffer = line.strip().lower()
                first_letter = buffer[0]
                #Check if letter exists in the dictionary, add it if not
                if not first_letter in self.words:
                    self.words[first_letter] = []
                self.words[first_letter].append(buffer)

    def get_word(self, first_letter):
        """
        This function returns a random word starting with the specified letter.
        """

        #i = random.randrange(len(self.words[first_letter.lower()]))
        i = secrets.randbelow(len(self.words[first_letter.lower()]))
        return self.words[first_letter][i]

