import ramdom
import os

def run ():

      IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



    DB =[
        "C",
        "PYTHON",
        "JAVASCRIPT",
         "JAVA",
         "PHP"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while true:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
            print(IMAGES[attemps])
        letter = input("Elige una letra").upper()

        found = flase
        for  idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = true

                if not found:
                    attemps =- 1

                    if "_" not in  spaces:
                        os.system("clear")
                        print("Ganaste")
                        break
                        input()

                        if attemps == 0:
                        os.system("clear")
                        print("Perdiste")
                        break
                        input()

    if _name_ == '_main_':
        run()