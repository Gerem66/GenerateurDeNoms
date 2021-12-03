#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Generator.Functions import Clear, Align
from Generator.NameCreator import NameCreator

generatorH = NameCreator()
generatorH.LoadFile('db/prenom.txt')
generatorH.Calculate()

generatorW = NameCreator()
generatorW.LoadFile('db/wow.txt')
generatorW.Calculate()

generatorS = NameCreator()
generatorS.LoadFile('db/skyrim.txt')
generatorS.Calculate()

allGenerators = {
    'Human': generatorH,
    'Warcraft': generatorW,
    'Skyrim': generatorS
}

namesPerGeneration = 10
userInput = ''
while userInput != 'q':
    Clear()
    print(''.join(map(Align, allGenerators.keys())), end='\n\n')
    for _ in range(namesPerGeneration):
        names = []
        for generator in allGenerators.values():
            names.append(generator.Generate(1)[0])
        print(''.join(map(Align, names)))
    userInput = input('\nPress q to quit, or any other key to continue: ')