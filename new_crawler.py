import requests


def save_from_www(link):
    filename = link.split('/')[-1]
    print(filename)
    r = requests.get(link, allow_redirects=True)
    open(filename, "wb").write(r.content)


link1 = 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B7%D0%B0%D0%B4_%D0%B2_%D0%B1%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B5_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)'

save_from_www(link1)