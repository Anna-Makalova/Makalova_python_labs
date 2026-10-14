import time
import sys
import os


BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'


def flag():
    pixel = '    '
    lenght = 5
    height = 10
    

    for i in range(height):
        if i < height // 2:
            print(GREEN + pixel * (lenght) + YELLOW + pixel * (lenght) + RESET)
        else:
            print(GREEN + pixel * (lenght) + RED + pixel * (lenght) + RESET)





diamond = [
    '...#...',
    '..###..',
    '.#####.',
    '#######',
    '.#####.',
    '..###..',
    '...#...'
]

def draw_diamond(count):
    for row in diamond:
        full_row = row *count
        line =''
        for symbol in full_row:
            if symbol == '#':
                line += f'{RED}  '
            else:
                line += f'{RESET}  '
        print(f'{line}{RESET}')



def two_diamonds():
    height = 7
    center = height //2
    step = 1
    colors = [87, 196, 226]
    offset1 = center
    lenght1 = 1
    offset2 = center
    lenght2 = 1
    max_width = height 

    while True:
        for color in colors:
            os.system("cls")
            for line in range(height):
                
                diamond1 = f'{'  ' * offset1}\u001b[48;5;{color}m{'  ' * lenght1}{RESET}'
                diamond2 = f'{'  ' * offset2}\u001b[48;5;{color}m{'  ' * lenght2}{RESET}'
                lenght_d1 = offset1 + lenght1
                padding = '  '* (max_width - lenght_d1)
                print(diamond1 + padding + diamond2)
                if line < center:
                    offset1 -= step 
                    lenght1 += step * 2
                    offset2 -= step
                    lenght2 += step * 2
                else:
                    offset1 += step
                    lenght1 -= step * 2
                    offset2 += step
                    lenght2 -= step * 2
            print(f'\u001b[{height}A', end='')
            offset1 = center
            lenght1 = 1
            offset2 = center
            lenght2 = 1
            time.sleep(1)

def sequence():
    file = open('sequence.txt', 'r')
    positive = []
    negative = []
    for line in file:
        if int(float(line) * 100) >= 0 and int(float(line) * 100) <600:
            positive.append(float(line))
        elif int(float(line) * 100) < 0 and int(float(line) * 100) >-600:
            negative.append(float(line))
    file.close()
    total = len(positive) + len(negative)
    if total>0:
        print(f'{BLUE}{' ' * int(len(positive) / 5)}{RESET} {len(positive)/(len(positive) + len(negative)) * 100}%')
        print(f'{RED}{' ' * int(len(negative) / 5)}{RESET} {len(negative)/(len(positive) + len(negative)) * 100}%')
    else:
        print('error')


#flag()
#draw_diamond(9)
#sequence()
two_diamonds()
