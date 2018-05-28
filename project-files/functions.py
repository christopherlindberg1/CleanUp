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


#Author: Martin
def get_tool_headlines():
    '''Listar namnen på alla text-filer i mappen tool_articles, samt tar bort filändelsen.'''
    headers = sorted(listdir("static/tool_articles"))
    header_list = []

    for header in headers:
        header = header[:-4]
        header_list.append(header)
    return header_list


#Author: Martin
def get_tool_content(a):
    '''Skapar utifrån textfilerna en väg, en läs-variabel och en variabel för text-filens innehåll.'''
    header = listdir("static/tool_articles")
    header_list = []
    for header in headers:
        if header == a + ".txt":
            path = "static/tool_articles/" + header
            fill = days_file = open(path,'r')
            text = fill.read()
            fill.close()
        else:
            print("test")
    return (text)
