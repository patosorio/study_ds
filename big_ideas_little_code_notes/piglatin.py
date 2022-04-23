""" Program that takes a string as input and translate it to pig latin """

def pig_latin(sentence):
    """ Translates a given string to Pig Latin """

    translated = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for word in sentence.split():
        if word[0] in vowels:
            translation = ((word + 'way'))
            translated.append(translation)
            
        elif word[0].isupper():
            translation = ((word[1].upper() + word[2:] + word[0].lower() + 'ay'))
            translated.append(translation)
        
        else:
            translation = ((word[1:] + word[0] + 'ay'))
            translated.append(translation)

    translated = ' '.join([str(word) for word in translated]).replace(',', '')
    return translated


while True:
    """ Ask user to input a string to translate to Pig Latin """
    sentence = input(str('Please enter the sentence you want to translate to Pig Latin: '))
    if sentence == '':
        break
    else:
        print(pig_latin(sentence))


""" Improvements : remove integers from user inputs """