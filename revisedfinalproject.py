def overallinfo():
    firstname = input('Enter the creator/author first name ')
    lastname = input('Enter the creator/author last name ')
    title = input('Enter the title of the thing ')
    datem = input('Enter the month the thing was created ')
    dated = input('Enter the day the thing was written ')
    datey = input('Enter the year the thing was written ')
    fulllist = [firstname, lastname, title, datem, dated, datey ]
    return fulllist

type = input('What type of style do you want? Type the first letter of whichever type you want in uppercase letters. APA, MLA, Chicago ')

if type == 'M':
    first = input ('What type of source are you citing? book, website, a journal article, or an online video/film? ')
   
    if first == 'book':
        overallinfo()
        publisher = input ('Enter the books publisher ')
        date = input ('Enter the year of publishing ')
        print ('Here is your final citation ')
        print (list(fulllist[1] + ', ') + (list(fulllist[0] + '. ') + (list(fulllist[2] + '. ') + str(publisher + ', ') + str(date + '.' ))

    if first == 'website'
        title = input ('Enter the title of the article')
        authornf = input ('Enter the authors first name ')
        authornl = input ('Enter the authors last name ')
        date = input ('Enter the date the article/website was published ')
        url = input ('Enter the articles url ')
       
        print ('Here is your final citation ')
        print (list(fulllist[2]) + ', ' + str(authornf) + '. ' + ('"') + str(title + ', ') 
        + str(date + ', ') + str(url))

elif type == 'C':
    first = input ('What type of source are you citing? A book, website, or journal? ')


    if first == 'book':
        name1 = input('Enter the authors first name ')
        name2 = input ('Enter the authors last name ')
        title = input ('Enter the title of the book ')
        state = input ('Enter the state of publishing ')
        publisher = input ('Enter the publisher ')
        date =  input ('Enter the date of publishment ')


        print ('Here is your final citation ')
        print (str(name2 + ', ') + str(name1 + ', ') + str(title + '. ') + str(state + ': ') + str(publisher + ', ') + str(date + '.'))

elif type == 'A':
    first = input ('What type of source are you citing? A website, ')

    if first == 'website':
        name1 = input ('Enter the authors first name ')
        name2 = input ('Enter the authors last name ')
        year = input ('Enter the year the article was written ')
        month = input ('Enter the year the article was written in english, not numbers ')
        day = input ('Enter what day the article was written, in number(s) ')
        motto = input ('Enter the website/articles subtitle/motto with punctuation ')
        name = input ('Enter the websites name ')
        url = input ('Enter the url/link to the website ')
        print ('Here is your final citation! ')
        print (str(name2 + ', ') + str(name1[0] + '. ') + '(' + str(year + ', ') + str(month + ' ') + str(day + '). ')
         + str(motto + '. ') + str(name + '. ') + str(url) + '.')