#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from Generator.Functions import Clear, Align
from Generator.NameCreator import NameCreator

databases = [f for f in os.listdir('./db/') if f.endswith('.txt')]
databasesNames = [f.removesuffix('.txt') for f in databases]
generators = { db: NameCreator() for db in databases }
for db in databases:
    generators[db].LoadFile('db/' + db)
    generators[db].Calculate()

if not databases:
    print('No database files found in the "db" directory.')
    sys.exit(1)

namesPerGeneration = 10
userInput = ''

try:
    while userInput != 'q':
        Clear()
        print(''.join(map(Align, databasesNames)), end='\n\n')
        for _ in range(namesPerGeneration):
            names = []
            for generator in generators.values():
                generatedNames = generator.Generate(1)
                if generatedNames:
                    names.append(generatedNames[0])
            print(''.join(map(Align, names)))
        userInput = input('\nPress q to quit, or any other key to continue: ')
except KeyboardInterrupt:
    pass
