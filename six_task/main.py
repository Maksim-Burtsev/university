import requests
from bs4 import BeautifulSoup
import re


def parser(url: str) -> str:
    """Возвращает HTML страницы"""

    response = requests.get(url)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)


def get_text() -> tuple:
    """Возвращает очищенный/не очищеный от тегов текст страницы"""

    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    soup = BeautifulSoup(text, 'lxml')
    article = soup.find('article', {'class': 'gr-post gr-article'})

    text = re.sub(r'\<[^>]*\>', '', str(article))

    return text, article


def get_text_from_blocks(article):
    """Достаёт содержимое между begin и end внутри блоков и записывает всё в файл"""

    pre = article.find_all('pre', {'class': 'pascal geshifilter-pascal'})
    for i in range(len(pre)):
        pre[i] = re.sub(r'\<[^>]*\>', '', str(pre[i]))

    my_list = []

    for txt in pre:
        if 'begin' in txt:
            my_list.append(txt)

    with open('res.txt', 'a', encoding='utf=8') as f:
        for block in my_list:
            begin, end = [], []
            text = block.split()
            for i in range(len(text)):
                if text[i] == 'begin':
                    begin.append(i)
                if text[i] == 'end;':
                    end.append(i)
                if text[i][-1] == ';':
                    text[i] = text[i] + '\n'

            f.write(' '.join(text[begin[0]:end[-1]+1]) + '\n\n')
            f.write(' '.join(text[begin[1]:end[-2]+1]) + '\n\n')


def main():

    parser('http://grafika.me/node/37')

    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    text, article = get_text()

    regex = re.compile(r'begin(.*?)end', re.DOTALL)
    res = re.search(regex, text).group(1)

    with open('res.txt', 'a', encoding='utf-8') as f:
        f.write(f'{res} \n\n\n')

    get_text_from_blocks(article)


if __name__ == '__main__':
    main()


