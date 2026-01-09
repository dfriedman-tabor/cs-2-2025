from random import choice

nouns = []
file = open("nouns.txt", "r")
for word in file:
    nouns.append(word.strip())


verbs = ["ate", "passed", "walked", "swam"]

adjectives = ["blue", "big", "tall", "happy"]
articles = ["the", "a"]
punctuation = [".", "?", "!"]

leadsTo = {"articleS":["adjectiveS", "subject"],
           "articleO":["adjectiveO", "object"],
           "adjectiveS":["subject"],
           "adjectiveO":["object"],
           "subject":["verb"],
           "verb":["articleO","object"],
           "object":["punctuation"],
           "punctuation":[None]}

options = {"subject":nouns,
           "object":nouns,
           "verb":verbs,
           "articleS":articles,
           "articleO":articles,
           "adjectiveS":adjectives,
           "adjectiveO": adjectives,
           "punctuation":punctuation
           }

current = "articleS"
sentence = ""

while current != None:
    # print(current)
    currentOptions = options[current]
    sentence += choice(currentOptions) + " "

    nextOptions = leadsTo[current]
    current = choice(nextOptions)

print(sentence)






