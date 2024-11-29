import requests


LOGIN_INFO= {
    'username': '', # your username
    'password': ''  # your password
}
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
URL = 'https://hack.arrrg.de'

with requests.Session() as s:
    s.post(f'{URL}/login', data=LOGIN_INFO, headers=HEADER)
    s.get(f'{URL}/en')

    r = s.get(f'{URL}/challenge/338')
    ans = dict()

    for i in range(30):
        span = f'<span id="task{i}" style="width:3.5rem;display:inline-block;">'
        pos = r.text.index(span)
        prob = r.text[pos + len(span):pos + len(span) + 15].split('=')[0]

        ans[f'ans{i}'] = eval(prob)

    ans['answer'] = 'ok'
    r = s.post(f'{URL}/challenge/338', data=ans)

    print(r.text)

