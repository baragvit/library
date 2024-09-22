import logging
from pathlib import Path

import requests
from requests import HTTPError

logger = logging.getLogger(__name__)


def save_file(file_content, file_name):
    with(open(file_name, 'wb')) as f:
        f.write(file_content)


def check_for_redirect(response):
    if response.status_code == 302:
        raise HTTPError()


def main():
    Path("books").mkdir(parents=True, exist_ok=True)
    for file_id in range(11):
        response = requests.get(f'https://tululu.org/txt.php?id={file_id}', allow_redirects=False)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            save_file(response.content, f'books/{file_id}.txt')
        except HTTPError:
            logger.warning(f"book with id [{file_id}] does not exist")


if __name__ == '__main__':
    main()
