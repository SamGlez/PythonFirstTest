from pip._vendor.distlib.compat import raw_input

lives = 3
level = 1
success: str = "Congrats, you have reached a new level!" , (lives)
fail = "That was not correct. Try again with one less life.You have", (lives)
while lives > 0 :
    direction = raw_input("You are in the magic maze. Which way to go? ")

    print("Options\n (N)\n (S)\n (E)\n (W)")

    seleccion = raw_input('Escoge una direccion: ')
    print(seleccion)
    print("Voy a probar con los resultados")
    print(level)
    print(lives)

    def level1(a):
        print("Hi, you are in level 1")
        if a == "S":
            level = +1
            return success
        else:
            lives = -1
            return fail


    def level2(a):
        print("Hi, you are in level 2")
        if a == "S":
            level = +1
            return success
        else:
            lives = -1
            return fail


    def level3(a):
        print("Hi, you are in level 3")
        if a == "S":
            level = +1
            return success
        else:
            lives = -1
            return fail;


    d = {
        '1': level1(seleccion),
        '2': level2(seleccion),
        '3': level3(seleccion)
        }

    resultado = d[level]
    print (resultado)
       # except:
       #   print("Esa no vale")

else:
    print("You have no more lives. Sorry.")
