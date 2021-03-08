# -*- coding: utf-8 -*-

import json

from difflib import get_close_matches

dictionary=json.load(open('data.json'))

def translate(word):
    if word in dictionary:
        return dictionary[word]
    elif word.lower() in dictionary:
        return dictionary[word.lower()]
    else :
        return "Not Found"
        

word=input("Enter word to search: ")


output=translate(word)

i=1
for x in output:
    print("{}. ".format(i)+x)
    i=i+1