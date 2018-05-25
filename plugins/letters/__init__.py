from bs4 import BeautifulSoup
from pelican import signals, contents


def letters(content):
    if isinstance(content, contents.Static):
        return

    soup = BeautifulSoup(content._content, 'html.parser')
    letters = soup.findAll('div', {'class': 'letter'})

    if letters:
        row = soup.new_tag('div', **{'class': 'row'})
        soup.append(row)

        for letter in soup.findAll('div', {'class': 'letter'}):
            card = soup.new_tag('div', **{'class': 'card col-sm-6'})
            card_body = soup.new_tag('div', **{'class': 'card-body'})

            card_title = soup.new_tag('h5', **{'class': 'card-title'})
            card_title.string = letter.attrs['title']

            card_text = soup.new_tag('div', **{'class': 'card-text'})
            lines = letter.text.split('\n')
            for line in lines:
                p = soup.new_tag('p', **{'class': '' if line else 'break'})
                p.string = line
                card_text.append(p)

            card.append(card_body)
            card_body.append(card_title)
            card_body.append(card_text)

            letter.extract()
            row.append(card)

    content._content = soup.decode()


def register():
    signals.content_object_init.connect(letters)
