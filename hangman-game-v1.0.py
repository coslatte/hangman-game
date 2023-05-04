import os
import random as r

random_word = None


def word():
    global random_word
    if random_word is None:
        with open("./archivos/data.txt", 'r', encoding='utf-8') as f:
            data = dict(enumerate([line.strip("\n") for line in f]))
            random_word = data[r.randint(0, len(data))]
    return [letter for letter in random_word]


def printOnScreen():

    w_complete = ['_' for _ in word()]
    lifes = ['♥' for _ in range(5)]

    while True:
        count = 0
        os.system("cls")

        palabra = ''
        for index in range(len(w_complete)):
            palabra += w_complete[index].upper()
        for _ in range(1):
            palabra = ' '.join(palabra)

        vidas = ''
        for index in range(len(lifes)):
            vidas += lifes[index].upper()
        for _ in range(1):
            vidas = ' '.join(vidas)

        print(f"""
        {vidas}

        Adivina la palabra para ganar :D
        {palabra}

        """)

        if w_complete == word() or lifes == []:
            if w_complete == word():
                print("¡Ganaste!")
            else:
                print("Perdiste, intenta de nuevo :(")
            break
        else:
            letter_input = input(f'''
        Dime una letra: ''')

        while True:
            for pos, letter in enumerate(word()):
                if letter_input == letter:
                    w_complete[pos] = letter_input
                    count += 1
            break

        if count == 0:
            lifes.pop()


def run():
    os.system("cls")
    printOnScreen()


if __name__ == '__main__':
    run()
