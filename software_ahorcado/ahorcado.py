#el juego solo se hace en la consola
# Library
import random

#Palabras
ANSWERS = ['abeja', 'ancho', 'agua', 'alba', 'aire', ]
CHALLENGE = ANSWERS[random.randint(0, len(ANSWERS) - 1)]


def run():
    letters = list(CHALLENGE)
    hiddenWord = ''
    lettersChalleng = []
    for letter in letters:
        lettersChalleng.append(" -*- ")
    showIntroduction()
    tries = -1
    while tries != 7:
        word = input('Write a word: ')
        response = checkAnswere(word)
        if response is False:
            tries += 1
        else:
            count = 0
            for letter in letters:
                if(word == letter):
                    lettersChalleng[count] = letter
                count += 1
            hiddenWord = '|'.join(lettersChalleng)
        if ''.join(lettersChalleng) != CHALLENGE:
            printBoy(tries)
            print(hiddenWord)
        else:
            congratulation()
            tries = 8
            break


def showIntroduction():
    print(" &&&&jueguito del ahorcado&&&&")

    printBoy(-1)


def congratulation():
    print("####FELIIDADDES####")

    print("¡ Tu palabra es: {} !".format(CHALLENGE))
    exit()

#AQUI DEFINO EL MUÑEQUITO 
def printBoy(position):
    man = [
        '0',# Cabeza
        '/', '|', '\\', # Brazos
             '|', # Cuerpo
        '/', '\\'# Piernas
    ]
    sections = [
        '\n\t+--------+\n\t|\t |\n', # Parte superior de la horca
        '\n=========\n'  # Base de la horca
    ]
    body = ''
    for i in range(len(man)): # Iteramos sobre las partes del muñeco
        if i <= position and position >= 0:
            if i == 0:
                body = '\t|\t ' + man[i]
            elif i > 0 and i < 4:
                if i == 1:
                    body = body + "\n\t|\t"
                body = body + man[i]
            elif i == 4:
                body = body + '|\t ' + man[i] + '\n\t|\t'
            elif i > 4:
                body = body + man[i] + " "

            if i > 2 and i < 4:
                body = body + '\n\t'
        else:
            if i > 0:
                body += "\n"
            body = body + '\t|\t'
    body = sections[0] + body + sections[1]
    print(body)


def printHiddenWord():
    print(['-' * len(CHALLENGE)])


def checkAnswere(word):
    letters = list(CHALLENGE)
    for letter in letters:
        if(word == letter):
            return True
    return False


if __name__ == "__main__":
    run()