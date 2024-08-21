import random

print("Hoi, du chline Hueresohn")
print("Machemer Scherer Stei Papier")
print("Schere = s, Stien = r, Papier = p")

eingabe = input("Gib mir dini Uswahl:")
spielzuege = ["s", "r", "p"]

if eingabe in spielzuege:
    random.shuffle(spielzuege)
    computer = spielzuege[0]

    print("Spieler: " + eingabe)
    print("Computer: " + computer)

    if eingabe == computer:
        print("Unentschieden!")
    elif (eingabe == "s" and computer == "p") or (eingabe == "r" and computer == "s") or (eingabe == "p" and computer == "r"):
        print("Du gewinnst! ")
    else:
        print("Computer gewinnt! ")

else:
    print("Du Hs hesch öbbis falsches igeh")





