#!/usr/bin/env python3

"""Shuffle the english version of the original BIP39 wordlist"""

import random
import requests

URL_WORDLIST = 'https://raw.githubusercontent.com/' \
        'bitcoin/bips/master/bip-0039/english.txt'

R = requests.get(URL_WORDLIST)
WORDLIST = R.content.splitlines()

random.seed()
WORDLIST_SHUFFLE = random.sample(WORDLIST, len(WORDLIST))

for word in WORDLIST_SHUFFLE:
    print(word.decode())
