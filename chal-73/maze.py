import requests
import time
import sys

sys.setrecursionlimit(1000000)

LOGIN_INFO= {
    'username': '', # your username
    'password': ''  # your password
}
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
URL = 'https://hack.arrrg.de'

# login
s = requests.session()
s.post(f'{URL}/login', data=LOGIN_INFO, headers=HEADER)

# change language to EN
s.get(f'{URL}/en')

board = dict()
dead_point = {
    (-12, -4), (-6, 11)
}
dead_flag = True

def search(x, y):
    global dead_flag

    if dead_flag:
        return

    time.sleep(1.5)
    print(f'We got ({x}, {y})')

    r = s.get(f'{URL}/chal/maze')
    
    if 'This is the entrance to the labyrinth.' in r.text and (x, y) != (0, 0):
        dead_point.add((x, y))
        dead_flag = True
        print(f'Dead!! ({x}, {y})')

    if (x, y) not in board:
        board[(x, y)] = r.text

    print(f'Message = {board[(x, y)]}')

    if (x + 1, y) not in dead_point and (x + 1, y) not in board and 'maze/east' in r.text:
        s.get(f'{URL}/chal/maze/east')
        search(x + 1, y)
        s.get(f'{URL}/chal/maze/west')
    if (x - 1, y) not in dead_point and (x - 1, y) not in board and 'maze/west' in r.text:
        s.get(f'{URL}/chal/maze/west')
        search(x - 1, y)
        s.get(f'{URL}/chal/maze/east')
    if (x, y - 1) not in dead_point and (x, y - 1) not in board and 'maze/south' in r.text:
        s.get(f'{URL}/chal/maze/south')
        search(x, y - 1)
        s.get(f'{URL}/chal/maze/north')
    if (x, y + 1) not in dead_point and (x, y + 1) not in board and 'maze/north' in r.text:
        s.get(f'{URL}/chal/maze/north')
        search(x, y + 1)
        s.get(f'{URL}/chal/maze/south')


while dead_flag:
    dead_flag = False
    board = dict()
    search(0, 0)

