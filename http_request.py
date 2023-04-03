import requests

def send_request(url, method, headers, body):
    if method == 'GET':
        response = requests.request(url=url, method=method, headers=headers)
        print(response.content)
    else:
        requests.request(url=url, method=method, headers=headers, data=body)