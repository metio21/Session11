#dictionary
d = {} #empty dictionary
eng_to_spa = {"one": "uno", "two": "does", "three": "tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes": "si", "no": "no"}) #update a dict with a new dict
print(eng_to_spa)
del eng_to_spa["no"]
print(eng_to_spa)

print(eng_to_spa.popitem()) #not very useful as we dont really know what the last item in the dictionary is

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means){key}")

for key, value in eng_to_spa.items():
    print(f"{value} means {key}")


#link analyses
import requests

from midterm_exercises import punctuation

link = "https://www.gutenberg.org/cache/epub/84/pg84.txt"

result = requests.get(link)
# print(result.text)
unique_words = {}
punctuation = ",.?=-()"
print(result.text)
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word,0) + 1

freq = list(unique_words.values())
freq = sorted(freq, reverse = True)
freq = freq[:100]
print(freq)
print("herro ")
for f in freq:
    for key, value in unique_words.items():
        if value == f:
            print(key)


#function
import requests

from midterm_exercises import punctuation

link = "https://www.gutenberg.org/cache/epub/84/pg84.txt"

result = requests.get(link)
# print(result.text)
unique_words = {}
punctuation = ",.?=-()"
print(result.text)
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word,0) + 1

freq = list(unique_words.values())
freq = sorted(freq, reverse = True)
freq = freq[:100]
print(freq)
print("herro ")
for f in freq:
    for key, value in unique_words.items():
        if value == f:
            print(key)





