from bs4 import BeautifulSoup
from pelican import signals, contents


def tables(content):
    if isinstance(content, contents.Static):
        return

    soup = BeautifulSoup(content._content, 'html.parser')
    classes = ('table', 'table-bordered', 'table-responsive')

    for table in soup.findAll('table'):
        table.attrs['class'] = ' '.join(classes)

    soup.renderContents()
    content._content = soup.decode()


def register():
    signals.content_object_init.connect(tables)
