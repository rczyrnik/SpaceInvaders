''' SPACE INVADERS
'''

from datetime import datetime

def display(now, enemy):
    print(now, end='\n')
    for i in enemy:
        print("^O^ ", end = '')
    print('\n'*20)

if __name__ == '__main__':
    enemy = [1] * 12
    print(enemy)
    '''display()
'''
    x = 0
    while x < 1000000:
        now = datetime.now().microsecond
        if now % 100 == 0:
            display(now, enemy)
        x += 1






