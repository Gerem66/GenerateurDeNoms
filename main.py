#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Generator.Functions import Clear, Align, IsInt
from Generator.NameCreator import NameCreator

DATABASE_FILE = 'db/prenom.txt'

generator = NameCreator()
generator.LoadFile(DATABASE_FILE)
generator.Calculate()

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

print('Select mode:\n\t1) Generate many names\n\t2) Add names to current personnal DB', end='\n\n')
MODE = input('>> ')

if MODE not in [ '1', '2' ]:
    print('Err: Wrong choice')
    exit()

if MODE == '1':
    Clear()
    for _ in range(10):
        names = generator.Generate(5)
        print(''.join(map(Align, names)))

# Can be used to create its own database
elif MODE == '2':
    f = open('db/newBDD.txt', 'a')
    userInput = ''
    while userInput != 'q':
        namesLength = 8
        namesPerRow = 4

        names = generator.Generate(namesLength)
        Clear()

        for i in range(namesLength):
            name = Align(str(i + 1) + '-' + names[i])
            endRow = '\n' if (i - namesPerRow + 1) % namesPerRow == 0 else ''
            print(name, end=endRow)

        try:
            userInput = input('\n>> ')

            if userInput == '': continue
            elif IsInt(userInput) and int(userInput) <= namesLength and int(userInput) > 0:
                addName = names[int(userInput)-1]
                print(addName)
                f.write(addName + '\n')
        except KeyboardInterrupt:
            userInput = 'q'
            print()
    f.close()
