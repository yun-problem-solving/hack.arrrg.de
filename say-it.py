# https://app.transkriptor.com/
# https://mp3cut.net/

with open('say-it.png', 'wb') as f, open('say-it.data') as data:
    d = map(int, data.readline().split())
    for i in d:
        f.write((i).to_bytes(1))

