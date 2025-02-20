#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from Generator.Functions import UpperFirst

class NameCreator:
    def __init__(self) -> None:
        self.prenoms = []
        self.proba_first = {}
        self.proba_middle = {}

        '''
            If conditions is empty, all generated pseudo shown
            Else, it show only if one of conditions is True

            x  : Name is valid if it contains 'x'
            !x : Need 'x' in generated name
            x* : Name need to starts with 'x'
            *x : Name need to ends with 'x'
        '''
        self.conditions = []

    def LoadFile(self, filename):
        try:
            file = open(filename)
            lines = file.readlines()
            self.prenoms = [ line[:-1] + ' ' for line in lines ]
        except Exception as e:
            print(e)
            exit(1)

    def Calculate(self):
        for prenom in self.prenoms:
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

    def Generate(self, number, minLength = 4, maxLength = 8):
        if len(self.prenoms) == 0:
            return []

        names = []
        while len(names) < number:
            name = self.GetRandomFromDict(self.proba_first)
            while name[-1] != ' ':
                newDict = {}
                for d in self.proba_middle:
                    if d[:2] == name[-2:]:
                        newDict[d] = self.proba_middle[d]
                name += self.GetRandomFromDict(newDict)[-1]
            if minLength <= len(name[:-1]) <= maxLength:
                if len(self.conditions) == 0:
                    names.append(UpperFirst(name[:-1]))
                else:
                    simpleConditionsLength = 0
                    simpleConditionsValid = 0
                    otherConditionsLength = 0
                    otherConditionsValid = 0
                    for condition in self.conditions:
                        c = condition.upper()
                        if c.startswith('!'):
                            otherConditionsLength += 1
                            otherConditionsValid += 1 if c[1:] in name else -1000
                        elif c.startswith('*'):
                            otherConditionsLength += 1
                            otherConditionsValid += 1 if name.endswith(c[1:] + ' ') else -1000
                        elif c.endswith('*'):
                            otherConditionsLength += 1
                            otherConditionsValid += 1 if name.startswith(c[:-1]) else -1000
                        else:
                            simpleConditionsLength += 1
                            if c in name:
                                simpleConditionsValid += 1
                    simpleValid = simpleConditionsLength == 0 or simpleConditionsValid > 0
                    otherValid = otherConditionsLength == 0 or otherConditionsValid > 0
                    if simpleValid and otherValid:
                        names.append(UpperFirst(name[:-1]))
        return names
