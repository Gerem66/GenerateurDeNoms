#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from Generator.NameCreator import NameCreator

# Check if the user provided the database type
if len(sys.argv) < 2:
    available_dbs_raw = [f.removesuffix('.txt') for f in os.listdir('./db/') if f.endswith('.txt')]
    available_dbs = '|'.join(available_dbs_raw)
    print('Usage: python3 get-best-names.py <{}> [names_per_generation]'.format(available_dbs))
    sys.exit(1)

# Args
generationType = sys.argv[1]
namesPerGeneration = int(sys.argv[2]) if len(sys.argv) > 2 else 10

# Check if the database file exists
db_file_path = 'db/{}.txt'.format(generationType)
if not os.path.isfile(db_file_path):
    print(f'Error: Database file "{db_file_path}" not found.')
    sys.exit(1)

# Load the database and generate names
try:
    generator = NameCreator()
    generator.LoadFile(db_file_path)
    generator.Calculate()
    
    names = generator.Generate(namesPerGeneration)
    if not names:
        print('No names generated.')
        sys.exit(1)
    print(','.join(names))
except Exception as e:
    print(f'Error: {str(e)}')
    sys.exit(1)
