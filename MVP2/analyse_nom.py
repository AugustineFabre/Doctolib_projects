from nom_fonction import *
from nom_variable import *
import re

def seulement_alpha(list):
    alpha = []
    num_meaningful_a = 0
    for elem in list:
        if elem.isalpha() == True:
            alpha.append(elem)
        else:
            for i in elem:
                if i.isalpha() == False:
                    elem.split(i)
                    break
            for word in elem.split(i):
                if word == "a":
                    num_meaningful_a +=1
            alpha += elem.split(i)
    for elem1 in alpha:
        if elem1 == "":
            alpha.remove(elem1)

        if (elem1.islower() is False) and (elem1.isupper() is False):
            elem11 = re.findall('[a-zA-Z][^A-Z]*', elem1)
            alpha.remove(elem1)
            alpha += elem11
    return alpha, num_meaningful_a



import enchant
dict_en = enchant.Dict("en_US")
dict_fr = enchant.Dict("fr_FR")
def analyse_nom(list, num_a):
    num = 0
    num_single_a = 0
    ques = {}
    for elem in list:
        if len(elem) == 1:
            num += 1
            num_single_a += 1
            if elem != 'a':
                ques[elem] = "single letter is bad"
        else:
            if (dict_en.check(elem) is True) or (dict_fr.check(elem) is True):
                num = num
            else:
                ques[elem] = dict_en.suggest(elem) + dict_fr.suggest(elem)
                num += 1
    num -= num_a
    num_wrong_a = num_single_a - num_a
    print(num_wrong_a)
    for a in range(num_wrong_a):
        ques['a'] = "single letter is bad"
    return num, ques

print(seulement_alpha(nomFunc(candidate_rb)))
print(analyse_nom(seulement_alpha(nomFunc(candidate_rb))[0], seulement_alpha(nomFunc(candidate_rb))[1]))

print(seulement_alpha(nom_variable(candidate_rb)))
print(analyse_nom(seulement_alpha(nom_variable(candidate_rb))[0], seulement_alpha(nom_variable(candidate_rb))[1]))

print(seulement_alpha(['whereIsShe','i_like_you','a']))
print(analyse_nom(seulement_alpha(['whereIsShe','i_like_you','a'])[0], seulement_alpha(['whereIsShe','i_like_you','a'])[1]))
