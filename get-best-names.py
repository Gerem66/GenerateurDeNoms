#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Generator.NameCreator import NameCreator

if len(sys.argv) < 2:
    print('Usage: python3 get-best-names.py [db_type]')
    sys.exit(1)

generationType = sys.argv[1]
namesPerGeneration = int(sys.argv[2]) if len(sys.argv) > 2 else 10

generator = NameCreator()
generator.LoadFile('db/{}.txt'.format(generationType))
generator.Calculate()

names = generator.Generate(namesPerGeneration)
print(','.join(names))
