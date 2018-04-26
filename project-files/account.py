import pymysql

def get_articles(fields=["email", "password"]):
    '''Hämtar alla konton från databasen'''
    
    # Anslut till databasen
    db = pymysql.connect("localhost","root","cudb","article_collection", cursorclass=pymysql.cursors.DictCursor)

    # Skapa en pekare till databasen
    cursor = db.cursor()

    # Skicka frågan till databasen
    cursor.execute("SELECT * FROM articles ORDER BY email DESC".format(", ".join(fields)))

    # Spara filmerna i en variabel
    articles = cursor.fetchall()

    # Stäng databasanslutningen
    db.close()
    return articles

print(get_articles()) #=> Ger alla fält
print(get_articles(fields=["email", "password"])) #=> Ger bara title & image
