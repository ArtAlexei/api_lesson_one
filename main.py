import requests


def main():
    locations = ['london', 'svo', 'Череповец']
    for location in locations:
        param = {'n': '', 'T': '', 'q': '', 'm': '', 'lang': 'ru'}
        url = f'https://wttr.in/{location}'
        response = requests.get(url, param)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    main()
