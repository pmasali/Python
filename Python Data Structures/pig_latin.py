def pig_latin(wrd):
    first_letter = wrd[0]
    if first_letter in 'aeiou':
        pig_word = wrd + 'ay'
    else:
        pig_word = wrd[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('word'))