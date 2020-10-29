import sys
import requests
from collections import Counter
from pprint import pprint

token = '1f22f984a99e17a0f77e76ef60d37164abf700ec'
headers = {'Authorization': 'token ' + token}
login = requests.get('https://api.github.com/user', headers=headers)


class GitHubUser:

    def __init__(self, username):

        self.username = username
        self.user = requests.get(f'https://api.github.com/users/{self.username}').json()
        self.repos = self.user['public_repos']
        self.repos_url = requests.get(self.user['repos_url']).json()
        self.followers = self.user['followers']


    def repositories(self):
        return {repo['name']: repo['description'] for repo in self.repos_url}


    def languages(self):

        langs = Counter()
        for repo in self.repos_url:
            langs.update([repo['language']])

        return {l: rs for l, rs in langs.most_common()}



def find_user(users):

    for u in users:
        print(users.index(u) + 1, u)
    n = int(input('Выберите пользователя по номеру: '))
    username = users[n-1]

    user = GitHubUser(username)
    print('\nНазвание репозитория: Описание репозитория')
    pprint(user.repositories())
    print('\nЯзыки пользователя: Число репозиториев')
    pprint(user.languages())


def find_tops(users):

    max_repos = None
    max_followers = None
    top_langs = Counter()

    for u in users:
        user = GitHubUser(u)

        if max_repos is None or user.repos > max_repos[1]:
            max_repos = (user.username, user.repos)

        if max_followers is None or user.followers > max_followers[1]:
            max_followers = (user.username, user.followers)

        langs = user.languages()
        top_langs.update(langs.keys())

    top_lang = top_langs.most_common()[0][0]

    print(f'\nПользователь с наибольшим числом репозиториев: {max_repos}')
    print(f'Пользователь с наибольшим числом подписчиков: {max_followers}')
    print(f'Самый популярный язык: {top_lang}')


def main():
    users = sys.argv[1:]
    find_user(users)
    find_tops(users)


if __name__ == '__main__':
    main()
