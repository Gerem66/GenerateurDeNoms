#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from os import system
from random import randint

class NameCreator:
    def __init__(self, filename) -> None:
        file = open(filename)
        lines = file.readlines()
        self.lines = [ line[:-1] + ' ' for line in lines ]

        self.proba_first = {}
        self.proba_middle = {}

    def Calculate(self):
        for prenom in self.lines:
            if len(prenom) < 3 or ' ' in prenom[:-1]:
                continue
            pre = prenom[:3]
            if not pre in self.proba_first: self.proba_first[pre] = 1
            else: self.proba_first[pre] += 1

            for i in range(len(prenom) - 2):
                nom = prenom[i:i+3]
                if not nom in self.proba_middle: self.proba_middle[nom] = 1
                else: self.proba_middle[nom] += 1

    def GetRandomFromDict(self, dict):
        dict_sum = sum(dict.values())
        rnd = randint(0, dict_sum)
        total = 0
        for n in dict:
            total += dict[n]
            if total >= rnd:
                return n
        return None

    def Generate(self, number, length, delta = 0):
        names = []
        while len(names) < number:
            name = self.GetRandomFromDict(self.proba_first)
            while name[-1] != ' ':
                newDict = {}
                for d in self.proba_middle:
                    if d[:2] == name[-2:]:
                        newDict[d] = self.proba_middle[d]
                name += self.GetRandomFromDict(newDict)[-1]
            if abs(len(name[:-1]) - length) < delta:
                names.append(self.UpperFirst(name[:-1]))
        return names

    def UpperFirst(self, text):
        return text[0].upper() + text[1:].lower()

    def IsInt(self, text):
        try:
            int(text)
            return True
        except:
            return False

generator = NameCreator('db/prenom.txt')
generator.Calculate()

mode = 1

if mode == 1:
    for _ in range(10):
        names = generator.Generate(5, 7, 2)
        print('\t'.join(names))

elif mode == 2:
    f = open('db/newBDD.txt', 'a')
    userInput = ''
    while userInput != 'q':
        names = generator.Generate(4, 7, 2)
        system('clear || cls')
        for i in range(len(names)):
            print(str(i+1) + '-' + names[i], end='\t')

        try:
            userInput = input('\n>> ')

            if userInput == '': continue
            elif generator.IsInt(userInput) and int(userInput) < 5 and int(userInput) > 0:
                addName = names[int(userInput)-1]
                print(addName)
                f.write(addName + '\n')
        except KeyboardInterrupt:
            userInput = 'q'
            print()
    f.close()