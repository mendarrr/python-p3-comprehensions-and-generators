#!/usr/bin/env python3

def return_evens(num_list):
     even_list = [num for num in num_list if num % 2 == 0]
     return even_list
     pass

def make_exclamation(sentence_list):
     exclamation_list = [sentence + "!" for sentence in sentence_list]
     return exclamation_list
     pass