import os.path
from pathlib import Path

import requests


def save_file(file_content, file_name):
    with(open(file_name, 'wb')) as f:
        f.write(file_content)


def main():
    url = 'https://tululu.org/txt.php?id=32168'
    response = requests.get(url)
    response.raise_for_status()
    Path("books").mkdir(parents=True, exist_ok=True)
    save_file(response.content, 'books/first_book.txt')


if __name__ == '__main__':
    main()
    file_is_created = os.path.exists('books/first_book.txt')
    assert file_is_created
