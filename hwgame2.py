from pip._vendor.distlib.compat import raw_input

lives = 3
level = 1
def success():
    global level
    level += 1
    print("Congrats, you have reached level", (level), "! You have", (lives), "lives")

def fail():
    global lives
    lives -= 1
    print("That was not correct. Try again with one less life.You have", (lives), "lives")

while lives > 0 :

    seleccion = raw_input("You are in the magic maze. Which way to go? Options (N) (S) (E) or (W)")

    if level == 1:
        if seleccion == "S":
            success()
        else:
            fail()
    elif level == 2:
        if seleccion == "S":
            success()

        else:
            fail()

    elif level == 3:
        if seleccion == "N":
            success()

        else:
            fail()

    elif level == 4:
        if seleccion == "W":
            success()
        else:
            fail()

    elif level == 5:
        if seleccion == "E":
            success()
        else:
            fail()

    elif level == 6:
        if seleccion == "S":
            print("You reached the end of the game. Congrats!")
            break
        else:
            fail()

else:
    print("END OF GAME: You have no more lives. Sorry.")
