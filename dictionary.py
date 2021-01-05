#!/usr/bin/env python

import json
import pprint
import random

DEBUG = False
CHECK_RAND = False
DICTIONARY_FILE_PATH = "dictionary.txt"


def read_dictionary():
    with open(DICTIONARY_FILE_PATH) as json_file:
        dictionary_json = json.load(json_file)
        if DEBUG:
            print("********************* JSON DICTIONARY - begin ******************")
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(dictionary_json)
            sizeofdict = len(dictionary_json['lword'])
            print("JSON dictionary size = ", sizeofdict)
            print("********************* JSON DICTIONARY - end ********************")
        dictionary = []
        for word_json in dictionary_json['lword']:
            word = {}
            word['foreign'] = word_json['m']
            word['translation'] = word_json['t']
            word['add_text'] = []
            if 'gcl' in word_json.keys():
                for add_text_json1 in word_json['gcl']:
                    if 'lcw' in add_text_json1.keys():
                        for add_text_json2 in add_text_json1['lcw']:
                            if 'l' in add_text_json2.keys():
                                word['add_text'].append(add_text_json2['l'])
            dictionary.append(word)
        return dictionary


def select_word(dictionary):
    sizeofdict = len(dictionary)
    return dictionary[random.randint(0, sizeofdict-1)]


def show_word(word):
    print("Word:", word['translation'])
    ii = 1
    while True:
        user_input = input("Answer: ")
        if (user_input == word['foreign']):
            break
        print(word['foreign'][0:ii])
        if (ii >= len(word['foreign'])):
            break

        ii += 1
    print("------------------------------------------------------")
    print("SUCCESS!")
    print(word['foreign'], " - ", word['translation'])
    for textToPrint in word['add_text']:
        print(textToPrint)
    print("------------------------------------------------------")

    return


def check_rand(sizeofdict, nrOfTrys):
    checkRand = [0 for ii in range(sizeofdict)]
    for ii in range(nrOfTrys):
        randValue = random.randint(0, sizeofdict-1)
        checkRand[randValue] += 1
    print("Size=", sizeofdict)
    for ii in range(sizeofdict):
        print(ii, checkRand[ii])
    return


def main():
    # initilize rand generator
    random.seed(a=None, version=2)

    # read json dictionary
    my_dictionary = read_dictionary()

    # checking random function - debug
    if CHECK_RAND:
        check_rand(len(my_dictionary), 10)
        exit()
    # print dictionary - debug
    if DEBUG:
        print("********************* MY DICTIONARY - begin *******************")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(my_dictionary)
        sizeofdict = len(my_dictionary)
        print("Dictionary size = ", sizeofdict)
        print("********************* MY DICTIONARY - end *********************")
    # main action
    firstRun = True
    while True:
        if firstRun:
            print("Let's start!")
            user_input = 'Y'
            firstRun = False
        else:
            user_input = input("Try another word(Y/N):")
        print("------------------------------------------------------")
        if ((user_input == 'Y') or (user_input == 'y')):
            selected_word = select_word(my_dictionary)
            show_word(selected_word)
            continue
        if ((user_input == 'N') or (user_input == 'n')):
            print("Thanks for participation. Goodbye!")
            break
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
