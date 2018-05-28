from os import listdir

#Author: Martin
def get_headlines():
    '''Listar namnen på alla text-filer i mappen cleaning_articles, samt tar bort filändelsen.'''
    headlines = sorted(listdir("static/cleaning_articles"))
    headline_list = []

    for headline in headlines:
        headline = headline[:-4]
        headline_list.append(headline)
    return headline_list


#Author: Martin
def get_title_content(a):
    '''Skapar utifrån textfilerna en väg, en läs-variabel och en variabel för text-filens innehåll.'''
    headlines = listdir("static/cleaning_articles")
    headline_list = []
    for headline in headlines:
        if headline == a + ".txt":
            path = "static/cleaning_articles/" + headline
            fill = days_file = open(path,'r')
            text = fill.read()
            fill.close()
        else:
            print("test")
    return (text)


    '''Nedan skickas verktygsartiklarna'''
    #Author: Martin
    def get_tool_headlines():
        '''Listar namnen på alla text-filer i mappen tool_articles, samt tar bort filändelsen.'''
        headlines = sorted(listdir("static/tool_articles"))
        headline_list = []

        for headline in headlines:
            headline = headline[:-4]
            headline_list.append(headline)
        return headline_list


    #Author: Martin
    def get_tool_content(a):
        '''Skapar utifrån textfilerna en väg, en läs-variabel och en variabel för text-filens innehåll.'''
        headlines = listdir("static/tool_articles")
        headline_list = []
        for headline in headlines:
            if headline == a + ".txt":
                path = "static/tool_articles/" + headline
                fill = days_file = open(path,'r')
                text = fill.read()
                fill.close()
            else:
                print("test")
        return (text)
