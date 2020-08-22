import json
from difflib import get_close_matches
from os import system,name
from time import sleep

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

data=json.load(open("data.json"))
ch=1
while(ch):
    word=input("Enter the Word\n\n")
    word=word.lower()
    if word in data:
        for i in data[word]:
            print("*",i)
    elif word.title() in data:
        for i in data[word.title()]:
            print("*",i)

    elif word.upper() in data:
        for i in data[word.upper()]:
            print("*",i)
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did u mean %s" %get_close_matches(word, data.keys())[0])
        dec=input("press y for yes and n for no\n") 
        if dec=="y":
            print(get_close_matches(word, data.keys())[0])
        elif dec=="n":
            print("Sorry . Word not fownd in dictionary.☺☺☺")
        else:
            print("please enter y or n.")

    else:
        print("Sorry . Word not found in dictionary.☺☺☺")

    print("\nif you want to exit press 0, else press 1 to continue")
    ch=int(input())
    sleep(1)
    clear()
print("Thank you, have a nice day.")
sleep(3)
clear()