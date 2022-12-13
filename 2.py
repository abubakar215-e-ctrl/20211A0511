import phonetics
import re

def same(word, file):
    phonetic_search_word = phonetics.metaphone(word)
    with open(file, 'r') as f:
        contents = f.read()
    regex = re.compile(r'\b[A-Za-z]+\b')
    matches = regex.findall(contents)
    Similar = [word for word in matches if phonetics.metaphone(word) == phonetic_search_word]
    return Similar

word = input()
file = 'words.txt'
Similar = same(word, file)
print(Similar)