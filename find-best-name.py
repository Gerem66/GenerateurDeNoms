#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, random
from Generator.Functions import Clear, Align, IsInt
from Generator.NameCreator import NameCreator

CUSTOM_DATABASE_FILE = 'db/customDB.txt'

databases = [f for f in os.listdir('./db/') if f.endswith('.txt') and not f.endswith('customDB.txt')]
generators = { db: NameCreator() for db in databases }
for db in databases:
    generators[db].LoadFile('db/' + db)
    generators[db].Calculate()

if not databases:
    print('No database files found in the "db" directory.')
    sys.exit(1)



# Need x : !x
# Contain x : x
# Ends with x : *x
# Starts with x : x*
# Eg:
#     Starts with a and end with i:
#         generator.conditions = [ 'a*', '*i' ]
#     Contain (h or b) and i:
#         generator.conditions = [ 'h', 'b', '!i' ]
#generator.conditions = [ 'h', 'k', '!y' ]


userInput = ''
customMode = False
customGenerator = None
f = open(CUSTOM_DATABASE_FILE, 'a')

while userInput != 'q':
    namesCount = 9
    namesPerRow = 3

    # Custom database mode
    if customMode:
        if customGenerator is None:
            customGenerator = NameCreator()
            customGenerator.LoadFile(CUSTOM_DATABASE_FILE)
            customGenerator.Calculate()
        names = customGenerator.Generate(namesCount)
    else:
        generatorIndex = random.randint(0, len(databases) - 1)
        names = generators[databases[generatorIndex]].Generate(namesCount)

    Clear()

    if customMode:
        print('Custom Database')
        print('================\n')

    for i in range(namesCount):
        name = Align(str(i + 1) + '-' + names[i])
        endRow = '\n' if (i - namesPerRow + 1) % namesPerRow == 0 else ''
        print(name, end=endRow)

    try:
        # Main menu
        print()
        bold = '\033[1m'
        reset = '\033[0m'
        print(f'{bold}1-{namesCount}{reset}\tAdd your favorite name to the custom database')
        print(f'{bold}Enter{reset}\tgenerate new names')
        if customMode:
            print(f'{bold}m{reset}\tCome back to the random generation mode to feed your custom database')
        else:
            print(f'{bold}m{reset}\tGenerate new names from your custom database')
        print(f'{bold}q or ctrl-c{reset} to quit')

        # User input
        userInput = input('\n>> ')
        if userInput == '':
            continue
        elif userInput == 'm':
            customMode = not customMode
        elif IsInt(userInput) and int(userInput) <= namesCount and int(userInput) > 0:
            addName = names[int(userInput)-1]
            print(f'Adding name: {addName}')
            f.write(addName + '\n')
    except KeyboardInterrupt:
        userInput = 'q'
        print()

f.close()
