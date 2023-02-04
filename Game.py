import os
import Riddlez as rz
import TypeYourThought as tyt
import NaiveBeyes as nb
import math

def Header():
    os.system('cls')
    print(' ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ')
    print('█ █ ▄ █ █       █   ▄  █ █  ▄    █       █')
    print('█ ██ ██ █   ▄   █  █ █ █ █ █▄█   █  ▄▄▄▄▄█')
    print('█       █  █ █  █   █▄▄█▄█       █ █▄▄▄▄▄ ')
    print('█       █  █▄█  █    ▄▄  █  ▄   ██▄▄▄▄▄  █')
    print('█   ▄   █       █   █  █ █ █▄█   █▄▄▄▄▄█ █')
    print('█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█')
    print('\n')

def Exit():
    os.system('cls')
    print('▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄')
    print('█      █      ██   █       █       █')
    print('█  ▄   █  ▄    █   █   ▄   █  ▄▄▄▄▄█')
    print('█ █▄█  █ █ █   █   █  █ █  █ █▄▄▄▄▄ ')
    print('█      █ █▄█   █   █  █▄█  █▄▄▄▄▄  █')
    print('█  ▄   █       █   █       █▄▄▄▄▄█ █')
    print('█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█')
    print('\n')

def Option():
    print('1. RiddLez')
    print('2. TypeYourThought')
    print('3. NaiveBeyes')
    print('4. Exit')

def FirstOption(riddlez):
    os.system('cls')
    randomWord = rz.getRandomWord(riddlez)
    maskingWord = rz.getMaskingWord(randomWord[0])
    answerWord = randomWord[0]
    definitionWord = randomWord[1]
    exampleWord = randomWord[2]

    print(f'The riddle: {maskingWord}\n')
    print(f'Definition: {definitionWord}\n')
    i = 0
    for s in exampleWord:
        i = i + 1
        print(f'{i}. example: "{s}"')
    print('')

    life = 5
    win = False
    for n in range(life,0,-1):
        str = input(f'input your answer [you got {n} life remaining] -> ')
        if str == answerWord:
            print(f'your answer is currect!! It is {answerWord}')
            win = True
            break

    if win == False:
        print(f'you lose!! The right answer is {randomWord[0]}')

    input('\npress enter to continue...')

def SecondOption():
    os.system('cls')
    text = ''
    while True:
        text = input('input your desired sentence [4 words minimum]: ')
        if tyt.isInputValid(text):
            break
    res = tyt.getMostInputtedWord(text)
    print(f'one of the word that you are typing: "{res[0]}"')
    print(f'definition: {res[1][0]}')
    i = 0
    for s in res[1][1]:
        i = i + 1
        print(f'{i}. example: "{s}"')
    input('\npress enter to continue...')

def ThirdOption(train):
    os.system('cls')
    print('showing result of the trained model\n')
    print(f'With more than {train[1]} data, we divide it into 7:3 ratio of training ({train[2]} data) and testing ({train[3]}). The result is magneficent, we achieve the accuracy of {math.ceil(float(train[0]))}%!!')
    input('\npress enter to continue...')

def Mechanism():

    #take all the list of words
    riddlez = rz.initData()
    #get the trained model
    train = nb.getSavedTrainedModel()

    n = -24
    while True:
        Header()
        Option()
        n = input('choose -> ')
        if n.isnumeric():
            if int(n) == 1:
                FirstOption(riddlez)
            elif int(n) == 2:
                SecondOption()
            elif int(n) == 3:
                ThirdOption(train)
            elif int(n) == 4:
                break
    Exit()