import requests


def main():
    send_stick_line('stamp', 4, 303)


def send_stick_line(msg, package_id, sticker_id):
    acc_token = 'YDIy66MOGRxPuRiN65b7uFtAPLarIs4yX6GxoMjWWve'
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer+{acc_token}'}
    payload = {
        'message': '{msg}',
        'stickerPackageId': '{package_id}',
        'stickerId': {sticker_id},
    }
    requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    main()
