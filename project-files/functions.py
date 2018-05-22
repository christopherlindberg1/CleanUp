from functools import wraps
from os import listdir

#Author: Martin
def get_headlines():
    '''Listar namnen på alla text-filer i mappen cleaning_articles, samt tar bort filändelsen.'''
    headlines = listdir("static/cleaning_articles")
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
        else:
            print("test")
    return (a + ": " + text)


def is_logged_in(f):
    ''' Används för att göra vissa sidor synliga för endast inloggade användare '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("För att ta del av den här sidan måste du logga in", "primary")
            return redirect(url_for("login"))
    return wrap
