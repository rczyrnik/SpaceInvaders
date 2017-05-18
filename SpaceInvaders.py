''' SPACE INVADERS
'''

from datetime import datetime
import os
import readline

def display(screen):
    for array in screen:
        for char in array:
            print(char, end='')
        print()
    ans = input("")
    print('')


'''
    for i in enemy:
        print("^O^ ", end = '')
    print('\n'*20)
'''
def makeScreen():
    
    # default variables
    height = 21
    w = 60

    # create a 2d array filled with blank spaces
    screen = []
    while height > 0:
        screen += [[height]] 
        height -= 1
    
    # fill in elements of the screen
    screen[0] = ['\n']
    screen[1] = ["   Welcome to my Awesome Game"]
    screen[2] = ['']
    
    screen[-6] = [" "*(w-8) + "  __    "] 
    screen[-5] = [" "*(w-8) + " /  \   "] 
    screen[-4] = [" "*(w-8) + "/    \  "] 
    screen[-3] = [" "*(w-8) + "|    |  "] 
    screen[-2] = [" "*(w-8) + "|    |  "] 
    screen[-1] = ["^"*w]
    return screen

if __name__ == '__main__':
    #os.system('setterm -cursor off')
    screen = makeScreen()
    display(screen)

    letter = input_char('') 
    #readline.get_line_buffer()
    if letter == 'a':
        print("Hurrah!")
'''
    enemy = [1] * 12
    
    print(enemy)
    x = 0

    while x < 1000000:
        now = datetime.now().microsecond
        if now % 100 == 0:
            display(screen)
        x += 1
'''





