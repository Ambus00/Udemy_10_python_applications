import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

cursor = con.cursor()

word = input("Enter a word: ")

cursor.execute("SELECT * FROM Dictionary WHERE Expression = %s", (word,))

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE %s", ("%"+word+"%",))
    words = [result[0] for result in cursor.fetchall()]
    if words:
        match = get_close_matches(word, words)[0]
        answer = input("Did you mean %s? Enter y for Yes or n for No: " % match)
        if answer.lower() == "y":
            cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = %s", (match,))
            results = cursor.fetchall()
            for result in results:
                print(result[0])
        elif answer.lower() == "n":
            print("Sorry, we couldn't find this. Please try again.")
    else:
        print("Sorry, we didn't understand your request. Please try again.") 
