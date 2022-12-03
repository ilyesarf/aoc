import requests
import os

if not os.path.exists('inputs'):
    os.makedirs('inputs')

def get_cookies():
    cookies = {}
    inf = open('cookies.txt', 'r').readlines()[-1]
    cookies['session'] = inf.split('session')[1].replace('\t', '')
    
    return cookies

def get_input(day, year='2022', lines=True):
    file = f'inputs/input.{year}.{day}'
    
    if not os.path.isfile(file):
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        cookies = get_cookies() 

        r = requests.get(url, cookies=cookies)
        input = r.text
        save_input(day, file, input)
        
        return input.splitlines(True)
    else:
        input = read_input(day, file, lines)
        return input


def save_input(day, file, input):
    with open(file, 'w') as f:
        f.write(input)

def read_input(day, file, lines=True):
    with open(file, 'r') as f:
        if lines:
            return f.readlines()
        else:
            return f.read()
