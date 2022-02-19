import requests
from bs4 import BeautifulSoup


class Translation:
    base_url = "https://context.reverso.net/translation/"
    s = requests.Session()

    def __init__(self, _word, _lng_from):
        self.word = _word
        self.lng_from = _lng_from
        self.lng_to = ''
        self.words = []
        self.examples = []
        self.soup = None
        self.output = ''

    def get_info_from_site(self):
        url = f"{Translation.base_url}{self.lng_from.lower()}-{self.lng_to.lower()}/{self.word}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = Translation.s.get(url, headers=headers)
        if r.status_code == 404:
            print(f'Sorry, unable to find {self.word}')
            exit()
        elif r.status_code != 200:
            print('Something wrong with your internet connection')
            exit()
        else:
            self.soup = BeautifulSoup(r.content, 'html.parser')

    def find_words(self):
        self.words = []
        div = self.soup.find("div", id="translations-content")
        for w in div.find_all('a', class_='translation', limit=6):
            self.words.append(w.text.strip() + '\n')

    def find_examples(self):
        self.examples = []
        section = self.soup.find("section", id="examples-content")
        for ex in section.find_all('div', {'class': ['src ltr', 'trg ltr']}, limit=10):
            ex = ex.text.replace('\n', '').replace('\r', '').strip()
            self.examples.append(ex)

    def get_results(self, n_ex=None):
        if n_ex is None:
            n_ex = len(self.examples) // 2

        self.output += f'\n{self.lng_to.capitalize()} Translations:\n'
        for w in self.words[1:n_ex + 1]:
            self.output += w
        self.output += f'\n{self.lng_to.capitalize()} Examples:\n'
        for i in range(0, n_ex * 2, 2):
            self.output += f'{self.examples[i]}\n{self.examples[i + 1]}\n\n'

    def translate(self, _lng_to):
        self.lng_to = _lng_to
        self.get_info_from_site()
        self.find_words()
        self.find_examples()
