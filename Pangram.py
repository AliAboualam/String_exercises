""" Function to verify if a sentence uses all the letters of the alphabet"""


def is_pangram(sentence):
    new_sentence=sentence.lower()
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    panagram=True
    dict={}
    for letter in alphabet:
        dict[letter]=0
    for letter in new_sentence:
        dict[letter]=1
    for letter in alphabet:
        if dict[letter]==0:
            panagram=False
    return panagram