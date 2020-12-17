#!/usr/bin/env python

import json
import pprint
import random

DEBUG = False


def read_dictionary():
    with open('dictionary.txt') as json_file:
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
    print("Selected word = ", word)
    return


def main():
    # read json dictionary
    my_dictionary = read_dictionary()
    pp = pprint.PrettyPrinter(indent=4)
    if DEBUG:
        print("********************* MY DICTIONARY - begin *******************")
        pp.pprint(my_dictionary)
        sizeofdict = len(my_dictionary)
        print("Dictionary size = ", sizeofdict)
        print("********************* MY DICTIONARY - end *********************")
    while True:
        user_input = input("Try another word(Y/N):")
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
