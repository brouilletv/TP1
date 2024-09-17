"""
projet fair par: Vincent Brouillet
groupe: 405
conteur de mots
"""


def count_word():
    mots = input("")
    print(mots.count(" ") + mots.count("'") + 1)


count_word()
