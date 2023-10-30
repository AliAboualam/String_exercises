"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return("un"+word)


def make_word_groups(vocab_words):
    for i in range(1,len(vocab_words)):
        vocab_words[i]=vocab_words[0]+vocab_words[i]
    return " :: ".join(vocab_words)

def remove_suffix_ness(word):
    new_word=""
    if word[-5]=="i":
        new_word=word[:-5]+"y"
    else:
        new_word=word[:-4]
    return new_word


def adjective_to_verb(sentence, index):
    list=sentence.split()
    myword=list[index]
    if myword[-1]==".":
        myword=myword[:-1]
    return (myword+"en")