import requests

acc_token = 'l6Ij9QW8CyZ4ta0c5yFDKhFOkYaaMa4dXO6nJTaqORz'


def send_line(msg):

    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    send_line('Pythonからこんにちは！')
    print('OK')
