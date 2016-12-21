# python 3.5.2
# -*- coding: utf-8 -*-
from os.path import exists
from collections import OrderedDict


class Dictionary:
    def __init__(self):
        # initialize
        self.file_path = None
        self.content = None
        self.dictionary = {}
        self.ordered_dictionary = {}

    def file_load(self, file_path, permission='r'):
        # check whether the file is existing
        try:
            assert exists(str(file_path))
        except:
            print("The file ain't existing")

        self.file_path = file_path

        # read the file
        with open(file_path, permission) as f:
            self.content = filter(len, f.read().split())
            f.close()

        return self.content or []

    def file_parse(self):
        # check whether the content of file is an empty
        try:
            assert self.content
        except:
            print("The file is an empty")

        # generate a dictionary file that has a first letter to be a key to mapping with value
        for value in self.content:
            key = value[0]
            self.dictionary.setdefault(key, []).append(value)

    def get_key(self, word):
        # return the first letter of word
        return word[0] or None

    def order_dictionary(self):
        # order dictionary
        return OrderedDict(sorted(self.dictionary.items()))

    def search(self, word):
        key = self.get_key(word)
        if word in self.dictionary.get(key):
            print(word + " is in a dictionary")
        else:
            print("The word is not in the dictionary")

    def insert(self, word):
        key = self.get_key(word)
        if word in self.dictionary.get(key):
            print("The word is existing in the dictionary")
            return
        self.dictionary.setdefault(key, []).append(word)
        print("inserted successfully")

    def delete(self, word):
        key = self.get_key(word)
        if word not in self.dictionary.get(key, 'empty'):
            print("The word is not existing in the dictionary")
            return
        self.dictionary.get(key).remove(word)
        print("Deleted successfully")

    def save_file(self, save_path="./save_dict.txt", permission='w'):
        self.ordered_dictionary = self.order_dictionary()
        with open(save_path, permission) as f:
            for key, value in self.ordered_dictionary.items():
                f.write(str(key))
                f.write(str(value))
                f.write("\n")
            f.close()

    def search_by_letter(self, letter):
        if self.dictionary.get(letter, 'empty') == "empty":
            print("The letter is not existing in the dictionary")
            return
        for index, value in enumerate(self.dictionary.get(letter)):
            print(index + 1, value)

    def print_dictionary(self):
        self.ordered_dictionary = self.order_dictionary()
        for index, value in self.ordered_dictionary.items():
            print(index, " : ", value)

    def exe(self):
        while 1:
            option = input("1.search  2.insert  3.delete  4.save  5.search_by_letter  6.print  7.exit")

            if option == '1':
                word = input("Enter the word")
                self.search(word)
            elif option == '2':
                word = input("Enter the word")
                self.insert(word)
            elif option == '3':
                word = input("Enter the word")
                self.delete(word)
            elif option == '4':
                self.save_file()
            elif option == '5':
                word = input("Enter the word")
                self.search_by_letter(word)
            elif option == '6':
                self.print_dictionary()
            elif option == '7':
                break
            else:
                print("Wrong input")


test = Dictionary()
test.file_load('./words.txt')
test.file_parse()
test.exe()
