import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "PAST":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense.upper() == "FUTURE":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    elif tense == "PRESENT":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition(quantity):
    if quantity == 1:
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    else:
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):

    preposition = get_preposition(quantity)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_sentences = f"{preposition} {determiner} {noun}"
    return prepositional_sentences.lower()

def get_prepositional_phrase_2(quantity):

    preposition = get_preposition(quantity)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_sentences_2 = f"{preposition} {determiner} {noun}."
    return prepositional_sentences_2.lower()

def make_sentence(quantity, tense):
    
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner} {noun} {verb}"
    return sentence.capitalize()

def main():
    sentences = [
        make_sentence(1, "PAST"),
        make_sentence(1, "PRESENT"),
        make_sentence(1, "FUTURE"),
        make_sentence(2, "PAST"),
        make_sentence(2, "PRESENT"),
        make_sentence(2, "FUTURE"),
    ]

    prepositional_sentences = [
        get_prepositional_phrase(1),
        get_prepositional_phrase(1),
        get_prepositional_phrase(1),
        get_prepositional_phrase(2),
        get_prepositional_phrase(2),
        get_prepositional_phrase(2),
    ]
    prepositional_sentences_2 = [
        get_prepositional_phrase_2(1),
        get_prepositional_phrase_2(1),
        get_prepositional_phrase_2(1),
        get_prepositional_phrase_2(2),
        get_prepositional_phrase_2(2),
        get_prepositional_phrase_2(2),
    ]
    for x in range(6):
        print(f"{sentences[x]} {prepositional_sentences[x]} {prepositional_sentences_2[x]}")

main()
