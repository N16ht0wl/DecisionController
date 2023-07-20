import random

film = ["a","b","c"]
izlendi=[]
while True:
    movie = random.choice(film)
    print(movie)
    watched = input("bu filmi izlediniz mi?")

    if (watched == "y"):
        izlendi.append(movie)
        film.remove(movie)
        print(izlendi)
        print(film)
        break
    elif (watched == "n"):
        print(izlendi)
        print(film)

    else:
        print("pls y/n")

