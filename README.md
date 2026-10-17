# Password Generator
Copyright (C) 2026 by Spectre

For licensing information, see [LICENSE.MD](LICENSE.MD).

## Description
The Password Generator is a collection of programs designed to produce passwords for use when logging in to various services.  These generate random passwords and have various options to add (or remove) entropy with the intent of making passwords harder to guess / crack.

Currently, this consists of two programs:
- Password Generator (`pwdgen.py`)
- Passphrase Generator (`ppgen.py`)

### Password Generator (pwdgen.py)
Password Generator (`pwdgen.py`) generates a random password of specified length.  The user can specify various options, including:
- Generate multiple passwords at once
- Include only certain character sets / exclude certain sets
- Exclude similar looking characters, e.g., O and 0
- Allow certain symbols that may be forbidden in passwords, e.g., \ or "

Specify `python pwdgen.py --help` to obtain more details.

### Passphrase Generator (ppgen.py)
Passphrase Generator (`ppgen.py`) generates a random passphrase of a specified number of words.  The user can specify various options, including:
- Generate multiple passphrases at once
- Provide a specific seed word
- Randomly capitalize letters
- Convert letters to "1337", e.g., e = 3
- Include a delimiter between the words

Specify `python ppgen.py --help` to obtain more details.

Passphrase generator uses dictionaries obtained from [Dr. Phillip M. Feldman](https://phillipmfeldman.org/English/spelling_dictionaries.html).  To the best of my knowledge, these dictionaries are open source and do not include any licensing terms.

### Dependencies
All modules used should be available from a standard Python installation.  No custom `pip` packages are necessary.
