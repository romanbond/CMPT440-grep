import re
import argparse

tFile = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
'''

sentence = 'Start a sentence and then bring it to an end'
#since '.' is any character it's not just limited to - or . so we do:
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d') 
matches = pattern.finditer(tFile)

for match in matches:
    print(match)

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


