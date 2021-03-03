#choice function
def stylechoice():
    style = input ('What type of style do you want? Type the number in front of whichever style you want. (1) APA, (2) MLA, (3) Chicago ')
    if style == 1:
        print ('APA')
    elif style == 2:
        print ('MLA')
    elif style == 3:
        print ('Chicago')
    return style

print ('Your citation style is ' + str(stylechoice()))
