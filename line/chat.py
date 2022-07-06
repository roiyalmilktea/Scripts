import requests


def send_line(msg):

    url = "https://notify-api.line.me/api/notify"
    acc_token = 'hCorZzr4SKc1nfeu0K5GHgBjKhMaq0zoZxfSSVY4o3N'
    headers = {'Authorization': 'Bearer' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    send_line('Python3')
    print('exit')
