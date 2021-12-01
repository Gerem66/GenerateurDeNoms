#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Generator.Functions import Clear, IsInt
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
generator.conditions = [ 'h', 'k', '!y' ]

MODE = 1

if MODE == 1:
    Clear()
    for _ in range(10):
        def align(text): return text.ljust(20)
        names = generator.Generate(5)
        print(''.join(map(align, names)))

elif MODE == 2:
    f = open('db/newBDD.txt', 'a')
    userInput = ''
    while userInput != 'q':
        names = generator.Generate(4, 7, 2)
        Clear()
        for i in range(len(names)):
            print(str(i+1) + '-' + names[i], end='\t')

        try:
            userInput = input('\n>> ')

            if userInput == '': continue
            elif IsInt(userInput) and int(userInput) < 5 and int(userInput) > 0:
                addName = names[int(userInput)-1]
                print(addName)
                f.write(addName + '\n')
        except KeyboardInterrupt:
            userInput = 'q'
            print()
    f.close()