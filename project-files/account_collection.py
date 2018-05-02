import pymysql

def get_accounts(fields=["email", "password"]):
    '''Hämtar alla konton från databasen'''
    
    # Anslut till databasen
    db = pymysql.connect("localhost","root","cudb","account_collection", cursorclass=pymysql.cursors.DictCursor)

    # Skapa en pekare till databasen
    cursor = db.cursor()

    # Skicka frågan till databasen
    cursor.execute("SELECT * FROM accounts ORDER BY email DESC".format(", ".join(fields)))

    # Spara kontona i en variabel
    accounts = cursor.fetchall()

    # Stäng databasanslutningen
    db.close()
    return accounts

print(get_accounts()) #=> Ger alla fält
print(get_accounts(fields=["email", "password"])) #=> Ger bara e-mail och lösenord
