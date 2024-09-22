import os.path

import requests


def save_file(file_content, file_name):
    with(open(file_name, 'wb')) as f:
        f.write(file_content)


def main():
    url = 'https://dvmn.org/tilda_assets/tild6435-3366-4037-b963-323530656465__devman_logo_heart_wi.svg'
    response = requests.get(url)
    response.raise_for_status()
    save_file(response.content, '/tmp/picture.svg')


if __name__ == '__main__':
    main()
    file_is_created = os.path.exists('/tmp/picture.svg')
    assert file_is_created
