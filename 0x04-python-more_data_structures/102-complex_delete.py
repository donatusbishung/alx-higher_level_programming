#!/usr/bin/python3
 def complex_delete(a_dictionary, value):
     de_k = []

     for i in a_dictionary:
         if a_dictionary[i] == value:
             de_k.append(i)

    for i in de_k:
        del (a_dictionary[i])

    return a_dictionary
