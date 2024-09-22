import os.path
from pathlib import Path

import requests


def save_file(file_content, file_name):
    with(open(file_name, 'wb')) as f:
        f.write(file_content)


def main():
    Path("books").mkdir(parents=True, exist_ok=True)
    for file_id in range(1, 11):
        response = requests.get(f'https://tululu.org/txt.php?id={file_id}')
        response.raise_for_status()
        save_file(response.content, f'books/{file_id}.txt')


if __name__ == '__main__':
    main()
    file_is_created = os.path.exists('books/first_book.txt')
    assert file_is_created
